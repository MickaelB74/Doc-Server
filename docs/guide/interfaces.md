---
title: Les interfaces
description: Les menus illustrés et classiques de Valmont, le code couleur des écrans, le panneau de la touche Tab, le panneau Quêtes, le journal de quêtes, la carte des personnages, les dialogues et les notifications.
---

# Les interfaces

Les menus des personnages existent en deux styles, qui donnent accès **aux mêmes actions**, à quelques exceptions près (voir [Avec les menus classiques](#8-avec-les-menus-classiques)). Cette page vous apprend à les lire, ainsi que les panneaux affichés à l'écran.
{ .chapeau }

## 1. Menus illustrés ou classiques

| Style | Comment l'obtenir |
|---|---|
| **Illustré « Valmont »** : écrans en pixel art, portraits, panneaux à l'écran | Accepter le pack de ressources à la connexion, ou `/city ui valmont` |
| **Classique** : fenêtres de coffre avec des objets | Refuser le pack, ou `/city ui classique` |

`/city ui` bascule d'un style à l'autre. Les coffres, fours, villageois et autres menus de Minecraft ne changent jamais.

## 2. Lire un écran illustré

<div class="vm-fiche" markdown>

![L'accueil d'un artisan : nom et métier en haut, rang en étoiles, portrait, boutons Vendre, Entrepôt, Boutique et Quêtes, barre d'expérience en bas](../assets/ecrans/artisan.png){ .vm-fiche__decor }

<div class="vm-fiche__infos" markdown>

<p class="vm-fiche__titre">Les repères communs</p>

| | |
|---|---|
| En haut | Le nom du personnage et son métier |
| En-tête | ![](../assets/ui/icones/ic_back.png){ .vm-icone } retour, le ruban qui nomme l'écran, ![](../assets/ui/icones/ic_info.png){ .vm-icone } aide et légende, ![](../assets/ui/icones/ic_close.png){ .vm-icone } fermer |
| Au milieu | Portrait et grands boutons, ou une grille de cases |
| En bas | Une barre de progression ou un pied de page, et ![](../assets/ui/icones/ic_prev.png){ .vm-icone } ![](../assets/ui/icones/ic_next.png){ .vm-icone } pour changer de page |

</div>

</div>

**Survolez tout** : les bulles contiennent les détails (prix, exigences, progression). Dans ces écrans, rien ne peut être pris ni déposé : chaque clic déclenche seulement l'action du bouton. Votre inventaire reste visible en bas, c'est normal.

### Le code couleur

| Cadre | Sens général |
|---|---|
| ![](../assets/ui/anneaux/ring_green.png){ .vm-anneau } Vert | Disponible, conforme, accompli, à jour |
| ![](../assets/ui/anneaux/ring_amber.png){ .vm-anneau } Ambre | En cours, prix réduit, stock entamé |
| ![](../assets/ui/anneaux/ring_red.png){ .vm-anneau } Rouge | Bloqué, incomplet, plein, en rupture |
| ![](../assets/ui/anneaux/ring_gold.png){ .vm-anneau } Doré | Réservé, choix actuel, à accepter |
| ![](../assets/ui/anneaux/ring_gray.png){ .vm-anneau } Gris | Masqué, indisponible |
| ![](../assets/ui/anneaux/ring_purple.png){ .vm-anneau } Violet | Quête bonus, garde |
| ![](../assets/ui/icones/lock.png){ .vm-anneau } Cadenas | Verrouillé (rang ou personnage pas encore atteint) |

Le sens exact est rappelé dans la bulle ![](../assets/ui/icones/ic_info.png){ .vm-icone } de chaque écran.

### Les écrans de commerce

| Écran | Cadres de couleur |
|---|---|
| ![Vendre](../assets/ui/rubans/rib_vendre.png){ .vm-ui } | Vert : prix plein · Ambre : prix réduit · Rouge : entrepôt plein · Gris : vous n'en avez pas assez |
| ![Entrepôt](../assets/ui/rubans/rib_entrepot.png){ .vm-ui } | Vert : disponible · Ambre : stock entamé · Rouge : vide |
| ![Boutique](../assets/ui/rubans/rib_boutique.png){ .vm-ui } | Vert : disponible · Rouge : en rupture (ingrédients manquants) · Cadenas : rang insuffisant |

### L'écran des quêtes d'un artisan

Deux cartes : **Principale** (à gauche) et **Spéciale** (à droite), avec la récompense ou le temps de repos, les objectifs et leur progression, et un bouton d'action :

| Bouton | Signification |
|---|---|
| ![Accepter](../assets/ui/boutons/qb_accepter.png){ .vm-ui } | Une quête vous est proposée |
| ![En cours](../assets/ui/boutons/qb_encours.png){ .vm-ui } | Réunissez ce qui est demandé |
| ![Valider](../assets/ui/boutons/qb_valider.png){ .vm-ui } | Tout est prêt : cliquez pour toucher la récompense |
| ![En repos](../assets/ui/boutons/qb_repos.png){ .vm-ui } | L'artisan prépare sa prochaine quête |

Au centre, le bouton vertical ![Récits](../assets/ui/onglets/vb_recits.png){ .vm-ui .vm-ui--grand } ouvre les récits du personnage. Un personnage qui en a plus de cinq (Gambrinus, ainsi que Robin des Bois et Indiana Jones avec leurs mods facultatifs) les affiche quatre par page, avec des flèches pour passer d'une page à l'autre. C'est aussi depuis cet écran, ouvert dans le menu du personnage, que se remettent les objets des récits « Rapporter… ».

<div class="grid" markdown>

<figure markdown>
  ![L'écran des quêtes d'un artisan, avec ses deux cartes et le bouton Récits](../assets/ecrans/quetes_pnj.png){ width="280" loading="lazy" }
  <figcaption>Les quêtes d'un artisan — illustration</figcaption>
</figure>

<figure markdown>
  ![L'écran des récits d'un personnage : cinq récits, un par rang, avec leur état](../assets/ecrans/recits.png){ width="280" loading="lazy" }
  <figcaption>Les récits d'un personnage — illustration</figcaption>
</figure>

</div>

## 3. Le panneau de la touche Tab

En maintenant ++tab++, deux panneaux s'affichent au-dessus de la liste des joueurs, de part et d'autre de la plaque **MyCivilisation** :

| Panneau | Contenu |
|---|---|
| **La cité** (à gauche) | Nom, palier et niveau, **habitants** (vivants / places), **satisfaction** des habitants (barre et pourcentage), **trésor** (caisse), **parcelles** (revendiquées / emplacements) |
| **Vous** (à droite) | Pseudo, **niveau**, **XP**, **bourse**, **métier** |

<figure markdown>
  ![Écran entier en 1080p avec les panneaux de la touche Tab et le panneau Quêtes](../assets/ecrans/ecran_tab_1080p.png){ loading="lazy" }
  <figcaption>Les panneaux à l'écran en 1080p — illustration, données d'exemple</figcaption>
</figure>

## 4. Le panneau « Quêtes »

Un panneau titré **Quêtes** reste affiché à gauche de l'écran :

- une ligne par personnage chez qui vous avez une quête en cours, puis chaque objectif avec son compteur et une fine barre ;
- texte **violet** pour une quête spéciale, **vert** quand l'objectif est atteint ;
- **« ★ Voir … ! »** quand une quête est prête à être validée.

### Le régler : `/city quests`

Le **journal de quêtes**, onglet ![Suivi](../assets/ui/onglets/tab_suivi_on.png){ .vm-ui }, permet de :

- choisir **les personnages suivis** (cadre vert = affiché, gris = masqué) ;
- choisir **la position du panneau** selon votre écran ;
- choisir **l'affichage du suivi** (clic gauche : suivant, clic droit : précédent), ou tout **suivre** d'un clic (![Tous](../assets/ui/onglets/track_all.png){ .vm-ui }).

| Affichage | Où se trouve le suivi |
|---|---|
| **Visible** (par défaut) | Le panneau à gauche de l'écran (sans le pack : le tableau à droite) |
| **Accroché** | Avec la liste des joueurs : il n'apparaît qu'en maintenant ++tab++ |
| **Masqué** | Nulle part |

`/city quests toggle` fait défiler ces trois affichages ; `/city quests toggle visible` (ou `accroche`, `masque`) en choisit un directement.

| Position | Pour quels écrans |
|---|---|
| ![Bord](../assets/ui/positions/pos_bord.png){ .vm-ui } (par défaut) | 1080p avec l'interface à l'échelle 4 |
| ![Marge](../assets/ui/positions/pos_gauche.png){ .vm-ui } | 1440p, 720p ou 1366 × 768 |
| ![Près](../assets/ui/positions/pos_pres.png){ .vm-ui } (contre l'inventaire) | Écrans 16:10 ou interface agrandie |

Vos réglages sont conservés d'une connexion à l'autre.

### L'onglet « Récits » : `/city quests recits`

Tous les personnages et l'état de leurs récits, dans l'ordre de l'histoire :

| Repère | Signification |
|---|---|
| ![](../assets/ui/anneaux/ring_gold.png){ .vm-anneau } Doré | Au moins un récit à accepter |
| ![](../assets/ui/anneaux/ring_amber.png){ .vm-anneau } Ambre | Un récit en cours |
| ![](../assets/ui/anneaux/ring_green.png){ .vm-anneau } Vert | À jour |
| ![](../assets/ui/anneaux/ring_gray.png){ .vm-anneau } Gris | En ville, mais pas encore installé |
| ![](../assets/ui/icones/lock.png){ .vm-anneau } Cadenas | Pas encore à Valmont |

Un clic sur un personnage installé ouvre ses récits. En bas, un compteur affiche tous les récits accomplis.

<div class="grid" markdown>

<figure markdown>
  ![Le journal de quêtes, onglet Suivi : personnages suivis et position du panneau](../assets/ecrans/quetes_suivies.png){ width="280" loading="lazy" }
  <figcaption>Le journal, onglet « Suivi » — illustration</figcaption>
</figure>

<figure markdown>
  ![Le journal de quêtes, onglet Récits : tous les personnages et l'état de leurs récits](../assets/ecrans/journal_recits.png){ width="280" loading="lazy" }
  <figcaption>Le journal, onglet « Récits » — illustration</figcaption>
</figure>

</div>

## 5. Où sont-ils ? `/city locate`

Une carte vue du ciel, dessinée par le plugin : à gauche, les personnages de Valmont (cadenas tant que personne ne les a rencontrés) ; à droite, la carte, avec les limites de la ville en or, les personnages en rouge, celui que vous avez choisi en jaune et vous en blanc.

- Un clic sur un personnage centre la carte sur lui et affiche ses coordonnées. Un personnage rencontré mais pas encore venu en ville y figure aussi.
- **Clic gauche** sur la carte : zoom avant. **Clic droit** : zoom arrière. Le bouton carte de l'en-tête revient à la vue d'ensemble de Valmont.
- Sans le pack, les mêmes informations s'affichent dans le chat.

## 6. Les dialogues

Les personnages parlent **au-dessus de votre barre d'objets**, lettre par lettre, jamais dans le chat. Les longues répliques s'affichent en plusieurs morceaux. Un seul dialogue se joue à la fois.

!!! dialogue "Un personnage vous parle"

    C'est ainsi que les répliques des personnages sont présentées dans ce guide.

Pour réentendre un personnage : ![Son histoire](../assets/ui/boutons/btn_histoire.png){ .vm-ui }. Pour réentendre Alderic : ![Récit](../assets/ui/boutons/fb_recit.png){ .vm-ui }

## 7. Les notifications

| Événement | Ce que vous voyez |
|---|---|
| Entrée / sortie de la ville | « 🏰 Territoire de Valmont » / « 🌲 Quitter le territoire de la ville » |
| Entrée dans un bâtiment | Son nom, son type et ses étoiles |
| Bâtiment conforme ou qui gagne un niveau | Un titre et un son |
| Nouveau palier pour la ville | Grand titre, fanfare, puis le récit d'Alderic |
| Un artisan monte de rang | « 🎉 … est passé Apprenti ! De nouveaux articles sont disponibles. » |
| Quête remplie | « ✅ Quête remplie ! » avec un petit son |
| Étape de progression accomplie | La notification de progrès de Minecraft (touche ++l++) |
| Siège | Titre « ⚔ Siège ! », barre rouge en haut de l'écran, puis « Victoire ! » ou « Siège perdu » |
| ![](../assets/ui/badges/badge_new.png){ .vm-icone } **!** rouge au-dessus d'un personnage | Une nouveauté vous attend auprès de lui (quête à valider, récit à accepter…) |
| **/!\\** jaune au-dessus d'un artisan | Il ne parvient pas à rejoindre son poste : dégagez le passage |

## 8. Avec les menus classiques

Sans le pack, presque tout reste accessible :

- les menus s'ouvrent dans des fenêtres de coffre ;
- le choix du type d'un bâtiment se fait avec des boutons cliquables dans le chat ;
- le suivi des quêtes est un tableau **« Quêtes actives »** à droite de l'écran ;
- le panneau ++tab++ s'affiche en texte ;
- chez Alderic, le bouton « 🗺 Agrandir la ville » reste sur l'accueil, et le bilan de la population s'affiche dans le chat ;
- Roland n'a pas d'écran de la garde : formez et renvoyez les gardes avec `/city garde former` et `/city garde renvoyer` (voir [La garde](garde.md)) ;
- l'embauche des employés et la création d'une annexe de travail ne sont pas proposées : passez aux menus illustrés (`/city ui valmont`) pour cela.
