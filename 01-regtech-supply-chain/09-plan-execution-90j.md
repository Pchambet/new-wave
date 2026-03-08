# Plan d'Exécution 90 Jours — RegTech Supply Chain / CBAM / Tarifs

## Phase 0 — Validation Marché (Semaines 1-3)

### Semaine 1 : Préparation et Outreach

| Jour | Action | Livrable |
|------|--------|----------|
| L | Lister 80 courtiers en douane EU (Belgique, NL, DE, FR) via LinkedIn Sales Navigator + annuaires CLECAT/ODASCE | Fichier prospects avec nom, email, port d'attache, secteurs |
| M | Rédiger le script d'interview (10 questions clés sur le workflow CBAM actuel) | Script d'interview validé |
| Me | Rédiger 3 variantes de cold email. Focus : "Comment gérez-vous le CBAM définitif ?" | Templates email prêts |
| J | Envoyer les 30 premiers emails (batch 1) | 30 emails envoyés |
| V | Rechercher et télécharger : Règlement 2023/956 (Annexes III-IV), schéma XSD CBAM (TAXUD), nomenclature CN | Corpus réglementaire local |

### Semaine 2 : Interviews et Immersion Réglementaire

| Jour | Action | Livrable |
|------|--------|----------|
| L-V | Conduire 8-12 interviews discovery (30 min chacune) | Notes structurées par interview |
| L-V | Lecture approfondie Annexe IV du Règlement 2023/956 — méthode de calcul Mass Balance | Document d'analyse technique CBAM |
| V | Envoyer batch 2 (30 emails supplémentaires) | 60 emails envoyés au total |

### Semaine 3 : Synthèse et Go/No-Go

| Jour | Action | Livrable |
|------|--------|----------|
| L-Me | Conduire 5-8 interviews supplémentaires (total : 15-20) | — |
| J | Synthèse des interviews : patterns récurrents, WTP confirmée, objections principales | **Rapport de validation marché** |
| V | **DÉCISION GO / NO-GO** : le marché confirme-t-il l'urgence et la WTP? | Décision documentée |

**Critères de Go :**
- ≥ 70% des interviewés confirment que le CBAM définitif est un problème urgent
- ≥ 3 interviewés expriment une intention de payer pour une solution logicielle
- Aucun concurrent dominant identifié par les interviewés eux-mêmes

**Si No-Go :** Pivoter vers le module tariff stacking US (re-interviewer des courtiers côté US) ou l'opportunité HealthTech.

---

## Phase 1 — Construction du MVP (Semaines 4-8)

### Semaine 4 : Socle de Données

| Jour | Action | Livrable |
|------|--------|----------|
| L | Setup du repo Git, CI/CD (GitHub Actions), Docker de base | Repo structuré avec Dockerfile |
| M | Parser la nomenclature CN via l'API TARIC (Commission EU). Stocker dans PostgreSQL. | Table `cn_codes` avec hiérarchie complète |
| Me | Télécharger et parser le schéma XSD CBAM (TAXUD). Implémenter le validateur XML. | Module `cbam_xml_validator.py` fonctionnel |
| J | Modéliser la structure de données pour les "installations" (producteurs hors-UE) et leurs émissions | Schéma de BDD `installations`, `emissions`, `precursors` |
| V | Implémenter l'API de base (FastAPI) avec les endpoints CRUD pour les installations et les produits | API skeleton fonctionnelle |

### Semaine 5 : Moteur CBAM Core

| Jour | Action | Livrable |
|------|--------|----------|
| L | Implémenter le calcul récursif SEE (Specific Embedded Emissions) pour les biens simples (un seul précurseur) | Fonction `calculate_see_simple()` avec tests |
| M | Étendre le calcul aux biens complexes (multiples précurseurs, arbre de BOM) | Fonction `calculate_see_complex()` avec tests |
| Me | Implémenter la règle 80/20 (validation du ratio données réelles vs défaut) + alertes | Module de validation avec tests |
| J | Implémenter le générateur XML CBAM Quarterly Report conforme au schéma XSD | Endpoint API `/generate-cbam-report` |
| V | Tests d'intégration end-to-end : input produit → calcul SEE → validation → export XML | Suite de tests verts |

### Semaine 6 : Interface de Collecte et UI Minimale

