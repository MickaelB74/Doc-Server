# Commandes

Toutes les commandes de la ville commencent par **`/city`**, ou par son raccourci **`/c`** : `/c claim` équivaut à `/city claim`.

- La touche **Tab** complète les commandes et les noms (bâtiments, habitants, personnages déjà rencontrés).
- Les accents sont facultatifs : `recits` ou `récits`, `siege` ou `siège`.
- `/city` seul affiche l'aide. Elle liste aussi quelques commandes réservées à l'équipe du serveur, qui vous seront refusées.

## La ville

| Commande | Effet |
|---|---|
| `/city info` | Niveau de la ville, caisse, parcelles revendiquées / emplacements, prix de la prochaine parcelle |
| `/city deposit <montant>` | Verse des coins de votre bourse dans la caisse de la ville |
| `/city progression` | Rappelle comment ouvrir l'onglet « La Renaissance de Valmont » (touche L). Alias : `progres`, `avancement`, `chroniques` |
| `/city create` | Fonde Valmont à l'endroit où vous êtes. **Une seule fois pour tout le serveur** |

## Les parcelles

| Commande | Où | Effet |
|---|---|---|
| `/city claim` | Dans un chunk qui touche la ville | Ajoute ce chunk à la ville (il faut un emplacement libre) |
| `/city unclaim` | Dans un chunk de la ville | Retire ce chunk de la ville, et l'emplacement redevient libre |
| `/city map` | Partout | Affiche le contour de la ville pendant 5 secondes |

Pour **acheter un emplacement** supplémentaire : Alderic → **🗺 Agrandir la ville**.

## Les bâtiments

| Commande | Effet |
|---|---|
| `/city build` | Liste des bâtiments ; un clic affiche les bordures d'un bâtiment |
| `/city build new` | Crée un bâtiment : type, puis nom, puis zone avec le bâton |
| `/city build new <type> [artisan\|libre] [nom]` | Raccourci de création. Types : `habitation`, `atelier`, `mairie`, `divers` |
| `/city build skip` | Pendant l'étape « Point NPC », crée le bâtiment sans poste d'artisan (gardez l'outil en main) |
| `/city build inspect [nom]` | Rapport d'inspection complet. Sans nom : le bâtiment où vous êtes |
| `/city build type <nom> <type> [artisan]` | Change le type d'un bâtiment, ou réserve un atelier à un artisan |
| `/city build assign <bâtiment> <artisan>` | Installe un artisan arrivé en ville dans un atelier conforme |
| `/city build remove <nom>` | Supprime la déclaration d'un bâtiment (les blocs restent). **Définitif** |
| `/city build show` | Affiche ou masque les contours de tous les bâtiments (nécessite un mod client d'affichage des sélections WorldEdit) |

L'**artisan** s'écrit par son prénom, sans accent. Seuls les personnages déjà rencontrés sont acceptés et proposés par la touche Tab.

Les **noms de bâtiments** font un seul mot : les espaces deviennent `_` (exemple : `Maison_du_port`).

<details>
<summary>Avancé : régler la hauteur inspectée</summary>

| Commande | Effet |
|---|---|
| `/city build hauteur <nom> auto` | Revient à la règle normale (40 blocs sous le sol, 100 au-dessus) |
| `/city build hauteur <nom> <sol>` | Définit un nouveau niveau de sol (Y) pour le bâtiment |
| `/city build hauteur <nom> <bas> <haut>` | Fixe à la main la tranche verticale inspectée |

</details>

## Les quêtes

| Commande | Effet |
|---|---|
| `/city quests` | Ouvre le journal de quêtes, onglet **Suivi** (personnages suivis, position du panneau) |
| `/city quests toggle` | Masque ou réaffiche le panneau des quêtes |
| `/city quests recits` | Ouvre directement l'onglet **Récits** |

## L'interface

| Commande | Effet |
|---|---|
| `/city ui` | Bascule entre menus illustrés et menus classiques. Alias : `interface`, `menus` |
| `/city ui valmont` | Menus illustrés (le pack de ressources est reproposé si besoin) |
| `/city ui classique` | Menus classiques (le pack n'est plus proposé à la connexion) |

## Les habitants et la garde

| Commande | Effet |
|---|---|
| `/city habitants` | Bilan de la population : maisons, occupants, lits en deuil, prochaine arrivée. Alias : `population` |
| `/city garde` | Bilan de la garde : gardes, recrues en formation, rôles disponibles. Alias : `guard` |
| `/city garde former <habitant> <rôle>` | Envoie un habitant en formation. Rôles : `soldat`, `archer`, `sergent` |
| `/city garde renvoyer <nom>` | Rend un garde ou une recrue à la vie civile |

## Les événements et les sièges

| Commande | Effet |
|---|---|
| `/city event` | Calendrier des sièges et compte à rebours jusqu'au prochain. Alias : `evenements` |
| `/city siege` | État du siège en cours (vague, direction, temps restant, pertes) |

## Ce qui se fait sans commande

| Action | Comment |
|---|---|
| Acheter une parcelle | Alderic → 🗺 Agrandir la ville |
| Signer la charte | Alderic → 📜 Quêtes de la cité → bouton de la charte |
| Lancer la recherche d'un personnage | Alderic → 📜 Quêtes de la cité → clic sur la quête de recrutement |
| Livrer un chantier | Alderic → 📜 Quêtes de la cité → clic gauche (livrer) ou Maj + clic droit (réquisitionner) |
| Recruter un personnage | Clic droit sur lui → 👣 Suivez-moi, puis 🏠 Choisir son logis en ville |
| Commercer, faire une quête | Clic droit sur un artisan installé |
| Devenir employé d'un artisan | Icône métier dans son écran d'accueil |
| Former un garde | Capitaine de la garde → portrait → 🛡 Actions → La garde |
| Voir la progression de la ville | Touche **L**, onglet « La Renaissance de Valmont » |
| Annuler une saisie dans le chat | Tapez `annuler` |
