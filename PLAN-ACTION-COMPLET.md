# Plan d'Action Complet — New Wave RegTech

> **Objectif** : Transformer ce projet de documentation en entreprise réelle et rentable.
> Ce plan couvre tout ce qu'il faut faire, dans l'ordre, pour y arriver.

---

## Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PHASE -1     PHASE 0        PHASE 1        PHASE 2        PHASE 3     PHASE 4  │
│  Fondations   Validation     MVP            Traction       Scale        Consol.  │
│  (1-2 sem)   (3 sem)        (5 sem)        (5 sem)        (3 mois)     (6 mois) │
│                                                                                  │
│  • Setup      • 20 inter-   • Code          • 3 clients    • 20+        • 50+    │
│  • Nom          views         CBAM            payants        clients      clients │
│  • Juridique  • Go/No-Go    • Bêta          • Étude cas   • White-     • Équipe  │
│  • Outils     • Rapport     • Prod          • Pricing        label        2-3 p.  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

# PHASE -1 : FONDATIONS (Semaine 0 — Avant de commencer)

> **Durée** : 1-2 semaines | **Objectif** : Poser les bases avant toute action commerciale ou technique.

## 1.1 Identité et Positionnement

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 1 | **Choisir un nom de produit/marque** — court, mémorisable, dispo en .com | Nom validé + domaine réservé | 2h |
| 2 | **Rédiger le pitch en 1 phrase** (déjà dans README-github : "On aide les entreprises à ne pas se faire gronder par les douanes") | Pitch finalisé | 30 min |
| 3 | **Définir les 3 personas cibles** avec noms fictifs, douleurs, objectifs (CCO, Directeur courtage, PM éditeur) | Fiche persona par cible | 1h |
| 4 | **Créer l'email professionnel** (ex: pierre@nomdomaine.com) | Email opérationnel | 30 min |

## 1.2 Structure Juridique et Administrative

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 5 | **Décider du statut juridique** : SASU (recommandé pour solo) ou auto-entrepreneur (limite 77K€) | Décision documentée | 1h |
| 6 | **Créer la société** (si SASU : LegalStart, Captain Contrat, ou notaire) | Kbis, statuts | 1-5 jours |
| 7 | **Ouvrir un compte bancaire pro** (Qonto, N26 Business, ou banque trad.) | Compte opérationnel | 1-3 jours |
| 8 | **Souscrire une assurance responsabilité civile pro** (RC Pro) — obligatoire | Attestation | 1 jour |
| 9 | **Préparer le budget initial** : 15-20K€ disponibles (runway 6 mois avec salaire) ou 5K€ (sans salaire) | Budget validé | 1h |

## 1.3 Outils et Infrastructure de Travail

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 10 | **Créer le repo Git** (GitHub/GitLab) — structure vide avec README | Repo `new-wave` ou nom produit | 30 min |
| 11 | **Configurer un CRM/tableur prospects** (Notion, Airtable, ou Google Sheets) | Template avec colonnes : Nom, Email, Société, Statut, Notes | 1h |
| 12 | **Souscrire LinkedIn Sales Navigator** (80€/mois) — pour identifier les prospects | Accès actif | 30 min |
| 13 | **Préparer un calendrier** pour bloquer les créneaux interviews (30 min × 20 = 10h) | Calendrier réservé | 30 min |
| 14 | **Télécharger le corpus réglementaire** : Règlement UE 2023/956 (Annexes III-IV), schéma XSD CBAM TAXUD, nomenclature CN | Fichiers locaux | 2h |

## 1.4 Documents de Référence

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 15 | **Créer un document "Hypothèses à valider"** — liste des 10 hypothèses critiques à confirmer/infirmer en interviews | Fichier `hypotheses-validation.md` | 1h |
| 16 | **Rédiger le script d'interview** (10 questions, 30 min max) — voir modèle ci-dessous | Script validé | 1h |
| 17 | **Préparer 3 variantes de cold email** pour la prospection | Templates prêts | 1h |

