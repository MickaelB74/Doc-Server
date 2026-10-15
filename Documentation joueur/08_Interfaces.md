# Les interfaces

## 1. Menus illustrés ou classiques

Les menus des personnages existent en deux styles, qui donnent accès **exactement aux mêmes actions** :

| Style | Comment l'obtenir |
|---|---|
| **Illustré « Valmont »** : écrans en pixel art, portraits, panneaux à l'écran | Accepter le pack de ressources à la connexion, ou `/city ui valmont` |
| **Classique** : fenêtres de coffre avec des objets | Refuser le pack, ou `/city ui classique` |

`/city ui` bascule d'un style à l'autre. Les coffres, fours, villageois et autres menus de Minecraft ne changent jamais.

## 2. Lire un écran illustré

<!-- 🖼️ Image suggérée : un écran illustré annoté -->

- **En haut** : le nom du personnage et son métier.
- **Ligne d'en-tête** : flèche **← retour**, ruban qui nomme l'écran, icône **ℹ** (aide et légende des couleurs) et croix rouge **✖** pour fermer.
- **Au milieu** : portrait et grands boutons, ou une grille de cases.
- **En bas** : une barre de progression ou un pied de page, et des flèches de pages si la liste est longue.
- **Survolez tout** : les bulles contiennent les détails (prix, exigences, progression).

Dans ces écrans, rien ne peut être pris ni déposé : chaque clic déclenche seulement l'action du bouton. Votre inventaire reste visible en bas, c'est normal.

### Le code couleur des anneaux

| Anneau | Sens général |
|---|---|
| 🟢 Vert | Disponible, conforme, accompli, à jour |
| 🟠 Ambre | En cours, prix réduit, stock entamé |
| 🔴 Rouge | Bloqué, incomplet, plein, en rupture |
| 🟡 Doré | Réservé, choix actuel, à accepter |
| ⚪ Gris | Masqué, indisponible |
| 🟣 Violet | Quête bonus, garde |
| 🔒 Cadenas | Verrouillé (rang ou personnage pas encore atteint) |

Le sens exact est rappelé dans la bulle **ℹ** de chaque écran.

### Les écrans de commerce

| Écran | Cadres de couleur |
|---|---|
| **Vendre** | Vert : prix plein · Ambre : prix réduit · Rouge : entrepôt plein · Gris : vous n'en avez pas assez |
| **Entrepôt** | Vert : disponible · Ambre : stock entamé · Rouge : vide |
| **Boutique** | Vert : disponible · Rouge : en rupture (ingrédients manquants) · Cadenas : rang insuffisant |

### L'écran des quêtes d'un artisan

Deux cartes : **Principale** (à gauche) et **Spéciale** (à droite), avec la récompense ou le temps de repos, les objectifs et leur progression, et un bouton d'action :

| Bouton | Signification |
|---|---|
| **ACCEPTER** | Une quête vous est proposée |
| **EN COURS** | Réunissez ce qui est demandé |
| **VALIDER** | Tout est prêt : cliquez pour toucher la récompense |
| **EN REPOS** | L'artisan prépare sa prochaine quête |

Au centre, le bouton vertical **RÉCITS** ouvre les récits du personnage.

## 3. Le panneau de la touche Tab

En maintenant **Tab**, deux panneaux s'affichent au-dessus de la liste des joueurs, de part et d'autre de la plaque **MyCivilisation** :

| Panneau | Contenu |
|---|---|
| **La cité** (à gauche) | Nom, palier et niveau, **habitants** (vivants / places), **trésor** (caisse), **parcelles** (revendiquées / emplacements) |
| **Vous** (à droite) | Pseudo, **niveau**, **XP**, **bourse**, **métier** |

## 4. Le panneau « Quêtes »

Un panneau titré **Quêtes** reste affiché à gauche de l'écran :

- une ligne par personnage chez qui vous avez une quête en cours, puis chaque objectif avec son compteur et une fine barre ;
- texte **violet** pour une quête spéciale, **vert** quand l'objectif est atteint ;
- **« ★ Voir … ! »** quand une quête est prête à être validée.

### Le régler : `/city quests`

Le **journal de quêtes**, onglet **SUIVI**, permet de :

- choisir **les personnages suivis** (anneau vert = affiché, gris = masqué) ;
- choisir **la position du panneau** selon votre écran ;
- **afficher ou masquer** tout le panneau (aussi avec `/city quests toggle`), ou tout **suivre** d'un clic (**TOUS**).

| Position | Pour quels écrans |
|---|---|
| **BORD** (par défaut) | 1080p avec l'interface à l'échelle 4 |
| **MARGE** | 1440p, 720p ou 1366 × 768 |
| **PRÈS** (contre l'inventaire) | Écrans 16:10 ou interface agrandie |

Vos réglages sont conservés d'une connexion à l'autre.

### L'onglet « RÉCITS » : `/city quests recits`

Tous les personnages et l'état de leurs récits, dans l'ordre de l'histoire :

| Repère | Signification |
|---|---|
| 🟡 Doré | Au moins un récit à accepter |
| 🟠 Ambre | Un récit en cours |
| 🟢 Vert | À jour |
| ⚪ Gris | En ville, mais pas encore installé |
| 🔒 Cadenas | Pas encore à Valmont |

Un clic sur un personnage installé ouvre ses récits. En bas, un compteur affiche tous les récits accomplis.

## 5. Les dialogues

Les personnages parlent **au-dessus de votre barre d'objets**, lettre par lettre, jamais dans le chat. Les longues répliques s'affichent en plusieurs morceaux. Un seul dialogue se joue à la fois.

Pour réentendre un personnage : **📖 Son histoire**. Pour réentendre Alderic : **📜 Récit d'Alderic**.

## 6. Les notifications

| Événement | Ce que vous voyez |
|---|---|
| Entrée / sortie de la ville | « 🏰 Territoire de Valmont » / « 🌲 Quitter le territoire de la ville » |
| Entrée dans un bâtiment | Son nom, son type et ses étoiles |
| Bâtiment conforme ou qui gagne un niveau | Un titre et un son |
| Nouveau palier pour la ville | Grand titre, fanfare, puis le récit d'Alderic |
| Un artisan monte de rang | « 🎉 … est passé Apprenti ! De nouveaux articles sont disponibles. » |
| Étape de progression accomplie | La notification de progrès de Minecraft (touche L) |
| Siège | Titre « ⚔ Siège ! », barre rouge en haut de l'écran, puis « Victoire ! » ou « Siège perdu » |
| **!** rouge au-dessus d'un personnage | Une nouveauté vous attend auprès de lui |
| **/!\\** jaune au-dessus d'un artisan | Il ne parvient pas à rejoindre son poste |

## 7. Avec les menus classiques

Sans le pack, tout reste accessible :

- les menus s'ouvrent dans des fenêtres de coffre ;
- le choix du type d'un bâtiment se fait avec des boutons cliquables dans le chat ;
- le suivi des quêtes est un tableau **« Quêtes actives »** à droite de l'écran ;
- le panneau Tab s'affiche en texte.
