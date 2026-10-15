---
title: Les sièges
description: Les sièges de Valmont à partir du chapitre IV — calendrier, alerte, vagues, armées ennemies et champions, rôle de la garde, victoire et récompenses.
---

# Les sièges

Une ville prospère attire les convoitises. **À partir du chapitre IV**, Valmont subit des sièges : des **vagues d'ennemis** viennent s'en prendre à ses habitants et à ses gardes.
{ .chapeau }

!!! nouveau "Fonctionnalité récente"

    Les sièges sont arrivés récemment sur le serveur : certains comportements peuvent encore évoluer. Signalez tout comportement étrange à l'équipe.

## Quand ?

| | Par défaut |
|---|---|
| **Jours et heure** | Le **mercredi** et le **samedi** à **21 h 00** (heure de Paris) |
| **Joueurs minimum** | **2 joueurs connectés** à l'heure dite, sinon le siège est annulé |
| **Annonce** | Un coup de cloche et un message **5 minutes avant** |
| **Premier siège** | Une fois la ville arrivée au chapitre IV (le Bourg) |

`/city event` affiche le calendrier et le compte à rebours jusqu'au prochain siège. Aucun siège n'a lieu si le monde est en difficulté « paisible ».

> « ⚔ Siège dans 5 minutes ! Préparez la défense de Valmont. »

## Le déroulement

<ol class="vm-frise" markdown>
<li markdown>**L'alerte** : cloches d'alarme, titre **« ⚔ Siège ! »**, puis un **cor de guerre** qui vient **du côté attaqué**. Tendez l'oreille ! Vous avez **30 secondes** pour vous préparer.</li>
<li markdown>**Les vagues** : chaque vague peut arriver d'un côté différent, avec **30 secondes de répit** entre deux. Les assaillants apparaissent hors de la ville, une douzaine de blocs au-delà de la lisière.</li>
<li markdown>**La barre de siège** : une barre rouge en haut de l'écran suit le siège (vague en cours, direction, assaillants restants, temps restant).</li>
<li markdown>**La fin** : vous avez **20 minutes** pour repousser toutes les vagues.</li>
</ol>

| Chapitre de la ville | Nombre de vagues |
|---|---|
| IV à VI | 3 |
| VII et VIII | 4 |
| IX et X | 5 |

Les assaillants sont d'autant plus nombreux que la ville est avancée et que des joueurs sont connectés (même loin de la ville) : de 8 par vague au chapitre IV avec un seul joueur, jusqu'à 40 au maximum.

??? info "Le calcul exact du nombre d'assaillants"

    **(4 + chapitre) × (1 + 0,5 × (joueurs connectés − 1))**, arrondi, avec un maximum de 40.

    | Chapitre | 1 joueur | 2 joueurs | 3 joueurs | 4 joueurs | 5 joueurs |
    |---|---|---|---|---|---|
    | IV | 8 | 12 | 16 | 20 | 24 |
    | V | 9 | 14 | 18 | 23 | 27 |
    | VI | 10 | 15 | 20 | 25 | 30 |
    | VII | 11 | 17 | 22 | 28 | 33 |
    | VIII | 12 | 18 | 24 | 30 | 36 |
    | IX | 13 | 20 | 26 | 33 | 39 |
    | X | 14 | 21 | 28 | 35 | 40 |

## Qui attaque ?

À chaque siège, le type est tiré au hasard, une chance sur deux.

=== "Les hordes de monstres"

    | Chapitres | Monstres possibles |
    |---|---|
    | IV à VI | Zombies, squelettes, araignées, pillards, sorcières |
    | VII et VIII | Pillards, zombies, squelettes, araignées, vindicateurs, sorcières, évocateurs |
    | IX et X | Pillards, vindicateurs, zombies, squelettes, araignées, sorcières, évocateurs et **ravageurs** |

    Ces monstres **ne brûlent pas au soleil** et ne disparaissent pas d'eux-mêmes. Squelettes, pillards et vindicateurs ont leur arme, qu'ils ne lâchent jamais.

    **Champion (chapitres IX et X)** : la dernière vague est menée par **Gorvak le Brise-Portes**, un vindicateur lumineux doté de 120 PV et d'une hache en netherite.

