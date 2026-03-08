# Audit : Vision Initiale vs Application ClearBorder

> Comparaison exhaustive entre ce qui était prévu dans l'idée New Wave / RegTech et ce que l'application ClearBorder fait aujourd'hui.

---

## 1. Vue d'Ensemble

| Dimension | Vision Initiale (Docs) | ClearBorder Actuel | Écart |
|-----------|------------------------|---------------------|-------|
| **Scope produit** | 6 pain points (CBAM + Tariffs US + Classification ML + Landed Cost + Audit + DORA) | 1 pain point (CBAM uniquement) | ~17% du scope |
| **Architecture** | API Gateway + Message Queue + Workers + PostgreSQL | API monolithique + SQLite | Simplifié |
| **Phase plan** | Phase 0 (validation) → Phase 1 (MVP 8 sem) → Phase 2 (traction) | Phase 1 partielle, sans Phase 0 | Pas de validation marché |
| **Déploiement** | Cloud (Fargate/Cloud Run), CI/CD, monitoring | Local uniquement, Docker présent | Non déployé |

---

## 2. Les 6 Pain Points — État par État

### Pain Point 1 : Classification HTS/CN par ML

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Classification manuelle lente (5-15 min/ligne), 10-30% d'erreurs | — |
| **Solution** | Pipeline NLP/ML (Transformer/XGBoost), Top-3 codes + score de confiance | ❌ **Aucun** — L'utilisateur saisit le code CN manuellement |
| **Données** | Rulings CBP, EBTI (~1M+), entraînement sur corpus douanier | ❌ Table `cn_codes` vide, pas de données TARIC |
| **Métrique** | Précision Top-1 > 85%, < 2 s par ligne | — |

**Verdict** : **0% réalisé** — Priorité P0 dans le plan, non implémenté.

---

### Pain Point 2 : Tariff Stacking US

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Arbre de décision 5-7 régimes (Section 122, 301, 232, EO 14289, USMCA, anti-dumping) | — |
| **Solution** | Moteur DAG, règles en base (rules-as-data), versionnement temporel | ❌ **Aucun** |
| **Métrique** | Taux effectif en < 500 ms, détection exclusions 5-15% | — |

**Verdict** : **0% réalisé** — Priorité P0, non implémenté.

---

### Pain Point 3 : Calcul CBAM Mass Balance

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Calcul SEE récursif, règle 80/20, données fournisseurs | ✅ |
| **Solution** | Moteur Annexe IV, BOM, export XML XSD | ✅ **Partiel** |
| **Formule SEE** | SEE_g = (AttrEm_g + Σ M_i×SEE_i) / AL_g | ✅ Implémentée |
| **Règle 80/20** | Validation ratio données réelles ≥ 80% | ✅ Implémentée |
| **Export XML** | Conforme schéma XSD TAXUD | ✅ Structure XML, validation XSD non stricte |
| **Connexion O3CI** | Récupération données installations tierces | ❌ Non implémenté |
| **Interface collecte fournisseurs** | Formulaire multilingue, guide étape par étape | ⚠️ Formulaire basique dans le dashboard (pas dédié fournisseurs) |
| **Cas limites** | Coproduits, boucles recyclage, mix électrique variable | ❌ Cas simples uniquement |
| **6 secteurs CBAM** | Acier, alu, ciment, engrais, hydrogène, électricité | ⚠️ Structure prête, données par défaut partiellement (acier, alu, ciment) |

**Verdict** : **~70% réalisé** — Cœur du MVP livré, cas complexes et O3CI manquants.

---

### Pain Point 4 : Total Landed Cost

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Prix FOB + fret + assurance + droits + TVA + manutention + CBAM + courtage | — |
| **Solution** | API multiparamétrique, simulation multi-scénarios, indices fret temps réel | ❌ **Aucun** |
| **Métrique** | Précision ±2%, réponse < 1 s | — |

**Verdict** : **0% réalisé** — Priorité P1, non implémenté.

---

### Pain Point 5 : Audit Trail / Traçabilité

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Justification de chaque classification/taux pour audit douanier | — |
| **Solution** | Compliance Record horodaté et signé, input → règles → output, rétention 5-7 ans | ❌ **Aucun** — Pas de log d'audit |
| **Métrique** | 100% traçable, dossier audit < 30 min | — |

**Verdict** : **0% réalisé** — Priorité P1, non implémenté.

---

### Pain Point 6 : Module DORA

| Élément | Prévu | Réalisé |
|---------|-------|---------|
| **Problème** | Cartographie risques ICT supply chain pour entités financières | — |
| **Solution** | Graphe de dépendances, scoring résilience, reporting DORA Chapter V | ❌ **Aucun** |

**Verdict** : **0% réalisé** — Priorité P2, non implémenté.

---

## 3. Plan d'Exécution 90 Jours — Réalisation

### Phase 0 — Validation Marché (Semaines 1-3)

| Action | Prévu | Réalisé |
|--------|-------|---------|
| Lister 80 courtiers EU | ✅ | ❌ |
| Script d'interview + cold emails | ✅ | ❌ |
| 15-20 interviews discovery | ✅ | ❌ |
| Rapport validation + Go/No-Go | ✅ | ❌ |

**Verdict** : **0%** — Phase entièrement sautée.

---

### Phase 1 — Construction MVP (Semaines 4-8)

