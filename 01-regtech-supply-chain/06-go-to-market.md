# Go-to-Market — RegTech Supply Chain / CBAM / Tarifs

## 1. Stratégie de Segmentation : De Qui à Qui

### Phase 1 — Beachhead (Mois 1-6) : Courtiers en Douane Indépendants EU

**Pourquoi eux d'abord :**
- Décision d'achat rapide (1 personne décide, pas de procurement)
- Budget outil : 200-2000€/mois (dans leur fourchette)
- Impactés IMMÉDIATEMENT par le CBAM définitif
- Accessibles via les associations professionnelles (CLECAT en EU, NCBFAA aux US)
- Volume suffisant pour valider le produit (50-200 déclarations CBAM/trimestre chacun)

**Profil cible :**
- Courtier indépendant, 10-100 employés
- Basé en EU (Belgique, Pays-Bas, Allemagne, France — les grands ports)
- Clients importateurs dans les 6 secteurs CBAM
- Utilise actuellement Excel + emails pour collecter les données CBAM

**Objectif** : 10-20 clients payants à fin M6.

### Phase 2 — Expansion (Mois 6-12) : Éditeurs ERP/TMS en White-Label

**Pourquoi ensuite :**
- Un seul contrat white-label = accès à des centaines d'utilisateurs finaux
- Le Product Manager de l'éditeur est en demande de ce module (ses clients le réclament)
- Cycle de vente plus long (3-6 mois) mais LTV massive

**Profil cible :**
- Éditeurs TMS européens mid-market (pas SAP/Oracle — plutôt Transporeon, Shippeo, project44 level)
- Éditeurs ERP supply chain cherchant un module compliance

**Objectif** : 2-3 contrats white-label à fin M12.

### Phase 3 — Scaling (Mois 12-24) : Importateurs Industriels Directs + US

**Pourquoi en dernier :**
- Nécessite la crédibilité acquise en Phase 1-2
- Cycle de vente enterprise (6-12 mois)
- Nécessite le module tariff stacking US mature

---

## 2. Canal d'Acquisition

### Canal Principal : Outbound ciblé + Contenu Expert

| Canal | Action | Coût | Conversion attendue |
|-------|--------|------|-------------------|
| **LinkedIn Sales Navigator** | Identification et contact direct des directeurs de courtage et compliance managers | 80€/mois | 3-5% réponse, 10-20% conversion en démo |
| **Contenu technique** (LinkedIn articles, blog) | Articles sur "Comment calculer le CBAM Mass Balance", "Guide EO 14289" | 0€ (temps) | Lead inbound organique, autorité sectorielle |
| **Webinars sectoriels** | Co-animation avec un cabinet de droit douanier ou une association professionnelle | 0-500€ | 20-50 leads qualifiés par session |
| **Associations professionnelles** | Adhésion CLECAT, ODASCE (France), participation aux conférences sectorielles | 500-2000€/an | Réseau + crédibilité |
| **Partenariats cabinets-conseil** | Accord de recommandation avec 2-3 cabinets de conseil en douane qui n'ont pas d'outil | 0€ (rev share) | Flux qualifié continu |

### Canal Secondaire : Marketplace & SEO

- Listing sur les app stores des ERP partenaires (une fois Phase 2 amorcée)
- SEO sur les requêtes "CBAM compliance software", "CBAM XML report", "Landed Cost calculator API"
- Présence sur Product Hunt / HackerNews uniquement si angle tech fort (pour recrutement, pas pour clients)

---

## 3. Proposition de Valeur — Formulée pour Chaque Persona

### Pour le Courtier en Douane :
> "Générez vos rapports CBAM trimestriels en 2 heures au lieu de 2 semaines. Notre moteur calcule automatiquement les émissions intégrées, valide la conformité 80/20, et exporte le XML prêt à injecter dans le portail CBAM."

### Pour l'Éditeur ERP/TMS :
> "Intégrez la compliance CBAM et le calcul de Landed Cost dans votre plateforme en une semaine grâce à notre API RESTful. Vos clients obtiennent les calculs, vous conservez la relation et la marque."

### Pour le CCO d'un Grand Importateur :
> "Chaque conteneur d'acier importé sans rapport CBAM conforme coûte 3 000€ à 10 000€ de surestaries par jour. Notre moteur élimine ce risque et identifie les exclusions tarifaires que vos courtiers manquent."

---

## 4. Pricing

### Modèle Hybrid : SaaS + Usage

| Tier | Cible | Prix Mensuel | Inclus | Overage |
|------|-------|-------------|--------|---------|
| **Starter** | Petit courtier (< 50 déclarations CBAM/trimestre) | 490€/mois | 200 calculs CBAM + 500 classifications HTS/mois | 0,50€/calcul CBAM, 0,15€/classification |
| **Professional** | Courtier moyen (50-500 déclarations) | 1 490€/mois | 1 000 calculs CBAM + 5 000 classifications/mois | 0,30€/calcul, 0,10€/classification |
| **Enterprise** | Grand importateur / Éditeur white-label | Sur devis (5K-20K€/mois) | Usage illimité, SLA garanti, support dédié, co-branding | — |

### Modèle complémentaire : Performance Fee

Pour les calculs de Landed Cost qui identifient une économie tarifaire (exclusion détectée), option de facturer un pourcentage (5-10%) de l'économie réalisée, plafonné. Ce modèle aligne parfaitement les intérêts et rend le ROI immédiat et mesurable.

---

## 5. Stratégie de Lancement — Séquence Précise

### Semaine 1-2 : Génération de la Liste de Prospects
- Scraper LinkedIn Sales Navigator : tous les "customs broker", "compliance manager", "trade compliance" en Belgique, Pays-Bas, Allemagne, France
- Identifier les 50 courtiers les plus pertinents (taille, secteurs, ports)
- Préparer 3 variantes de cold email

### Semaine 3-4 : Interviews de Découverte (Avant le MVP)
- Objectif : 15-20 interviews de 30 min
- Questions clés : "Comment faites-vous votre reporting CBAM aujourd'hui ?", "Combien de temps ça prend ?", "Quel est votre plus gros problème avec le régime définitif ?"
- **Validation/invalidation de la thèse avant d'écrire une ligne de code**

### Semaine 5-8 : MVP et Bêta Fermée
- MVP fonctionnel sur le calcul CBAM (acier uniquement)
- 5 courtiers en bêta gratuite
- Feedback loop hebdomadaire

### Semaine 9-12 : Premiers Clients Payants
- Conversion des bêta-testeurs en clients payants (tier Starter)
- Première étude de cas publiée
- Lancement du pricing officiel

---

## 6. Métriques de Traction à Suivre

| Métrique | Cible M3 | Cible M6 | Cible M12 |
|----------|---------|---------|----------|
| Interviews réalisées | 20 | — | — |
| Utilisateurs bêta | 5 | — | — |
| Clients payants | 0 | 10-20 | 50-80 |
| MRR | 0€ | 5-15K€ | 30-80K€ |
| Taux de churn mensuel | — | < 5% | < 3% |
| NPS | — | > 40 | > 50 |
| Calculs CBAM traités/mois | 100 | 2 000 | 20 000 |
