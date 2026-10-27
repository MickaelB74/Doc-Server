---
title: Le territoire
description: Les parcelles et emplacements de Valmont, la revendication auprès d'Alderic, l'agrandissement, la caisse de la ville et les protections en ville.
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

Tout passe par **Alderic** et la barre **PARCELLES** de son accueil (menu classique : la carte « 🗺 Parcelles de la ville »). Elle agit sur le chunk où vous vous tenez :

1. Demandez à Alderic de vous **suivre** (icône 👣 de son accueil) jusqu'à la limite de la ville. Il ne la franchit pas : il vous attend à la frontière.
2. Placez-vous dans le chunk voulu et parlez-lui.
3. **Clic gauche** sur la barre PARCELLES. Sa bulle indique d'avance l'état du chunk (« parcelle libre, voisine de la ville », « parcelle trop éloignée de la ville »…).

Il faut que :

- le chunk **touche la ville par un côté** (un coin ne suffit pas) ;
- la ville ait **au moins un emplacement libre**.

++shift++ + **clic droit** sur la même barre rend le chunk où vous vous tenez : l'emplacement redevient libre et les protections de la ville ne s'y appliquent plus. On ne peut pas retirer le dernier chunk, ni un chunk où se trouve un bâtiment de la ville (supprimez-le d'abord).

!!! note "Les commandes /city claim et /city unclaim"

    Elles sont réservées à l'équipe du serveur. Tapées par un joueur, elles rappellent le chemin à suivre chez Alderic.

## Obtenir plus d'emplacements

- **En signant les chartes** : chaque nouveau palier offre des emplacements (voir [La trame principale](trame.md#5-la-charte)).
- **En les achetant chez Alderic** : Trésor → bouton ![Agrandir](../assets/ui/boutons/btn_agrandir.png){ .vm-ui } (+1 emplacement), **payé par la caisse de la ville**. Dans le menu classique, ce bouton est sur l'accueil d'Alderic.

| Emplacement acheté n° | Prix |
|---|---|
| 1 | 50 coins |
| 10 | 65 coins |
| 20 | 88 coins |
| 30 | 118 coins |
| 40 | 158 coins |
| 50 | 213 coins |
| 62 et suivants | 300 coins (plafond) |

Chaque emplacement acheté coûte **3 % de plus** que le précédent, sans jamais dépasser 300 coins. Les emplacements offerts par les chartes ne font pas monter le prix. Quand la caisse ne suffit pas, le bouton est grisé : ![Agrandir indisponible](../assets/ui/boutons/btn_agrandir_off.png){ .vm-ui }

!!! tip "Prévoyez quelques achats"

    À chaque chapitre, les objectifs de territoire demandent un peu plus d'emplacements que ceux offerts par les chartes. Comptez **36 emplacements achetés** (environ 3 200 coins au total) pour aller jusqu'au chapitre VIII (le détail est dans [La trame principale](trame.md#8-les-dix-chapitres-en-detail)).

## Voir les limites de la ville

- `/city map`, ou un **clic droit** sur la barre PARCELLES d'Alderic, affiche le **contour de la ville** en colonnes de particules dorées pendant 5 secondes.
- En franchissant la limite, vous lisez **« 🏰 Territoire de Valmont »** ou **« 🌲 Quitter le territoire de la ville »** au-dessus de la barre d'objets.

## La caisse de la ville

La caisse est **commune à tous les joueurs** et distincte de votre bourse.

| Elle reçoit | Elle paie |
|---|---|
| Vos dépôts : Alderic → Trésor → ![Déposer](../assets/ui/boutons/btn_deposer.png){ .vm-ui } | Les chartes |
| L'impôt des habitants, chaque matin | Les emplacements achetés |
| Les récompenses des sièges victorieux | |
| Les récompenses des [raids](raids.md) réussis | |
| Le cadeau de bienvenue d'Alderic (100 coins, une seule fois) | |

Les réquisitions pour les chantiers ne coûtent rien : elles puisent gratuitement dans les entrepôts des artisans.

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
