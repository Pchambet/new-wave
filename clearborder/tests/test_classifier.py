"""
Tests du classifieur CN — fallback mots-clés, suggestions.
"""
import pytest

from app.classifier import classify, _fallback_classify, train_classifier


class TestFallbackClassify:
    """Tests du fallback par mots-clés (sans modèle ML)."""

    def test_acier_keywords(self):
        result = _fallback_classify("tôle acier laminée à chaud", top_k=3)
        assert len(result) > 0
        codes = [r["code"] for r in result]
        assert "7208" in codes

    def test_tube_keywords(self):
        result = _fallback_classify("tube soudé en acier", top_k=3)
        assert len(result) > 0
        codes = [r["code"] for r in result]
        assert "7306" in codes

    def test_ciment_keywords(self):
        result = _fallback_classify("ciment portland", top_k=3)
        assert len(result) > 0
        assert "2523" in [r["code"] for r in result]

    def test_unknown_returns_fallback(self):
        result = _fallback_classify("xyz inconnu produit", top_k=3)
        assert len(result) > 0
        assert result[0]["code"] == "7208"
        assert "confidence" in result[0]

    def test_top_k_respected(self):
        result = _fallback_classify("acier laminé plaque feuille bande", top_k=2)
        assert len(result) <= 2


class TestClassify:
    """Tests de l'API classify (ML ou fallback)."""

    def test_returns_list_of_suggestions(self):
        result = classify("tôle acier", top_k=3)
        assert isinstance(result, list)
        for r in result:
            assert "code" in r
            assert "confidence" in r
            assert isinstance(r["code"], str)
            assert 0 <= r["confidence"] <= 1

    def test_top_k_parameter(self):
        result = classify("acier", top_k=5)
        assert len(result) <= 5


class TestTrainClassifier:
    """Tests de l'entraînement du modèle."""

    def test_requires_minimum_samples(self):
        pytest.importorskip("sklearn")
        result = train_classifier(["a", "b"], ["7208", "7208"])
        assert "error" in result

    def test_train_success(self):
        pytest.importorskip("sklearn")
        descriptions = [
            "tôle acier laminée",
            "plaque acier",
            "feuille acier",
            "tube soudé acier",
            "ciment portland",
        ]
        codes = ["7208", "7208", "7208", "7306", "2523"]
        result = train_classifier(descriptions, codes)
        assert "accuracy" in result
        assert result["n_samples"] == 5
        assert result["n_classes"] == 3
