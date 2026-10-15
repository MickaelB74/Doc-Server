---
title: Alderic
description: Alderic, intendant et maire de Valmont, présent dès la fondation — son rôle, ses menus (quêtes de la cité, bâtiments, trésor, agrandissement), son cadeau de bienvenue et ses récits de chapitre.
---

# Alderic

<div class="vm-fiche" markdown>

![Décor du portrait d'Alderic : mur de pierre orné de deux bannières rouges frappées d'un carré doré](../assets/ui/decors/pf_mairie.png){ .vm-fiche__decor }

<div class="vm-fiche__infos" markdown>

<p class="vm-fiche__titre">✦ Intendant & maire ✦</p>

| | |
|---|---|
| Statut | <span class="vm-badge vm-badge--or">Maire</span> |
| Chapitre | Dès la fondation de la ville |
| Rôle | Quêtes de la cité, charte, bâtiments, caisse de la ville, agrandissement |
| Où le trouver | En ville, qu'il ne quitte jamais |
| Commerce | Aucun |

</div>

</div>

> Dernier intendant de Valmont, il a sauvé la Charte de la ville la nuit où le dragon l'a brûlée.
>
> — *Sa biographie en jeu*

Vingt hivers après la Nuit Noire, Alderic fait renaître Valmont avec vous. C'est lui qui **raconte chaque chapitre**, propose les **quêtes de la cité**, fait **signer la charte** et tient la **caisse commune**. Contrairement aux artisans, il ne se recrute pas, ne vend ni n'achète rien, et n'a ni quêtes personnelles ni récits à accomplir.

## Son rôle

Alderic apparaît à la fondation de la ville, devant le joueur qui la fonde (commande `/city create`, une seule fois pour tout le serveur). Le fondateur lit alors « 🏰 Valmont renaît de ses cendres ! », « 📍 Chunk de départ claim. » et « 👴 Le Maire est apparu devant vous. » La ville commence avec un seul emplacement de chunk : celui de la fondation.

Ensuite, tout passe par lui :