=== "Les armées ennemies"

    L'armée d'une faction rivale, tirée au hasard, marche **bannière en tête**. Ses soldats ressemblent à des joueurs, leur nom affiché dans la couleur de leur faction.

    | Faction | Couleur |
    |---|---|
    | **L'Ost du Corbeau** | Noir |
    | **Les Lames de Grisval** | Rouge |
    | **La Horde des Marais** | Vert |

    | Unité | Vie | Combat | Équipement |
    |---|---|---|---|
    | **Milicien** | 20 PV | Au contact | Épée en pierre, armure de cuir |
    | **Archer** | 20 PV | À distance (arc) | Arc, casque et plastron de cuir |
    | **Soldat** | 30 PV | Au contact | Épée en fer, fer et cotte de mailles |
    | **Arbalétrier** | 26 PV | À distance (arbalète) | Arbalète, cotte de mailles et cuir |
    | **Chevalier** | 44 PV | Au contact | Épée en diamant, diamant et fer |

    | Chapitres | Composition de l'armée |
    |---|---|
    | IV à VI | Miliciens, soldats et archers, à parts égales |
    | VII et VIII | Surtout des soldats et des archers, quelques arbalétriers et chevaliers |
    | IX et X | Surtout des chevaliers, des soldats et des arbalétriers |

    **Le porte-étendard** : chaque vague est ouverte par un soldat qui porte la bannière de sa faction sur la tête. Sa chute est annoncée à tous, avec une fanfare.

    **Champion (chapitres VII à X)** : la dernière vague est menée par **Morvan le Noir**, lumineux, doté de 140 PV, d'une armure complète et d'une épée en netherite, qui frappe plus vite que ses hommes.

## Ce que visent les ennemis

1. **D'abord l'habitant, la recrue ou le garde le plus proche.**
2. Faute de cible, les soldats d'une armée attaquent **un joueur proche**.
3. Sinon, tous **marchent sur la mairie** (le bâtiment de type Mairie).

Bonne nouvelle : les soldats ennemis **n'ouvrent pas les portes**, et une maison bien fermée protège ses habitants. Tous les assaillants entrent dans la ville : les tireurs ne restent pas à la lisière.

## Le rôle de la garde

1. **Pendant l'alerte et les répits**, la garde se met en ligne le long du bord attaqué : soldats et sergents en première ligne, archers en seconde ligne.
2. **Dès qu'une vague arrive**, la garde **sort à la rencontre de l'ennemi**, jusqu'à 64 blocs.
3. **Quand il n'y a plus d'assaillant**, les gardes reviennent à leurs postes, puis rentrent chez eux à la fin du siège.

Avant que [Roland](../personnages/survivants/roland.md), le capitaine de la garde, ne rejoigne Valmont, la défense repose entièrement sur les joueurs. Protégez vos habitants !

## Votre rôle pendant un siège

!!! danger "Pendant un siège, vous pouvez être blessé, même en ville"

    Les monstres du siège et les soldats ennemis peuvent vous atteindre. Hors siège, vous restez invulnérable dans la ville.

- **Aucun bloc n'est jamais endommagé** : pas de porte enfoncée, pas d'incendie, pas d'explosion.
- Vous pouvez frapper les soldats ennemis à l'épée ou à l'arc ; un soldat frappé se retourne contre vous.
- Les monstres du siège laissent leur butin habituel (jamais leur arme) ; les soldats ennemis ne laissent ni butin ni expérience.
- Les monstres que vous abattez comptent pour vos **contrats de chasse** auprès des artisans.

## Victoire ou défaite

| | Résultat |
|---|---|
| 🏆 **Victoire** | Fanfare, cloches et **feux d'artifice** aux couleurs de Valmont au-dessus de la mairie. La caisse de la ville reçoit **150 coins + 50 par chapitre**, et Roland gagne de l'expérience |
| 💀 **Défaite** (temps écoulé) | Les assaillants se retirent, sans récompense |

| Chapitre | Coins versés à la caisse | Expérience pour Roland |
|---|---|---|
| IV | 350 | 80 |
| V | 400 | 90 |
| VI | 450 | 100 |
| VII | 500 | 110 |
| VIII | 550 | 120 |
| IX | 600 | 130 |
| X | 650 | 140 |

La récompense va **dans la caisse de la ville**, pas dans votre bourse. Dans les deux cas, le chat affiche un **bilan** : les trois meilleurs défenseurs, les ennemis abattus par la garde et les pertes.

> « Bilan : Arthur (12), Brigitte (7), Céleste (3) ; la garde : 9 ; pertes : 1 habitant(s), 0 garde(s) »

## Commandes utiles

| Commande | Effet |
|---|---|
| `/city event` | Calendrier des sièges et compte à rebours jusqu'au prochain. Alias : `evenements` |
| `/city siege` | État du siège en cours : ennemi, vague, direction, temps restant, assaillants, pertes |
| `/city garde` | Bilan de la garde |
| `/city habitants` | Bilan de la population |