### Modèle Script d'Interview (à adapter)

1. Quel est votre rôle exact dans la gestion des déclarations CBAM ?
2. Comment gérez-vous aujourd'hui le reporting CBAM trimestriel ?
3. Combien de temps cela prend-il par trimestre ? Combien de personnes ?
4. Qu'est-ce qui a changé avec le régime définitif (janvier 2026) ?
5. Avez-vous déjà eu des problèmes (retards, erreurs, pénalités) ?
6. Utilisez-vous un outil logiciel ? Lequel ? Pourquoi ?
7. Si un outil automatisait 80% du travail pour 500€/mois, seriez-vous intéressé ?
8. Qui décide de l'achat d'un nouvel outil dans votre structure ?
9. Quel est votre plus gros point de blocage actuel ?
10. Puis-je vous recontacter pour une démo quand j'aurai un prototype ?

---

# PHASE 0 : VALIDATION MARCHÉ (Semaines 1-3)

> **Durée** : 3 semaines | **Objectif** : Confirmer que des gens paieront avant d'écrire une ligne de code.
> **Gate critique** : Go/No-Go à la fin de la Semaine 3.

## Semaine 1 : Prospection et Premier Contact

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 18 | **Construire la liste de 80 prospects** — courtiers en douane EU (BE, NL, DE, FR) via LinkedIn + annuaires CLECAT, ODASCE | Fichier CSV/Sheet avec : Nom, Prénom, Email, Société, LinkedIn, Port | 1 jour |
| 19 | **Enrichir les 30 premiers** — vérifier les emails (Hunter.io, Apollo) | 30 prospects avec email vérifié | 2h |
| 20 | **Envoyer le batch 1** — 30 cold emails (personnaliser le prénom/société) | 30 emails envoyés | 2h |
| 21 | **Poster sur LinkedIn** — "Je mène une étude sur le CBAM définitif, 20 min d'échange en échange de mes conclusions" | Post publié | 30 min |
| 22 | **Contacter 5 personnes de ton réseau** — "Tu connais quelqu'un en douane / import-export ?" | 5 relances envoyées | 1h |
| 23 | **Lire l'Annexe IV du Règlement 2023/956** — comprendre la méthode Mass Balance | Notes de lecture | 4h |

## Semaine 2 : Interviews et Itération

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 24 | **Conduire 8-12 interviews** (30 min chacune) — enregistrer (avec accord) ou prendre des notes détaillées | 8-12 fiches interview remplies | 6-8h |
| 25 | **Envoyer le batch 2** — 30 emails supplémentaires | 60 emails envoyés au total | 1h |
| 26 | **Ajuster le script** si les premières interviews révèlent des questions manquantes | Script v2 | 30 min |
| 27 | **Relancer les non-répondeurs** du batch 1 (1 relance max) | Relances envoyées | 1h |
| 28 | **Documenter les patterns** — quelles douleurs reviennent ? Quels mots exacts ? | Notes synthétiques | 2h |

## Semaine 3 : Synthèse et Décision

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 29 | **Conduire 5-8 interviews supplémentaires** (total visé : 15-20) | — | 4-6h |
| 30 | **Rédiger le rapport de validation marché** — synthèse, citations, patterns, objections | Document `rapport-validation-marche.md` | 4h |
| 31 | **Calculer les métriques** : % qui confirment l'urgence, % avec intention de payer, % qui mentionnent un concurrent | Tableau de bord | 1h |
| 32 | **DÉCISION GO / NO-GO** — réunion avec toi-même (ou mentor) : documenter la décision et les critères | Fichier `decision-go-nogo.md` | 1h |

### Critères de GO (à atteindre)

- [ ] ≥ 15 interviews réalisées
- [ ] ≥ 70% confirment que le CBAM définitif est un problème urgent
- [ ] ≥ 3 personnes expriment une intention de payer ("oui je serais intéressé", "on cherche une solution")
- [ ] Aucun concurrent dominant cité spontanément par la majorité
- [ ] Au moins 2-3 prospects chauds prêts pour une bêta

