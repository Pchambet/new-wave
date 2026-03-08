# Pain Points & Solutions — RegTech Supply Chain / CBAM / Tarifs

## Matrice Complète : Problème → Solution → Métrique de Succès

---

### Pain Point 1 : Classification HTS/CN manuelle, lente et sujette aux erreurs

**Description du problème :**
Un courtier en douane traite 50-500 lignes de classification par jour. Chaque ligne nécessite l'identification du code HTS à 10 chiffres (US) ou CN à 8 chiffres (EU) à partir de descriptions textuelles souvent ambiguës fournies par les exportateurs. Le taux d'erreur humain documenté est de 10-30%, chaque erreur exposant l'importateur à des pénalités de 20-100% de la valeur déclarée.

**Solution technique :**
Pipeline NLP/ML de classification automatique :
1. Ingestion de descriptions textuelles non structurées (factures, manifestes, packing lists)
2. Preprocessing : tokenisation, normalisation des unités, extraction d'entités (matériaux, dimensions, usage)
3. Modèle de classification : architecture Transformer fine-tuné sur les rulings historiques CBP/TAXUD + XGBoost en ensemble pour le scoring de confiance
4. Output : Top-3 codes HTS/CN avec score de confiance + justification traçable
5. Boucle de feedback : les corrections humaines ré-entraînent le modèle

**Métrique de succès :**
- Précision Top-1 > 85%, Top-3 > 95%
- Temps de classification : < 2 secondes par ligne (vs 5-15 minutes manuellement)
- Réduction du taux de litiges douaniers de > 60%

---

### Pain Point 2 : Tariff Stacking US — impossibilité de calculer le droit effectif

**Description du problème :**
Post-invalidation IEEPA (20 février 2026), un importateur US doit résoudre un arbre de décision à 5-7 branches pour chaque SKU :
- Section 122 (10-15%) : s'applique-t-elle ?
- Section 301 (7,5-100%) : le produit est-il d'origine chinoise ?
- Section 232 (25% acier/alu, taux variables pour semi-conducteurs/cuivre) : le matériau est-il couvert ?
- Exclusions EO 14289 : un régime annule-t-il un autre ?
- Zones de libre-échange (USMCA, etc.) : le produit est-il éligible ?
- Anti-dumping/Countervailing duties : y a-t-il un ordre en vigueur ?

La hiérarchie entre ces régimes est partiellement contradictoire et évolutive.

**Solution technique :**
Moteur de résolution de graphe décisionnel :
1. Modélisation de chaque régime tarifaire comme un nœud dans un graphe orienté acyclique (DAG)
2. Règles de hiérarchie codifiées (EO 14289 et ses exceptions) comme des arêtes pondérées
3. Pour chaque code HTS + pays d'origine + date d'entrée : parcours du DAG pour calculer le taux effectif cumulé
4. Détection automatique des exclusions applicables (gain immédiat pour le client)
5. Versionnement temporel : chaque modification réglementaire est un snapshot dans le graphe

**Métrique de succès :**
- Calcul du taux effectif en < 500ms par ligne
- Détection d'exclusions manquées : objectif 5-15% des lignes (= économies directes pour le client)
- Couverture : 100% des chapitres HTS actifs

---

### Pain Point 3 : Calcul des émissions intégrées CBAM (Mass Balance)

**Description du problème :**
Le régime définitif CBAM exige le calcul des Specific Embedded Emissions (SEE) pour chaque bien importé dans l'UE. Pour les biens complexes (acier transformé, aluminium forgé), ce calcul est récursif : il faut remonter l'arbre des précurseurs industriels, obtenir les émissions réelles de chaque installation de production, appliquer l'équation de Mass Balance, et prouver que ≥80% des données sont réelles (pas des valeurs par défaut).

La majorité des importateurs ne savent même pas quelles données demander à leurs fournisseurs.

