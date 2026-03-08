"""Modèles SQLAlchemy pour la base de données."""
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class CNCode(Base):
    """Nomenclature Combinée (EU) - codes douaniers."""
    __tablename__ = "cn_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, index=True, nullable=False)
    description = Column(Text)
    level = Column(Integer)
    parent_code = Column(String(10), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Installation(Base):
    """Installation de production (producteur hors-UE)."""
    __tablename__ = "installations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    country_code = Column(String(2), nullable=False)
    sector = Column(String(50), nullable=False)
    emissions_per_tonne = Column(Numeric(12, 4), nullable=True)  # tCO2e/tonne
    o3ci_id = Column(String(50), nullable=True)  # ID registre O3CI
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    products = relationship("Product", back_populates="installation")


class Product(Base):
    """Produit importé soumis au CBAM."""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    cn_code = Column(String(10), nullable=False)
    sector = Column(String(50), nullable=False)
    installation_id = Column(Integer, ForeignKey("installations.id"), nullable=False)
    activity_level = Column(Numeric(12, 4), nullable=False)  # kg
    attributed_emissions = Column(Numeric(12, 4), default=0)  # kg CO2e
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    installation = relationship("Installation", back_populates="products")
    precursors = relationship("ProductPrecursor", back_populates="product", cascade="all, delete-orphan")


class ProductPrecursor(Base):
    """Précurseur pour un produit complexe (BOM)."""
    __tablename__ = "product_precursors"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    mass_kg = Column(Numeric(12, 4), nullable=False)
    see_per_kg = Column(Numeric(12, 6), nullable=False)  # kg CO2e/kg
    is_real_data = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="precursors")


class DefaultEmissionFactor(Base):
    """Facteurs d'émission par défaut (secteur/pays)."""
    __tablename__ = "default_emission_factors"

    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String(50), nullable=False)
    country_code = Column(String(2), nullable=False)
    emission_factor_kg_co2_per_tonne = Column(Numeric(12, 4), nullable=False)
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)


class CBAMReport(Base):
    """Rapport CBAM généré (historique)."""
    __tablename__ = "cbam_reports"

    id = Column(Integer, primary_key=True, index=True)
    report_period = Column(String(10), nullable=False)
    declarant_id = Column(String(100), nullable=False)
    xml_content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
