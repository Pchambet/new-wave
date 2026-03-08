"""
Tests d'intégration API — endpoints FastAPI.
"""
import pytest
from fastapi.testclient import TestClient


class TestHealth:
    """Tests des endpoints de santé."""

    def test_root(self, client: TestClient):
        r = client.get("/")
        assert r.status_code == 200
        data = r.json()
        assert data["name"] == "ClearBorder"
        assert "version" in data

    def test_health(self, client: TestClient):
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"


class TestInstallations:
    """Tests CRUD installations."""

    def test_create_installation(self, client: TestClient):
        payload = {
            "name": "Aciérie Test",
            "country_code": "TR",
            "sector": "iron_steel",
            "emissions_per_tonne": 1.65,
        }
        r = client.post("/api/v1/installations", json=payload)
        assert r.status_code == 200
        data = r.json()
        assert data["name"] == "Aciérie Test"
        assert data["country_code"] == "TR"
        assert "id" in data

    def test_list_installations(self, client: TestClient):
        r = client.get("/api/v1/installations")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_get_installation_not_found(self, client: TestClient):
        r = client.get("/api/v1/installations/99999")
        assert r.status_code == 404

    def test_get_installation(self, client: TestClient):
        create = client.post("/api/v1/installations", json={
            "name": "Inst", "country_code": "CN", "sector": "iron_steel",
        })
        inst_id = create.json()["id"]
        r = client.get(f"/api/v1/installations/{inst_id}")
        assert r.status_code == 200
        assert r.json()["id"] == inst_id


class TestProducts:
    """Tests CRUD produits."""

    def test_create_product_requires_installation(self, client: TestClient):
        # Créer d'abord une installation
        inst = client.post("/api/v1/installations", json={
            "name": "Inst", "country_code": "TR", "sector": "iron_steel",
        })
        inst_id = inst.json()["id"]
        payload = {
            "name": "Tôle acier",
            "cn_code": "7208",
            "sector": "iron_steel",
            "installation_id": inst_id,
            "activity_level": 1000,
            "attributed_emissions": 50,
            "precursors": [
                {"mass_kg": 1050, "see_per_kg": 1.6, "is_real_data": True},
            ],
        }
        r = client.post("/api/v1/products", json=payload)
        assert r.status_code == 200
        data = r.json()
        assert data["name"] == "Tôle acier"
        assert data["cn_code"] == "7208"

    def test_list_products(self, client: TestClient):
        r = client.get("/api/v1/products")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_get_product_not_found(self, client: TestClient):
        r = client.get("/api/v1/products/99999")
        assert r.status_code == 404


class TestCbamReport:
    """Tests génération rapport CBAM."""

    def test_generate_report_requires_valid_products(self, client: TestClient):
        payload = {
            "declarant_id": "EU-001",
            "reporting_period": "2026-Q1",
            "products": [{"product_id": 99999, "quantity_tonnes": 10}],
        }
        r = client.post("/api/v1/generate-cbam-report", json=payload)
        assert r.status_code == 400

    def test_generate_report_success(self, seeded_client: TestClient):
        # seeded_client a une installation et un produit
        products = seeded_client.get("/api/v1/products").json()
        assert len(products) >= 1
        product_id = products[0]["id"]
        payload = {
            "declarant_id": "EU-CBAM-TEST",
            "reporting_period": "2026-Q1",
            "products": [{"product_id": product_id, "quantity_tonnes": 5}],
        }
        r = seeded_client.post("/api/v1/generate-cbam-report", json=payload)
        assert r.status_code == 200
        data = r.json()
        assert "results" in data
        assert "xml_content" in data
        assert "compliant" in data
        assert len(data["results"]) >= 1
        assert "CBAMReport" in data["xml_content"]


class TestCnCodes:
    """Tests codes CN."""

    def test_list_cn_codes_empty(self, client: TestClient):
        r = client.get("/api/v1/cn-codes")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_list_cn_codes_with_data(self, seeded_client: TestClient):
        r = seeded_client.get("/api/v1/cn-codes")
        assert r.status_code == 200
        codes = r.json()
        assert isinstance(codes, list)
        if len(codes) > 0:
            assert "code" in codes[0]
            assert "description" in codes[0]


class TestClassify:
    """Tests classification CN."""

    def test_classify_product(self, client: TestClient):
        r = client.post("/api/v1/classify", json={
            "description": "Tôle acier laminée à chaud",
            "top_k": 3,
        })
        assert r.status_code == 200
        data = r.json()
        assert "suggestions" in data
        assert len(data["suggestions"]) >= 1
        assert "code" in data["suggestions"][0]
        assert "confidence" in data["suggestions"][0]
