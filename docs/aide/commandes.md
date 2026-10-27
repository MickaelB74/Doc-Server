---
title: Commandes
description: Les commandes /city des joueurs de Valmont — consultations de la ville, bâtiments, quêtes, interface, habitants, garde, sièges et raids — et tout ce qui se fait auprès des personnages.
---

# Commandes

Toutes les commandes de la ville commencent par **`/city`**, ou par son raccourci **`/c`** : `/c info` équivaut à `/city info`.
{ .chapeau }

!!! info "On agit par les personnages"

    À Valmont, tout ce qu'un personnage sait faire passe par lui : **Alderic** pour les parcelles, la caisse, les bâtiments et les raids, **les artisans** pour leur logis et leurs employés, **Roland** pour la garde. Les commandes des joueurs servent surtout à **consulter** et à **régler votre confort**. Une commande réservée à l'équipe du serveur, tapée par un joueur, rappelle le personnage à aller voir (par exemple `/city claim` : « Cette action passe par les habitants de Valmont… »).

- La touche ++tab++ complète les commandes et les noms (bâtiments, habitants, personnages déjà rencontrés).
- Les accents sont facultatifs : `recits` ou `récits`, `siege` ou `siège`.
- `/city` seul affiche l'aide : seulement les commandes que vous pouvez utiliser, et un rappel des personnages à qui s'adresser pour le reste.

## La ville

| Commande | Effet |
|---|---|
| `/city info` | Niveau de la ville, caisse, parcelles revendiquées / emplacements, prix du prochain emplacement |
| `/city map` | Affiche le contour de la ville pendant 5 secondes |
| `/city progression` | Présélectionne l'onglet « La Renaissance de Valmont » (touche ++l++) et rappelle votre touche. Alias : `progres`, `avancement`, `chroniques` |
| `/city locate [personnage]` | « Où sont-ils ? » : une carte de Valmont et la position des personnages déjà rencontrés ou arrivés en ville. Avec un nom, la carte se centre sur ce personnage. Sans le pack de ressources, la réponse s'affiche dans le chat. Alias : `localiser`, `ou`, `où` |

## Les bâtiments

