# Matrice de Risques — RegTech Supply Chain / CBAM / Tarifs

## Matrice Probabilité × Impact

```
Impact ▲
Critique │  R3          R7
         │
Élevé    │  R1    R5    R8
         │
Modéré   │  R2    R4    R6
         │
Faible   │              R9
         └──────────────────────→ Probabilité
           Faible  Moyenne  Élevée
```

---

## Risques Détaillés

### R1 — Adoption plus lente que prévue (Probabilité: Moyenne | Impact: Élevé)

**Description :** Les courtiers en douane adoptent une posture attentiste face au CBAM définitif, espérant que les autorités prolongeront la tolérance des valeurs par défaut ou que leurs solutions manuelles suffiront.

**Indicateurs précoces :**
- Taux de conversion interview → pilote < 10%
- Feedback récurrent : "on va attendre de voir"
- L'enforcement CBAM est mou (peu de contrôles en Q1-Q2 2026)

**Mitigation :**
- Pivoter vers les importateurs directs (qui ont des volumes plus grands et plus à perdre)
- Accélérer le module tariff stacking US (douleur plus immédiate côté américain)
- Proposer un tier freemium pour réduire la friction d'adoption

---

### R2 — Concurrent incumbent se réveille (Probabilité: Moyenne | Impact: Modéré)

**Description :** Descartes, SAP GTS ou un outsider bien financé lance un module CBAM compétitif en 6-12 mois.

**Indicateurs précoces :**
- Annonces produit lors des conférences sectorielles (WCO, CLECAT)
- Acquisitions d'acteurs CBAM spécialisés (Verico, CarbonChain)

**Mitigation :**
- Vitesse d'exécution : être le premier avec 50 clients et des études de cas
- Construire le moat données (base de rulings + données fournisseurs collectées)
- Le concurrent incumbent sera plus cher et plus lent à intégrer → se positionner sur l'agilité et le pricing

---

### R3 — Changement réglementaire majeur (Probabilité: Faible | Impact: Critique)

**Description :** L'UE reporte le régime définitif CBAM, ou les US simplifient drastiquement leur régime tarifaire (peu probable mais non nul si changement d'administration).

**Indicateurs précoces :**
- Signals politiques (élections, changement de commissaire EU)
- Lobbying industriel fort contre le CBAM

**Mitigation :**
- Diversification géographique : si le CBAM ralentit, accélérer le module US tariffs
- L'investissement n'est pas perdu : la compétence ML/classification est transférable
- Scénario très improbable : le CBAM est acté dans le Green Deal et soutenu par une majorité politique

---

### R4 — Qualité des données fournisseurs insuffisante (Probabilité: Élevée | Impact: Modéré)

**Description :** Les fournisseurs hors-UE (Inde, Turquie, Chine) ne fournissent pas les données d'émissions réelles, rendant le calcul CBAM incomplet.

**Indicateurs précoces :**
- Taux de réponse aux formulaires fournisseurs < 30%
- Majorité des calculs s'appuient sur des valeurs par défaut

**Mitigation :**
- Le logiciel gère élégamment le fallback vers les valeurs par défaut avec scoring de qualité
- Module de collecte fournisseur multilingue (anglais, chinois, turc, hindi)
- À terme : effet réseau — les données collectées par un importateur bénéficient à tous

---

### R5 — Précision ML insuffisante pour la compliance (Probabilité: Moyenne | Impact: Élevé)

**Description :** Le modèle de classification HTS ne dépasse pas 80% de précision Top-1, ce qui est insuffisant pour un usage compliance sans revue humaine intensive.

**Indicateurs précoces :**
- Accuracy stagne malgré l'ajout de données d'entraînement
- Feedback clients : "l'outil se trompe trop souvent"

**Mitigation :**
- Approche hybride ML + règles + revue humaine obligatoire sous 90% de confiance
- Spécialiser par secteur (acier d'abord, puis aluminium) plutôt que de viser la couverture universelle
- Le modèle n'a PAS besoin d'être parfait pour apporter de la valeur — il réduit le temps de classification de 80% même à 85% de précision

---

### R6 — Risque juridique (responsabilité en cas d'erreur) (Probabilité: Élevée | Impact: Modéré)

**Description :** Un client subit une pénalité douanière et attribue l'erreur au logiciel.

**Mitigation :**
- CGU explicites : l'outil est une "aide à la décision", pas un conseil juridique
- Assurance E&O professionnelle (2-5K€/an)
- Score de confiance + disclaimer systématique quand le score est bas
- Audit trail immutable démontrant que le client a vu et validé la recommandation

---

### R7 — Incident de sécurité / fuite de données (Probabilité: Faible | Impact: Critique)

**Description :** Compromission des données clients (manifestes douaniers, données d'émissions, informations commerciales sensibles).

**Mitigation :**
- Chiffrement at-rest et in-transit (AES-256, TLS 1.3)
- Isolation des données par tenant (multi-tenancy logique stricte)
- Authentification forte (API keys + OAuth2, rate limiting)
- Audit de sécurité indépendant avant la mise en production (option : programme bug bounty)
- Conformité RGPD (données stockées en UE pour les clients UE)

---

### R8 — Burnout de l'ingénieur solo (Probabilité: Élevée | Impact: Élevé)

**Description :** L'ingénieur solo porte simultanément le développement, le commercial, le support, la veille réglementaire, et la maintenance. La charge est insoutenable au-delà de 6-9 mois.

**Mitigation :**
- Automatisation maximale (CI/CD, monitoring, alerting)
- Recrutement d'un premier collaborateur (support/commercial) dès que le MRR dépasse 10K€
- Externaliser la veille réglementaire à un expert freelance
- Discipline stricte : pas de feature creep, pas d'opportunité 2 ou 3 en parallèle

---

### R9 — Risque technologique (obsolescence du modèle ML) (Probabilité: Élevée | Impact: Faible)

**Description :** L'évolution rapide de l'écosystème ML (nouveaux modèles, nouvelles architectures) rend le modèle initial obsolète.

**Mitigation :**
- Architecture modulaire permettant de swapper le modèle ML sans refactoring
- Ce "risque" est en réalité une opportunité : chaque nouveau modèle améliore la précision
- Ne pas over-engineer l'infra ML au départ — XGBoost + embeddings sont suffisants pour le MVP

---

## Synthèse des Risques

| # | Risque | Prob. | Impact | Score | Action Prioritaire |
|---|--------|-------|--------|-------|--------------------|
| R8 | Burnout solo | Élevée | Élevé | **9** | Recruter dès MRR > 10K€ |
| R1 | Adoption lente | Moyenne | Élevé | **6** | 20 interviews AVANT le MVP |
| R5 | Précision ML | Moyenne | Élevé | **6** | Approche hybride, scope restreint |
| R4 | Données fournisseurs | Élevée | Modéré | **6** | Module collecte + fallback |
| R6 | Responsabilité juridique | Élevée | Modéré | **6** | Assurance E&O + CGU + disclaimers |
| R2 | Concurrent incumbent | Moyenne | Modéré | **4** | Vitesse d'exécution |
| R7 | Sécurité données | Faible | Critique | **4** | Best practices dès J1 |
| R3 | Changement réglementaire | Faible | Critique | **4** | Diversification géographique |
| R9 | Obsolescence ML | Élevée | Faible | **3** | Architecture modulaire |
