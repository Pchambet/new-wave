# Benchmark Comparatif — Décision : Projet RegTech

> Document de synthèse et de décision finale.
> **Décision :** Focus exclusif sur le projet 1 (RegTech / Supply Chain). Les projets 2 et 3 ont été abandonnés.
> Analyses détaillées : [01-regtech-supply-chain/](01-regtech-supply-chain/)

---

## 1. Vue d'Ensemble

| Dimension | 🥇 RegTech / Supply Chain | 🥈 HealthTech / Bloc Opératoire | 🥉 Infra / Eau / H2 |
|-----------|--------------------------|--------------------------------|---------------------|
| **Pitch** | CBAM compliance + tariff stacking engine | Digital twin stochastique pour blocs opératoires | HSCN geospatial optimizer + leak detection |
| **Score Final** | **8.10 / 10** | **6.30 / 10** | **3.95 / 10** |
| **Recommandation** | **Lancer immédiatement** | Phase 2 (après RegTech établi) | Ne pas poursuivre en solo |

---

## 2. Comparaison Détaillée par Critère

### 2.1 Marché

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| TAM global | 4.2 Mds $ | 4.5 Mds $ | 4-5 Mds $ |
| SAM (zone cible) | 800M-1.2B $ | 1.5-2.5 Mds $ | ~1 Mds $ |
| **SOM 24 mois** | **4-12M € ARR** | **2-5M € ARR** | **500K-2M €** |
| Maturité du marché | Marché actif (réglementation en vigueur) | Marché existant mais résistant | Pré-commercial (H2) à émergent (eau) |
| Urgence client | 🔴 Critique (deadlines CBAM, tarifs appliqués) | 🟡 Modérée (inefficiences chroniques) | 🟢 Faible (pas de deadline) |
| Catalyseur réglementaire | CBAM definitif 2026, IEEPA tarifs actifs, DORA 2025 | MS-GHM, LFSS 2024, HAS indicateurs | CSRD (eau, indirect), AFIR (H2, horizon 2030) |

**Verdict Marché** : Le RegTech est le seul avec un marché urgent et des deadlines réglementaires contraignantes. Le HealthTech a un marché existant mais des cycles longs. L'Infra/H2 est fondamentalement un pari sur le futur.

