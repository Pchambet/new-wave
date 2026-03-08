# Faisabilité Technique — RegTech Supply Chain / CBAM / Tarifs

## 1. Architecture Cible

```
┌─────────────────────────────────────────────────────────┐
│                    API Gateway (Edge)                     │
│         Auth (API Key/OAuth2) + Rate Limiting            │
│              + Schema Validation (JSON)                   │
└─────────────┬───────────────────────┬───────────────────┘
              │                       │
    ┌─────────▼─────────┐   ┌────────▼────────────┐
    │  Classification    │   │  Landed Cost         │
    │  Service           │   │  Calculator Service  │
    │  (HTS/CN Lookup    │   │  (Tariff DAG +       │
    │   + ML Inference)  │   │   CBAM Engine)       │
    └─────────┬──────────┘   └────────┬─────────────┘
              │                       │
    ┌─────────▼───────────────────────▼──────────────┐
    │              Message Queue (Redis/SQS)          │
    │         (pour calculs longs : CBAM batch)       │
    └─────────┬───────────────────────┬──────────────┘
              │                       │
    ┌─────────▼─────────┐   ┌────────▼────────────┐
    │  CBAM Worker       │   │  Report Generator   │
    │  (Mass Balance     │   │  Worker             │
    │   Recursive Calc)  │   │  (XML/XSD Export)   │
    └─────────┬──────────┘   └────────┬─────────────┘
              │                       │
    ┌─────────▼───────────────────────▼──────────────┐
    │            PostgreSQL (Primary Store)            │
    │   - HTS/CN reference data                       │
    │   - Tariff rule graph (versioned)                │
    │   - Classification history & audit logs          │
    │   - Customer data & emission records             │
    └────────────────────────────────────────────────┘
```

## 2. Stack Technique Recommandée

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Langage principal | **Python** | Écosystème ML/NLP dominant. Pandas, scikit-learn, XGBoost, HuggingFace natifs. |
| API Framework | **FastAPI** | Async natif, validation Pydantic, OpenAPI auto-générée. Performant. |
| Base de données | **PostgreSQL** | ACID, JSON/JSONB natif, extensions géographiques si besoin, maturité. |
| Message Queue | **Redis (Bull)** ou **AWS SQS** | Léger pour le MVP. Passage à Kafka si scale exige. |
| ML Inference | **ONNX Runtime** ou **scikit-learn** | XGBoost/Random Forest exportés en ONNX pour inférence rapide sans GPU. |
| NLP / Embeddings | **sentence-transformers** | Embeddings pré-entraînés pour la similarité sémantique des descriptions produits. |
| XML Validation | **lxml** + **xmlschema** | Validation contre schémas XSD CBAM (TAXUD). Bibliothèques Python matures. |
| Conteneurisation | **Docker** | Portabilité. Déploiement uniforme dev/staging/prod. |
| Cloud | **AWS (Fargate)** ou **GCP (Cloud Run)** | Serverless containers. Pay-per-use. Scaling automatique. |
| CI/CD | **GitHub Actions** | Gratuit pour repos privés. Pipeline test → build → deploy. |
| Monitoring | **Sentry** (erreurs) + **Prometheus/Grafana** (métriques) | Observabilité minimale mais suffisante. |

## 3. Évaluation de Complexité par Module

### 3.1 Parseur de Bases Tarifaires (HTS/CN)

**Complexité : ★★★☆☆ (Moyenne)**

- **Source US (HTSUS)** : Disponible en format structuré (CSV/XML) sur le site de l'USITC. ~18 000 codes. Structure hiérarchique à 6 niveaux (chapitre → sous-partie → item → sous-item).
- **Source EU (CN/TARIC)** : Disponible via l'API TARIC de la Commission Européenne (REST, format XML/JSON). ~15 000 codes CN + mesures TARIC associées.
- **Difficulté réelle** : Le parsing pur est trivial. La difficulté est dans la modélisation des notes de sections/chapitres qui qualifient ou excluent des codes. Ces notes sont en langage naturel juridique et nécessitent une interprétation humaine ou NLP.

**Estimation de temps** : 1-2 semaines pour un parseur robuste avec tests.

### 3.2 Moteur de Classification ML

**Complexité : ★★★★☆ (Élevée)**

- **Données d'entraînement** : Les rulings historiques de la CBP (~500 000 rulings publics) et les EBTI (European Binding Tariff Information, ~1M+) constituent le jeu d'entraînement.
- **Approche recommandée** :
  - Phase 1 : TF-IDF + XGBoost (baseline rapide, ~80% accuracy)
  - Phase 2 : Embeddings (sentence-transformers) + classification neuronale (~85-90%)
  - Phase 3 : Fine-tuning d'un modèle Transformer sur le corpus juridique douanier (~90-95%)
