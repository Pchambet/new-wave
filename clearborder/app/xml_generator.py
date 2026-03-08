"""
Générateur de rapports XML CBAM Quarterly Report
Structure conforme au schéma XSD TAXUD (simplifié pour MVP)
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from pathlib import Path
from typing import Optional
from decimal import Decimal


def create_cbam_report_xml(
    declarant_id: str,
    reporting_period: str,  # Format: "2026-Q1"
    products: list[dict],
    installation_emissions: Optional[dict] = None,
) -> str:
    """
    Génère un rapport XML CBAM trimestriel.
    
    products: liste de dicts avec:
    - cn_code: code nomenclature CN (8 chiffres)
    - product_name: nom du produit
    - quantity_kg: quantité importée en kg
    - see_per_kg: émissions spécifiques en kg CO2e/kg
    - country_of_origin: pays d'origine (code ISO)
    - installation_id: ID installation (optionnel)
    """
    # Namespace CBAM (à adapter selon schéma officiel TAXUD)
    ns = {
        "cbam": "https://taxation-customs.ec.europa.eu/cbam",
    }
    
    # Root element
    root = ET.Element("CBAMReport", attrib={
        "xmlns": "https://taxation-customs.ec.europa.eu/cbam",
        "version": "1.0",
        "reportingPeriod": reporting_period,
    })
    
    # Métadonnées
    meta = ET.SubElement(root, "ReportMetadata")
    ET.SubElement(meta, "DeclarantId").text = declarant_id
    ET.SubElement(meta, "ReportDate").text = datetime.utcnow().strftime("%Y-%m-%d")
    ET.SubElement(meta, "ReportType").text = "Quarterly"
    
    # Section produits
    products_elem = ET.SubElement(root, "ReportedProducts")
    
    for i, p in enumerate(products):
        product_elem = ET.SubElement(products_elem, "Product", attrib={"id": str(i + 1)})
        ET.SubElement(product_elem, "CNCode").text = str(p.get("cn_code", ""))
        ET.SubElement(product_elem, "ProductName").text = str(p.get("product_name", ""))
        ET.SubElement(product_elem, "Quantity").text = str(p.get("quantity_kg", 0))
        ET.SubElement(product_elem, "Unit").text = "kg"
        ET.SubElement(product_elem, "SpecificEmbeddedEmissions").text = str(
            round(float(p.get("see_per_kg", 0)), 6)
        )
        ET.SubElement(product_elem, "UnitEmissions").text = "kgCO2e/kg"
        ET.SubElement(product_elem, "CountryOfOrigin").text = str(
            p.get("country_of_origin", "")
        )
        if p.get("installation_id"):
            ET.SubElement(product_elem, "InstallationId").text = str(p["installation_id"])
    
    # Section installations (si fournie)
    if installation_emissions:
        installations_elem = ET.SubElement(root, "Installations")
        for inst_id, data in installation_emissions.items():
            inst_elem = ET.SubElement(installations_elem, "Installation", attrib={"id": inst_id})
            ET.SubElement(inst_elem, "Country").text = data.get("country", "")
            ET.SubElement(inst_elem, "Sector").text = data.get("sector", "")
            ET.SubElement(inst_elem, "TotalEmissions").text = str(data.get("total_emissions", 0))
    
    # Pretty print
    xml_str = ET.tostring(root, encoding="unicode", method="xml")
    dom = minidom.parseString(xml_str)
    return dom.toprettyxml(indent="  ", encoding=None)


class CBAMReportGenerator:
    """Générateur de rapports XML CBAM."""

    def generate_quarterly_report(
        self,
        declarant_id: str,
        reporting_period: str,
        results: list[dict],
    ) -> str:
        """
        Génère le XML du rapport trimestriel.
        results: liste de dicts avec cn_code, description, see_kg_co2_per_tonne,
                 quantity_tonnes, country_of_origin (optionnel)
        """
        products = []
        for r in results:
            # see_kg_co2_per_tonne -> see_per_kg = / 1000
            see_per_kg = r.get("see_kg_co2_per_tonne", 0) / 1000
            qty_tonnes = r.get("quantity_tonnes", 0)
            products.append({
                "cn_code": r.get("cn_code", ""),
                "product_name": r.get("description", ""),
                "quantity_kg": qty_tonnes * 1000,
                "see_per_kg": see_per_kg,
                "country_of_origin": r.get("country_of_origin", ""),
                "installation_id": r.get("installation_id"),
            })
        return create_cbam_report_xml(
            declarant_id=declarant_id,
            reporting_period=reporting_period,
            products=products,
        )


def _local_name(tag: str) -> str:
    """Extrait le nom local d'un tag (sans namespace)."""
    return tag.split("}")[-1] if "}" in tag else tag


def _find_by_localname(parent, localname: str):
    """Trouve le premier enfant avec ce nom local."""
    for e in parent.iter():
        if _local_name(e.tag) == localname:
            return e
    return None


def _findall_by_localname(parent, localname: str) -> list:
    """Trouve tous les descendants avec ce nom local."""
    return [e for e in parent.iter() if _local_name(e.tag) == localname]


def validate_xml_against_xsd(xml_content: str, xsd_path: str | None = None) -> tuple[bool, list[str]]:
    """
    Valide le XML contre un schéma XSD TAXUD (si fourni).
    Le schéma officiel est disponible via le CBAM Declarant Portal.
    Placez cbam_report.xsd dans clearborder/schemas/ pour activer.
    """
    path = Path(xsd_path) if xsd_path else Path(__file__).parent.parent / "schemas" / "cbam_report.xsd"
    if not path.exists():
        return True, []  # Pas de XSD = skip (validation structure suffit en dev)
    try:
        from lxml import etree
        schema_doc = etree.parse(str(path))
        schema = etree.XMLSchema(schema_doc)
        doc = etree.fromstring(xml_content.encode("utf-8"))
        schema.assertValid(doc)
        return True, []
    except etree.XMLSchemaParseError as e:
        return False, [f"Schéma XSD invalide: {e}"]
    except etree.DocumentInvalid as e:
        return False, [str(err) for err in e.error_log]
    except Exception as e:
        return False, [f"Erreur validation XSD: {e}"]


def validate_xml_structure(xml_content: str) -> tuple[bool, list[str]]:
    """
    Validation stricte de la structure XML CBAM.
    Vérifie les éléments requis selon le format Quarterly Report.
    Pour validation XSD officielle : schéma TAXUD sur CBAM Registry.
    """
    errors = []
    try:
        root = ET.fromstring(xml_content)
        if _local_name(root.tag) != "CBAMReport":
            errors.append("Element racine doit être CBAMReport")

        meta = _find_by_localname(root, "ReportMetadata")
        if meta is None:
            errors.append("ReportMetadata manquante")
        else:
            for req in ["DeclarantId", "ReportDate", "ReportType"]:
                if _find_by_localname(meta, req) is None:
                    errors.append(f"ReportMetadata.{req} manquant")

        products_elem = _find_by_localname(root, "ReportedProducts")
        if products_elem is None:
            errors.append("Section ReportedProducts manquante")
        else:
            prods = _findall_by_localname(products_elem, "Product")
            for i, p in enumerate(prods):
                for req in ["CNCode", "ProductName", "Quantity", "SpecificEmbeddedEmissions", "CountryOfOrigin"]:
                    elem = _find_by_localname(p, req)
                    if elem is None or (elem.text or "").strip() == "":
                        errors.append(f"Product[{i+1}].{req} manquant ou vide")

        return len(errors) == 0, errors
    except ET.ParseError as e:
        return False, [f"Erreur XML: {str(e)}"]
