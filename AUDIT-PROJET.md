# Audit Complet du Projet New Wave — RegTech Supply Chain

> Audit réalisé le 7 mars 2025 — Projet focalisé sur l'opportunité RegTech (CBAM + Tariff Stacking)

---

## 1. Vue d'Ensemble

### 1.1 Structure Actuelle du Projet

```
new-wave/
├── new-wave.md                    # Document racine (contenu brut du rapport stratégique original)
├── benchmark-comparatif.md        # Synthèse comparative (référence aux 3 projets, décision RegTech)
├── AUDIT-PROJET.md               # Ce document
└── 01-regtech-supply-chain/       # Dossier principal du projet retenu
    ├── README.md                  # Vue d'ensemble et structure
    ├── README-github.md           # Pitch vulgarisé pour GitHub/public
    ├── 01-analyse-marche.md       # TAM/SAM/SOM, catalyseurs réglementaires
    ├── 02-benchmark-concurrentiel.md
    ├── 03-pain-points-solutions.md
    ├── 04-faiblesses-mitigation.md
    ├── 05-faisabilite-technique.md
    ├── 06-go-to-market.md
    ├── 07-modele-financier.md
    ├── 08-matrice-risques.md
    ├── 09-plan-execution-90j.md    # Plan opérationnel détaillé
    └── 10-scoring-final.md
```

### 1.2 État du Projet

| Dimension | État | Commentaire |
|-----------|------|-------------|
| **Phase** | Pré-lancement | Aucun code, aucune interview réalisée |
| **Décision stratégique** | Actée | Focus exclusif RegTech, projets 2 et 3 supprimés |
| **Documentation** | Très complète | 10+ documents d'analyse structurés |
| **Exécution** | Non démarrée | Plan 90j défini mais pas exécuté |

---

## 2. Points Forts

### 2.1 Qualité de l'Analyse

- **Rigueur méthodologique** : Chaque dimension (marché, concurrence, technique, finance, risque) est traitée dans un document dédié avec des sources et des justifications.
- **Cohérence interne** : Les chiffres se recoupent entre les documents (TAM 4,2 Mds$, ARR M12 ~450K€, score 8,10/10).
- **Profondeur réglementaire** : Le contexte CBAM (régime définitif 1er janv. 2026), IEEPA, Section 122/301/232 est bien documenté.
- **Matrice risque complète** : 9 risques identifiés avec probabilité, impact, mitigation et priorisation.

### 2.2 Positionnement Stratégique

- **Zone de convergence vide** : L'analyse concurrentielle identifie correctement que Tarifs US + CBAM EU + API moderne est une niche quasi-inoccupée.
- **Timing** : La fenêtre Q1 2026 est bien argumentée (CBAM définitif, tarifs US en chaos).
- **Ciblage progressif** : Courtiers EU → Éditeurs white-label → Importateurs directs — séquence logique.

### 2.3 Faisabilité

- **Données publiques** : HTSUS, TARIC, schémas XSD CBAM accessibles sans dépendance externe bloquante.
- **Stack maîtrisable** : Python/FastAPI/PostgreSQL — stack standard pour un ingénieur solo.
- **Budget réaliste** : ~1 400€ pour 90 jours, bootstrappable sans levée.

### 2.4 Plan d'Exécution

- **Validation marché avant code** : Semaines 1-3 dédiées aux interviews (15-20) avant toute ligne de code — approche lean correcte.
- **Jalons avec critères de succès** : Gates définis (Go/No-Go S3, MVP S7, premier client S11).
- **Séquence technique claire** : Socle données → Moteur CBAM → UI → Hardening → Bêta.

---

## 3. Lacunes et Incohérences

### 3.1 Lacunes Structurelles

| Lacune | Gravité | Détail |
|--------|---------|--------|
| **Pas de code source** | Moyenne | Le projet est 100% documentation. Aucun repo, aucun prototype. |
| **Pas de validation terrain** | Critique | Les 15-20 interviews de la Phase 0 n'ont pas été réalisées. La thèse "les courtiers paieront 490€/mois" n'est pas validée. |
| **Références temporelles obsolètes** | Moyenne | Le document cite "février 2026", "7 avril 2026" — nous sommes en mars 2025. Ces dates sont-elles des projections ou des erreurs ? |
| **Pas de structure juridique** | Faible | Aucune mention de création de société (SAS, SASU) ni de statut fiscal. |
| **Pas de nom de produit/marque** | Faible | Le projet n'a pas de nom commercial défini. |

### 3.2 Incohérences Entre Documents

