# 🧮 RegTech Supply Chain

**La calculatrice magique pour les entreprises qui envoient des produits d'un pays à un autre.**

---

## C'est quoi ?

Quand une usine en Chine fabrique un vélo et l'envoie en Europe, le gouvernement dit :
**"Tu dois payer une taxe avant d'entrer."**

Sauf qu'aujourd'hui, ce n'est plus UNE taxe. C'est plein de taxes en même temps :

- 🇪🇺 Une taxe de l'Europe sur le CO₂ du vélo (**CBAM**)
- 🇺🇸 Une taxe des États-Unis qui change toutes les semaines (**tarifs Trump**)
- 📦 La taxe douanière classique qui existe depuis toujours

**Notre outil calcule tout ça d'un coup**, automatiquement, et dit à l'entreprise :
> "Voilà exactement combien tu dois payer, et voilà les papiers à remplir."

---

## À quoi ça sert ?

Imagine que tu as une tirelire, et que trois personnes différentes te demandent des pièces en même temps, mais chacune change le montant tous les jours.

C'est ça le problème des entreprises aujourd'hui. Elles importent des matières premières (acier, aluminium, ciment, engrais...) et elles doivent payer le bon montant aux douanes. **Si elles se trompent, elles ont une amende.**

Notre outil :
1. **Lit les règles** de chaque pays automatiquement
2. **Calcule le vrai prix total** d'un produit importé (le "Total Landed Cost")
3. **Prépare les documents** pour les douanes
4. **Prévient l'entreprise** quand une règle change

---

## C'est quoi les douleurs ?

Les entreprises souffrent de **6 problèmes concrets** :

| # | Le problème | En langage enfant |
|---|------------|-------------------|
| 1 | **Classifier le produit** — Trouver le bon code dans un catalogue de 15 000 codes douaniers | C'est comme devoir trouver le bon tiroir parmi 15 000 tiroirs, et chaque tiroir a un prix différent |
| 2 | **Empiler les taxes** — Plusieurs taxes s'appliquent en même temps, dans un ordre précis | C'est comme un mille-feuille : chaque couche change le prix de la couche suivante |
| 3 | **Calculer le carbone** — Prouver combien de CO₂ a été utilisé pour fabriquer le produit | C'est comme demander à l'usine "combien d'air sale tu as fait ?" et l'usine ne sait pas, ou ment |
| 4 | **Savoir le vrai prix final** — Additionner tout ensemble pour connaître le vrai coût | C'est comme faire les courses dans 3 magasins qui changent leurs prix tous les jours |
| 5 | **Garder une trace** — Tout documenter pour les contrôles douaniers | C'est comme montrer ton carnet de notes au maître : si tu n'as rien écrit, tu es puni |
| 6 | **Suivre les changements** — Les règles changent sans arrêt | C'est comme un jeu où les règles changent en plein milieu de la partie |

---

## Pourquoi ces douleurs existent ?

**Parce que tout est arrivé en même temps :**

- 🗓️ **2025** : Les États-Unis remettent des gros tarifs douaniers (IEEPA, Section 301). Ça change toutes les semaines.
- 🗓️ **2026** : L'Europe lance le CBAM en mode définitif. Maintenant il faut vraiment payer pour le carbone.
- 🗓️ **2025** : La réglementation DORA oblige les entreprises financières à tout tracer numériquement.

Avant, il y avait un système de taxes stable depuis des années. **Maintenant, trois systèmes bougent en même temps.** Les entreprises sont perdues.

---

## Pourquoi personne ne le fait déjà ?

Bonne question. Il y a des gens qui font **un morceau chacun** :

| Qui | Ce qu'ils font | Ce qu'ils ne font pas |
|-----|---------------|----------------------|
| Avalara, Descartes | Les vieilles taxes douanières | Le carbone (CBAM) |
| Sphera, CarbonChain | Le calcul du carbone | Les taxes douanières |
| SAP GTS | Un gros logiciel qui fait tout, mais mal | Rien de spécifique, et ça coûte 500 000€ |

**Personne ne fait les trois ensemble.** Pourquoi ?

1. **C'est tout neuf.** Le CBAM + les tarifs Trump ensemble, ça n'existait pas il y a 18 mois. Le problème est trop récent.
2. **Les gros sont trop lents.** SAP et Oracle mettront 2-3 ans à s'adapter. C'est notre fenêtre.
3. **C'est technique.** Assembler les trois (douane + carbone + tarifs US) demande de la data science, du NLP et de l'optimisation. Chaque brique existe, mais personne ne les a encore collées ensemble.

---

## En une phrase ?

> **On aide les entreprises à ne pas se faire gronder par les douanes — partout dans le monde, en temps réel, automatiquement.**

---

## Pour aller plus loin

📂 L'analyse complète du projet est dans le dossier [`01-regtech-supply-chain/`](.)
📊 Le benchmark des 3 opportunités étudiées est dans [`benchmark-comparatif.md`](../benchmark-comparatif.md)