- **L'histoire** : à chaque charte signée, il raconte le chapitre qui s'ouvre (voir plus bas, *Les récits d'Alderic*). La trame complète est décrite dans [La trame en dix chapitres](../guide/trame.md).
- **Les quêtes de la cité** : c'est dans son menu que vous lancez la recherche des survivants (voir [Retrouver et installer un personnage](recrutement.md)), livrez les chantiers et signez la charte.
- **Les bâtiments** : il tient la liste des bâtiments de la ville et permet d'en ajouter ou d'en supprimer.
- **La caisse** : il garde l'argent commun de la ville et vend des emplacements de chunk supplémentaires.

Alderic peut vous suivre, mais il ne quitte jamais la ville. S'il vous accompagne et que vous sortez du territoire, il s'arrête : « Je vous attends là, je dois surveiller la ville... » La barre d'action affiche alors « 🌲 Alderic ne peut pas quitter la ville. »

## Ses menus

Un clic droit sur Alderic ouvre la mairie. Avec le pack de ressources « Valmont », c'est un écran illustré. Sans lui, un menu classique offre les mêmes fonctions ; ses boutons portent parfois un autre nom, indiqué entre parenthèses.

<figure markdown>

![Accueil d'Alderic](../assets/ecrans/maire.png){ width="320" }

<figcaption>L'accueil de la mairie (illustration avec des données d'exemple)</figcaption>

</figure>

### L'accueil

| Élément | Ce qu'il fait |
|---|---|
| En-tête (palier et niveau, par exemple « VILLAGE NIV. 3 ») | Au survol : le chapitre en cours et la taille de la ville |
| Icône « 📜 Récit d'Alderic » | Réécouter le récit du chapitre en cours |
| Icône « 👣 Demander de suivre » / « ⛔ Arrêter de suivre » | Alderic vous accompagne dans la ville ; il s'arrête à la frontière |
| ![Bouton Quêtes](../assets/ui/boutons/btn_quetes.png){ .vm-ui }<br>« 📜 Quêtes de la cité » (classique : « 📖 Infos de la ville ») | Les quêtes du chapitre et la charte. La mention **[PRÊT]** s'affiche quand toutes les quêtes obligatoires sont faites |
| ![Bouton Bâtiments](../assets/ui/boutons/btn_batiments.png){ .vm-ui }<br>« 🏗 Bâtiments » | Gérer les bâtiments de la ville |
| ![Bouton Trésor](../assets/ui/boutons/btn_tresor.png){ .vm-ui }<br>« 💰 Trésor » (classique : « 💰 Économie ») | Voir la caisse de la ville et y déposer des coins |
| ![Bouton Agrandir](../assets/ui/boutons/btn_agrandir.png){ .vm-ui }<br>« 🗺 Agrandir la ville » | Acheter +1 emplacement de chunk avec la caisse |
| Barre « PARCELLES x / y » | Parcelles revendiquées sur emplacements disponibles |

Quand la caisse ne suffit pas, le bouton d'agrandissement est grisé : ![Bouton Agrandir grisé](../assets/ui/boutons/btn_agrandir_off.png){ .vm-ui }. Le menu classique rappelle aussi que la vue d'ensemble de la progression se trouve dans l'écran des progrès de Minecraft (touche ++l++), onglet « La Renaissance de Valmont ».

### Quêtes de la cité

La liste montre les quêtes du chapitre en cours, plus les **quêtes bonus (★) des chapitres précédents** pas encore terminées. Un anneau de couleur entoure chaque quête : **vert** pour une quête accomplie, **ambre** pour une quête en cours, **violet** pour une quête bonus. Une quête bonus porte la mention « Bonus : ne bloque pas l'amélioration ».

| Type de quête | Ce que vous voyez | Ce que fait le clic |
|---|---|---|
| Recruter un personnage | Trois étapes : le trouver, le ramener en ville, l'installer dans un bâtiment | Lance les recherches, ou vous redonne la piste si elles sont déjà lancées. Une fois le personnage en ville, parlez-lui pour l'installer |
| Livrer des matériaux | « Livré : x / y » et ce que vous avez sur vous | **Clic gauche** : livrer depuis votre sac, même des objets achetés à un artisan. ++shift++ + **clic droit** : réquisitionner dans les stocks des artisans ; la caisse paie le prix de revente (le double du prix de rachat), en commençant par l'offre la moins chère |
| Réserve chez un artisan | « Stock de … : x / y » | Rien à cliquer : vendez cette ressource à l'artisan concerné |
| Rang d'un artisan | Rang actuel et rang requis | Rien à cliquer : commercez avec l'artisan pour le faire monter |
| Parcelles, bâtiments, chasse | Progression x / y | Rien à cliquer : la progression est commune à tous les joueurs |

En bas du menu, ![Bouton Récit](../assets/ui/boutons/fb_recit.png){ .vm-ui } permet de réécouter le récit du chapitre (menu classique : le livre « 📜 *titre du chapitre* »). À côté se trouve **la charte**. La signer fait passer la ville au chapitre suivant : il faut que **toutes les quêtes non bonus** soient terminées et que la **caisse de la ville** puisse payer son prix. Le bouton change selon la situation (menu classique : « ⬆ Améliorer la ville → *palier suivant* ») :

| Bouton | Signification |
|---|---|
| ![Bouton Quêtes à finir](../assets/ui/boutons/fb_charte_lock.png){ .vm-ui .vm-ui--grand } | Il reste des quêtes obligatoires (leur nombre est indiqué au survol) |
| ![Bouton Caisse vide](../assets/ui/boutons/fb_charte_fonds.png){ .vm-ui .vm-ui--grand } | Les quêtes sont faites, mais la caisse ne couvre pas le prix de la charte (« Il manque … coins dans la caisse ») |
| ![Bouton Signer charte](../assets/ui/boutons/fb_charte.png){ .vm-ui .vm-ui--grand } | Cliquez pour passer au chapitre suivant (au survol : prix, caisse, emplacements offerts) |
| ![Bouton Capitale](../assets/ui/boutons/fb_capitale.png){ .vm-ui .vm-ui--grand } | Dernier palier atteint : « ⭐ Niveau maximum atteint ! », « Votre cité est la capitale des Marches. », « Les hauts faits restent à accomplir. » |

| Charte signée au chapitre | Pour devenir | Prix (payé par la caisse) | Emplacements de chunk offerts |
|---|---|---|---|
| I — Les cendres et la charte | Hameau | 150 coins | +6 |
| II — Du pain pour l'hiver | Village | 400 coins | +6 |
| III — Les pierres et la rivière | Bourg | 800 coins | +8 |
| IV — La Fosse et le Chaudron | Ville | 1 500 coins | +8 |
| V — Le marteau et le métier | Ville franche | 2 500 coins | +10 |
| VI — Les routes et la garde | Cité | 4 000 coins | +12 |
| VII — La foi et le savoir | Grande cité | 6 000 coins | +14 |
| VIII — L'or, le verre et le feu | Citadelle | 8 500 coins | +16 |
| IX — La Porte du Néant | Capitale | 12 000 coins | +20 |

Au total, les chartes coûtent **35 850 coins** jusqu'à la Capitale. Les emplacements offerts ne font pas monter le prix des agrandissements. Les objectifs de chaque chapitre sont détaillés dans [La trame en dix chapitres](../guide/trame.md).

### Bâtiments

- La liste montre tous les bâtiments de la ville, rangés par type (habitations, ateliers, mairie, divers). Au survol : type, zone, hauteur, personnage installé, habitants d'une maison et état de l'inspection (niveau, ce qui manque).
- Un **cercle doré** signale un bâtiment habité par un artisan, un **cercle rouge** un bâtiment incomplet.
- **Clic gauche** sur un bâtiment : ses bordures s'affichent pendant 5 secondes. **Clic droit** (menu illustré) : changer son type.
- ![Bouton Ajouter](../assets/ui/boutons/fb_ajouter.png){ .vm-ui } « ➕ Ajouter un bâtiment » : choisissez le type, donnez un nom, puis délimitez la zone avec le bâton.
- ![Bouton Retirer](../assets/ui/boutons/fb_supprimer.png){ .vm-ui } « ➖ Supprimer un bâtiment » : un clic sur un bâtiment le supprime.

!!! warning "La suppression est définitive"

    Un bâtiment supprimé ne se récupère pas. Si un artisan y était installé, il se retrouve sans atelier : choisissez-lui un nouveau logis, son stock, ses quêtes et son rang l'attendent.

La **mairie** est un type de bâtiment à part : « Siège d'Alderic et de la Charte. Une seule par ville. » Elle demande un pupitre (pour la Charte) et une bannière de Valmont (n'importe quelle bannière convient), plus les exigences communes : 1 porte, un toit sur 60 % du sol, 2 sources de lumière. Une cloche et une bibliothèque y rapportent des points bonus. Tout est détaillé dans [Les bâtiments](../guide/batiments.md).

