---
title: Les habitants
description: Les habitants de Valmont — leur arrivée dans les maisons, leur vie de jour comme de nuit, l'impôt de l'aube, leurs besoins et leur satisfaction, leur travail chez les artisans, les dangers, le deuil et les départs.
---

# Les habitants

Valmont n'est pas qu'une ville d'artisans. Des **habitants** viennent s'installer dans vos maisons, y vivent, y dorment et paient l'impôt chaque matin.
{ .chapeau }

!!! nouveau "Fonctionnalité récente"

    Les habitants, leurs besoins, leurs emplois, la garde et les sièges viennent d'arriver sur le serveur : certains comportements et réglages peuvent encore évoluer. Signalez tout comportement étrange à l'équipe.

## Leur offrir un toit

**Chaque lit d'une habitation conforme accueille un habitant.** Une maison avec trois lits offre trois places. Pour être conforme, une habitation doit être déclarée comme **Habitation** et contenir au moins :

- un **lit** ;
- une **porte** ;
- **deux sources de lumière** ;
- un **toit** couvrant 60 % du sol.

Si une habitation devient incomplète (porte retirée, toit abîmé…), ses habitants restent, mais elle n'en accueille plus de nouveaux. La déclaration d'un bâtiment est expliquée dans [Les bâtiments](batiments.md).

## Leur arrivée