| Incohérence | Localisation | Détail |
|-------------|--------------|--------|
| **Dates 2025 vs 2026** | Multiple | `new-wave.md` et les analyses parlent de "2026" comme présent. Si le projet est conçu en 2025, le CBAM définitif est pour janvier 2026 — la fenêtre est donc future, pas actuelle. |
| **Benchmark : projets 2 et 3** | `benchmark-comparatif.md` | Le document conserve les tableaux comparatifs HealthTech et Infra alors que ces projets ont été supprimés. Utile pour la trace décisionnelle, mais peut prêter à confusion. |
| **Séquencement HealthTech** | `benchmark-comparatif.md` §4 | Le diagramme mentionne encore "HealthTech (exploration)" en Phase 2 après ARR >250K€. Cohérent avec la décision, mais les dossiers HealthTech n'existent plus. |
| **Budget 90j vs 6 mois** | `07-modele-financier.md` vs `09-plan-execution-90j.md` | Plan 90j : 1 400€. Faisabilité technique : 1 630-3 730€ pour 6 mois. Pas d'incohérence mais le budget 90j ne couvre pas l'assurance E&O (400€ prorata) si premier client en M11. |

### 3.3 Hypothèses Non Vérifiées

| Hypothèse | Document | Risque |
|-----------|----------|--------|
| "70% des interviewés confirment l'urgence CBAM" | Plan 90j | Critère de Go arbitraire. Pas de benchmark sectoriel. |
| "3 clients payants en M3 (bêta → payant)" | Modèle financier | Très optimiste. Les bêta-testeurs convertis en payants en 1 mois est agressif. |
| "Cycle de vente 1-3 mois pour courtiers" | GTM | À valider. Les courtiers peuvent avoir des processus d'achat plus lents. |
| "Précision ML Top-1 > 85% en 2-3 mois" | Pain points, Faisabilité | La faisabilité technique indique 3-5 semaines pour baseline, 3-6 mois pour précision industrielle. Incohérence sur le délai. |

---

## 4. Risques Non Couverts ou Sous-Évalués

### 4.1 Risques Identifiés mais Insuffisamment Mitigés

| Risque | Évaluation | Manque |
|--------|------------|--------|
| **R8 — Burnout solo** | Score 9, priorité 1 | La mitigation "recruter dès MRR > 10K€" suppose une trésorerie pour embaucher. À 10K€ MRR avec churn, le cash flow peut ne pas permettre un recrutement immédiat. |
| **R4 — Données fournisseurs** | Probabilité élevée | Le plan 90j ne prévoit pas explicitement de module de collecte fournisseurs multilingue. C'est en "P1" dans les pain points mais absent du MVP. |
| **R6 — Responsabilité juridique** | Assurance E&O 2-5K€/an | Le budget 90j inclut 400€ prorata. Une assurance E&O complète pour un logiciel de compliance peut coûter plus cher. |

### 4.2 Risques Non Documentés

| Risque | Description |
|--------|-------------|
| **Conformité RGPD** | Les données clients (manifestes, classifications) sont des données commerciales sensibles. Hébergement UE, DPA, registre des traitements — non mentionnés. |
| **Certification / Audit** | Pour vendre à des courtiers, une certification ou un audit de la méthodologie CBAM pourrait être requis. Non planifié. |
| **Dépendance à l'API TARIC** | Si l'API TARIC change ou devient payante, impact non quantifié. |
| **Prix EU ETS** | Le premier prix trimestriel CBAM (7 avril 2026) — intégration de la source officielle non détaillée. |

---

## 5. Qualité des Documents

### 5.1 Par Document

| Document | Qualité | Complétude | Actionabilité |
|----------|---------|------------|---------------|
| `01-analyse-marche.md` | ★★★★★ | Excellente | Bonne — catalyseurs clairs |
| `02-benchmark-concurrentiel.md` | ★★★★★ | Excellente | Bonne — gaps bien identifiés |
| `03-pain-points-solutions.md` | ★★★★☆ | Bonne | Moyenne — prioritisation P0/P1/P2 utile |
| `04-faiblesses-mitigation.md` | ★★★★★ | Excellente | Bonne — stratégies concrètes |
| `05-faisabilite-technique.md` | ★★★★☆ | Bonne | Bonne — stack et complexité par module |
| `06-go-to-market.md` | ★★★★☆ | Bonne | Bonne — séquence et canaux définis |
| `07-modele-financier.md` | ★★★★☆ | Bonne | Bonne — sensibilités utiles |
| `08-matrice-risques.md` | ★★★★★ | Excellente | Bonne — tableau de synthèse clair |
| `09-plan-execution-90j.md` | ★★★★☆ | Bonne | Excellente — jalons et livrables |
| `10-scoring-final.md` | ★★★★☆ | Bonne | Moyenne — verdict synthétique |
| `README-github.md` | ★★★★★ | Excellente | Bonne — pitch vulgarisé très efficace |
| `new-wave.md` | ★★☆☆☆ | Faible | Faible — contenu brut, non structuré |