### Trésor

- **CAISSE** : l'argent commun de la ville. Elle paie les chartes, les agrandissements et les réquisitions.
- **BOURSE** : votre argent personnel.
- ![Bouton Déposer](../assets/ui/boutons/btn_deposer.png){ .vm-ui } « ⬆ Déposer des coins » : Alderic vous demande le montant dans le chat (« ⬆ Combien de coins voulez-vous déposer dans la caisse ? »). La somme passe de votre bourse à la caisse : « ✅ … coins déposés dans la caisse de la ville. » Vous pouvez aussi taper `/city deposit <montant>`.
- La barre du bas compare la caisse au prix de la prochaine parcelle.

!!! warning "Pas de retrait"

    Une fois déposés, les coins appartiennent à la ville : personne ne peut les reprendre.

### Agrandir la ville

Chaque achat ajoute **+1 emplacement de chunk**, c'est-à-dire le droit de revendiquer une parcelle de plus avec `/city claim`. Le prix est payé par la caisse. Il ne dépend que du nombre d'emplacements déjà **achetés** : ceux offerts par Alderic et par les chartes ne comptent pas. Le premier coûte 150 coins, chacun des suivants 8 % de plus, sans jamais dépasser 2 500 coins.

| Emplacement acheté n° | 1 | 2 | 3 | 4 | 5 | 10 | 20 | 30 | 37 | 38 et suivants |
|---|---|---|---|---|---|---|---|---|---|---|
| Prix (coins) | 150 | 162 | 175 | 189 | 204 | 300 | 647 | 1 398 | 2 395 | 2 500 |

