---
title: Foire aux questions
description: Les réponses aux questions les plus fréquentes des joueurs de Valmont — démarrage, personnages, quêtes, commerce, bâtiments, habitants, sièges, raids et spoilers.
---

# Foire aux questions

Les questions que se posent le plus souvent les habitants de Valmont. Cliquez sur une question pour afficher sa réponse.
{ .chapeau }

## Démarrer

??? question "Par où commencer ?"

    Parlez à **Alderic** (clic droit) et ouvrez **Quêtes de la cité** : vous y verrez les objectifs du moment. Voir [Premiers pas](../guide/index.md). À Valmont, on agit par les personnages : les commandes `/city` servent surtout à consulter (voir [Commandes](commandes.md)).

??? question "Je ne vois pas les menus illustrés."

    Vous avez sans doute refusé le pack de ressources. Tapez `/city ui valmont` : il vous sera reproposé.

??? question "Le panneau des quêtes déborde ou est mal placé."

    Ouvrez `/city quests` et choisissez la position **BORD**, **MARGE** ou **PRÈS** selon votre écran. `/city quests toggle` fait défiler les trois affichages : **visible**, **accroché** (le suivi passe dans la liste des joueurs, touche ++tab++) et **masqué**.

## Les personnages

??? question "Je ne trouve pas le personnage recherché."

    Suivez la **barre en haut de l'écran** : elle se remplit et change de couleur à mesure que vous approchez. Si elle reste vide, vous êtes à plus de 500 blocs. Partez vers les paysages qui correspondent à son métier : ils sont indiqués sur [sa fiche](../personnages/index.md).

??? question "J'ai perdu la piste de recrutement."

    Cliquez de nouveau sur la quête dans le menu d'Alderic : *« Cliquez pour récupérer la piste. »*

??? question "Le jeu dit « Impossible de trouver un endroit sûr »."

    Le personnage n'apparaît que dans des zones déjà explorées. Explorez davantage autour de la ville, puis relancez la recherche.

??? question "Mon personnage me suit mal."

    Il vous rejoint s'il est distancé, nage et monte dans votre barque. S'il s'est arrêté, reparlez-lui et choisissez **Suivez-moi**.

??? question "Il refuse de s'installer dans l'atelier."

    L'atelier est incomplet pour lui. Survolez l'atelier dans **Choisir son logis**, ou tapez `/city build inspect <nom>` : la liste de ce qui manque s'affiche. Vérifiez aussi qu'il s'agit bien d'un bâtiment de type **Atelier**, libre ou réservé à lui. Les exigences de chaque artisan sont dans l'[aide-mémoire des ateliers](../personnages/ateliers.md).

??? question "Un artisan est « sans logis »."

    Son atelier a été supprimé. Rien n'est perdu : choisissez-lui un nouvel atelier conforme avec **Choisir son logis**.

??? question "Que veulent dire les signes au-dessus des personnages ?"

    Un **!** rouge : une nouveauté vous attend (quête à valider, récit à accepter…). Un **/!\\** jaune : l'artisan n'arrive pas à rejoindre son poste. Dégagez le passage.