### 5.2 Document Racine (`new-wave.md`)

**Problème** : Le fichier `new-wave.md` contient le rapport stratégique original complet (les 3 opportunités) en un seul bloc de texte sans structure markdown. Il fait doublon avec le contenu des dossiers et n'est pas exploitable comme point d'entrée.

**Recommandation** : Soit le transformer en index/sommaire pointant vers les documents, soit le supprimer si redondant.

---

## 6. Recommandations Prioritaires

### 6.1 Avant de Démarrer le Plan 90j

| # | Action | Priorité | Effort |
|---|--------|----------|--------|
| 1 | **Corriger les références temporelles** | Haute | 1h |
| 2 | **Définir un nom de produit** | Moyenne | 2h |
| 3 | **Créer la structure juridique** (SASU) si engagement sérieux | Moyenne | 1-2 jours |
| 4 | **Réécrire `new-wave.md`** en sommaire/vision du projet | Basse | 30 min |

### 6.2 Pendant la Phase 0 (Semaines 1-3)

| # | Action | Priorité | Effort |
|---|--------|----------|--------|
| 1 | **Réaliser les 15-20 interviews** — c'est le gate critique | Critique | 3 semaines |
| 2 | **Documenter les critères de Go/No-Go** avec des seuils réalistes | Haute | 2h |
| 3 | **Vérifier l'accès aux sources de données** (API TARIC, schéma XSD) | Haute | 1 jour |

### 6.3 Ajustements au Plan 90j

| # | Ajustement | Raison |
|---|------------|--------|
| 1 | **Ajouter le module de collecte fournisseurs** en Semaine 6 ou 7 | Pain point P1, risque R4 élevé |
| 2 | **Réviser les hypothèses de conversion M3** | 3 bêta → payant en 1 mois est très optimiste. Prévoir 1-2. |
| 3 | **Prévoir une phase RGPD** (DPA, hébergement UE) avant le premier client | Obligation légale pour données B2B |
| 4 | **Clarifier le scope ML du MVP** | Classification HTS : baseline TF-IDF + XGBoost suffit. Pas de Transformer pour le MVP. |

### 6.4 Documents à Créer

| Document | Contenu | Utilité |
|----------|---------|---------|
| `CHANGELOG.md` | Historique des décisions et évolutions | Traçabilité |
| `ROADMAP.md` | Vision produit au-delà de 90j (M4-M12) | Alignement |
| `LEGAL.md` | CGU, politique confidentialité, conformité RGPD | Préparation commerciale |
| `.cursor/rules` ou `CONTRIBUTING.md` | Si collaboration future | Onboarding |

---

## 7. Synthèse du Verdict

### 7.1 Score Global du Projet (Documentation)

| Critère | Note /10 | Commentaire |
|---------|----------|-------------|
| Complétude de l'analyse | 9 | Très exhaustif, peu de zones d'ombre |
| Cohérence interne | 8 | Quelques incohérences mineures (dates, hypothèses) |
| Actionabilité | 8 | Plan 90j détaillé, mais dépend de la validation marché |
| Réalisme des hypothèses | 7 | Projections financières optimistes, à valider |
| Prêt pour l'exécution | 6 | Phase 0 non réalisée, pas de validation terrain |

**Score global documentation : 7,6 / 10**

### 7.2 Verdict Final

Le projet **New Wave / RegTech Supply Chain** dispose d'une **documentation d'exception** pour un projet pré-lancement. L'analyse est rigoureuse, le positionnement est clair, et le plan d'exécution est structuré.

**Cependant**, le projet n'a pas encore franchi l'étape critique de **validation du marché**. Toute la thèse repose sur l'hypothèse que des courtiers en douane EU paieront 490-1490€/mois pour un outil CBAM. Cette hypothèse doit être validée par 15-20 interviews avant tout investissement en développement.

**Recommandation** : Exécuter la Phase 0 du plan 90j (Semaines 1-3) en priorité absolue. Si le Go est confirmé, le reste du plan est solide. Si le No-Go survient, pivoter sans avoir investi dans le code.

---

*Audit réalisé le 7 mars 2025. Document vivant — à mettre à jour après chaque phase majeure.*