### Si NO-GO

- Pivoter vers le module Tariff Stacking US (re-interviewer des courtiers US)
- Ou documenter l'apprentissage et archiver le projet
- Ne pas coder sans validation

---

# PHASE 1 : CONSTRUCTION DU MVP (Semaines 4-8)

> **Durée** : 5 semaines | **Objectif** : Produit fonctionnel que 3-5 courtiers peuvent tester sur un cas réel.
> **Prérequis** : GO validé en Phase 0.

## Semaine 4 : Socle Technique

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 33 | **Initialiser le projet** — structure Python (FastAPI), Docker, docker-compose, .env | Repo avec structure de base | 2h |
| 34 | **Configurer PostgreSQL** — local + script de migration (Alembic ou SQL brut) | BDD opérationnelle | 2h |
| 35 | **Parser la nomenclature CN** — API TARIC ou fichier XML Commission EU → table `cn_codes` | Données importées | 1 jour |
| 36 | **Télécharger et intégrer le schéma XSD CBAM** (TAXUD) — module de validation XML | `cbam_xml_validator.py` | 4h |
| 37 | **Modéliser le schéma de données** — `installations`, `emissions`, `precursors`, `products` | Schéma SQL + migrations | 4h |
| 38 | **Créer l'API skeleton** — FastAPI, endpoints CRUD installations/produits, auth API key | API testable (Postman/curl) | 4h |
| 39 | **Configurer CI/CD** — GitHub Actions : test, build Docker, (optionnel) deploy | Pipeline vert | 2h |

## Semaine 5 : Moteur CBAM

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 40 | **Implémenter `calculate_see_simple()`** — biens avec un seul précurseur, équation Annexe IV | Fonction + tests unitaires | 4h |
| 41 | **Implémenter `calculate_see_complex()`** — arbre BOM, calcul récursif | Fonction + tests | 1 jour |
| 42 | **Implémenter la règle 80/20** — validation ratio données réelles vs défaut, alertes | Module validation | 4h |
| 43 | **Implémenter le générateur XML** — export conforme schéma XSD CBAM Quarterly Report | Endpoint `/generate-cbam-report` | 1 jour |
| 44 | **Tests d'intégration E2E** — input produit → calcul → validation → XML téléchargeable | Suite de tests | 4h |
| 45 | **Créer la table `default_emission_factors`** — valeurs sectorielles/pays (Ecoinvent, UNFCCC) | Données de fallback | 4h |

## Semaine 6 : Interface et Collecte

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 46 | **Concevoir le formulaire de collecte fournisseurs** — champs nécessaires par type d'installation | Spec (Figma, doc, ou schéma) | 2h |
| 47 | **Implémenter le formulaire** — formulaire web simple (HTML/JS ou React minimal) ou Typeform/Google Form pour MVP | Formulaire fonctionnel | 4h |
| 48 | **Implémenter le dashboard minimal** — Streamlit ou React : liste produits, statut calculs, bouton télécharger XML | Dashboard v0 | 1 jour |
| 49 | **Auth et sécurité** — API keys par client, chiffrement at-rest (optionnel MVP), isolation des données | Checklist sécurité | 4h |
| 50 | **Documentation API** — OpenAPI auto-générée par FastAPI, déployée (Swagger UI) | Docs accessibles | 1h |

## Semaine 7 : Hardening et Déploiement

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 51 | **Tests de charge** — 100 produits, 5 niveaux de précurseurs : temps de réponse < 30s ? | Rapport perf | 2h |
| 52 | **Cas de test réel** — calcul CBAM pour acier turc importé en EU (cas documenté) | Rapport XML validé | 4h |
| 53 | **Déploiement cloud** — AWS Fargate ou GCP Cloud Run, PostgreSQL managé (RDS/Cloud SQL) | URL de prod | 1 jour |
| 54 | **Domaine + SSL** — api.nomdomaine.com ou app.nomdomaine.com | HTTPS opérationnel | 2h |
| 55 | **Monitoring** — Sentry (erreurs), logs structurés | Alertes configurées | 2h |
| 56 | **Gel du scope MVP** — liste des features "hors scope pour la bêta" | Document scope | 30 min |