??? question "Une légende installée ne commerce pas."

    Onze légendes dépendent d'un mod : Robinson Crusoé (Tough As Nails), le capitaine Achab (Tide), Jack Sparrow (Tax' Ocean Villager), Obélix (Wilder Nature **et** Farmer's Delight), Miyamoto Musashi (Epic Fight), Gambrinus (Let's Do Brewery), Geppetto (Handcrafted **et** Furniture), Ragnar (Small Ships), Jeanne d'Arc (Valarian Conquest), Harold (Dragon Mounts Remastered) et Hercule (Mowzie's Mobs). Si leur mod est absent du serveur, elles s'installent mais n'ouvrent ni boutique ni quêtes : elles l'expliquent dans un dialogue, suivi d'une ligne grise qui nomme le mod. Voir [Mods et plugins](../serveur/mods-et-plugins.md#les-mods-de-contenu).

??? question "Je n'arrive pas à remettre les objets d'un récit « Rapporter… »."

    Ouvrez les récits **depuis le menu du personnage lui-même**, pas depuis le journal de quêtes, et cliquez sur le récit en cours quand vous avez tous les objets sur vous. Les objets achetés à un PNJ ou pris dans une réserve sont refusés.

## Les quêtes

??? question "Ma quête ne progresse pas."

    - **Fermez votre inventaire** : c'est à ce moment que la progression se met à jour.
    - Les **objets achetés à un artisan** ne comptent pas pour ses quêtes.
    - Pour la chasse, seules les créatures que **vous** abattez comptent.
    - Si l'artisan est « sans logis », ses quêtes sont en pause.

??? question "Pourquoi je ne peux pas passer au chapitre suivant ?"

    Il reste des quêtes obligatoires (bouton **QUÊTES À FINIR**), ou la caisse ne couvre pas le prix de la charte (**CAISSE VIDE**). Les quêtes **★** sont facultatives et ne bloquent jamais.

??? question "Si on passe au chapitre suivant, perd-on les quêtes bonus ★ ?"

    Non. Une quête bonus non terminée reste proposée dans les chapitres suivants.

??? question "Les récits se refont-ils ?"

    Non : chaque récit ne se fait qu'**une fois par joueur**. Chaque joueur a bien ses propres récits.

??? question "Il n'y a plus assez d'emplacements pour la quête de territoire."

    Les chartes n'offrent pas tous les emplacements demandés : achetez la différence chez Alderic, **Trésor** → **Agrandir la ville** (payé par la caisse). Voir [Le territoire](../guide/territoire.md#obtenir-plus-demplacements).

## Le commerce

??? question "Pourquoi je ne peux pas revendre cet objet ?"

    Il a été acheté à un artisan, pris dans la réserve d'un entrepôt, ou fabriqué avec un tel objet : il est **marqué** et ne se revend pas. Il reste utilisable pour construire, fabriquer et livrer les chantiers de la ville.

??? question "L'artisan n'achète plus ma ressource."

    Son **entrepôt est plein**. Revenez plus tard (les artisans consomment leurs stocks), vendez autre chose, ou améliorez son atelier pour agrandir son entrepôt.

??? question "Le prix a baissé depuis ce matin."

    L'entrepôt de l'artisan se remplit, avec vos ventes et celles des autres joueurs. Au-delà de 40 % de remplissage, le prix baisse. Les quêtes, elles, paient toujours au prix plein.

??? question "Un article de la boutique est en rupture."

    Il manque un ingrédient dans les stocks. Survolez l'article pour savoir lequel, puis vendez-le à l'artisan concerné.

??? question "Comment récupérer des coins de la caisse ?"

    Ce n'est pas possible : une fois déposés, les coins appartiennent à la ville.

## La ville et les bâtiments

??? question "La commande /city claim est refusée. Comment revendiquer une parcelle ?"

    Les parcelles passent par **Alderic**. Demandez-lui de vous suivre jusqu'à la limite de la ville, placez-vous sur le chunk voulu, parlez-lui, puis **clic gauche** sur la barre **Parcelles** de son menu. Voir [Le territoire](../guide/territoire.md#revendiquer-une-parcelle).

??? question "Comment déposer des coins dans la caisse ?"

    Chez Alderic : **Trésor** → **Déposer des coins**, puis tapez le montant dans le chat. La commande `/city deposit` est réservée à l'équipe du serveur.

??? question "Puis-je perdre mes constructions pendant un siège ?"

    Non. Aucun bloc n'est jamais endommagé dans la ville : ni explosion, ni incendie, ni porte enfoncée.

??? question "Un joueur a supprimé mon bâtiment !"

    Tout joueur peut supprimer un bâtiment. Rassurez-vous, **les blocs restent en place** : il suffit de le redéclarer chez Alderic (**Bâtiments** → **Ajouter un bâtiment**). Concertez-vous avant de réorganiser la ville.

??? question "Un habitant est parti."

    Son lit a été cassé, ou sa maison a été supprimée ou a changé de type. Un habitant mécontent, lui, ne part jamais.

??? question "La satisfaction des habitants est basse. Est-ce grave ?"

    Non : c'est un bonus. Basse, elle ralentit un peu les arrivées et réduit l'impôt ; haute, elle les accélère et l'augmente. Cliquez sur le portrait d'Alderic pour voir quel besoin manque. Voir [Les habitants](../guide/habitants.md#besoins-et-satisfaction).

??? question "Mon bâtiment n'atteint pas 60 % de toit."

    Délimitez la zone au plus près des murs : une cour ou un jardin inclus comptent comme sol à ciel ouvert. Le feuillage ne compte pas comme toit.

## Les sièges

??? question "Quand ont lieu les sièges ?"

    Par défaut **tous les jours à 22 h** (heure de Paris), à partir du chapitre IV, s'il y a au moins **2 joueurs connectés**. `/city event`, ou Alderic → Événements → Sièges, donne le prochain rendez-vous.

??? question "Puis-je mourir en ville pendant un siège ?"

    Oui : pendant un siège, les assaillants peuvent vous blesser, même en ville. Le reste du temps, vous y êtes invulnérable.

??? question "Qui reçoit la récompense d'un siège ?"

    La **caisse de la ville** : 150 coins + 50 par chapitre (350 coins au chapitre IV). Le capitaine de la garde gagne aussi de l'expérience.

## Les raids

??? question "Comment partir en raid ?"

    Parlez à Alderic : **Événements** → **Raids**, choisissez la difficulté puis la cible, et sonnez le rassemblement. Les joueurs réunis autour d'Alderic partent ensemble. Les raids s'ouvrent au chapitre II. Tout est expliqué dans [Les raids](../guide/raids.md).

??? question "Comment quitter un raid en cours ?"

    Parlez au héraut du camp, ou tapez `/city raid quitter` : vous rentrez à Valmont et l'expédition continue sans vous.

## Spoilers

??? question "Où voir toute l'histoire d'un coup ?"

    Dans l'onglet de progression (touche ++l++) : l'arbre est entièrement visible dès le départ. Si vous voulez garder la surprise, n'y survolez pas les étapes lointaines ! Dans ce guide, tout ce qui dévoile l'histoire est replié dans des blocs violets.
