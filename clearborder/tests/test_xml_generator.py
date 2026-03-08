"""
Tests du générateur XML CBAM — structure, validation, conformité.
"""
import xml.etree.ElementTree as ET

from app.xml_generator import (
    create_cbam_report_xml,
    CBAMReportGenerator,
    validate_xml_structure,
)

CBAM_NS = "https://taxation-customs.ec.europa.eu/cbam"


def _find_by_localname(parent, localname: str):
    """Trouve le premier élément par nom local (ignore namespace)."""
    for e in parent.iter():
        tag_local = e.tag.split("}")[-1] if "}" in e.tag else e.tag
        if tag_local == localname:
            return e
    return None


def _findall_by_localname(parent, localname: str):
    """Trouve tous les éléments par nom local."""
    return [e for e in parent.iter() if (e.tag.split("}")[-1] if "}" in e.tag else e.tag) == localname]


class TestCreateCbamReportXml:
    """Tests de la génération XML."""

    def test_basic_structure(self):
        xml = create_cbam_report_xml(
            declarant_id="EU-12345",
            reporting_period="2026-Q1",
            products=[
                {
                    "cn_code": "7208",
                    "product_name": "Tôle acier",
                    "quantity_kg": 5000,
                    "see_per_kg": 1.65,
                    "country_of_origin": "TR",
                },
            ],
        )
        root = ET.fromstring(xml)
        assert root.tag.endswith("CBAMReport") or root.tag == "CBAMReport"
        assert root.get("reportingPeriod") == "2026-Q1"

    def test_report_metadata(self):
        xml = create_cbam_report_xml(
            declarant_id="EU-999",
            reporting_period="2026-Q2",
            products=[],
        )
        root = ET.fromstring(xml)
        meta = _find_by_localname(root, "ReportMetadata")
        assert meta is not None
        decl = _find_by_localname(meta, "DeclarantId")
        assert decl is not None
        assert decl.text == "EU-999"

    def test_multiple_products(self):
        products = [
            {"cn_code": "7208", "product_name": "Acier", "quantity_kg": 1000, "see_per_kg": 1.5, "country_of_origin": "TR"},
            {"cn_code": "7606", "product_name": "Alu", "quantity_kg": 500, "see_per_kg": 8.0, "country_of_origin": "CN"},
        ]
        xml = create_cbam_report_xml(
            declarant_id="EU-1",
            reporting_period="2026-Q1",
            products=products,
        )
        root = ET.fromstring(xml)
        prods_elem = _find_by_localname(root, "ReportedProducts")
        prods = _findall_by_localname(prods_elem, "Product")
        assert len(prods) == 2

    def test_installation_emissions_section(self):
        xml = create_cbam_report_xml(
            declarant_id="EU-1",
            reporting_period="2026-Q1",
            products=[],
            installation_emissions={
                "INST-001": {"country": "TR", "sector": "iron_steel", "total_emissions": 15000},
            },
        )
        root = ET.fromstring(xml)
        inst_elem = _find_by_localname(root, "Installations")
        assert inst_elem is not None


class TestCBAMReportGenerator:
    """Tests du générateur de rapports."""

    def test_generate_quarterly_report(self):
        gen = CBAMReportGenerator()
        results = [
            {
                "cn_code": "7208",
                "description": "Tôle acier",
                "see_kg_co2_per_tonne": 1650,
                "quantity_tonnes": 5,
                "country_of_origin": "TR",
            },
        ]
        xml = gen.generate_quarterly_report(
            declarant_id="EU-1",
            reporting_period="2026-Q1",
            results=results,
        )
        root = ET.fromstring(xml)
        assert root is not None
        # quantity_tonnes=5 -> quantity_kg=5000
        prods_elem = _find_by_localname(root, "ReportedProducts")
        assert prods_elem is not None
        prods = _findall_by_localname(prods_elem, "Product")
        assert len(prods) >= 1
        qty = _find_by_localname(prods[0], "Quantity")
        assert qty is not None
        assert qty.text == "5000"


class TestValidateXmlStructure:
    """Tests de validation de structure XML."""

    def test_valid_xml_passes(self):
        xml = create_cbam_report_xml(
            declarant_id="EU-1",
            reporting_period="2026-Q1",
            products=[
                {"cn_code": "7208", "product_name": "Acier", "quantity_kg": 1000, "see_per_kg": 1.5, "country_of_origin": "TR"},
            ],
        )
        valid, errors = validate_xml_structure(xml)
        assert valid is True
        assert len(errors) == 0

    def test_invalid_root_fails(self):
        invalid_xml = '<?xml version="1.0"?><WrongRoot></WrongRoot>'
        valid, errors = validate_xml_structure(invalid_xml)
        assert valid is False
        assert any("CBAMReport" in e for e in errors)

    def test_malformed_xml_fails(self):
        valid, errors = validate_xml_structure("<not valid xml")
        assert valid is False
        assert len(errors) > 0