- **Infrastructure** : L'entraînement initial nécessite un GPU (quelques heures sur un A100). L'inférence tourne sur CPU standard.
- **Risque technique** : La performance dépend fortement de la qualité du preprocessing (normalisation des descriptions multilingues, extraction d'entités matériaux).

**Estimation de temps** : 3-5 semaines pour un modèle baseline déployable. 3-6 mois pour atteindre une précision industrielle.

### 3.3 Graphe Décisionnel Tarifaire (US Tariff Stacking)

**Complexité : ★★★☆☆ (Moyenne)**

- L'arbre de décision est complexe mais fini et déterministe.
- Modélisable comme un DAG avec ~50-100 nœuds de décision et ~200-500 arêtes.
- Le défi est la maintenance : chaque nouvel Executive Order modifie le graphe.
- L'architecture "rules-as-data" (règles en base, pas en code) résout ce problème.

**Estimation de temps** : 2-3 semaines pour le moteur initial + la couverture des régimes principaux.

### 3.4 Moteur CBAM Mass Balance

**Complexité : ★★★★★ (Très Élevée)**

- **Difficulté mathématique** : Le calcul récursif de SEE est conceptuellement simple mais la diabolique complexité est dans les cas limites :
  - Produits avec coproduits (allocation massique des émissions entre produits principaux et sous-produits)
  - Boucles de recyclage (l'acier recyclé a des émissions différentes de l'acier primaire — comment le traiter dans le Mass Balance ?)
  - Mix électrique variable (les émissions indirectes dépendent du mix électrique du pays de production au moment de la production)
  - Données manquantes (fallback vers valeurs par défaut avec comptage 80/20)
- **Réglementation en évolution** : Les implementing acts (actes d'exécution) de la Commission sont encore en cours de publication. Le logiciel doit être adaptable.
- **Validation** : Aucun jeu de données de référence "ground truth" public n'existe pour valider les calculs. Il faudra auto-valider contre des cas manuels documentés.

**Estimation de temps** : 4-6 semaines pour un moteur fonctionnel sur les cas simples (acier direct). 3-6 mois pour la couverture complète des 6 secteurs et des cas complexes.

### 3.5 Générateur de Rapports XML/XSD

**Complexité : ★★☆☆☆ (Faible-Moyenne)**

- Le schéma XSD est publié par TAXUD.
- La génération XML conforme est un exercice de sérialisation standard.
- Le risque est dans les erreurs de mapping entre les données internes et les champs XSD.

**Estimation de temps** : 1 semaine.

## 4. Dépendances Externes Critiques

| Dépendance | Risque | Mitigation |
|------------|--------|------------|
| API TARIC (Commission EU) | Disponibilité variable, rate limits | Cache local avec mise à jour quotidienne |
| Schéma XSD CBAM (TAXUD) | Peut changer sans préavis | Versionnement + tests de régression |
| Rulings CBP (US) | Format non standardisé, scraping fragile | Base vectorielle locale, mise à jour mensuelle |
| Registre O3CI | Pas encore pleinement opérationnel en 2026 | Feature optional, pas bloquante pour le MVP |
| Prix EU ETS | Volatil, source officielle pas toujours en temps réel | Intégration ICE/EEX pour le prix spot |

## 5. Prérequis Techniques pour l'Ingénieur

| Compétence | Niveau Requis | Critique ? |
|------------|---------------|-----------|
| Python avancé | Expert | Oui |
| ML/NLP (scikit-learn, transformers) | Intermédiaire-Expert | Oui |
| SQL / PostgreSQL | Intermédiaire | Oui |
| Architecture API REST | Intermédiaire | Oui |
| Docker / Cloud deployment | Intermédiaire | Oui |
| Droit douanier international | Bases + capacité d'apprentissage | Critique mais acquérable |
| XML/XSD | Bases | Oui, mais simple |
| Réglementation CBAM | Lecture approfondie du Règlement 2023/956 | Critique |

## 6. Estimation Budget Infrastructure (MVP, 6 mois)

| Poste | Coût Mensuel | Coût 6 mois |
|-------|-------------|-------------|
| Cloud (Fargate/Cloud Run, PostgreSQL managé) | 50-150€ | 300-900€ |
| GPU pour entraînement ML (spot instances) | 50-200€ (ponctuel) | 100-400€ |
| Domaine + SSL | 5€ | 30€ |
| Monitoring (Sentry free tier + Grafana Cloud free) | 0€ | 0€ |
| Assurance E&O (si premier client) | 200-400€ | 1200-2400€ |
| **Total** | | **1 630 - 3 730€** |

**Conclusion faisabilité technique : FAISABLE par un ingénieur solo avec expertise Python/ML.** Le module le plus risqué est le moteur CBAM Mass Balance, principalement en raison de l'ambiguïté réglementaire résiduelle et de l'absence de données de validation. Tous les autres modules sont bien balisés techniquement.
