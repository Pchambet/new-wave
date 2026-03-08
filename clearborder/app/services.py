"""
Services layer - Business logic connecting API, DB and CBAM engine.
"""
from typing import Optional
from decimal import Decimal

from sqlalchemy.orm import Session

from .models import Installation, Product, ProductPrecursor, DefaultEmissionFactor, CNCode
from .schemas import (
    InstallationCreate, ProductCreate, PrecursorInput,
    CBAMReportRequest, CBAMReportResponse, CBAMProductResult, ProductReportItem,
)
from .cbam_engine import calculate_see, ProductEmissionData, PrecursorData
from .xml_generator import create_cbam_report_xml
from .classifier import classify as ml_classify
from .models import CNCode


def create_installation(db: Session, data: InstallationCreate) -> Installation:
    """Create a new installation."""
    inst = Installation(
        name=data.name,
        country_code=data.country_code.upper(),
        sector=data.sector,
        emissions_per_tonne=data.emissions_per_tonne,
        o3ci_id=data.o3ci_id,
    )
    db.add(inst)
    db.commit()
    db.refresh(inst)
    return inst


def get_installation(db: Session, inst_id: int) -> Optional[Installation]:
    """Get installation by ID."""
    return db.query(Installation).filter(Installation.id == inst_id).first()


def list_installations(db: Session, skip: int = 0, limit: int = 100):
    """List all installations."""
    return db.query(Installation).offset(skip).limit(limit).all()


def create_product(db: Session, data: ProductCreate) -> Product:
    """Create a new product with optional precursors."""
    product = Product(
        name=data.name,
        cn_code=data.cn_code,
        sector=data.sector,
        installation_id=data.installation_id,
        activity_level=data.activity_level,
        attributed_emissions=data.attributed_emissions,
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    if data.precursors:
        for p in data.precursors:
            prec = ProductPrecursor(
                product_id=product.id,
                mass_kg=p.mass_kg,
                see_per_kg=p.see_per_kg,
                is_real_data=p.is_real_data,
            )
            db.add(prec)
        db.commit()
        db.refresh(product)

    return product


def get_product(db: Session, product_id: int) -> Optional[Product]:
    """Get product by ID with precursors loaded."""
    return db.query(Product).filter(Product.id == product_id).first()


def list_products(db: Session, skip: int = 0, limit: int = 100):
    """List all products."""
    return db.query(Product).offset(skip).limit(limit).all()


def _product_to_emission_data(product: Product) -> ProductEmissionData:
    """Convert Product model to ProductEmissionData for CBAM engine."""
    precursors = [
        PrecursorData(
            mass_kg=float(p.mass_kg),
            see_per_kg=float(p.see_per_kg),
            is_real_data=p.is_real_data,
        )
        for p in product.precursors
    ]
    return ProductEmissionData(
        attr_em=float(product.attributed_emissions),
        activity_level=float(product.activity_level),
        precursors=precursors,
    )


def calculate_product_see(product: Product) -> dict:
    """Calculate SEE for a single product."""
    data = _product_to_emission_data(product)
    return calculate_see(data)


def calculate_cbam_report(db: Session, request: CBAMReportRequest) -> CBAMReportResponse:
    """Calculate CBAM SEE for products and generate XML report."""
    results = []
    inst_country = {}
    product_inst = {}  # product_id -> installation_id

    for item in request.products:
        product = get_product(db, item.product_id)
        if not product:
            raise ValueError(f"Product {item.product_id} not found")

        see_result = calculate_product_see(product)
        see_per_tonne = see_result["see_per_kg"] * 1000

        results.append(CBAMProductResult(
            product_id=product.id,
            cn_code=product.cn_code,
            description=product.name,
            see_kg_co2_per_tonne=see_per_tonne,
            real_data_ratio=see_result["real_data_ratio"],
            compliant_80_20=see_result["rule_80_20_compliant"],
            quantity_tonnes=item.quantity_tonnes,
        ))

        product_inst[product.id] = product.installation_id
        if product.installation_id not in inst_country:
            inst = get_installation(db, product.installation_id)
            if inst:
                inst_country[product.installation_id] = {
                    "country": inst.country_code,
                    "sector": inst.sector,
                }

    xml_products = [
        {
            "cn_code": r.cn_code,
            "product_name": r.description,
            "quantity_kg": float(r.quantity_tonnes * 1000),
            "see_per_kg": r.see_kg_co2_per_tonne / 1000,
            "country_of_origin": inst_country.get(
                product_inst.get(r.product_id), {}
            ).get("country", ""),
        }
        for r in results
    ]

    xml_content = create_cbam_report_xml(
        declarant_id=request.declarant_id,
        reporting_period=request.reporting_period,
        products=xml_products,
    )

    return CBAMReportResponse(
        results=results,
        xml_content=xml_content,
        compliant=all(r.compliant_80_20 for r in results),
    )


def list_cn_codes(db: Session, skip: int = 0, limit: int = 100):
    """Liste les codes CN (nomenclature douanière)."""
    rows = db.query(CNCode).offset(skip).limit(limit).all()
    return [{"id": r.id, "code": r.code, "description": r.description, "level": r.level} for r in rows]


def classify_product(db: Session, description: str, top_k: int = 3) -> dict:
    """Suggère des codes CN à partir d'une description (ML ou fallback)."""
    suggestions = ml_classify(description, top_k=top_k)
    # Enrichir avec les descriptions des codes CN depuis la BDD
    for s in suggestions:
        cn = db.query(CNCode).filter(CNCode.code == s["code"]).first()
        s["description"] = cn.description if cn else ""
    return {"suggestions": suggestions}
