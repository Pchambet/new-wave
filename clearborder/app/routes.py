"""Routes API."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .auth import get_api_key
from .database import get_db
from .schemas import (
    InstallationCreate, InstallationResponse,
    ProductCreate, ProductResponse,
    CBAMReportRequest, CBAMReportResponse,
    ClassifyRequest,
)
from . import services

router = APIRouter()


# --- Installations ---
@router.post("/installations", response_model=InstallationResponse)
def create_installation(
    data: InstallationCreate,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    return services.create_installation(db, data)


@router.get("/installations", response_model=List[InstallationResponse])
def list_installations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    return services.list_installations(db, skip=skip, limit=limit)


@router.get("/installations/{installation_id}", response_model=InstallationResponse)
def get_installation(
    installation_id: int,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    inst = services.get_installation(db, installation_id)
    if not inst:
        raise HTTPException(status_code=404, detail="Installation not found")
    return inst


# --- Products ---
@router.post("/products", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    return services.create_product(db, data)


@router.get("/products", response_model=List[ProductResponse])
def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    return services.list_products(db, skip=skip, limit=limit)


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    product = services.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# --- CBAM Report ---
@router.post("/generate-cbam-report", response_model=CBAMReportResponse)
def generate_cbam_report(
    request: CBAMReportRequest,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    try:
        return services.calculate_cbam_report(db, request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- Classification HTS/CN ---
@router.get("/cn-codes")
def list_cn_codes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    """Liste les codes CN (nomenclature douanière EU)."""
    return services.list_cn_codes(db, skip=skip, limit=limit)


@router.post("/classify")
def classify_product(
    data: ClassifyRequest,
    db: Session = Depends(get_db),
    _api_key: str | None = Depends(get_api_key),
):
    """Suggère des codes CN à partir d'une description produit (ML)."""
    return services.classify_product(db, data.description, top_k=data.top_k)
