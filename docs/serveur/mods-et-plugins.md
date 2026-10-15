---
title: Mods et plugins
description: Les mods de contenu et les plugins du serveur MyCivilisation, et ce que le joueur en perçoit en jeu.
---

# Mods et plugins

MyCivilisation est un serveur **hybride** : il charge à la fois des **mods NeoForge**, qui ajoutent du contenu au monde, et des **plugins**, qui gèrent la ville, les personnages et l'économie. Cette page présente ce que vous en verrez en jeu.
{ .chapeau }

## Le plugin de la ville : CityCore

**CityCore** est le plugin maison du serveur. C'est lui qui fait vivre tout ce que décrit ce guide :

<div class="grid cards" markdown>

-   **La ville et son territoire**

    Valmont, ses parcelles, sa caisse et ses protections.

-   **L'histoire**

    Les dix chapitres, les quêtes de la cité, la charte et l'onglet de progression (++l++).

-   **Les personnages**

    Alderic, les survivants et les légendes : recrutement, commerce, quêtes et récits.

-   **Les bâtiments**

    Déclaration, inspection automatique et niveaux de 0 à 5.

-   **La vie de la cité**

    Habitants, impôt, garde et sièges.

-   **Les interfaces**

    Menus illustrés, panneau ++tab++, panneau Quêtes et journal de quêtes.

</div>

Sa commande principale est **`/city`**, avec le raccourci **`/c`**. Toutes les commandes sont listées dans la page [Commandes](../aide/commandes.md).

## Les autres plugins

| Plugin | Ce que vous en percevez |
|---|---|
| **Citizens** | Il fait exister les personnages : des PNJ à apparence de joueur |
| **Vault** et **EssentialsX** | La monnaie (les coins) et la bourse de chaque joueur. EssentialsX apporte aussi ses commandes habituelles (`/balance`, `/pay`, `/msg`, `/spawn`…), selon les permissions accordées sur le serveur <span class="vm-badge vm-badge--orange">à confirmer</span> |
| **WorldEdit** | Présent sur le serveur, mais **vous n'en avez pas besoin** pour délimiter un bâtiment : la ville fournit son propre bâton « Sélection ». Il sert seulement à afficher les contours des bâtiments avec `/city build show` |
| **SkinsRestorer** | La gestion des skins des joueurs |

## Les mods de contenu

Le monde contient du contenu de mods, en plus de Minecraft « vanilla » : créatures, objets, structures. Deux mods sont liés à des personnages de l'histoire.

=== "Dragon Mounts Remastered"

    **Des dragons !** Œufs à trouver, éclosion, apprivoisement au poisson, vol à dos de dragon, selles et sifflets.

    Personnage lié : [Harold, le dresseur de dragons](../personnages/legendes/harold.md) (chapitre X, légende ★).

=== "Tax' Ocean Villager"

    **Des navires au large** : navires pirates (océans tempérés et chauds), vaisseaux de la Marine (océans froids et profonds), navires maudits (pirates et marins zombies) et vaisseau de guerre du roi pirate illageois, avec capitaines et matelots marchands. Le mod ajoute aussi des armures, des outils et des disques de pirate et de marin.

    Personnage lié : [Jack Sparrow](../personnages/legendes/jack-sparrow.md) (chapitre III, légende ★).

!!! info "Si un mod manque"

    Si l'un de ces deux mods n'est pas installé sur le serveur, son personnage se recrute et s'installe quand même, mais **ne commerce pas** et **ne donne pas de quêtes**. Il l'explique lui-même dans un dialogue.

D'autres mods peuvent être présents sur le serveur.

!!! equipe "Liste complète du modpack"

    La liste des mods du serveur et du modpack client reste à fournir par l'équipe.

## Mod client facultatif : WorldEditCUI

Le mod client **WorldEditCUI** (version 1.21.1) permet de voir les contours de **tous** les bâtiments avec `/city build show`. Il est **facultatif** : sans lui, la liste des bâtiments d'Alderic affiche quand même les bordures d'un bâtiment en particules bleues. <span class="vm-badge vm-badge--orange">à confirmer</span> s'il fait partie du modpack.
