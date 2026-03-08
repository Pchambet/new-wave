# ClearBorder — Démarrage en 2 minutes

## Ce qui a été créé

**ClearBorder** est un MVP fonctionnel du moteur CBAM (Mécanisme d'Ajustement Carbone aux Frontières). Il calcule les émissions intégrées spécifiques (SEE) et génère les rapports XML pour le portail douanier EU.

### Fonctionnalités livrées

- ✅ **API REST** (FastAPI) — CRUD installations, produits, génération rapport CBAM
- ✅ **Moteur de calcul SEE** — Formule Mass Balance conforme Annexe IV Règlement 2023/956
- ✅ **Règle 80/20** — Validation automatique pour les biens complexes
- ✅ **Export XML** — Structure compatible portail CBAM TAXUD
- ✅ **Dashboard Streamlit** — Interface pour créer installations, produits, générer rapports
- ✅ **Base SQLite** — Fonctionne sans PostgreSQL (dev local)
- ✅ **Données de démo** — Installation aciérie Turquie + produit tôle d'acier

---

## Lancer l'outil

### Option 1 : Tout en un (recommandé)

```bash
cd clearborder
./run.sh
```

- **API** : http://localhost:8000
- **Docs API** : http://localhost:8000/docs
- **Dashboard** : http://localhost:8501

### Option 2 : Conteneurs avec PostgreSQL (prod-like)

Sur Mac, [OrbStack](https://orbstack.dev) est recommandé. PostgreSQL + API + Dashboard.

```bash
cd clearborder
docker compose up
```

Au premier lancement, charger les données de démo :
```bash
make seed
```

- **API** : http://localhost:8000
- **Docs API** : http://localhost:8000/docs
- **Dashboard** : http://localhost:8501

### Option 3 : Manuel

```bash
cd clearborder
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python scripts/seed_data.py

# Terminal 1
uvicorn app.main:app --reload --port 8000

# Terminal 2
streamlit run dashboard/app.py --port 8501
```

---

## Test rapide (sans interface)

```bash
# Après avoir lancé l'API
curl -X POST http://localhost:8000/api/v1/generate-cbam-report \
  -H "Content-Type: application/json" \
  -d '{"declarant_id":"EU-001","reporting_period":"2026-Q1","products":[{"product_id":1,"quantity_tonnes":10}]}'
```

---

## Prochaines étapes (pour vendre / trouver des partenaires)

1. **Montrer le démo** — Le dashboard + l'API avec les données seed prouvent que ça marche
2. **Pitch 30 secondes** — "ClearBorder calcule automatiquement les émissions CBAM et génère le XML pour les douanes. Les courtiers passent de 2 semaines à 2 heures."
3. **Cibles** — Courtiers en douane EU (Belgique, NL, DE, FR), éditeurs TMS/ERP
4. **Lever** — Pas nécessaire pour démarrer. Bootstrappable. Premier client possible en 2-3 mois.

---

*ClearBorder — Projet New Wave — MVP livré le 7 mars 2026*
