"""Schémas Pydantic pour validation API."""
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field


class InstallationCreate(BaseModel):
    name: str
    country_code: str = Field(..., min_length=2, max_length=2)
    sector: str
    emissions_per_tonne: Optional[Decimal] = None
    o3ci_id: Optional[str] = None


class InstallationResponse(BaseModel):
    id: int
    name: str
    country_code: str
    sector: str
    emissions_per_tonne: Optional[Decimal] = None
    created_at: datetime

    class Config:
        from_attributes = True


class PrecursorInput(BaseModel):
    mass_kg: Decimal = Field(..., gt=0)
    see_per_kg: Decimal = Field(..., ge=0)
    is_real_data: bool = False


class ProductCreate(BaseModel):
    name: str
    cn_code: str
    sector: str
    installation_id: int
    activity_level: Decimal = Field(..., gt=0)
    attributed_emissions: Decimal = Field(default=0, ge=0)
    precursors: Optional[List[PrecursorInput]] = []


class ProductResponse(BaseModel):
    id: int
    name: str
    cn_code: str
    sector: str
    installation_id: int
    activity_level: Decimal
    attributed_emissions: Decimal
    created_at: datetime

    class Config:
        from_attributes = True


class ProductReportItem(BaseModel):
    product_id: int
    quantity_tonnes: Decimal = Field(default=1, gt=0)


class CBAMReportRequest(BaseModel):
    declarant_id: str = Field(..., description="ID déclarant CBAM")
    reporting_period: str = Field(..., description="Ex: 2026-Q1")
    products: List[ProductReportItem]


class CBAMProductResult(BaseModel):
    product_id: int
    cn_code: str
    description: str  # product name
    see_kg_co2_per_tonne: float
    real_data_ratio: float
    compliant_80_20: bool
    quantity_tonnes: Decimal


class CBAMReportResponse(BaseModel):
    results: List[CBAMProductResult]
    xml_content: str
    compliant: bool


class ClassifyRequest(BaseModel):
    description: str = Field(..., min_length=1)
    top_k: int = Field(default=3, ge=1, le=10)


class CNCodeResponse(BaseModel):
    id: int
    code: str
    description: Optional[str] = None
    level: Optional[int] = None

    class Config:
        from_attributes = True