**Solution technique :**
Moteur de calcul CBAM conforme Annexe IV, Règlement 2023/956 :
1. Modélisation de la Bill of Materials (BOM) comme un arbre de précurseurs avec poids massiques
2. Interface de collecte des données fournisseurs (émissions par installation, mix électrique, facteurs d'émission)
3. Calcul récursif automatisé : SEE_g = (AttrEm_g + Σ M_i × SEE_i) / AL_g
4. Validation de la règle 80/20 : alerte si le ratio valeurs réelles/par défaut est insuffisant
5. Export XML conforme au schéma XSD CBAM Quarterly Report
6. Connexion O3CI pour récupération automatique des données d'installations tierces enregistrées

**Métrique de succès :**
- Validation 100% des rapports contre le schéma XSD TAXUD
- Temps de génération d'un rapport trimestriel : < 2 heures (vs 2-4 semaines manuellement)
- Couverture des 6 secteurs CBAM initiaux (acier, alu, ciment, engrais, hydrogène, électricité)

---

### Pain Point 4 : Calcul du Total Landed Cost intégré

**Description du problème :**
Le "Total Landed Cost" d'une marchandise importée inclut : le prix FOB + le fret maritime/aérien + l'assurance + les droits de douane (multi-régimes) + les taxes à l'importation (TVA, GST) + les frais de manutention portuaire + les surestaries éventuelles + le coût des certificats CBAM + les frais de courtage. L'incapacité à calculer ce coût a priori empêche les directions achats de comparer les fournisseurs ou de simuler des relocalisations.

**Solution technique :**
API de calcul de Landed Cost multiparamétrique :
1. Input : code HTS/CN, pays d'origine, pays de destination, Incoterm, valeur déclarée, poids, mode de transport
2. Composition automatique des couches de coûts (tarifs, taxes, surcharges, CBAM le cas échéant)
3. Simulation multi-scénarios : "que se passe-t-il si je source du Vietnam au lieu de la Chine ?"
4. Intégration des indices de fret en temps réel (Freightos Baltic Index, Drewry WCI) pour les composantes transport

**Métrique de succès :**
- Précision du calcul : ±2% du coût réel constaté a posteriori
- Temps de réponse API : < 1 seconde
- Couverture : corridors US, EU, UK initialement

---

### Pain Point 5 : Absence de traçabilité et d'auditabilité

**Description du problème :**
En cas d'audit douanier, l'importateur doit prouver la justification de chaque classification, chaque taux appliqué, chaque exclusion invoquée. Les processus manuels (emails, tableurs) ne fournissent aucune piste d'audit structurée.

**Solution technique :**
Log d'audit immutable par requête :
1. Chaque appel API génère un "Compliance Record" horodaté et signé
2. Traçabilité complète : input brut → classification → règles appliquées → taux calculé → justification
3. Export en format compatible avec les exigences de documentation CBP/TAXUD
4. Rétention configurable (minimum 5 ans pour CBAM, 7 ans pour CBP)

**Métrique de succès :**
- 100% des calculs traçables et reproductibles
- Temps de préparation d'un dossier d'audit : < 30 minutes (vs 2-5 jours)

---

### Pain Point 6 : Compliance DORA pour les sous-traitants industriels du secteur financier

**Description du problème :**
Les entités financières (banques, assureurs) doivent cartographier les risques ICT de leurs fournisseurs et sous-traitants. Les industriels qui fournissent ces entités doivent prouver leur résilience opérationnelle, incluant la fiabilité de leur supply chain.

**Solution technique :**
Module complémentaire "Supply Chain ICT Risk" :
1. Mapping automatique des dépendances fournisseurs en graphe de risque
2. Scoring de résilience par nœud (diversification géographique, alternatives de sourcing)
3. Reporting structuré conforme aux exigences DORA Chapter V (gestion des risques tiers ICT)

**Métrique de succès :**
- Score de couverture DORA : > 80% des exigences Chapter V
- Ce module est un upsell, pas le cœur du produit — il augmente le panier moyen de 20-30%

---

## Synthèse de Priorisation

| Pain Point | Urgence Client | Complexité Technique | Valeur Économique | Priorité MVP |
|------------|---------------|---------------------|-------------------|-------------|
| Classification HTS/CN | ★★★★★ | ★★★★ | ★★★★ | **P0** |
| Tariff Stacking US | ★★★★★ | ★★★ | ★★★★★ | **P0** |
| Calcul CBAM Mass Balance | ★★★★★ | ★★★★★ | ★★★★ | **P0** |
| Total Landed Cost | ★★★★ | ★★★ | ★★★★ | P1 |
| Audit Trail | ★★★ | ★★ | ★★★ | P1 |
| Module DORA | ★★ | ★★★ | ★★ | P2 |

**Recommandation MVP** : Attaquer P0 en séquence — d'abord le CBAM (urgence immédiate, données publiques disponibles, marché naissant sans leader), puis la classification HTS, puis le tariff stacking.