## Semaine 8 : Lancement Bêta

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 57 | **Contacter les 3-5 prospects chauds** des interviews — "J'ai un prototype, voulez-vous tester ?" | Invitations envoyées | 1h |
| 58 | **Onboarding du premier bêta-testeur** — call 1h, setup compte, premier produit saisi ensemble | Premier utilisateur actif | 2h |
| 59 | **Onboarding des bêta-testeurs 2 à 5** | 3-5 utilisateurs actifs | 4h |
| 60 | **Créer un canal de feedback** — Slack, Discord, ou email dédié | Canal opérationnel | 30 min |
| 61 | **Premier debrief** — qu'est-ce qui marche ? Qu'est-ce qui manque ? Qu'est-ce qui bloque ? | Feedback log | 2h |

---

# PHASE 2 : TRACTION ET PREMIER REVENU (Semaines 9-13)

> **Durée** : 5 semaines | **Objectif** : 3 clients payants, 1 étude de cas, pricing validé.

## Semaines 9-10 : Itérations Produit

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 62 | **Prioriser les 3 bugs/features critiques** remontés en bêta | Backlog priorisé | 1h |
| 63 | **Corriger et déployer** — cycle itératif sur les retours | Version améliorée | 1 semaine |
| 64 | **Ajouter les "must-have"** identifiés (ex: export Excel, secteur aluminium, etc.) | Features livrées | 3-5 jours |
| 65 | **Rédiger le premier article de contenu** — "Guide Pratique du CBAM Définitif 2026" (LinkedIn ou blog) | Article publié | 4h |
| 66 | **Préparer la page de pricing** — 3 tiers (Starter 490€, Pro 1490€, Enterprise sur devis) | Page web ou doc | 2h |

## Semaine 11 : Conversion

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 67 | **Proposer le pricing aux bêta-testeurs** — "Merci d'avoir testé. Voici l'offre pour continuer." | Propositions envoyées | 1h |
| 68 | **Préparer les CGU et la politique de confidentialité** — template + adaptation | Documents prêts | 4h |
| 69 | **Souscrire l'assurance E&O** (Erreurs & Omissions) — 2-5K€/an, obligatoire avant facturation | Attestation | 1 jour |
| 70 | **Configurer la facturation** — Stripe, Pennylane, ou factures manuelles | Premier client facturable | 2h |
| 71 | **Objectif : 2-3 conversions** en clients payants (tier Starter) | 2-3 clients payants | — |
| 72 | **Demander l'autorisation pour une étude de cas** au client le plus satisfait | Accord signé (email ou doc) | 30 min |

## Semaines 12-13 : Scale de l'Acquisition

| # | Action | Livrable | Temps |
|---|--------|----------|-------|
| 73 | **Rédiger l'étude de cas** — problème, solution, résultat (avec chiffres si possible) | Étude de cas 1 page | 2h |
| 74 | **Publier l'étude de cas** sur le site, LinkedIn, et l'utiliser dans les emails | Contenu publié | 1h |
| 75 | **Lancer la vague 2 de prospection** — 50 nouveaux prospects avec social proof | 50 emails envoyés | 2h |
| 76 | **Contacter 2-3 éditeurs TMS/ERP** — Transporeon, Shippeo, ou équivalents pour explorer white-label | 2-3 conversations initiées | 2h |
| 77 | **Créer la landing page** — nomdomaine.com avec valeur prop, pricing, CTA | Site en ligne | 4h |
| 78 | **SEO basique** — page "CBAM compliance software", "calcul CBAM automatisé" | Mots-clés ciblés | 2h |

