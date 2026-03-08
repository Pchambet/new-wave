"""
Moteur de calcul CBAM - Specific Embedded Emissions (SEE)
Conforme à l'Annexe IV du Règlement (UE) 2023/956

Formules:
- SEE_g = (AttrEm_g + EEInpMat) / AL_g
- EEInpMat = Σ (M_i × SEE_i) pour chaque précurseur
"""

from decimal import Decimal
from typing import Optional
from dataclasses import dataclass


@dataclass
class PrecursorData:
    """Données d'un précurseur dans le BOM"""
    mass_kg: float
    see_per_kg: float  # Émissions spécifiques en kg CO2e/kg
    is_real_data: bool  # True = données réelles, False = valeur par défaut


@dataclass
class ProductEmissionData:
    """Données d'émission pour le calcul SEE"""
    attr_em: float  # Émissions attribuées au processus de production (kg CO2e)
    activity_level: float  # AL_g - niveau d'activité ou masse totale (kg)
    precursors: list[PrecursorData]
    installation_id: Optional[str] = None


def calculate_ee_inp_mat(precursors: list[PrecursorData]) -> tuple[float, float, float]:
    """
    Calcule EEInpMat = Σ (M_i × SEE_i)
    Retourne (EEInpMat, masse_totale_reelle, masse_totale_defaut) pour la règle 80/20
    """
    ee_inp_mat = 0.0
    mass_real = 0.0
    mass_default = 0.0
    
    for p in precursors:
        contribution = p.mass_kg * p.see_per_kg
        ee_inp_mat += contribution
        if p.is_real_data:
            mass_real += p.mass_kg
        else:
            mass_default += p.mass_kg
    
    return ee_inp_mat, mass_real, mass_default


def validate_80_20_rule(mass_real: float, mass_total: float) -> tuple[bool, float]:
    """
    Règle 80/20 : au moins 80% des données doivent provenir de valeurs réelles
    pour les biens complexes.
    Retourne (conforme, ratio_réel)
    """
    if mass_total == 0:
        return False, 0.0
    ratio = mass_real / mass_total
    return ratio >= 0.80, ratio


def calculate_see(data: ProductEmissionData) -> dict:
    """
    Calcule les Specific Embedded Emissions (SEE) pour un bien.
    
    SEE_g = (AttrEm_g + EEInpMat) / AL_g
    
    Retourne un dict avec:
    - see_per_kg: émissions spécifiques en kg CO2e/kg
    - ee_inp_mat: émissions des précurseurs
    - attr_em: émissions du processus
    - activity_level: niveau d'activité
    - rule_80_20_compliant: conformité règle 80/20
    - real_data_ratio: ratio des données réelles
    - warnings: liste d'alertes
    """
    warnings = []
    
    # Calcul EEInpMat
    ee_inp_mat, mass_real, mass_default = calculate_ee_inp_mat(data.precursors)
    mass_total_precursors = mass_real + mass_default
    
    # Règle 80/20 pour biens complexes (avec précurseurs)
    rule_80_20_compliant = True
    real_data_ratio = 1.0
    
    if data.precursors:
        rule_80_20_compliant, real_data_ratio = validate_80_20_rule(
            mass_real, mass_total_precursors
        )
        if not rule_80_20_compliant:
            warnings.append(
                f"Règle 80/20 non respectée: {real_data_ratio*100:.1f}% de données réelles "
                f"(minimum 80% requis pour les biens complexes)"
            )
    
    # Calcul SEE
    numerator = data.attr_em + ee_inp_mat
    if data.activity_level <= 0:
        raise ValueError("Le niveau d'activité (AL_g) doit être strictement positif")
    
    see_per_kg = numerator / data.activity_level
    
    return {
        "see_per_kg": round(see_per_kg, 6),
        "ee_inp_mat": round(ee_inp_mat, 6),
        "attr_em": data.attr_em,
        "activity_level": data.activity_level,
        "rule_80_20_compliant": rule_80_20_compliant,
        "real_data_ratio": round(real_data_ratio, 4),
        "warnings": warnings,
        "total_emissions_kg_co2e": round(numerator, 6),
    }


def calculate_see_recursive(bom_tree: dict) -> dict:
    """
    Calcule SEE de manière récursive pour un arbre de BOM (Bill of Materials).
    
    bom_tree structure:
    {
        "attr_em": float,
        "activity_level": float,
        "precursors": [
            {
                "mass_kg": float,
                "see_per_kg": float | None,  # Si None, calcul récursif
                "is_real_data": bool,
                "nested_bom": dict | None  # BOM du précurseur si see_per_kg est None
            }
        ]
    }
    """
    precursors_data = []
    
    for p in bom_tree.get("precursors", []):
        see_per_kg = p.get("see_per_kg")
        if see_per_kg is None and p.get("nested_bom"):
            # Calcul récursif
            nested_result = calculate_see_recursive(p["nested_bom"])
            see_per_kg = nested_result["see_per_kg"]
        
        if see_per_kg is not None:
            precursors_data.append(PrecursorData(
                mass_kg=p["mass_kg"],
                see_per_kg=see_per_kg,
                is_real_data=p.get("is_real_data", False)
            ))
    
    data = ProductEmissionData(
        attr_em=bom_tree.get("attr_em", 0),
        activity_level=bom_tree["activity_level"],
        precursors=precursors_data
    )
    
    return calculate_see(data)


class CBAMCalculator:
    """Calculateur SEE qui travaille avec les modèles SQLAlchemy."""

    def __init__(self, db_session=None):
        self.db = db_session

    def calculate_see(self, product) -> "CBAMCalculationResult":
        """
        Calcule SEE pour un Product (modèle SQLAlchemy).
        Retourne un objet avec see_kg_co2_per_tonne, real_data_ratio, compliant_80_20.
        """
        precursors_data = []
        for prec in product.precursors:
            precursors_data.append(PrecursorData(
                mass_kg=float(prec.mass_kg),
                see_per_kg=float(prec.see_per_kg),
                is_real_data=prec.is_real_data,
            ))

        data = ProductEmissionData(
            attr_em=float(product.attributed_emissions or 0),
            activity_level=float(product.activity_level),
            precursors=precursors_data,
        )
        result = calculate_see(data)

        # SEE en kg CO2e/tonne (activity_level en kg, donc * 1000)
        see_per_tonne = result["see_per_kg"] * 1000

        return CBAMCalculationResult(
            see_kg_co2_per_tonne=see_per_tonne,
            real_data_ratio=result["real_data_ratio"],
            compliant_80_20=result["rule_80_20_compliant"],
            warnings=result["warnings"],
        )


class CBAMCalculationResult:
    """Résultat du calcul SEE pour un produit."""
    def __init__(self, see_kg_co2_per_tonne: float, real_data_ratio: float,
                 compliant_80_20: bool, warnings: list = None):
        self.see_kg_co2_per_tonne = see_kg_co2_per_tonne
        self.real_data_ratio = real_data_ratio
        self.compliant_80_20 = compliant_80_20
        self.warnings = warnings or []
