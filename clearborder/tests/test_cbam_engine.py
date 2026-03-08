"""
Tests unitaires du moteur CBAM — calcul SEE, règle 80/20, BOM récursif.
Conforme à l'Annexe IV du Règlement (UE) 2023/956.
"""
import pytest
from decimal import Decimal

from app.cbam_engine import (
    PrecursorData,
    ProductEmissionData,
    calculate_ee_inp_mat,
    validate_80_20_rule,
    calculate_see,
    calculate_see_recursive,
    CBAMCalculator,
    CBAMCalculationResult,
)


class TestCalculateEeInpMat:
    """Tests du calcul EEInpMat = Σ (M_i × SEE_i)."""

    def test_empty_precursors(self):
        ee, mass_real, mass_default = calculate_ee_inp_mat([])
        assert ee == 0.0
        assert mass_real == 0.0
        assert mass_default == 0.0

    def test_single_precursor_real(self):
        precursors = [PrecursorData(mass_kg=100, see_per_kg=1.5, is_real_data=True)]
        ee, mass_real, mass_default = calculate_ee_inp_mat(precursors)
        assert ee == 150.0
        assert mass_real == 100.0
        assert mass_default == 0.0

    def test_multiple_precursors_mixed(self):
        precursors = [
            PrecursorData(mass_kg=500, see_per_kg=1.6, is_real_data=True),
            PrecursorData(mass_kg=200, see_per_kg=2.0, is_real_data=False),
        ]
        ee, mass_real, mass_default = calculate_ee_inp_mat(precursors)
        assert ee == pytest.approx(1200.0)  # 500*1.6 + 200*2.0
        assert mass_real == 500.0
        assert mass_default == 200.0


class TestValidate8020Rule:
    """Tests de la règle 80/20 (données réelles vs par défaut)."""

    def test_zero_total(self):
        compliant, ratio = validate_80_20_rule(0, 0)
        assert compliant is False
        assert ratio == 0.0

    def test_100_percent_real(self):
        compliant, ratio = validate_80_20_rule(100, 100)
        assert compliant is True
        assert ratio == 1.0

    def test_80_percent_real_compliant(self):
        compliant, ratio = validate_80_20_rule(80, 100)
        assert compliant is True
        assert ratio == 0.8

    def test_79_percent_real_non_compliant(self):
        compliant, ratio = validate_80_20_rule(79, 100)
        assert compliant is False
        assert ratio == 0.79


class TestCalculateSee:
    """Tests du calcul SEE_g = (AttrEm_g + EEInpMat) / AL_g."""

    def test_simple_product_no_precursors(self):
        data = ProductEmissionData(
            attr_em=100,
            activity_level=1000,
            precursors=[],
        )
        result = calculate_see(data)
        assert result["see_per_kg"] == pytest.approx(0.1)
        assert result["ee_inp_mat"] == 0
        assert result["rule_80_20_compliant"] is True
        assert result["warnings"] == []

    def test_product_with_precursors(self):
        precursors = [
            PrecursorData(mass_kg=1050, see_per_kg=1.6, is_real_data=True),
        ]
        data = ProductEmissionData(
            attr_em=50,
            activity_level=1000,
            precursors=precursors,
        )
        result = calculate_see(data)
        # EEInpMat = 1050 * 1.6 = 1680, numerator = 50 + 1680 = 1730
        assert result["see_per_kg"] == pytest.approx(1.73)
        assert result["ee_inp_mat"] == pytest.approx(1680.0)
        assert result["rule_80_20_compliant"] is True

    def test_activity_level_zero_raises(self):
        data = ProductEmissionData(
            attr_em=100,
            activity_level=0,
            precursors=[],
        )
        with pytest.raises(ValueError, match="strictement positif"):
            calculate_see(data)

    def test_80_20_violation_warning(self):
        precursors = [
            PrecursorData(mass_kg=200, see_per_kg=1.0, is_real_data=True),
            PrecursorData(mass_kg=800, see_per_kg=1.5, is_real_data=False),
        ]
        data = ProductEmissionData(
            attr_em=0,
            activity_level=1000,
            precursors=precursors,
        )
        result = calculate_see(data)
        assert result["rule_80_20_compliant"] is False
        assert "80/20" in result["warnings"][0]
        assert result["real_data_ratio"] == 0.2


class TestCalculateSeeRecursive:
    """Tests du calcul SEE récursif pour BOM."""

    def test_flat_bom(self):
        bom = {
            "attr_em": 50,
            "activity_level": 1000,
            "precursors": [
                {"mass_kg": 1050, "see_per_kg": 1.6, "is_real_data": True},
            ],
        }
        result = calculate_see_recursive(bom)
        assert result["see_per_kg"] == pytest.approx(1.73)

    def test_nested_bom(self):
        bom = {
            "attr_em": 0,
            "activity_level": 100,
            "precursors": [
                {
                    "mass_kg": 100,
                    "see_per_kg": None,
                    "is_real_data": True,
                    "nested_bom": {
                        "attr_em": 10,
                        "activity_level": 100,
                        "precursors": [],
                    },
                },
            ],
        }
        result = calculate_see_recursive(bom)
        # nested SEE = 10/100 = 0.1, EEInpMat = 100*0.1 = 10, SEE = 10/100 = 0.1
        assert result["see_per_kg"] == pytest.approx(0.1)


class TestCBAMCalculator:
    """Tests du calculateur avec modèles SQLAlchemy."""

    def test_calculate_see_from_product(self, sample_product):
        calc = CBAMCalculator()
        result = calc.calculate_see(sample_product)
        assert isinstance(result, CBAMCalculationResult)
        assert result.see_kg_co2_per_tonne > 0
        assert result.real_data_ratio == 1.0
        assert result.compliant_80_20 is True

    def test_calculation_result_attributes(self, sample_product):
        calc = CBAMCalculator()
        result = calc.calculate_see(sample_product)
        assert hasattr(result, "warnings")
        assert isinstance(result.warnings, list)