---

# PHASE 3 : SCALE (Mois 4-6)

> **Durée** : 3 mois | **Objectif** : 15-25 clients, MRR 8-15K€, premier recrutement envisagé.

## Produit

| # | Action | Livrable |
|---|--------|----------|
| 79 | **Module classification HTS (ML)** — baseline TF-IDF + XGBoost sur rulings CBP, précision Top-1 > 80% | Module déployé |
| 80 | **Élargir les secteurs CBAM** — aluminium, ciment (au-delà de l'acier) | Couverture étendue |
| 81 | **Module Tariff Stacking US** — graphe EO 14289, Section 122/301/232 (si validation marché US) | Module déployé |
| 82 | **Améliorer le dashboard** — UX, onboarding, support multilingue (EN, FR, DE) | V2 dashboard |

## Commercial

| # | Action | Livrable |
|---|--------|----------|
| 83 | **Adhérer à CLECAT ou ODASCE** — présence aux événements sectoriels | Réseau étendu |
| 84 | **Webinar sectoriel** — co-animer avec un cabinet douanier ou expert | 20-50 leads |
| 85 | **Partenariat cabinet-conseil** — 1-2 cabinets qui recommandent l'outil (rev share) | Accord signé |
| 86 | **Objectif M6** : 15-25 clients payants, MRR 8-15K€ | Traction validée |

## Opérations

| # | Action | Livrable |
|---|--------|----------|
| 87 | **Mettre en place la veille réglementaire** — abonnement Federal Register, EUR-Lex, expert freelance 1-2K€/mois | Processus opérationnel |
| 88 | **Architecture "rules-as-data"** — règles tarifaires en BDD, pas en code, versionnement | Maintenance facilitée |
| 89 | **Documenter les runbooks** — incident, déploiement, mise à jour réglementaire | Docs internes |

## Recrutement (si MRR > 10K€)

| # | Action | Livrable |
|---|--------|----------|
| 90 | **Définir le premier poste** — commercial ou support client (priorité selon le goulot) | Fiche de poste |
| 91 | **Recruter** — freelance puis CDI si traction confirmée | Premier collaborateur |

---

# PHASE 4 : CONSOLIDATION (Mois 7-12)

> **Durée** : 6 mois | **Objectif** : 50+ clients, ARR 400-600K€, équipe 2-3 personnes, white-label signé.

## Produit

| # | Action | Livrable |
|---|--------|----------|
| 92 | **API white-label** — documentation, sandbox, SLA pour éditeurs | Offre enterprise mature |
| 93 | **Module DORA** (Supply Chain ICT Risk) — upsell pour clients secteur financier | Module complémentaire |
| 94 | **Certification ou audit** — cabinet Big 4 valide la méthodologie CBAM (crédibilité) | Certificat ou rapport |

## Commercial

| # | Action | Livrable |
|---|--------|----------|
| 95 | **1-2 contrats white-label** signés avec éditeurs TMS/ERP | Revenus récurrents B2B2B |
| 96 | **Cibler les importateurs directs** — grands groupes industriels (cycle long) | Pipeline enterprise |
| 97 | **Expansion US** — module tariff stacking, courtiers NCBFAA | Présence US |

## Organisation

| # | Action | Livrable |
|---|--------|----------|
| 98 | **Équipe 2-3 personnes** — tech, commercial, ou ops | Structure scalable |
| 99 | **Processus de support** — ticketing, SLA réponse, documentation self-service | Support structuré |
| 100 | **Conformité RGPD** — DPA, registre des traitements, hébergement UE | Conformité validée |

---

# TÂCHES RÉCURRENTES ET ONGOING

## Hebdomadaire

| Fréquence | Action |
|-----------|--------|
| Chaque lundi | Revue des métriques : MRR, churn, nouveaux leads, tickets support |
| Chaque vendredi | Mise à jour du backlog, priorisation de la semaine suivante |

## Mensuel

| Fréquence | Action |
|-----------|--------|
| Début du mois | Vérifier les mises à jour réglementaires (CBAM, tarifs US) |
| Fin du mois | Clôture comptable, facturation, trésorerie |
| 1x/mois | Article de contenu ou post LinkedIn |

## Trimestriel

| Fréquence | Action |
|-----------|--------|
| Chaque trimestre | Revue stratégique : objectifs vs réalisé, ajustements |
| Q1, Q2, Q3, Q4 | Déclarations CBAM clients — pic d'activité à anticiper |

---

# BUDGET CONSOLIDÉ

| Phase | Poste | Montant |
|-------|-------|---------|
| **Phase -1** | Création société (SASU) | 200-500€ |
| | Compte bancaire | 0-20€/mois |
| | RC Pro | 300-600€/an |
| | Domaine | 10-15€/an |
| **Phase 0** | LinkedIn Sales Navigator | 80€/mois × 3 = 240€ |
| | Outils prospection (Hunter, etc.) | 0-100€ |
| **Phase 1** | Cloud (Fargate, RDS) | 100-200€/mois |
| | Divers (outils, déplacements) | 200-500€ |
| **Phase 2** | Assurance E&O | 400-500€ (prorata) |
| | Stripe/Pennylane | ~2% des revenus |
| | Site web, hébergement | 50-100€ |
| **Total 6 premiers mois** | | **3 000 - 5 000€** |

*Hors salaire. Avec salaire 4K€/mois : runway 15-20K€ nécessaire.*

---

# GATES DE DÉCISION

| Gate | Quand | Critère | Si échec |
|------|-------|---------|----------|
| **G0** | Fin Phase -1 | Société créée, outils prêts | Reporter le lancement |
| **G1** | Fin Semaine 3 | GO validé (15+ interviews, 70%+ urgence, 3+ WTP) | Pivoter ou arrêter |
| **G2** | Fin Semaine 7 | MVP déployé, calcul CBAM fonctionnel | Réduire le scope |
| **G3** | Fin Semaine 8 | ≥ 1 bêta-testeur actif | Simplifier l'UX |
| **G4** | Fin Semaine 11 | ≥ 1 client payant | Revoir le pricing |
| **G5** | Fin Semaine 13 | ≥ 3 clients + 1 étude de cas | Réévaluer le positionnement |
| **G6** | Fin M6 | MRR > 8K€ | Pivoter ou lever des fonds |
| **G7** | Fin M12 | ARR > 400K€ | Scale ou consolidation |

---

# CHECKLIST "PROJET RÉEL"

Coche au fur et à mesure. Quand tout est coché, le projet est réel et concret.

## Fondations
- [ ] Nom de produit choisi et domaine réservé
- [ ] Société créée (SASU ou équivalent)
- [ ] Compte bancaire pro ouvert
- [ ] Assurance RC Pro souscrite
- [ ] Email professionnel opérationnel
- [ ] Repo Git créé
- [ ] CRM/tableur prospects configuré

## Validation
- [ ] 15-20 interviews réalisées
- [ ] Rapport de validation marché rédigé
- [ ] Décision GO documentée
- [ ] 2-3 prospects chauds identifiés pour la bêta

## Produit
- [ ] MVP déployé en production
- [ ] Calcul CBAM + export XML fonctionnel
- [ ] Dashboard utilisable
- [ ] Documentation API publiée
- [ ] 3-5 bêta-testeurs actifs

## Commercial
- [ ] Premier client payant
- [ ] 3 clients payants
- [ ] Étude de cas publiée
- [ ] Landing page en ligne
- [ ] Assurance E&O souscrite

## Opérations
- [ ] Veille réglementaire en place
- [ ] Processus de support défini
- [ ] Conformité RGPD assurée

---

*Document créé le 7 mars 2025. À mettre à jour à chaque phase majeure.*
