# La ville et ses bâtiments

## Partie 1 : le territoire

### Parcelles et emplacements

Le territoire de Valmont se compte en **parcelles** (des chunks de 16 × 16 blocs). Deux chiffres sont à suivre, affichés sous la forme `7/13` dans le panneau **Tab**, chez Alderic et avec `/city info` :

| Notion | Signification |
|---|---|
| **Parcelles revendiquées** (à gauche) | Les chunks qui font réellement partie de la ville |
| **Emplacements** (à droite) | Le nombre maximal de parcelles que la ville peut revendiquer |

### Revendiquer une parcelle : `/city claim`

Placez-vous dans le chunk voulu et tapez `/city claim`. Il faut que :

- le chunk **touche la ville par un côté** (un coin ne suffit pas) ;
- la ville ait **au moins un emplacement libre**.

`/city unclaim` rend le chunk où vous vous tenez : l'emplacement redevient libre. Les protections de la ville ne s'y appliquent plus. On ne peut pas retirer le dernier chunk.

### Obtenir plus d'emplacements

- **En signant les chartes** : chaque nouveau palier offre des emplacements (voir [La trame principale](03_La_trame_principale.md)).
- **En les achetant chez Alderic** : bouton **🗺 Agrandir la ville** (+1 emplacement), **payé par la caisse de la ville**.

| Emplacement acheté n° | Prix |
|---|---|
| 1 | 150 coins |
| 5 | 204 coins |
| 10 | 300 coins |
| 20 | 647 coins |
| 30 | 1 398 coins |
| 38 et suivants | 2 500 coins (plafond) |

Chaque emplacement acheté coûte **8 % de plus** que le précédent, sans jamais dépasser 2 500 coins. Les emplacements offerts ne font pas monter le prix.

### Voir les limites

- `/city map` affiche le **contour de la ville** en colonnes de particules dorées pendant 5 secondes.
- En franchissant la limite, vous lisez **« 🏰 Territoire de Valmont »** ou **« 🌲 Quitter le territoire de la ville »** au-dessus de la barre d'objets.

### La caisse de la ville

La caisse est **commune à tous les joueurs** et distincte de votre bourse.

| Elle reçoit | Elle paie |
|---|---|
| Vos dépôts (`/city deposit <montant>`, ou Alderic → 💰 Trésor → Déposer) | Les chartes |
| L'impôt des habitants, chaque matin | Les emplacements achetés |
| Les récompenses des sièges victorieux | Les réquisitions pour les chantiers |

Une fois déposés, les coins appartiennent à la ville : ils ne se reprennent pas.

### Ce qui est protégé en ville

Sur toutes les parcelles de Valmont, du fond jusqu'au ciel :

- **Vous êtes invulnérable** : monstres, chute, lave, noyade, feu… Seule exception : **pendant un siège**, les assaillants peuvent vous blesser.
- **Aucune explosion** : creepers, TNT, boules de feu, Wither… n'abîment rien.
- **Aucun incendie** : seul un joueur peut allumer un feu, et il ne se propage pas.
- **Les monstres ne touchent pas aux blocs** : pas d'enderman qui vole des blocs, pas de porte enfoncée par les zombies.
- **Cultures et œufs de tortue** ne sont jamais piétinés.
- **Tableaux, cadres et porte-armures** ne sont abîmés que par un joueur.
- Les **habitants** et les **gardes** ne peuvent pas être blessés par les joueurs.

> ⚠️ Ces protections visent les monstres et les catastrophes, **pas les joueurs** : rien n'empêche un joueur de casser un bloc ou d'ouvrir un coffre. Valmont est une ville coopérative, respectez le travail des autres.

---

## Partie 2 : les bâtiments

Une construction ne devient un **bâtiment** qu'une fois **déclarée** : vous lui donnez un type, un nom et une zone. La ville l'**inspecte** alors en permanence et lui attribue un **niveau de 0 à 5**.

### Les quatre types

