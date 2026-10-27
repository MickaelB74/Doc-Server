---
title: La garde de Valmont
description: Former des gardes auprès de Roland, le capitaine de la garde — rôles, taille de la garde, formation, patrouilles et renvoi.
---

# La garde de Valmont

Parmi les survivants à retrouver figure **[Roland](../personnages/survivants/roland.md), le capitaine de la garde** (chapitre VI). Une fois installé dans son atelier, il peut **former des habitants** pour en faire des gardes qui patrouillent et défendent la ville.
{ .chapeau }

!!! nouveau "Fonctionnalité récente"

    La garde est arrivée récemment sur le serveur : certains comportements peuvent encore évoluer.

## Former une recrue

<div class="grid cards" markdown>

-   ![](../assets/ui/icones/ic_story.png){ .vm-icone } **Avec les menus illustrés**

    ---

    Parlez à Roland, cliquez sur son **portrait**, puis ![Actions](../assets/ui/boutons/btn_actions.png){ .vm-ui } et **La garde**. Cliquez sur un habitant (anneau vert), puis choisissez son **rôle**.

-   ![](../assets/ui/icones/ic_info.png){ .vm-icone } **Par commande**

    ---

    `/city garde former <habitant> <rôle>`, avec le rôle `soldat`, `archer` ou `sergent`. Cette commande est réservée aux **menus classiques**, où Roland n'a pas d'écran de la garde. Avec les menus illustrés, elle vous renvoie chez Roland.

</div>

Il faut que Roland soit **installé dans son atelier**, qu'il reste de la place dans la garde, et qu'il ne forme pas déjà le maximum de recrues. Dans la liste de la garde, les anneaux indiquent l'état de chacun :

| Anneau | Signification |
|---|---|
| ![](../assets/ui/anneaux/ring_purple.png){ .vm-anneau } Violet | Un garde en service |
| ![](../assets/ui/anneaux/ring_amber.png){ .vm-anneau } Ambre | Une recrue en formation |
| ![](../assets/ui/anneaux/ring_green.png){ .vm-anneau } Vert | Un habitant que l'on peut former |
| ![](../assets/ui/anneaux/ring_gray.png){ .vm-anneau } Gris | Un habitant, mais plus de place dans la garde |

## Les rôles

| Rôle | Rang de Roland requis | Formation | Vie | Combat | Équipement |
|---|---|---|---|---|---|
| **Soldat** | ★ Novice | 10 min | 30 PV | Au contact | Épée, casque, plastron, jambières et bottes en fer |
| **Archer** | ★★ Apprenti | 15 min | 24 PV | À distance, à l'arc | Arc, cuir et cotte de mailles |
| **Sergent** | ★★★★ Expert | 25 min | 40 PV | Au contact, lourdement équipé | Épée et plastron en diamant, pièces en fer |

## La taille de la garde

| Rang de Roland | Gardes au maximum (recrues comprises) | Formations simultanées |
|---|---|---|
| ★ Novice | 8 | 2 |
| ★★ Apprenti | 16 | 3 |
| ★★★ Compagnon | 25 | 4 |
| ★★★★ Expert | 36 | 5 |
| ★★★★★ Maître | 50 | 6 |

Pour agrandir la garde, faites **monter Roland en rang** : commercez avec lui, faites ses quêtes (ses quêtes spéciales sont des contrats de chasse) et **remportez des sièges**, qui lui rapportent de l'expérience.

## Comment ça marche

- **La garde est commune** : n'importe quel joueur peut lancer une formation ou renvoyer un garde.
- La recrue s'**entraîne à côté de Roland**, jour et nuit, avec un minuteur au-dessus de la tête. **Le temps n'avance que si au moins un joueur est connecté** ; sinon le minuteur affiche « ⏸ ». Un redémarrage du serveur ne fait pas perdre la progression.
- À la fin, elle revêt **l'uniforme de la garde** et reçoit l'équipement de son rôle :

    > « 🛡 Jehan a terminé sa formation : Soldat de la garde de Valmont. »

- Les gardes **patrouillent dans la ville jour et nuit**. Ils ne dorment pas et n'entrent pas dans les bâtiments.
- Ils repèrent les monstres **dans la ville** jusqu'à 16 blocs. Soldats et sergents attaquent au contact ; les archers tirent jusqu'à 14 blocs. En temps normal, ils ne poursuivent pas un monstre hors de la ville.
- Ils ne blessent jamais **un joueur, un habitant ni un animal**, même par une flèche perdue, et les joueurs ne peuvent pas les blesser.
- Au repos, un garde regagne peu à peu sa vie.
- Un garde **garde son lit** et ne paie pas l'impôt. Un habitant employé chez un artisan quitte son emploi en entrant en formation.
- La garde fait la **sécurité** des habitants, l'un de leurs besoins : 1 garde pour 5 habitants donne 100 % (voir [Les habitants](habitants.md#besoins-et-satisfaction)).

## Renvoyer un garde

**Maj + clic droit** sur lui dans la liste de la garde, ou `/city garde renvoyer <nom>` avec les menus classiques. Il redevient un habitant ordinaire, retrouve son apparence et paie de nouveau l'impôt. Le même geste sur une recrue arrête sa formation.

!!! danger "Un garde tombé n'est pas remplacé automatiquement"

    Son lit reste en deuil 20 minutes, puis un nouvel habitant arrive : il faudra le former à son tour. Un garde mort ne laisse ni arme, ni armure.

## Pendant un siège

La garde se met en ligne sur le côté attaqué pendant l'alerte, puis **sort à la rencontre de l'ennemi** à l'arrivée de chaque vague. Tout est expliqué dans [Les sièges](sieges.md#le-role-de-la-garde).

Le suivi complet : `/city garde` (ou `/city guard`) affiche la taille de la garde, les gardes en service, les recrues en formation et les rôles disponibles.