### 2.2 Concurrence

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| Score concurrentiel | 8/10 | 6/10 | 5/10 |
| Nb de concurrents directs | ~3-5 | ~5-8 | ~2-3 |
| Concurrents financés | Avalara, Descartes | LeanTaaS (200M$), Qventus (100M$) | WINT (14M$), Fracta |
| Zone de convergence vide | **OUI** (CBAM+Tariffs = quasi vide) | **Partiellement** (EU OR = vide, mais US saturé) | **OUI** (mais reflète peut-être l'absence de demande) |
| Barrière à l'entrée propre | Expertise réglementaire + pipeline ML | Accès données cliniques | Intégration terrain SCADA |
| Moat long terme | Faible (données publiques) | Fort (si data clinique acquise) | Moyen (relations terrain) |

**Verdict Concurrence** : Le RegTech a la meilleure fenêtre d'opportunité (convergence CBAM+Tariffs vide). Le HealthTech a le meilleur moat potentiel. L'Infra a peu de concurrence mais aussi peu de demande prouvée.

### 2.3 Faisabilité Technique

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| Score faisabilité | 9/10 | 6/10 | 5/10 |
| Complexité du module le plus dur | ★★★★★ (CBAM Mass Balance) | ★★★★★ (Intégration FHIR/HL7) | ★★★★★ (MILP HSCN) |
| Données d'entraînement | **Publiques** (tarifs douaniers, taux CBAM) | **Synthétiques** (Synthea) puis cliniques | **Synthétiques** puis SCADA |
| Dépendances externes | Faible (APIs publiques) | Forte (hôpitaux, DSI, HDS) | Moyenne (SCADA, clients industriels) |
| MVP en 90 jours ? | **OUI** (confiant) | **Partiellement** (démo Synthea, pas de données réelles) | **Partiellement** (démo eau sur synthétique) |
| Stack size | Compact (Python/FastAPI/PG) | Large (FHIR, HL7, HDS, Synthea) | Très large (géo, MILP, ML, SCADA, edge) |
| Budget 6 mois | 1 630-3 730€ | 1 800-7 800€ | 300-1 700€ |

**Verdict Technique** : Le RegTech est le plus faisable techniquement pour un solo (données publiques, stack compact, pas de dépendance externe). Le HealthTech est bloqué par l'accès aux données cliniques. L'Infra nécessite le plus large éventail de compétences.

### 2.4 Modèle Financier

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| ARR M12 (conservateur) | **~450 K€** | ~81 K€ | ~41 K€ |
| Breakeven avec salaire 4K€ | **M8-M9** | M6 (consulting-led) | **Non atteint Y1** |
| LTV/CAC | **>14x** | 8-12x | 3-5x |
| Investissement initial | <15K€ | <8K€ | <5K€ |
| Modèle dominant | SaaS pur | Consulting → SaaS | Terrain + projets |
| Scalabilité | Forte | Moyenne | Faible |
| Runway nécessaire | 3-6 mois | 6-9 mois | **12+ mois** |

**Verdict Financier** : Le RegTech est le seul qui s'auto-finance rapidement avec un modèle SaaS scalable. Le HealthTech est viable grâce au consulting. L'Infra/H2 nécessite un financement personnel important sans garantie de retour en Y1.

### 2.5 Profil de Risque

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| Score risque moyen | 5.4 | 7.1 | **7.5** |
| Risques critiques (score ≥16) | 1 | 3 | **5** |
| Risque max | 9/25 (burnout) | 10/25 (data access) | **20/25 (timing, B2G, burnout)** |
| Risques structurels (non mitigeables) | 0 | 1 (accès data clinique) | **3** (timing H2, cycle B2G, dispersion) |
| Risque de burnout | Moyen | Élevé | **Très élevé** |

**Verdict Risque** : Le RegTech a le profil de risque le plus sain. Le HealthTech a un risque structurel (accès data) qui peut bloquer tout le projet. L'Infra cumule les risques (timing, B2G, crédibilité, dispersion, burnout).

### 2.6 Go-to-Market

| Indicateur | RegTech | HealthTech | Infra/Eau/H2 |
|------------|---------|------------|-------------|
| Canal principal | Inbound SEO/contenu + Outbound ciblé | Consulting → Software | Outbound terrain + AAP |
| Cible premier client | Customs broker EU (~1000 cibles) | Clinique privée (Ramsay/Elsan) | Usine ETI (agroalim, chimie) |
| Cycle de vente | **1-3 mois** | 6-18 mois | 3-6 mois (eau), 12-36 mois (H2) |
| Premier revenu possible | **M2-M3** | M4-M6 (consulting) | M3-M4 (audit) |
| Pricing entry | 490€/mois | 3-5K€/mois consulting | 490€/mois SaaS |
| Besoin de déplacement physique | Faible (full remote) | Modéré (hôpitaux) | **Élevé** (sites industriels) |

**Verdict GTM** : Le RegTech a le cycle le plus court et le canal le plus scalable (inbound digital). Le HealthTech compense le cycle long par du consulting. L'Infra est le plus exigeant en présence physique.

---

## 3. Matrice de Décision Finale

| Critère (Poids) | RegTech | HealthTech | Infra/Eau/H2 |
|-----------------|---------|------------|-------------|
| Marché (15%) | 8 → 1.20 | 5 → 0.75 | 4 → 0.60 |
| Urgence (15%) | 9 → 1.35 | 6 → 0.90 | 3 → 0.45 |
| Concurrence (10%) | 8 → 0.80 | 7 → 0.70 | 6 → 0.60 |
| Faisabilité (15%) | 9 → 1.35 | 6 → 0.90 | 5 → 0.75 |
| Finances Y1 (15%) | 8 → 1.20 | 5 → 0.75 | 3 → 0.45 |
| Scalabilité (10%) | 9 → 0.90 | 6 → 0.60 | 4 → 0.40 |
| Risque (10%) | 7 → 0.70 | 5 → 0.50 | 3 → 0.30 |
| Solo fit (10%) | 8 → 0.80 | 5 → 0.50 | 4 → 0.40 |
| **TOTAL** | **8.10** | **6.30** | **3.95** |

---

## 4. Recommandation Stratégique

### Séquencement Optimal

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   M0          M6          M12         M18         M24           │
│   │           │           │           │           │             │
│   ▼           ▼           ▼           ▼           ▼             │
│   ╔═══════════════════════════════════════════════════════╗      │
│   ║  REGTECH / SUPPLY CHAIN (100% focus)                 ║      │
│   ║  → MVP M3, premiers clients M4-5, ARR 450K M12      ║      │
│   ╚═══════════════════════════════════════════════════════╝      │
│                           │                                     │
│                   ARR stable >250K€ ?                           │
│                   OUI ↓                                         │
│                           ╔═══════════════════════════╗         │
│                           ║  HEALTHTECH (exploration) ║         │
│                           ║  → R&D, réseau hôpital    ║         │
│                           ║  → Consulting M15-18      ║         │
│                           ╚═══════════════════════════╝         │
│                                                                 │
│   ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐      │
│     INFRA / H2 : veille passive, articles, pas de dev            │
│   └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Résumé Actionable

1. **Lancer le RegTech immédiatement** — C'est l'opportunité dominante sur tous les critères. Urgence marché, faisabilité technique, viabilité financière, scalabilité, profil de risque. Le plan 90 jours est dans [01-regtech-supply-chain/09-plan-execution-90j.md](01-regtech-supply-chain/09-plan-execution-90j.md).

2. **Mettre le HealthTech en veille active** — Construire le réseau hospitalier en parallèle (networking, lectures, Synthea en hobby). Ne lancer qu'une fois le RegTech stabilisé avec un ARR > 250K€ et la bande passante pour un second projet.

3. **Abandonner l'Infra/H2 comme projet solo** — Le timing est trop précoce, le cycle B2G trop long, et la dispersion H2+Eau est un piège. Maintenir une veille passive et publier occasionnellement sur le sujet pour être positionné quand le marché s'ouvrira (2027-2030).

---

## 5. Le Test Ultime : "Si tu n'avais que 5K€ et 90 jours"

| Question | RegTech | HealthTech | Infra/Eau/H2 |
|----------|---------|------------|-------------|
| Peux-tu avoir un MVP fonctionnel ? | ✅ Oui (M3) | 🟡 Démo Synthea (pas de données réelles) | 🟡 Démo synthétique (pas de données SCADA) |
| Peux-tu avoir un premier client payant ? | ✅ Probable (M4-5) | 🟡 Consulting possible (M5-6) | ❌ Très improbable |
| Peux-tu te payer un salaire ? | ✅ M8-9 | 🟡 Avec consulting dès M6 | ❌ Non en Y1 |
| Le marché existe-t-il maintenant ? | ✅ Oui (réglementation active) | 🟡 Oui mais lent | ❌ Pas encore (H2) / fragile (eau) |
| Es-tu autonome (pas de dépendance externe) ? | ✅ Oui (données publiques) | ❌ Non (hôpitaux) | ❌ Non (SCADA, consortiums) |

**Le RegTech est la seule réponse cohérente au test des 5K€/90j.**

---

*Document de synthèse — Décision : focus exclusif sur le RegTech / Supply Chain.*
*Dossier détaillé : [01-regtech-supply-chain/](01-regtech-supply-chain/)*