- **Un nouvel habitant arrive au plus toutes les 5 minutes**, s'il reste un lit libre et qu'au moins un joueur est connecté. Ce délai varie avec la [satisfaction](#besoins-et-satisfaction) des habitants.
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

Plus Valmont est peuplée, plus elle est riche. Les gardes et les recrues servent la ville et ne paient pas. Si plusieurs jours passent d'un coup (une nuit sautée en dormant), l'impôt n'est versé qu'une fois. Le montant est multiplié selon la [satisfaction](#besoins-et-satisfaction) des habitants ; le message l'indique alors, par exemple « (satisfaction : ×1,5) ».

## Besoins et satisfaction

Juste avant l'impôt, à chaque aube, les habitants **mangent et se soignent** dans les entrepôts des artisans. Le chat publie le bilan : *« 🌅 Aube à Valmont : satisfaction 72 % (nourriture …, sécurité …, santé …, confort …) »*.

| Besoin | Poids | D'où il vient | Compté dès que… |
|---|---|---|---|
| **Nourriture** | 35 | Chaque habitant mange 4 rations, prises dans les entrepôts d'[Hélène](../personnages/survivants/helene.md) (cultures) et de [Rosalie](../personnages/survivants/rosalie.md) (viandes) | Hélène ou Rosalie est installée |
| **Sécurité** | 25 | 1 garde pour 5 habitants donne 100 %. Les 3 derniers [sièges](sieges.md) comptent pour 40 % : une défaite la fait chuter | [Roland](../personnages/survivants/roland.md) est installé |
| **Santé** | 15 | Chaque habitant reçoit 1 soin, pris dans l'entrepôt de [frère Anselme](../personnages/survivants/frere-anselme.md) (miel, verrues du Nether, poudre lumineuse…) | Frère Anselme est installé |
| **Confort** | 25 | Le niveau de sa maison : 20 % si elle est incomplète, puis 40, 55, 70, 85 et 100 % du niveau 1 au niveau 5 | Il y a des habitants |

- La **satisfaction**, de 0 à 100 %, est la moyenne des besoins comptés, selon leur poids. Gardes et recrues comptent parmi les habitants.
- Nourriture et santé sont lissées : la moitié vient de l'aube précédente, l'autre moitié du jour même.
- Pour nourrir et soigner la ville, vendez des cultures et des viandes à Hélène et à Rosalie, et des remèdes à frère Anselme. Leurs entrepôts baissent aussi un peu chaque heure (voir [Commerce et économie](commerce.md#les-artisans-consomment)).

!!! tip "Un bonus, jamais une punition"

    Un habitant mécontent **ne quitte jamais la ville**. La satisfaction ne fait qu'accélérer ou ralentir un peu la vie de Valmont :

    | Satisfaction | Délai entre deux arrivées | Impôt de l'aube |
    |---|---|---|
    | 80 % et plus | × 0,6 (3 minutes) | × 1,5 |
    | De 50 à 79 % | × 1 (5 minutes) | × 1 |
    | Moins de 50 % | × 1,5 (7 min 30) | × 0,75 |

Pour suivre la satisfaction :

- panneau ++tab++ : ligne **Satisfaction**, avec une barre (verte à 70 % et plus, ambre à 40 % et plus, rouge en dessous) ;
- Alderic → **clic sur son portrait** : l'écran **Population** détaille chaque besoin, ses conseils, les effets sur les arrivées et l'impôt, et le confort de chaque habitation (menu classique : le bouton « 😊 Satisfaction des habitants » affiche le bilan dans le chat) ;
- `/city habitants besoins` : le même bilan dans le chat.

## Le travail des habitants

Les artisans installés peuvent **embaucher des habitants** pour remplir leur entrepôt, la réserve de la ville où chacun se sert gratuitement.

<ol class="vm-frise" markdown>
<li markdown>**Créez son annexe de travail.** Chez l'artisan, cliquez sur son **portrait**, puis ![Actions](../assets/ui/boutons/btn_actions.png){ .vm-ui } → **Créer son annexe de travail** : donnez un nom, délimitez la zone au bâton, puis placez le **point de travail** (ou `/city build skip` : le centre de la zone).</li>
<li markdown>**Embauchez.** Actions → **Employés** : cliquez sur un habitant sans emploi. ++shift++ + clic droit sur un employé le renvoie.</li>
<li markdown>**Laissez-les travailler.** Le jour, l'employé se rend à l'annexe ; à chaque cycle, il ajoute à l'entrepôt **8 exemplaires de chaque objet courant** que l'artisan rachète. La nuit, il dort.</li>
</ol>

| Repère | Valeur |
|---|---|
| Employés par artisan | 1 au rang Novice, 2 aux rangs Apprenti et Compagnon, 3 aux rangs Expert et Maître |
| Annexe de travail | Une zone de la ville, comme un bâtiment : 1 source de lumière, ni porte ni toit exigés, et les deux premiers outils du métier de l'artisan (les blocs bonus de son atelier ; les suivants rapportent des points) |
| Durée d'un cycle | 4 minutes avec une annexe de niveau 1, puis 3 min 30, 3 min, 2 min 30 et 2 minutes au niveau 5 |
| Objets de valeur | Produits plus rarement ; au-delà de 20 coins l'unité, jamais |
| Plafond | Les employés s'arrêtent à 50 % de la capacité de l'entrepôt : vos ventes gardent leur prix |

- La production n'a lieu que **le jour**, quand au moins un joueur est connecté. Elle ne rapporte ni coins ni expérience à l'artisan.
- Le menu des employés est commun à tous les joueurs. Un employé reste un habitant : il paie l'impôt et peut être formé à la garde (il quitte alors son emploi).
- Ce menu passe par les écrans illustrés : il n'existe pas dans les menus classiques.
- Le bilan de tous les artisans : `/city emplois`.

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

Ce sont les seules raisons : une faible satisfaction ne fait jamais partir personne.

!!! warning "Avant de réaménager une maison"

    Casser un lit fait partir son occupant, même s'il est garde. Prévenez les autres joueurs avant de transformer une habitation.

## Suivre la population

- Panneau ++tab++ : ligne **Habitants**, au format « vivants / places », puis la ligne **Satisfaction**.
- Liste des bâtiments d'Alderic : *« Habitants : 2 / 3 lits (1 en deuil) »* sur chaque habitation.
- Écran **Population** d'Alderic (clic sur son portrait) : habitants, places, gardes, recrues, deuils et employés.
- `/city habitants` (ou `/city population`) : le bilan complet. Un employé y est suivi du nom de son artisan.

```text
🏘 Habitants de Valmont : 3/4 (lits des habitations conformes) — 1 lit(s) en deuil
• Maison (3 lits) : Jehan, Margot, ☠ Perrine (12 min)
• Cabane (0 lits, incomplète) : personne
Prochaine arrivée possible dans 3 min 12 s ; impôt : 2 coin(s) par habitant civil à l'aube.
```

`/city habitants besoins` donne le bilan des besoins et de la satisfaction, et `/city emplois` celui des emplois.