| Livrable | Prévu | Réalisé |
|----------|-------|---------|
| Repo Git, CI/CD, Docker | ✅ | ⚠️ Docker présent, pas de CI/CD |
| Nomenclature CN via API TARIC | ✅ | ❌ Table `cn_codes` vide |
| Schéma XSD CBAM + validateur | ✅ | ⚠️ XML généré, validation XSD non stricte |
| Modèles BDD installations, produits, précurseurs | ✅ | ✅ |
| API CRUD installations + produits | ✅ | ✅ |
| Calcul SEE simple + complexe | ✅ | ✅ |
| Règle 80/20 + alertes | ✅ | ✅ |
| Générateur XML CBAM | ✅ | ✅ |
| Formulaire collecte fournisseurs | ✅ | ⚠️ Formulaire produit dans dashboard, pas dédié |
| Dashboard minimal | ✅ | ✅ Streamlit |
| Valeurs par défaut sectorielles | ✅ | ✅ `default_emission_factors` |
| Auth API, chiffrement, sécurité | ✅ | ❌ Pas d'auth |
| Tests de charge | ✅ | ❌ |
| Documentation API | ✅ | ✅ OpenAPI auto-générée |
| Déploiement cloud | ✅ | ❌ Local uniquement |

**Verdict** : **~60%** — Cœur CBAM livré, socle de données et déploiement manquants.

---

### Phase 2 — Traction (Semaines 9-13)

| Action | Prévu | Réalisé |
|--------|-------|---------|
| Bêta-testeurs | ✅ | ❌ |
| Conversion clients payants | ✅ | ❌ |
| Étude de cas | ✅ | ❌ |
| Page pricing | ✅ | ❌ |
| Contacts white-label | ✅ | ❌ |

**Verdict** : **0%** — Non démarré.

---

## 4. Architecture Technique — Prévu vs Réel

| Composant | Vision | ClearBorder |
|-----------|--------|-------------|
| **API** | FastAPI + Auth (API Key/OAuth2) + Rate limiting | FastAPI, pas d'auth |
| **Base de données** | PostgreSQL | SQLite |
| **Message Queue** | Redis/SQS pour calculs asynchrones | Aucune — tout synchrone |
| **Classification Service** | ML (HTS/CN) | Absent |
| **Landed Cost Service** | Tariff DAG + CBAM | Absent |
| **CBAM Worker** | Worker isolé, batch | Intégré dans l'API |
| **Report Generator** | Worker XML | Intégré dans l'API |
| **Cloud** | AWS Fargate / GCP Cloud Run | Local |
| **CI/CD** | GitHub Actions | Absent |
| **Monitoring** | Sentry, Prometheus/Grafana | Absent |

---

## 5. Modèle de Monétisation — Prévu vs Réel

| Élément | Vision | ClearBorder |
|---------|--------|-------------|
| **Pricing** | 490€/mois Starter, 1490€ Pro, 8K€ Enterprise | — Pas de pricing implémenté |
| **Facturation** | Par appel API (0,15$/classification) + % économies | — |
| **Cibles** | Courtiers EU, éditeurs ERP white-label | — Pas de ciblage commercial |
| **Site web** | Landing, pricing, études de cas | — Absent |

---

## 6. Synthèse : Ce qui Fonctionne Aujourd'hui

### ✅ Livré et opérationnel

1. **Moteur CBAM** — Calcul SEE (Annexe IV), formule Mass Balance, règle 80/20
2. **API REST** — CRUD installations, produits, génération rapport
3. **Export XML** — Structure CBAM Quarterly Report
4. **Dashboard Streamlit** — Création installations/produits, génération rapport, téléchargement XML
5. **Données par défaut** — Facteurs d'émission secteur/pays (acier, alu, ciment)
6. **Produits avec précurseurs** — BOM à un niveau, calcul récursif de base

### ⚠️ Partiel ou simplifié

1. **Validation XSD** — XML généré mais pas de validation stricte contre le schéma TAXUD officiel
2. **Formulaire fournisseurs** — Les données sont saisies dans le formulaire produit, pas de module dédié
3. **Secteurs CBAM** — 6 secteurs prévus, facteurs par défaut pour 3 (acier, alu, ciment)
4. **Produits sans précurseurs** — Calcul possible mais pas de fallback automatique sur émissions installation

### ❌ Non réalisé

1. Classification HTS/CN par ML
2. Tariff Stacking US (DAG, Section 122/301/232)
3. Total Landed Cost
4. Audit trail / traçabilité
5. Module DORA
6. Connexion O3CI
7. Nomenclature CN/TARIC complète
8. Auth API, rate limiting
9. Déploiement cloud
10. Validation marché (interviews)
11. Bêta-testeurs, clients payants
12. Site web, pricing

---

## 7. Score Global

| Dimension | Score | Commentaire |
|-----------|-------|-------------|
| **Pain Points (6)** | 1/6 complet, 1 partiel | Seul CBAM est livré |
| **Plan 90j — Phase 0** | 0% | Validation marché non faite |
| **Plan 90j — Phase 1** | ~60% | Cœur CBAM + dashboard, pas de TARIC ni déploiement |
| **Plan 90j — Phase 2** | 0% | Pas de traction |
| **Architecture** | ~30% | Simplifiée, pas de queue ni workers |
| **Monétisation** | 0% | Pas de pricing ni GTM |

**Score global : ~25-30% de la vision initiale.**

---

## 8. Recommandations

### Pour aller vers la vision complète

1. **Court terme** — Valider le CBAM actuel : interviews courtiers, premier client bêta
2. **Moyen terme** — Charger la nomenclature TARIC, ajouter la classification ML (baseline TF-IDF + XGBoost)
3. **Long terme** — Tariff Stacking US, Landed Cost, audit trail

### Pour maximiser la valeur du MVP actuel

1. Déployer en production (Cloud Run, domaine)
2. Ajouter l'authentification API
3. Valider le schéma XML contre le XSD officiel TAXUD
4. Créer une landing page + démo

---

*Audit réalisé le 7 mars 2026 — Document de référence pour le suivi du projet.*