| Commande | Effet |
|---|---|
| `/city build inspect [nom]` | Rapport d'inspection complet. Sans nom : le bâtiment où vous êtes |
| `/city build show` | Affiche ou masque les contours de tous les bâtiments (nécessite un mod client d'affichage des sélections WorldEdit) |
| `/city build skip` | Pendant l'étape « Point NPC » (ou « Point de travail » d'une annexe), termine le bâtiment sans placer ce point (gardez l'outil en main) |

Créer un bâtiment, changer son type ou le supprimer se fait chez **Alderic → Bâtiments** ; installer un artisan, en lui parlant (**Choisir son logis**). Voir [Les bâtiments](../guide/batiments.md).

!!! tip "Écrire les noms"

    - Les **noms de bâtiments** font un seul mot : les espaces deviennent `_` (exemple : `Maison_du_port`).
    - Pour `/city locate`, le **personnage** s'écrit par son nom complet, sans espace ; les accents et les majuscules sont facultatifs, et le début du nom suffit (`/city locate helene`, `/city locate frereanselme`, `/city locate robin`). La touche ++tab++ complète les noms. Un personnage que personne n'a encore rencontré reste caché : « 🔒 … n'est pas encore arrivé à Valmont. »

## Les quêtes

| Commande | Effet |
|---|---|
| `/city quests` | Ouvre le journal de quêtes, onglet **Suivi** (personnages suivis, position et affichage du panneau) |
| `/city quests toggle` | Fait défiler l'affichage du suivi des quêtes : **visible**, **accroché** (avec la liste des joueurs, touche ++tab++), **masqué** |
| `/city quests toggle <visible\|accroche\|masque>` | Choisit directement cet affichage |
| `/city quests recits` | Ouvre directement l'onglet **Récits** |

## L'interface

| Commande | Effet |
|---|---|
| `/city ui` | Bascule entre menus illustrés et menus classiques. Alias : `interface`, `menus` |
| `/city ui valmont` | Menus illustrés (le pack de ressources est reproposé si besoin) |
| `/city ui classique` | Menus classiques (le pack n'est plus proposé à la connexion) |

## Les habitants, les emplois et la garde

| Commande | Effet |
|---|---|
| `/city habitants` | Bilan de la population : maisons, occupants, lits en deuil, prochaine arrivée. Alias : `population` |
| `/city habitants besoins` | Besoins des habitants, satisfaction et ses effets sur les arrivées et l'impôt. Alias : `satisfaction` |
| `/city emplois` | Emplois des habitants : employés et annexe de travail de chaque artisan. Alias : `jobs`, `travail` |
| `/city garde` | Bilan de la garde : gardes, recrues en formation, rôles disponibles. Alias : `guard` |
| `/city garde former <habitant> <rôle>` | **Menus classiques seulement** : envoie un habitant en formation. Rôles : `soldat`, `archer`, `sergent` |
| `/city garde renvoyer <nom>` | **Menus classiques seulement** : rend un garde ou une recrue à la vie civile |

Avec les menus illustrés, la garde se forme et se renvoie chez Roland (portrait → Actions → La garde) : les deux dernières commandes vous y renvoient. Le rôle est le dernier mot de la commande : le nom de l'habitant peut en compter plusieurs (`/city garde former Jehan 2 archer`).

## Les événements, les sièges et les raids

| Commande | Effet |
|---|---|
| `/city event` | Calendrier des sièges et compte à rebours jusqu'au prochain. Alias : `evenements` |
| `/city siege` | État du siège en cours (vague, direction, temps restant, pertes) |
| `/city raid` | État de l'expédition en cours. Alias : `raids`, `expedition` |
| `/city raid quitter` | Pendant un raid : battre en retraite et rentrer à Valmont ; l'expédition continue sans vous. Alias : `retraite` |

Les raids se lancent chez Alderic : voir [Les raids](../guide/raids.md).

??? note "Pour l'équipe du serveur"

    Ces commandes demandent une permission `citycore.admin` (op par défaut). La plupart s'utilisent aussi depuis la console.

    | Commande | Effet |
    |---|---|
    | `/city create` | Fonde Valmont à l'endroit où vous êtes. **Une seule fois pour tout le serveur** |
    | `/city claim`, `/city unclaim` | Revendique ou rend le chunk où vous êtes, sans passer par Alderic |
    | `/city expand`, `/city deposit <montant>` | Achète un emplacement, verse des coins dans la caisse, sans passer par Alderic |
    | `/city build new`, `type`, `remove`, `assign`, `hauteur` | Gère les bâtiments en commande (voir [Les bâtiments](../guide/batiments.md)) |
    | `/city mods` | Bilan des mods connus du plugin : présents ou absents, comment ils ont été détectés, et les personnages qui en dépendent ou en profitent. Alias : `integrations` |
    | `/city npc <id> spawn` | Fait apparaître un personnage devant vous (en jeu seulement) |
    | `/city npc <id> levelUp` ou `levelDown` | Fait monter ou descendre son rang |
    | `/city npc <id> remove` | Retire le personnage |
    | `/city npc <id> activer` | Pour les tests : votre clic droit sur le personnage ouvre son menu complet (vente, entrepôt, boutique, quêtes, récits), même sans atelier ou encore sur les routes |
    | `/city npc <id> menu` | Ouvre ce menu complet à distance, même si le personnage n'est pas encore apparu (en jeu seulement) |
    | `/city npc <id> desactiver` | Revient au menu normal |
    | `/city npc tous activer` ou `desactiver` | Les mêmes réglages pour tous les personnages d'un coup |

    Le mode test ne vaut que pour l'équipe (les joueurs gardent le menu normal) et n'enregistre rien : le personnage n'est pas installé pour autant (pas d'étape de recrutement validée, ni emplois, ni besoins), et tout s'efface au redémarrage du serveur.

    Identifiants de `/city npc` : les survivants par leur métier (`woodcutter`, `farmer`, `stonemason`, `fisherman`, `miner`, `innkeeper`, `blacksmith`, `weaver`, `stablemaster`, `guard`, `monk`, `scribe`, `glassmaker`, `goldsmith`), les légendes par leur nom (`robin`, `jacksparrow`, `indiana`, `docbrown`, `gandalf`, `geralt`, `harold`, `robinson`, `achab`, `obelix`, `musashi`, `gambrinus`, `geppetto`, `ragnar`, `jeanne`, `hercule`).

## Ce qui se fait auprès des personnages

| Action | Comment |
|---|---|
| Revendiquer une parcelle | Alderic → **clic gauche** sur la barre Parcelles, debout sur le chunk voulu |
| Rendre une parcelle | Alderic → ++shift++ + **clic droit** sur la barre Parcelles |
| Déposer des coins dans la caisse | Alderic → Trésor → Déposer des coins |
| Acheter un emplacement de parcelle | Alderic → Trésor → Agrandir la ville (menu classique : sur l'accueil) |
| Créer, retyper ou supprimer un bâtiment | Alderic → Bâtiments |
| Signer la charte | Alderic → Quêtes de la cité → bouton de la charte |
| Lancer la recherche d'un personnage | Alderic → Quêtes de la cité → clic sur la quête de recrutement |
| Livrer un chantier | Alderic → Quêtes de la cité → clic gauche (livrer) ou ++shift++ + clic droit (réquisitionner) |
| Voir la population et sa satisfaction | Alderic → clic sur son portrait |
| Lancer un raid | Alderic → Événements → Raids |
| Recruter un personnage | Clic droit sur lui → Suivez-moi, puis Choisir son logis en ville |
| Commercer, faire une quête | Clic droit sur un artisan installé |
| Devenir employé d'un artisan | Icône métier dans son écran d'accueil |
| Embaucher des habitants, créer une annexe de travail | Artisan → portrait → Actions → Employés, ou Créer son annexe de travail |
| Former ou renvoyer un garde | Roland → portrait → Actions → La garde |
| Voir la progression de la ville | Touche ++l++, onglet « La Renaissance de Valmont » |
| Annuler une saisie dans le chat | Tapez `annuler` |
