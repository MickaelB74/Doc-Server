---
title: Le territoire
description: Les parcelles et emplacements de Valmont, la revendication avec /city claim, l'agrandissement chez Alderic, la caisse de la ville et les protections en ville.
---

# Le territoire

Le territoire de Valmont se compte en **parcelles** : des chunks de 16 × 16 blocs, du fond du monde jusqu'au ciel. Cette page explique comment la ville s'agrandit, comment fonctionne sa caisse et ce qui y est protégé.
{ .chapeau }

## Parcelles et emplacements

Deux chiffres sont à suivre, affichés sous la forme `7/13` dans le panneau ++tab++, chez Alderic et avec `/city info` :

| Notion | Signification |
|---|---|
| **Parcelles revendiquées** (à gauche) | Les chunks qui font réellement partie de la ville |
| **Emplacements** (à droite) | Le nombre maximal de parcelles que la ville peut revendiquer |

## Revendiquer une parcelle

Placez-vous dans le chunk voulu et tapez `/city claim`. Il faut que :

- le chunk **touche la ville par un côté** (un coin ne suffit pas) ;
- la ville ait **au moins un emplacement libre**.

`/city unclaim` rend le chunk où vous vous tenez : l'emplacement redevient libre et les protections de la ville ne s'y appliquent plus. On ne peut pas retirer le dernier chunk.

## Obtenir plus d'emplacements

- **En signant les chartes** : chaque nouveau palier offre des emplacements (voir [La trame principale](trame.md#5-la-charte)).
- **En les achetant chez Alderic** : bouton ![Agrandir](../assets/ui/boutons/btn_agrandir.png){ .vm-ui } (+1 emplacement), **payé par la caisse de la ville**.

| Emplacement acheté n° | Prix |
|---|---|
| 1 | 150 coins |
| 5 | 204 coins |
| 10 | 300 coins |
| 20 | 647 coins |
| 30 | 1 398 coins |
| 38 et suivants | 2 500 coins (plafond) |

Chaque emplacement acheté coûte **8 % de plus** que le précédent, sans jamais dépasser 2 500 coins. Les emplacements offerts par les chartes ne font pas monter le prix. Quand la caisse ne suffit pas, le bouton est grisé : ![Agrandir indisponible](../assets/ui/boutons/btn_agrandir_off.png){ .vm-ui }

!!! tip "Prévoyez quelques achats"

    Dès le chapitre II, les objectifs de territoire demandent un peu plus d'emplacements que ceux offerts. Comptez **7 emplacements achetés** pour aller jusqu'au chapitre VIII (le détail est dans [La trame principale](trame.md#8-les-dix-chapitres-en-detail)).

## Voir les limites de la ville

- `/city map` affiche le **contour de la ville** en colonnes de particules dorées pendant 5 secondes.
- En franchissant la limite, vous lisez **« 🏰 Territoire de Valmont »** ou **« 🌲 Quitter le territoire de la ville »** au-dessus de la barre d'objets.

## La caisse de la ville

La caisse est **commune à tous les joueurs** et distincte de votre bourse.

| Elle reçoit | Elle paie |
|---|---|
| Vos dépôts : `/city deposit <montant>`, ou Alderic → Trésor → ![Déposer](../assets/ui/boutons/btn_deposer.png){ .vm-ui } | Les chartes |
| L'impôt des habitants, chaque matin | Les emplacements achetés |
| Les récompenses des sièges victorieux | Les réquisitions pour les chantiers |
| Le cadeau de bienvenue d'Alderic (100 coins, une seule fois) | |

!!! warning "Un dépôt est définitif"

    Une fois déposés, les coins appartiennent à la ville : ils ne se reprennent pas.

## Ce qui est protégé en ville

Sur toutes les parcelles de Valmont, du fond jusqu'au ciel :

<div class="grid cards" markdown>

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Vous êtes invulnérable**

    ---

    Monstres, chute, lave, noyade, feu… Seule exception : **pendant un siège**, les assaillants peuvent vous blesser.

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Aucune explosion**

    ---

    Creepers, TNT, boules de feu, Wither… n'abîment rien.

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Aucun incendie**

    ---

    Seul un joueur peut allumer un feu, et il ne se propage pas.

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Les monstres ne touchent pas aux blocs**

    ---

    Pas d'enderman qui vole des blocs, pas de porte enfoncée par les zombies.

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Cultures et décors préservés**

    ---

    Cultures et œufs de tortue ne sont jamais piétinés. Tableaux, cadres et porte-armures ne sont abîmés que par un joueur.

-   ![](../assets/ui/badges/badge_check.png){ .vm-icone } **Habitants et gardes intouchables**

    ---

    Les habitants et les gardes ne peuvent pas être blessés par les joueurs.

</div>

!!! warning "Les protections visent les monstres, pas les joueurs"

    Rien n'empêche un joueur de casser un bloc ou d'ouvrir un coffre. Valmont est une ville coopérative : respectez le travail des autres.
