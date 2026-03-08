#!/usr/bin/env python3
"""Script pour charger des données de démo (installations, produits, facteurs par défaut)."""
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from decimal import Decimal
from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app.models import Installation, Product, ProductPrecursor, DefaultEmissionFactor


def seed():
    init_db()
    db = SessionLocal()
    try:
        # Facteurs d'émission par défaut (kg CO2e/tonne) - valeurs indicatives
        defaults = [
            ("iron_steel", "TR", 1.8),   # Turquie - acier
            ("iron_steel", "CN", 2.2),   # Chine - acier
            ("iron_steel", "IN", 2.5),   # Inde - acier
            ("aluminium", "TR", 8.0),
            ("aluminium", "CN", 12.0),
            ("cement", "TR", 0.65),
            ("cement", "CN", 0.85),
        ]
        for sector, country, factor in defaults:
            if not db.query(DefaultEmissionFactor).filter(
                DefaultEmissionFactor.sector == sector,
                DefaultEmissionFactor.country_code == country,
            ).first():
                db.add(DefaultEmissionFactor(
                    sector=sector,
                    country_code=country,
                    emission_factor_kg_co2_per_tonne=Decimal(str(factor)),
                    source="Default EU CBAM",
                ))
        db.commit()

        # Installation exemple - Aciérie Turquie
        inst = db.query(Installation).filter(Installation.name == "Demir Celik Acieri").first()
        if not inst:
            inst = Installation(
                name="Demir Celik Acieri",
                country_code="TR",
                sector="iron_steel",
                emissions_per_tonne=Decimal("1.65"),
            )
            db.add(inst)
            db.commit()
            db.refresh(inst)
            print(f"Created installation: {inst.name} (id={inst.id})")

        # Produit exemple - Acier laminé
        prod = db.query(Product).filter(Product.cn_code == "7208").first()
        if not prod:
            prod = Product(
                name="Tôle d'acier laminée à chaud",
                cn_code="7208",
                sector="iron_steel",
                installation_id=inst.id,
                activity_level=Decimal("1000"),  # 1 tonne = 1000 kg
                attributed_emissions=Decimal("50"),  # kg CO2e du processus
            )
            db.add(prod)
            db.commit()
            db.refresh(prod)

            # Précurseur - brame d'acier
            db.add(ProductPrecursor(
                product_id=prod.id,
                mass_kg=Decimal("1050"),  # 1.05 kg de brame par kg de tôle
                see_per_kg=Decimal("1.6"),  # kg CO2e/kg
                is_real_data=True,
            ))
            db.commit()
            print(f"Created product: {prod.name} (id={prod.id})")

        print("Seed completed successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
