# Modèle Financier — RegTech Supply Chain / CBAM / Tarifs

## 1. Hypothèses Fondamentales

| Paramètre | Valeur | Source/Justification |
|-----------|--------|---------------------|
| Ticket moyen Starter | 490€/mois | Benchmark produits SaaS compliance mid-market |
| Ticket moyen Professional | 1 490€/mois | Benchmark + willingness-to-pay estimée |
| Ticket moyen Enterprise/White-label | 8 000€/mois | Benchmark API B2B industriel |
| Mix clients (M12) | 60% Starter / 30% Professional / 10% Enterprise | Hypothèse conservatrice |
| Churn mensuel | 4% (M1-M6) → 2,5% (M7-M12) | Moyenne SaaS B2B vertical |
| CAC moyen | 800€ (Starter) / 2 500€ (Professional) / 15 000€ (Enterprise) | Outbound + temps fondateur |
| Cycle de vente | 2-4 semaines (Starter) / 1-3 mois (Pro) / 3-6 mois (Enterprise) | Estimation courtiers vs enterprise |
| Coût marginal par client | ~5-15€/mois (infra cloud) | AWS/GCP pricing sur usage réel |

## 2. Projection de Revenus — Scénarios 12 Mois

### Scénario Conservateur

| Mois | Nouveaux Clients | Clients Totaux | MRR | ARR Implicite |
|------|-----------------|----------------|-----|---------------|
| M1-M2 | 0 (build + interviews) | 0 | 0€ | — |
| M3 | 3 (bêta → payant) | 3 | 1 470€ | — |
| M4 | 3 | 6 | 2 940€ | — |
| M5 | 4 | 9 | 5 160€ | — |
| M6 | 5 | 13 | 8 070€ | 96K€ |
| M7 | 5 + 1 Professional | 18 | 11 560€ | — |
| M8 | 5 + 1 Pro | 23 | 15 050€ | — |
| M9 | 4 + 2 Pro | 28 | 19 530€ | — |
| M10 | 4 + 2 Pro + 1 Enterprise | 34 | 30 510€ | — |
| M11 | 4 + 2 Pro | 39 | 34 000€ | — |
| M12 | 4 + 2 Pro | 44 | 37 490€ | **~450K€** |

*Note : Churn appliqué mais non détaillé ligne par ligne pour lisibilité.*

### Scénario Optimiste

Si l'urgence CBAM se confirme et qu'un contrat white-label se matérialise en M8-M9 :

| Mois | MRR Optimiste |
|------|--------------|
| M6 | 12 000€ |
| M9 | 35 000€ |
| M12 | 65 000€ (ARR ~780K€) |

### Scénario Pessimiste

Si l'adoption est plus lente (CBAM enforcement mou, ou concurrence plus rapide que prévue) :

| Mois | MRR Pessimiste |
|------|---------------|
| M6 | 3 000€ |
| M9 | 8 000€ |
| M12 | 15 000€ (ARR ~180K€) |

## 3. Unit Economics

### LTV (Lifetime Value)

| Tier | Ticket Mensuel | Durée de vie moyenne (mois) | LTV |
|------|---------------|---------------------------|-----|
| Starter | 490€ | 24 mois | 11 760€ |
| Professional | 1 490€ | 30 mois | 44 700€ |
| Enterprise | 8 000€ | 36+ mois | 288 000€ |

### LTV/CAC Ratio

| Tier | LTV | CAC | LTV/CAC |
|------|-----|-----|---------|
| Starter | 11 760€ | 800€ | **14,7x** ✅ |
| Professional | 44 700€ | 2 500€ | **17,9x** ✅ |
| Enterprise | 288 000€ | 15 000€ | **19,2x** ✅ |

*Ratios excellents. Le seuil de viabilité est généralement considéré à >3x.*

### Payback Period

