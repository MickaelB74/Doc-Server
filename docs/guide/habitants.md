---
title: Les habitants
description: Les habitants de Valmont — leur arrivée dans les maisons, leur vie de jour comme de nuit, l'impôt de l'aube, les dangers, le deuil et les départs.
---

# Les habitants

Valmont n'est pas qu'une ville d'artisans. Des **habitants** viennent s'installer dans vos maisons, y vivent, y dorment et paient l'impôt chaque matin.
{ .chapeau }

!!! nouveau "Fonctionnalité récente"

    Les habitants, la garde et les sièges viennent d'arriver sur le serveur : certains comportements peuvent encore évoluer. Signalez tout comportement étrange à l'équipe.

## Leur offrir un toit

**Chaque lit d'une habitation conforme accueille un habitant.** Une maison avec trois lits offre trois places. Pour être conforme, une habitation doit être déclarée comme **Habitation** et contenir au moins :

- un **lit** ;
- une **porte** ;
- **deux sources de lumière** ;
- un **toit** couvrant 60 % du sol.

Si une habitation devient incomplète (porte retirée, toit abîmé…), ses habitants restent, mais elle n'en accueille plus de nouveaux. La déclaration d'un bâtiment est expliquée dans [Les bâtiments](batiments.md).

## Leur arrivée

- **Un nouvel habitant arrive au plus toutes les 5 minutes**, s'il reste un lit libre et qu'au moins un joueur est connecté.
- Il apparaît à la lisière de la ville et **marche jusqu'à sa maison**. Le chat l'annonce : *« 🏠 Jehan s'installe à Valmont (Maison, lit 2/3) »*.
- Chacun porte un **prénom médiéval** : Jehan, Margot, Guillemette, Thibault, Perrine, Aliénor, Enguerrand, Mahaut, Héloïse, Baudouin, Mélisende… Au-delà de 55 habitants, les prénoms reviennent avec un numéro (« Jehan 2 »).
- Les habitants ont l'apparence de joueurs, avec des tenues qui varient.

## Leur vie

| | Ce que fait l'habitant |
|---|---|
| ☀ **Le jour** | Il flâne autour de sa maison, avec de petites pauses, **sans jamais quitter la ville** |
| ☾ **La nuit** | Il rentre chez lui et **dort dans son lit**, puis se lève au matin |

Les habitants ouvrent les portes. Pour ménager le serveur, seuls les habitants **les plus proches des joueurs** sont affichés : les autres continuent d'exister, comptent dans la population et paient l'impôt.

## L'impôt de l'aube

À chaque **nouveau jour de jeu**, chaque habitant verse **2 coins** dans la caisse de la ville :

> « 💰 Impôt de l'aube : 3 habitants → +6 coins »

Plus Valmont est peuplée, plus elle est riche. Les gardes et les recrues servent la ville et ne paient pas. Si plusieurs jours passent d'un coup (une nuit sautée en dormant), l'impôt n'est versé qu'une fois.

## Les dangers

- **Les joueurs ne peuvent pas blesser les habitants** : vos coups et vos flèches n'ont aucun effet sur eux.
- **Les monstres, si** : la nuit, un monstre qui rôde près d'un habitant peut s'en prendre à lui.
- Pendant un [siège](sieges.md), les assaillants les visent en priorité.

!!! tip "Protéger la population"

    Éclairez bien la ville, construisez des maisons bien fermées et formez une [garde](garde.md).

Quand un habitant meurt, **son lit reste en deuil 20 minutes**, puis un nouvel habitant peut s'y installer :

> « ☠ Jehan a été tué (Maison). Un nouvel habitant viendra dans 20 min. »

## Les départs

Un habitant **quitte la ville** :

- immédiatement si **son lit est cassé** ;
- si **sa maison est supprimée** ou **change de type**.

!!! warning "Avant de réaménager une maison"

    Casser un lit fait partir son occupant, même s'il est garde. Prévenez les autres joueurs avant de transformer une habitation.

## Suivre la population

- Panneau ++tab++ : ligne **Habitants**, au format « vivants / places ».
- Liste des bâtiments d'Alderic : *« Habitants : 2 / 3 lits (1 en deuil) »* sur chaque habitation.
- `/city habitants` (ou `/city population`) : le bilan complet.

```text
🏘 Habitants de Valmont : 3/4 (lits des habitations conformes) — 1 lit(s) en deuil
• Maison (3 lits) : Jehan, Margot, ☠ Perrine (12 min)
• Cabane (0 lits, incomplète) : personne
Prochaine arrivée possible dans 3 min 12 s ; impôt : 2 coin(s) par habitant civil à l'aube.
```

??? example "Bientôt : les besoins des habitants"

    Les habitants auront bientôt des **besoins** (nourriture, sécurité, santé, confort), dont découlera la satisfaction de la ville. Cette fonctionnalité **n'est pas encore disponible** : voir [Fonctionnalités à venir](../aide/a-venir.md).
