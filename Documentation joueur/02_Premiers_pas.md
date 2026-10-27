# Premiers pas

## 1. Rejoindre le serveur

| | |
|---|---|
| **Version de Minecraft** | 1.21.1 |
| **Type de serveur** | Serveur moddé (mods + plugins) |
| **Adresse** | 🛠️ À COMPLÉTER |
| **Modpack à installer** | 🛠️ À COMPLÉTER : lien et méthode d'installation (launcher, CurseForge, Modrinth…) |

<!-- 🛠️ À COMPLÉTER : préciser le chargeur (NeoForge 1.21.1), la liste des mods requis côté client (dont Dragon Mounts Remastered et Tax' Ocean Villager), et les mods facultatifs conseillés (ex. WorldEditCUI pour voir les contours des bâtiments). -->

### Le pack de ressources

À votre arrivée, le serveur vous propose un **pack de ressources** : *« Menus illustrés des habitants de Valmont (aucun bloc modifié) »*.

- **Acceptez-le** pour profiter des **menus illustrés en pixel art**, des portraits des personnages et des panneaux d'information à l'écran.
- Si vous le refusez, vous pouvez quand même jouer : les mêmes fonctions passent par des menus « classiques » (fenêtres de coffre).
- Le pack **ne modifie aucun bloc ni aucun objet** : seuls les menus des personnages changent.
- Vous pouvez changer d'avis à tout moment : `/city ui valmont` (menus illustrés) ou `/city ui classique`.

## 2. Rencontrer Alderic

**Alderic**, le maire, se tient au cœur de Valmont. **Faites un clic droit sur lui** : il se présente et vous raconte la Nuit Noire. C'est votre point d'entrée pour presque tout :

| Bouton | À quoi il sert |
|---|---|
| **📜 Quêtes de la cité** | Les objectifs du chapitre en cours, le récit d'Alderic et la signature de la charte |
| **🏗 Bâtiments** | La liste des bâtiments de la ville ; en ajouter, en supprimer, en changer le type |
| **💰 Trésor** | La caisse de la ville et votre bourse ; déposer des coins |
| **🗺 Agrandir la ville** | Acheter une parcelle supplémentaire (payée par la caisse) |

<!-- 🖼️ Image suggérée : écran d'accueil d'Alderic -->

> **Si Valmont n'existe pas encore**, la ville est fondée une seule fois pour tout le serveur avec `/city create` : le chunk où se tient le fondateur devient le cœur de la ville et Alderic apparaît devant lui. Le premier joueur qui lui parle reçoit pour la ville un **cadeau de bienvenue** : 10 parcelles offertes et 100 coins dans la caisse.

## 3. Comprendre votre écran

- **Touche Tab** : au-dessus de la liste des joueurs s'affichent deux panneaux.
  - **À gauche, la cité** : palier et niveau, habitants, trésor, parcelles.
  - **À droite, vous** : niveau, expérience, bourse et métier.
- **Panneau « Quêtes »**, à gauche de l'écran : vos quêtes en cours et leur avancement. `/city quests` permet de choisir ce qu'il affiche et où.
- **Touche L** (menu Progrès de Minecraft), onglet **« La Renaissance de Valmont »** : la progression de toute la ville.
- **Les dialogues** des personnages s'écrivent lettre par lettre **au-dessus de votre barre d'objets**, pas dans le chat.
- En entrant dans la ville, vous lisez **« 🏰 Territoire de Valmont »** au-dessus de la barre d'objets.

## 4. Vos premières heures : par où commencer ?

1. **Parlez à Alderic** et ouvrez **📜 Quêtes de la cité** pour voir ce que la ville attend.
2. **Lancez la recherche du premier survivant** depuis ce menu : vous recevez une **piste** et une **barre** en haut de l'écran qui vous guide vers lui (voir [Les personnages](04_Les_personnages.md)).
3. **Agrandissez la ville** en revendiquant des parcelles voisines avec `/city claim`.
4. **Construisez et déclarez des bâtiments** : une maison pour accueillir des habitants, un atelier pour chaque artisan (voir [La ville et ses bâtiments](05_La_ville_et_les_batiments.md)).
5. **Commercez** avec les artisans installés : vendez-leur vos ressources, faites leurs quêtes, gagnez des coins.
6. **Alimentez la caisse** (`/city deposit <montant>`) : c'est elle qui paie la charte pour passer au chapitre suivant.

## 5. Les règles d'or de Valmont

- **Tout est commun.** La caisse, les stocks des artisans, leurs rangs et l'avancement des chapitres sont partagés. Coordonnez-vous avec les autres joueurs.
- **En ville, vous ne craignez rien** : pas de dégâts, pas d'explosion, pas d'incendie, pas de bloc abîmé par les monstres. **Seule exception : les sièges.**
- **Un objet acheté à un artisan est « marqué »** : il sert à construire, à fabriquer et à livrer les chantiers de la ville, mais ne se revend pas.
- **Les menus se lisent au survol** : passez la souris sur un bouton ou un objet pour afficher sa bulle d'aide (prix, exigences, progression).
- **Pour annuler une saisie dans le chat** (nom d'un bâtiment, montant à déposer…), tapez `annuler`.