En cas de réussite : « ✅ Capacité étendue ! Max : … », puis « Caisse restante : … coins ». Si la caisse ne suffit pas : « ❌ Fonds insuffisants. Il manque … coins. », avec le rappel « 💡 /city deposit <montant> ». Les parcelles et leurs règles sont expliquées dans [Le territoire](../guide/territoire.md).

## Le cadeau de bienvenue

La première fois qu'un joueur lui parle, Alderic se présente (voir ci-dessous). À la fin de cette présentation, **une seule fois pour toute la ville** (au premier joueur qui l'écoute), il fait un cadeau. Il dit « Voici de quoi commencer... », puis le chat annonce « ✅ La ville a gagné +6 emplacements de chunk et +100 coins. »

- Les 6 emplacements sont offerts : ils ne font pas monter le prix des agrandissements.
- Les 100 coins vont dans la caisse de la ville.
- Avec le chunk de départ, la ville dispose ainsi de 7 emplacements : exactement ce que demande la première quête, « Planter les jalons » (7 chunks).
- Les joueurs suivants entendent la même présentation, mais ne déclenchent plus le cadeau.

## À la première rencontre

La première fois que chaque joueur lui parle (clic droit), Alderic se présente, puis le menu de la mairie s'ouvre. Les fois suivantes, le menu s'ouvre directement.

!!! dialogue "Alderic, à la première rencontre"

    Ah... vous voilà. Je suis Alderic, dernier intendant de Valmont.

    Il y a vingt hivers, un dragon venu du Néant a réduit notre cité en cendres.

    J'ai sauvé ceci : la Charte de Valmont. Avec elle, Valmont renaîtra de ses cendres.

    Parlez-moi pour suivre nos chantiers, agrandir nos terres et gérer la caisse.

## Les récits d'Alderic

À chaque charte signée, tous les joueurs connectés voient le nom du nouveau palier s'afficher en grand, puis lisent « 🎉 La ville devient *palier* (niveau *N*) ! » et « +*X* emplacements de chunk offerts. » Alderic raconte alors le chapitre qui s'ouvre, lettre par lettre au-dessus de la barre d'objets.

Seul le récit du **chapitre en cours** se réécoute en jeu : « 📜 Récit d'Alderic » sur son accueil, ou le bouton ![Bouton Récit](../assets/ui/boutons/fb_recit.png){ .vm-ui } du menu des quêtes. Le récit du chapitre I, qui précède toute charte, ne semble pas joué automatiquement à la fondation : écoutez-le depuis le menu des quêtes <span class="vm-badge vm-badge--orange">à vérifier</span>.

Tous les récits sont recopiés ci-dessous. À partir du chapitre II, ils dévoilent la suite de l'histoire : ils sont repliés, ouvrez-les quand votre ville y arrive.

!!! dialogue "Chapitre I — Les cendres et la charte"

    Vingt hivers ont passé depuis que Valmont a brûlé. Je suis Alderic, son dernier intendant.

    Cette charte est tout ce qui reste de notre ville. Avec elle, Valmont peut renaître, ici même.

    D'abord, délimitons le camp et dressons une palissade.

    On dit qu'un vieux charbonnier vit seul dans les bois. Il nous faut son bois et son savoir.

??? spoiler "Chapitre II — Du pain pour l'hiver"

    Le camp tient bon. Mais un toit ne nourrit personne, et l'hiver approche.

    Bastien jure qu'une fermière survit seule dans les plaines, avec les dernières semences de Valmont.

    Avec du grain en réserve, nous serons un vrai hameau.

    Et méfiez-vous des bois : un archer y détrousse les pillards... mais il paraît qu'il a bon cœur.