| Jour | Action | Livrable |
|------|--------|----------|
| L | Concevoir le formulaire de collecte des données fournisseurs (données nécessaires par installation) | Spec du formulaire |
| M | Implémenter le formulaire (web simple, peut être un Google Form enrichi pour le MVP) | Formulaire fonctionnel |
| Me | Implémenter un dashboard minimal (peut être Streamlit ou un simple frontend) : liste des produits, statut des calculs, téléchargement XML | Dashboard v0 |
| J | Implémenter les valeurs par défaut sectorielles (facteurs d'émission par pays/secteur) comme fallback | Table `default_emission_factors` |
| V | Revue de sécurité : auth API (API keys), chiffrement, isolation des données | Checklist sécurité validée |

### Semaine 7 : Hardening et Documentation

| Jour | Action | Livrable |
|------|--------|----------|
| L | Tests de charge : le calcul tient-il sur 100 produits avec 5 niveaux de précurseurs ? | Rapport de performance |
| M | Documentation API (auto-générée par FastAPI/OpenAPI) + guide utilisateur (2 pages) | Docs publiées |
| Me | Déploiement sur cloud (AWS Fargate ou GCP Cloud Run) + domaine + SSL | MVP accessible en production |
| J | Test end-to-end avec un cas réel : calcul CBAM pour un importateur fictif d'acier depuis la Turquie | Rapport CBAM XML généré et validé |
| V | Correction des bugs identifiés. Gel du scope MVP. | MVP feature-complete |

### Semaine 8 : Lancement Bêta

| Jour | Action | Livrable |
|------|--------|----------|
| L | Contacter les 3-5 courtiers les plus enthousiastes des interviews (semaine 2-3) pour la bêta | Invitations envoyées |
| M | Onboarding du premier bêta-testeur : session de 1h, setup de son premier produit | Premier utilisateur actif |
| Me-J | Onboarding des bêta-testeurs suivants | 3-5 bêta-testeurs actifs |
| V | Premier feedback formel : qu'est-ce qui marche ? Qu'est-ce qui manque cruellement ? | Feedback log structuré |

---

## Phase 2 — Itération et Premier Revenu (Semaines 9-13)

### Semaine 9-10 : Itérations Produit Critiques

- Corriger les 3 problèmes les plus critiques remontés par les bêta-testeurs
- Ajouter les fonctionnalités "must-have" identifiées en bêta (probablement : amélioration du formulaire fournisseur, ajout de secteurs CBAM, export en format alternatif)
- Commencer le contenu marketing : article LinkedIn "Guide Pratique du CBAM Définitif 2026"

### Semaine 11 : Conversion et Pricing

- Proposer le pricing officiel aux bêta-testeurs
- Objectif : convertir 2-3 bêta-testeurs en clients payants (tier Starter, 490€/mois)
- Préparer la première étude de cas client (avec permission)
- Créer la page de pricing sur le site web

### Semaine 12-13 : Scale de l'Acquisition

- Lancer la deuxième vague de cold emails (50 nouveaux prospects) avec le social proof des premiers clients
- Publier l'étude de cas et le contenu technique sur LinkedIn
- Contacter 2-3 éditeurs TMS/ERP pour explorer le white-label
- Préparer la roadmap pour le module classification HTS ML (Phase 2 du produit)

---

## Jalons Critiques (Gates)

| Semaine | Jalon | Critère de Succès | Action si Échec |
|---------|-------|-------------------|-----------------|
| S3 | Go/No-Go Marché | 70%+ des interviews confirment l'urgence | Pivoter vers US tariffs ou Opportunité 2 |
| S7 | MVP Feature-Complete | Calcul CBAM + export XML fonctionnels sur acier | Réduire le scope (un seul pays d'origine) |
| S8 | Premier Bêta-Testeur Actif | ≥ 1 courtier utilise l'outil sur un cas réel | Revoir l'UX, simplifier drastiquement |
| S11 | Premier Euro de Revenu | ≥ 1 client payant | Revoir le pricing (baisser ou offrir du freemium) |
| S13 | Traction Initiale | ≥ 3 clients payants + 1 étude de cas | Réévaluer le positionnement ou explorer le rachat partiel par un éditeur |

---

## Budget Phase 0-13 (90 jours)

| Poste | Montant |
|-------|---------|
| Infrastructure cloud | 200€ |
| LinkedIn Sales Navigator | 240€ (3 mois) |
| Domaine + hosting site web | 50€ |
| Assurance E&O (si premier client M11) | 400€ (prorata) |
| Divers (outils, déplacements éventuels) | 500€ |
| **Total 90 jours** | **~1 400€** |

*Hors rémunération de l'ingénieur.*