| Type | Usage | Exigences propres |
|---|---|---|
| **Habitation** | Maison des habitants : **1 lit = 1 place** | Au moins 1 lit |
| **Atelier** | Logis et commerce d'**un** artisan | Celles de l'artisan (un atelier « libre » n'a que les exigences communes) |
| **Mairie** | Siège de la Charte. **Une seule par ville** | 1 pupitre et 1 bannière |
| **Divers** | Entrepôt, place, rempart, décor… | Aucune |

Un atelier peut être **réservé** à un artisan déjà rencontré, ou laissé **libre** : le premier artisan qui s'y installe le réserve. Tous les types comptent pour les quêtes de la cité qui demandent un nombre de bâtiments.

### Créer un bâtiment, pas à pas

1. **Lancez la création** : `/city build new`, ou Alderic → 🏗 Bâtiments → **AJOUTER**.
2. **Choisissez le type** (et, pour un atelier, l'artisan ou « Atelier libre »). La bulle de chaque choix affiche ses prérequis.
3. **Donnez un nom dans le chat** : un seul mot, 24 caractères au plus, unique. Un nom vous est proposé : cliquez dessus pour le reprendre. Tapez `annuler` pour abandonner.
4. **Délimitez la zone avec le bâton « 🏗 Sélection »** que vous recevez :
   - **clic gauche** sur un bloc du sol : premier coin (colonne de flammes) ;
   - **clic droit** sur le coin opposé : second coin (colonne d'étincelles).

   La zone est un rectangle entièrement dans la ville, qui ne doit pas chevaucher un autre bâtiment. Cliquez **au niveau du sol du rez-de-chaussée** : c'est à partir de là que le toit est mesuré.
5. **Placez le poste de l'artisan** avec le bâton de Blaze « 📍 Point NPC » : **clic gauche** sur le sol, à l'intérieur de la zone, là où l'artisan se tiendra. Pour une habitation, une mairie ou un bâtiment divers, tapez plutôt `/city build skip` **en gardant l'outil en main**.
6. **C'est fait !** Une première inspection vous dit ce qu'il manque.

La hauteur est gérée automatiquement : tout ce qui est construit de **40 blocs sous le sol à 100 blocs au-dessus** compte. Caves et tours comprises.

### L'inspection et les niveaux

L'inspection est automatique : elle se refait une demi-seconde après chaque modification dans la zone.

**Les exigences communes** (habitations, ateliers, mairie) :

| Exigence | Ce qui compte |
|---|---|
| **Une porte** | Une vraie porte (bois, fer, cuivre). Les trappes et portillons ne comptent pas |
| **Un toit** couvrant **60 %** du sol | Tout bloc plein au-dessus du sol. Le feuillage ne compte pas |
| **Deux sources de lumière** | Torches, lanternes, pierre lumineuse, lanternes aquatiques, champilampes, bougies, feux de camp… (même éteints) |

**Les niveaux :**

| Niveau | Condition |
|---|---|
| 0 — Incomplet | Une exigence manque |
| 1 ★ — Conforme | Toutes les exigences sont remplies |
| 2 ★★ | Conforme + 15 points |
| 3 ★★★ | Conforme + 30 points |
| 4 ★★★★ | Conforme + 50 points |
| 5 ★★★★★ | Conforme + 75 points |

**Les points de détail :**

| Catégorie | Barème | Maximum |
|---|---|---|
| **Variété** | +1 par type de bloc de construction différent | 30 |
| **Décor** | +1 par décoration (4 identiques au plus) | 40 |
| **Bonus du métier** | +5 par bloc bonus présent | 15 |
| **Surface couverte** | +1 par tranche de 10 blocs de sol sous un toit | 15 |

- **Ne comptent pas pour la variété** : les blocs naturels (terre, herbe, roche naturelle, sable, gravier, neige, glace, feuillages, plantes, minerais, eau…).
- **Décorations reconnues** : pots de fleurs, tapis, bannières, bougies, panneaux, trappes, lanternes, chaînes, bibliothèques, poteries décorées, cloches, tableaux, cadres et porte-armures.
- **Bonus** : l'habitation en a trois (coffre, établi, four), la mairie deux (cloche, bibliothèque), et chaque atelier a les siens, liés au métier de son artisan.

### Ce que vous verrez

- Le bâtiment devient conforme ou gagne un niveau : un **titre** s'affiche avec un son, pour le joueur qui a fait le changement (« Forge est conforme », « Niveau 3 ★★★ »).
- Il perd un niveau ou devient incomplet : un avertissement s'affiche au-dessus de la barre d'objets.
- En entrant dans un bâtiment : son nom, son type et ses étoiles s'affichent au-dessus de la barre d'objets.
- **Le détail complet** : `/city build inspect` (dans le bâtiment) ou `/city build inspect <nom>`.

### À quoi sert le niveau ?

- Une **habitation** doit être **conforme** (niveau 1 ou plus) pour accueillir des habitants.
- Pour un **atelier**, chaque niveau au-delà du premier agrandit **l'entrepôt de l'artisan de 25 %**. Au niveau 5, l'entrepôt est doublé.

### Gérer les bâtiments

- **La liste** : Alderic → 🏗 Bâtiments, ou `/city build`. Un clic gauche affiche les **bordures** du bâtiment (particules bleues, 5 secondes, visibles par vous seul).
- **Changer le type** : clic droit sur le bâtiment dans la liste d'Alderic, ou `/city build type <nom> <type>`. Un bâtiment habité par un artisan reste son atelier.
- **Supprimer** : Alderic → 🏗 Bâtiments → **RETIRER**, ou `/city build remove <nom>`. **Les blocs restent en place**, seule la déclaration disparaît. Les habitants s'en vont et l'artisan devient « sans logis ».

> ⚠️ **Tout joueur peut supprimer n'importe quel bâtiment.** Concertez-vous avant de réorganiser la ville.

### Conseils de bâtisseur

1. **Délimitez au plus près des murs** : une cour ou un jardin inclus dans la zone font baisser le pourcentage de toit.
2. **Variez les matériaux** : pierre taillée, briques, planches de plusieurs essences, verre… Chaque bloc différent rapporte un point.
3. **Décorez sans répéter** : au-delà de 4 exemplaires d'une même décoration, les suivants ne rapportent plus rien. Alternez les couleurs.
4. **Posez un exemplaire de chaque bonus du métier** : +5 points chacun, c'est souvent l'écart entre deux niveaux.
5. **Pensez au sous-sol** : une cave sous le bâtiment est inspectée elle aussi.
6. **Vérifiez avant d'installer un artisan** : `/city build inspect <nom>` liste ce qui manque.