| Tier | CAC | Ticket Mensuel | Payback |
|------|-----|---------------|---------|
| Starter | 800€ | 490€ | **1,6 mois** ✅ |
| Professional | 2 500€ | 1 490€ | **1,7 mois** ✅ |
| Enterprise | 15 000€ | 8 000€ | **1,9 mois** ✅ |

## 4. Structure de Coûts

### Coûts Fixes Mensuels

| Poste | M1-M6 | M7-M12 |
|-------|-------|--------|
| Infrastructure cloud | 100€ | 300-500€ |
| Outils SaaS (monitoring, email, analytics) | 50€ | 100€ |
| Veille réglementaire (experts freelance) | 0€ (build phase) | 1 500-2 500€ |
| Assurance E&O | 200€ | 200€ |
| Comptabilité/juridique | 100€ | 200€ |
| Marketing (LinkedIn, domaine, etc.) | 100€ | 300€ |
| **Total fixe** | **550€** | **2 600-3 800€** |

### Coûts Variables

- Coût marginal par client : ~5-15€/mois (compute + storage)
- La marge brute sur le SaaS est de **>95%** (typique pour un produit logiciel sans hardware)

### Burn Rate et Runway

**Hypothèse** : l'ingénieur ne se verse pas de salaire les 6 premiers mois (ou se verse un minimum de survie couvert par épargne/chômage).

| Mois | Dépenses Totales | Revenus | Cash Flow Net | Cash Cumulé |
|------|-----------------|---------|---------------|-------------|
| M1-M2 | 1 100€ | 0€ | -1 100€ | -1 100€ |
| M3 | 550€ | 1 470€ | +920€ | -180€ |
| M4 | 550€ | 2 940€ | +2 390€ | +2 210€ |
| M5 | 550€ | 5 160€ | +4 610€ | +6 820€ |
| M6 | 550€ | 8 070€ | +7 520€ | +14 340€ |

**Point mort opérationnel : Mois 3.** Le produit s'autofinance très rapidement dans le scénario conservateur.

**Si l'ingénieur se verse un salaire de 4 000€ net/mois dès M1 :**

| Mois | Dépenses (avec salaire) | Revenus | Cash Flow Net | Cash Cumulé |
|------|------------------------|---------|---------------|-------------|
| M1-M2 | 9 100€ | 0€ | -9 100€ | -9 100€ |
| M3 | 4 550€ | 1 470€ | -3 080€ | -12 180€ |
| M4 | 4 550€ | 2 940€ | -1 610€ | -13 790€ |
| M5 | 4 550€ | 5 160€ | +610€ | -13 180€ |
| M6 | 4 550€ | 8 070€ | +3 520€ | -9 660€ |
| M9 | 6 800€ | 19 530€ | +12 730€ | +7 660€ |

**Point mort (avec salaire) : Mois 8-9.** Investissement initial requis : ~15K€.

## 5. Sensibilités

| Variable | Impact sur ARR M12 | Levier |
|----------|-------------------|--------|
| Ticket moyen +20% | +90K€ | Fort — négociable si valeur prouvée |
| 2x plus de clients | +450K€ | Fort — dépend de la traction GTM |
| Churn +2 points | -40K€ | Moyen — qualité produit critique |
| 1 contrat white-label à 15K€/mois | +180K€ | Très fort — game changer |
| Retard de 3 mois sur le MVP | -120K€ | Fort — urgence d'exécution |

## 6. Besoins de Financement

**Aucun financement externe n'est structurellement nécessaire** pour le scénario conservateur, à condition que l'ingénieur dispose d'une épargne de 15-20K€ pour couvrir les 6 premiers mois.

Un financement de 50-100K€ (Business Angel ou subvention BPI/Innovation) permettrait :
- D'embaucher un commercial spécialisé commerce international (M4-M6)
- D'accélérer la couverture produit (tariff stacking US en parallèle du CBAM)
- De se verser un salaire confortable dès M1

**Mais ce financement est optionnel, pas vital.**