??? spoiler "Chapitre III — Les pierres et la rivière"

    Nous voilà village ! Mais nos huttes ne passeront pas un autre hiver.

    Brennan, qui sculpta l'arche de la grande porte, erre dans les collines en dressant des cairns. Lui seul sait choisir la pierre.

    Et il nous faut la rivière : Martin, le passeur dont la barque a sauvé vingt enfants la Nuit Noire, vit toujours sur les rives.

    On signale une voile noire au large. Un capitaine sans navire, paraît-il...

??? spoiler "Chapitre IV — La Fosse et le Chaudron"

    Le village grandit. Il lui faut du charbon pour l'hiver et un lieu où se réchauffer le cœur.

    Godefroy, maître de la Fosse aux Corbeaux, était sous terre quand Valmont a brûlé. Il creuse encore, dans les montagnes.

    Rosalie tenait le Chaudron Doré, la taverne où buvaient toutes les guildes. Retrouvons-la, et sa louche avec.

    Les nuits sont dangereuses : sécurisons les abords avant tout.

??? spoiler "Chapitre V — Le marteau et le métier"

    Nous voici ville ! Le seigneur des Marches nous accorde le droit de marché... si nos ateliers produisent.

    Thorvald a forgé les portes de Valmont : elles ont tenu une heure face au dragon. Il dit que ce n'était pas assez.

    Agathe avait douze ans quand le grand étendard a brûlé. Apprentie des teinturiers, elle seule saurait le refaire.

    Brennan veut des remparts de pierre. « Cette fois, ils tiendront », répète-t-il.

    Un aventurier au chapeau de feutre fouille les ruines du monde. Il paraît qu'il cherche un marché...

??? spoiler "Chapitre VI — Les routes et la garde"

    Nous voici ville franche ! Nos échevins sont élus, et l'impôt nous revient.

    Edmond, maître des écuries royales, a ouvert les stalles la Nuit Noire. Il suit les hardes sauvages dans la savane.

    Roland, sergent de la garde, a perdu toute sa compagnie cette nuit-là. Offrons-lui une milice, et une raison de rester.

    Les pillards rançonnent nos marchands sur les routes. Il est temps de les chasser.

??? spoiler "Chapitre VII — La foi et le savoir"

    Notre renommée dépasse les Marches : nous voici cité ! Une cité doit soigner, et se souvenir.

    Frère Anselme a soigné nos survivants dans les ruines, puis s'est retiré à Saint-Clair. Bâtissons-lui une infirmerie.

    Isabeau, l'archiviste, a sauvé un coffre de registres. Elle cherche depuis vingt ans ce qui a causé la Nuit Noire.

    Un inventeur tombé du ciel dans un éclair cherche un laboratoire... génie ou fou ?

??? spoiler "Chapitre VIII — L'or, le verre et le feu"

    Isabeau a déchiffré les registres : la Nuit Noire est venue d'une Porte, ouverte avec des yeux de feu et de néant.

    Le feu de ces yeux vient des bâtons de blaze, au cœur des forteresses du Nether. Anselme sait les préparer.

    Et la cathédrale renaîtra : Léon porte au cou le dernier éclat de la rosace, Béatrice connaît les secrets du trésor.

    Un vieux magicien gris rôde autour de nos murs. Il semble en savoir long sur cette Porte...

??? spoiler "Chapitre IX — La Porte du Néant"

    Les registres ne mentaient pas : la Porte dort sous la terre, au fond d'un fort oublié.

    Le dragon qui a brûlé Valmont vit toujours, au-delà. Il faut douze yeux pour rouvrir le passage.

    Thorvald forge nos meilleures lames, Anselme prépare ses potions, Roland entraîne la garde.

    Il est temps d'en finir. Pour Valmont.

??? spoiler "Chapitre X — La nouvelle Valmont"

    Le dragon est tombé. Valmont est vengée... et redevient la capitale des Marches !

    Les chansons de Rosalie porteront vos noms pendant des siècles. Mais une capitale doit rester vigilante.

    D'anciens fléaux dorment encore : dans les profondeurs, sous les mers, dans les forteresses du Nether.

    Un chasseur de monstres aux cheveux blancs propose ses services... contre rémunération.

    Et l'on parle d'un jeune Viking qui apprivoise les dragons. Après la Nuit Noire... j'ai peine à y croire.
