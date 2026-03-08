# Benchmark Concurrentiel — RegTech Supply Chain / CBAM / Tarifs

## 1. Cartographie des Acteurs

### 1.1 Acteurs Majeurs — Global Trade Management (GTM)

| Acteur | Siège | Fondation | Levées/CA | Produit Principal | Forces | Faiblesses |
|--------|-------|-----------|-----------|-------------------|--------|------------|
| **Descartes Systems** | Canada | 1981 | CA ~550M USD (2025) | Customs & Regulatory Compliance | Leader historique. Couverture GTM complète. Réseau de 30+ acquisitions. | Monolithique. Lent à innover. Pas de module CBAM natif mature. Pricing enterprise prohibitif. |
| **Avalara** (Vista Equity) | USA | 2004 | Racheté 8,4 Mds USD (2022) | Tax compliance automation | Excellente API. Forte base installée (30K+ clients). | Focalisé sur la taxe de vente domestique US. Compliance douanière internationale = angle mort. |
| **Thomson Reuters ONESOURCE** | USA | — | Div. de TR | Global Trade Content | Base de données réglementaire la plus exhaustive du marché. | UX archaïque. Pas d'API moderne. Modèle de licensing lourd. Pas de calcul CBAM. |
| **C.H. Robinson (Navisphere)** | USA | 1905 | CA ~18 Mds USD | TMS + Customs | Volume transactionnel massif. Donnée de marché propriétaire. | C'est un freight broker, pas un éditeur logiciel. Navisphere est captif (réservé à ses clients). |
| **SAP GTS** | Allemagne | — | Div. de SAP | Global Trade Services | Intégration native SAP ERP. Base installée massive. | Complexe, coûteux (500K-2M+ d'implémentation). Rigide. Pas de CBAM natif. |
| **Oracle GTM Cloud** | USA | — | Div. d'Oracle | Trade Management Cloud | Intégré à Oracle SCM Cloud. | Captif écosystème Oracle. Innovation lente. CBAM non adressé. |

### 1.2 Acteurs Spécialisés — Classification Douanière & HTS

| Acteur | Siège | Levées | Produit | Forces | Faiblesses |
|--------|-------|--------|---------|--------|------------|
| **Tarifflo** | USA | Seed | Classification HTS par ML | Premier entrant ML/NLP sur classification HTS. API-first. | Très tôt. Pas de CBAM. Couverture limitée au marché US. |
| **3CE Technologies** | USA | ~5M | Customs classification | Forte précision sur textiles/chemicals. | Niche étroite. Pas d'API publique. Pas de composante carbone. |
| **Zonos** | USA | ~69M (Series A) | Landed cost calculator | UX excellente. API rapide. Focus e-commerce/DTC. | Orienté B2C/e-commerce (petits colis). Pas adapté au fret industriel B2B. Pas de CBAM. |
| **Customs4Trade (C4T)** | Belgique | Racheté par DP World | CAS (Customs & Compliance) | Très fort en Europe. Expertise AEO/UCC. | Désormais captif DP World. Accès restreint pour tiers. |
| **KGH Customs** | Suède | Racheté par Maersk | Customs advisory + tech | Expertise réglementaire profonde. | Captif Maersk. Plus un cabinet de conseil qu'un produit logiciel. |

### 1.3 Acteurs Émergents — CBAM Spécifique

| Acteur | Siège | Levées | Produit | Forces | Faiblesses |
|--------|-------|--------|---------|--------|------------|
| **Sphera** (Blackstone) | USA/Allemagne | Racheté ~1,4 Mds | ESG & Carbon accounting | Forte expertise LCA. Données d'émissions exhaustives (GaBi). | Produit ESG généraliste. CBAM est une feature, pas le cœur. UX lourde. Prix très élevé. |
| **Ecoinvent** | Suisse | Non-profit | Base de données LCA | Référence académique mondiale pour les facteurs d'émission. | C'est une base de données, pas un logiciel de compliance. Pas de calcul récursif Mass Balance. |
| **Carbon Chain** | UK | ~10M (Series A) | Carbon tracking supply chain | API-first. Focus commodities (métaux, chimie). Premier sur le tracking carbone amont. | CBAM est un module récent. Pas de douane/tarifs. Petit (< 50 employés). |
| **Verico SCE** | Allemagne | Early | CBAM compliance platform | Spécifiquement conçu pour le CBAM européen. | Très jeune. Peu de clients référencés. Scope limité au CBAM (pas de tarifs US). |
| **CBAM Compliance (Deloitte/PwC/EY)** | Global | N/A | Consulting + outils internes | Crédibilité institutionnelle. Accès aux décideurs C-Level. | Service humain (cher, non scalable). L'outil est le consultant, pas le logiciel. |

---

## 2. Matrice de Positionnement

```
                        CBAM / Carbone
                            ↑
                            |
          Sphera            |
          CarbonChain       |         ← ZONE VIDE ←
          Verico            |         (Convergence Tarifs + CBAM)
                            |         
    ─────────────────────────┼──────────────────────────→ Tarifs US / HTS
                            |         Classification
          SAP GTS           |         Descartes
          Oracle GTM        |         Thomson Reuters
                            |         Tarifflo
                            |         Zonos (B2C)
                            
```

**Observation critique** : La zone de convergence Tarifs US + CBAM EU + calcul de Landed Cost unifié est **quasi-vide**. Les acteurs legacy font l'un OU l'autre. Aucun ne fait les deux avec une API moderne et un pricing accessible aux PME.

---

## 3. Analyse des Gaps Concurrentiels

### Gap 1 : Absence de moteur CBAM Mass Balance automatisé
Aucun acteur identifié ne propose un calcul récursif automatisé de l'équation SEE conforme à l'Annexe IV du Règlement 2023/956 avec export XML validé XSD. Les "Big 4" (Deloitte, PwC, EY, KPMG) vendent du consulting humain à 200-500€/h pour faire ce calcul manuellement dans des tableurs.

### Gap 2 : Pas de résolution algorithmique du graphe EO 14289
Le tariff stacking US post-invalidation IEEPA est trop récent (février 2026) pour que les acteurs legacy aient adapté leurs moteurs. Les douaniers US eux-mêmes sont en train de re-liquider les entrées.

### Gap 3 : Pricing inaccessible pour les courtiers de taille moyenne
SAP GTS : 500K-2M€ d'implémentation. Descartes : licensing enterprise à 100K+/an. Il n'existe pas de solution API pay-per-use pour un courtier à 50-200 salariés.

### Gap 4 : Pas de bridge EU-US unifié
Un importateur qui opère des deux côtés de l'Atlantique utilise deux systèmes différents et non interopérables pour la compliance.

---

## 4. Positionnement Différenciant Recommandé

**Proposition de valeur unique : Le premier moteur de calcul unifié Tarifs US + CBAM EU, API-first, pay-per-use.**

| Dimension | Acteurs Legacy | Position ciblée |
|-----------|---------------|-----------------|
| Modèle | License enterprise | API pay-per-call + % économies |
| Scope | Tarifs OU carbone | Tarifs ET carbone, unifié |
| Calcul CBAM | Absent ou consulting | Automatisé, récursif, XML validé |
| Tariff stacking US | Statique, lent à mettre à jour | Temps réel, graphe décisionnel dynamique |
| Cible | Fortune 500 | PME industrielles + courtiers + white-label |
| Time to value | 6-18 mois d'implémentation | Première requête API en 24h |

---

## 5. Menaces Concurrentielles à Surveiller

### 5.1 Risque d'acquisition/consolidation
Les majors (Descartes, SAP) pourraient acquérir un acteur CBAM et combler le gap en 12-18 mois.

### 5.2 Risque "Big 4 productisent leur consulting"
Deloitte, PwC etc. pourraient transformer leurs fichiers Excel CBAM en outils SaaS. Ils ont la crédibilité client mais pas l'ADN produit.

### 5.3 Risque LLM/AI wrapper
Un acteur pourrait empiler GPT-4/Claude sur les textes réglementaires et proposer un "chatbot douanier". Faible menace car la compliance exige un calcul déterministe auditable, pas une génération probabiliste.

### 5.4 Risque open-source
Un projet open-source pourrait émerger autour des schémas XSD CBAM. Mitigation : l'open-source manquera de la base de données de rulings historiques et du support compliance.

---

## 6. Verdict Benchmark

**Score de positionnement concurrentiel : 8/10**

La fenêtre est ouverte et la zone de convergence identifiée est réellement vide. La menace la plus sérieuse vient de la capacité des incumbents à se réveiller (Descartes en particulier), mais leur inertie organisationnelle offre une fenêtre de 12-18 mois. Le marché du CBAM est en train de se créer sous nos yeux — il n'y a pas encore de leader établi.
