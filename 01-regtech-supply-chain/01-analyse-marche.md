# Analyse de Marché — RegTech Supply Chain / CBAM / Tarifs

## 1. Dimensionnement du Marché

### TAM (Total Addressable Market)

Le marché mondial de la RegTech est évalué à **~16,8 milliards USD en 2025**, avec une projection de **38-45 milliards USD d'ici 2029** (CAGR ~23-28%). Le segment spécifique "Trade Compliance & Customs Management" représente environ **4,2 milliards USD** en 2025.

**Décomposition :**
- Customs management software : ~2,1 Mds USD
- Global Trade Management (GTM) : ~1,4 Mds USD  
- Carbon border compliance (émergent, CBAM) : ~0,3-0,7 Mds USD (croissance explosive)
- Tariff classification & duty optimization : ~0,8 Mds USD

### SAM (Serviceable Addressable Market)

En ciblant spécifiquement :
- Les importateurs européens soumis au CBAM (acier, aluminium, ciment, engrais, hydrogène, électricité) : **~12 000 entreprises déclarantes enregistrées**
- Les courtiers en douane US/EU de taille moyenne impactés par le tariff stacking : **~3 500 entités**
- Les éditeurs ERP/TMS cherchant un module de compliance en white-label : **~200 éditeurs**

**SAM estimé : 800M - 1,2 Mds USD**

### SOM (Serviceable Obtainable Market)

En tant que nouvel entrant avec un produit API-First ciblant 0,5-1% du SAM sur 24 mois :

**SOM réaliste : 4-12M USD d'ARR après 24 mois** (hypothèse optimiste mais atteignable avec traction initiale)

---

## 2. Catalyseurs Réglementaires Spécifiques à 2026

### 2.1 CBAM — Régime Définitif (1er Janvier 2026)

| Paramètre | Période Transitoire (2023-2025) | Régime Définitif (2026+) |
|-----------|-------------------------------|--------------------------|
| Valeurs d'émission | Valeurs par défaut acceptées | Valeurs réelles obligatoires |
| Vérification | Auto-déclaration | Vérification par tiers accrédités |
| Certificats CBAM | Non requis | Achat et restitution obligatoires |
| Prix de référence | N/A | Indexé sur EU ETS (premier prix : 7 avril 2026) |
| Sanctions | Mineures / avertissements | Pénalités financières lourdes + blocage douanier |
| Complexité calcul | Basique (valeurs forfaitaires) | Récursif (Mass Balance réel par installation) |

**Impact concret** : Les ~12 000 déclarants CBAM enregistrés doivent passer d'un reporting trivial à un calcul industriel complexe en quelques mois. La plupart n'ont pas les outils.

### 2.2 Invalidation IEEPA et Cascade Tarifaire US

**Chronologie critique :**
- 20 février 2026 : Cour Suprême invalide les tarifs IEEPA
- 24 février 2026 : Section 122 imposée (10-15%)
- En cours : Section 301 (7,5-100% sur produits chinois)
- En cours : Section 232 (acier, aluminium, semi-conducteurs, cuivre)
- En cours : EO 14289 sur la hiérarchie des régimes

**Résultat** : Un importateur US doit résoudre un graphe décisionnel de 5-7 régimes tarifaires superposés pour chaque ligne de son manifeste. La probabilité d'erreur manuelle est massive, et chaque erreur coûte entre 10% et 100% de la valeur du fret en pénalités indues.

### 2.3 DORA (Digital Operational Resilience Act)

Entrée en vigueur en janvier 2025, DORA impose aux entités financières (et par extension à leurs fournisseurs industriels) :
- Cartographie exhaustive des risques ICT dans la chaîne d'approvisionnement
- Tests de résilience réguliers
- Reporting d'incidents structuré

**Lien avec l'opportunité** : Un outil de compliance supply chain qui intègre nativement la traçabilité des flux de données et des dépendances tierces peut se positionner comme enabler DORA.

---

## 3. Dynamiques de Marché et Tendances

### 3.1 Accélération du Nearshoring

La combinaison volatilité maritime (Suez -60%) + tarifs punitifs pousse les multinationales vers le nearshoring (Mexique, Europe de l'Est, Afrique du Nord). Chaque reconfiguration de supply chain déclenche de nouvelles problématiques de classification douanière et de calcul de coûts.

### 3.2 Complexification Réglementaire Irréversible

La tendance est structurelle : davantage de régimes tarifaires, davantage de contraintes environnementales (CBAM élargi à d'autres secteurs prévu 2028-2030), davantage de sanctions. Le problème ne va pas se simplifier — il va empirer.

### 3.3 Défaillance des ERP Legacy

Les systèmes SAP, Oracle, Microsoft Dynamics n'ont pas de modules natifs capables de :
- Résoudre le graphe de hiérarchie EO 14289
- Calculer les émissions intégrées récursives CBAM
- Générer des rapports XML validés XSD pour le portail CBAM

Cela crée un espace naturel pour des solutions spécialisées "bolt-on".

### 3.4 Consolidation du Freight Forwarding

Les grands commissionnaires (Kuehne+Nagel, DHL Global Forwarding, DB Schenker) investissent massivement dans la digitalisation. Ils sont acheteurs de solutions white-label qu'ils peuvent intégrer à leurs plateformes.

---

## 4. Profil de l'Acheteur Type

### Persona 1 : Chief Compliance Officer (Grand Importateur Industriel)
- **Budget** : 100K-500K€/an pour la compliance
- **Douleur** : Risque de pénalités, conteneurs bloqués, audit douanier
- **Cycle de décision** : 3-6 mois
- **Critère #1** : Fiabilité réglementaire et auditabilité

### Persona 2 : Directeur d'un Cabinet de Courtage en Douane
- **Budget** : 20K-100K€/an pour les outils
- **Douleur** : Volume de dossiers en hausse, complexité croissante, marges sous pression
- **Cycle de décision** : 1-3 mois
- **Critère #1** : Gain de productivité mesurable (dossiers traités/jour)

### Persona 3 : Product Manager chez un Éditeur ERP/TMS
- **Budget** : License white-label 50K-200K€/an
- **Douleur** : Ses clients demandent la conformité CBAM, il n'a pas le module
- **Cycle de décision** : 3-9 mois
- **Critère #1** : Qualité de l'API, documentation, SLA

---

## 5. Saisonnalité et Timing

Le marché présente des pics d'urgence liés au calendrier réglementaire :
- **Q1 (Janvier-Mars)** : Entrée en vigueur CBAM définitif → pic de demande
- **Avril 2026** : Premier prix trimestriel CBAM publié → urgence certificats
- **Q2-Q3** : Ajustements tarifaires US post-invalidation IEEPA → flux de demandes
- **Q4** : Préparation des déclarations annuelles

**Fenêtre optimale d'entrée : MAINTENANT (Q1 2026).** Chaque mois de retard réduit l'avantage du "first-mover" sur le segment CBAM.
