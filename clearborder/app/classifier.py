"""
Classification HTS/CN par ML - Baseline TF-IDF + Classifier
Suggère des codes CN à partir de descriptions produits.
"""

import pickle
from pathlib import Path
from typing import Optional

# Lazy import pour éviter de charger sklearn au démarrage
_vectorizer = None
_classifier = None
_labels = None


def _get_model_path() -> Path:
    return Path(__file__).parent.parent / "models" / "cn_classifier.pkl"


def train_classifier(descriptions: list[str], codes: list[str]) -> dict:
    """
    Entraîne le classifieur sur (description, code_cn).
    Retourne les métriques (accuracy, etc.)
    """
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import cross_val_score
        from sklearn.pipeline import Pipeline
    except ImportError:
        raise ImportError("scikit-learn requis: pip install scikit-learn")

    if len(descriptions) < 5:
        return {"error": "Minimum 5 exemples requis pour l'entraînement"}

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=500)),
    ])
    pipeline.fit(descriptions, codes)
    scores = cross_val_score(pipeline, descriptions, codes, cv=min(3, len(descriptions) - 1))
    acc = float(scores.mean())

    model_path = _get_model_path()
    model_path.parent.mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump({"pipeline": pipeline, "labels": list(set(codes))}, f)

    return {"accuracy": round(acc, 4), "n_samples": len(descriptions), "n_classes": len(set(codes))}


def classify(description: str, top_k: int = 3) -> list[dict]:
    """
    Suggère les top_k codes CN pour une description.
    Retourne [{"code": "7208", "confidence": 0.85, "description": "..."}, ...]
    """
    global _vectorizer, _classifier, _labels
    model_path = _get_model_path()

    if not model_path.exists():
        return _fallback_classify(description, top_k)

    try:
        with open(model_path, "rb") as f:
            data = pickle.load(f)
        pipeline = data["pipeline"]
        labels = data.get("labels", [])
    except Exception:
        return _fallback_classify(description, top_k)

    try:
        probs = pipeline.predict_proba([description])[0]
        label_to_idx = {l: i for i, l in enumerate(pipeline.classes_)}
        results = []
        for code in labels:
            idx = label_to_idx.get(code, 0)
            conf = float(probs[idx]) if idx < len(probs) else 0.0
            results.append({"code": code, "confidence": round(conf, 4)})
        results.sort(key=lambda x: x["confidence"], reverse=True)
        return results[:top_k]
    except Exception:
        return _fallback_classify(description, top_k)


def _fallback_classify(description: str, top_k: int) -> list[dict]:
    """
    Fallback basé sur des mots-clés quand le modèle n'est pas entraîné.
    """
    keywords = {
        "7208": ["acier", "laminé", "chaud", "tôle", "plaque", "feuille", "bande"],
        "7306": ["tube", "tuyau", "soudé", "profilé", "creux"],
        "7606": ["aluminium", "alu", "plaque", "feuille", "bande"],
        "2523": ["ciment", "portland"],
        "3102": ["engrais", "azoté", "urée", "nitrate"],
        "7213": ["barre", "profilé", "laminé"],
    }
    desc_lower = description.lower()
    scores = []
    for code, kws in keywords.items():
        score = sum(1 for kw in kws if kw in desc_lower) / max(len(kws), 1)
        if score > 0:
            scores.append({"code": code, "confidence": min(round(score * 0.5, 4), 0.95)})
    scores.sort(key=lambda x: x["confidence"], reverse=True)
    return scores[:top_k] if scores else [{"code": "7208", "confidence": 0.3, "description": "Acier (fallback)"}]
