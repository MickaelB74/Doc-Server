# Habitants, garde et sièges

Valmont n'est pas qu'une ville d'artisans. Des **habitants** viennent s'installer dans vos maisons, certains deviennent **gardes**, et la ville doit régulièrement repousser des **sièges**.

> 🆕 **Fonctionnalités récentes.** Les habitants, la garde et les sièges viennent d'arriver sur le serveur : certains comportements peuvent encore évoluer. Signalez tout comportement étrange à l'équipe.

## 1. Les habitants

### Leur offrir un toit

**Chaque lit d'une habitation conforme accueille un habitant.** Une maison avec trois lits offre trois places. Pour être conforme, une habitation doit être déclarée comme **Habitation** et contenir au moins un lit, une porte, deux sources de lumière et un toit sur 60 % du sol (voir [La ville et ses bâtiments](05_La_ville_et_les_batiments.md)).

### Leur vie

- **Un nouvel habitant arrive au plus toutes les 5 minutes**, s'il reste un lit libre et qu'au moins un joueur est connecté. Il arrive à pied depuis la lisière de la ville jusqu'à sa maison. Le chat l'annonce : *« 🏠 Jehan s'installe à Valmont (Maison, lit 2/3) »*.
- Chacun porte un **prénom médiéval** (Margot, Guillemette, Thibault, Aliénor, Enguerrand…).
- **Le jour**, il flâne autour de sa maison, sans jamais quitter la ville. **La nuit**, il rentre **dormir dans son lit**.
- Pour ménager le serveur, seuls les habitants les plus proches des joueurs sont affichés. Les autres continuent d'exister et de payer l'impôt.

### L'impôt de l'aube

À chaque **nouveau jour de jeu**, chaque habitant verse **2 coins** dans la caisse de la ville : *« 💰 Impôt de l'aube : 3 habitants → +6 coins »*. Plus Valmont est peuplée, plus elle est riche.

### Les dangers

- **Les joueurs ne peuvent pas blesser les habitants.**
- **Les monstres, si** : la nuit, un monstre qui rôde près d'un habitant peut s'en prendre à lui. Éclairez la ville, fermez les maisons et formez une garde.
- Quand un habitant meurt, **son lit reste en deuil 20 minutes**, puis un nouvel habitant peut s'y installer.

### Les départs

Un habitant **quitte la ville** si **son lit est cassé**, ou si **sa maison est supprimée** ou change de type. Pensez-y avant de réaménager une maison !

### Suivre la population

- Panneau **Tab** : ligne **Habitants**, au format « vivants / places ».
- Liste des bâtiments d'Alderic : *« Habitants : 2 / 3 lits (1 en deuil) »* sur chaque habitation.
- `/city habitants` : le bilan complet (maisons, occupants, deuils, prochaine arrivée).

## 2. La garde de Valmont

Parmi les survivants à retrouver figure **le capitaine de la garde**. Une fois installé dans son atelier, il peut **former des habitants** pour en faire des gardes, depuis son menu **🛡 Actions → La garde**, ou avec `/city garde`.

### Les rôles

| Rôle | Rang du capitaine requis | Formation | Combat |
|---|---|---|---|
| **Soldat** | Novice | 10 min | Au contact, en armure de fer |
| **Archer** | Apprenti | 15 min | À distance, à l'arc |
| **Sergent** | Expert | 25 min | Au contact, lourdement équipé |

### La taille de la garde

| Rang du capitaine | Gardes au maximum (recrues comprises) | Formations simultanées |
|---|---|---|
| Novice | 8 | 2 |
| Apprenti | 16 | 3 |
| Compagnon | 25 | 4 |
| Expert | 36 | 5 |
| Maître | 50 | 6 |

Pour agrandir la garde, faites **monter le capitaine en rang** : commercez avec lui, faites ses quêtes et **remportez des sièges**.

### Comment ça marche

- **La garde est commune** : n'importe quel joueur peut lancer une formation ou renvoyer un garde.
- La recrue s'**entraîne à côté du capitaine**, avec un minuteur au-dessus de la tête. **Le temps n'avance que si au moins un joueur est connecté.**
- À la fin, elle revêt **l'uniforme de la garde** et reçoit son équipement.
- Les gardes **patrouillent dans la ville jour et nuit** et attaquent les monstres qui y entrent. Ils ne blessent jamais un joueur, un habitant ni un animal, et les joueurs ne peuvent pas les blesser.
- Un garde **garde son lit** et ne paie pas l'impôt.
- **Renvoyer un garde** : **Maj + clic droit** sur lui dans la liste de la garde, ou `/city garde renvoyer <nom>`. Il redevient un habitant ordinaire.
- **Un garde tombé n'est pas remplacé automatiquement** : il faudra former une nouvelle recrue.

## 3. Les sièges

Une ville prospère attire les convoitises. **À partir du chapitre IV**, Valmont subit des sièges : des **vagues d'ennemis** viennent s'en prendre à ses habitants et à ses gardes.

### Quand ?

| | Par défaut |
|---|---|
| **Jours et heure** | Le **mercredi** et le **samedi** à **21 h 00** (heure de Paris) |
| **Joueurs minimum** | **2 joueurs connectés** à l'heure dite, sinon le siège est annulé |
| **Annonce** | Un coup de cloche et un message **5 minutes avant** |

`/city event` affiche le calendrier et le compte à rebours jusqu'au prochain siège.

### Le déroulement

1. **L'alerte** : cloches d'alarme, titre **« ⚔ Siège ! »**, puis un **cor de guerre** qui vient **du côté attaqué**. Tendez l'oreille ! Vous avez **30 secondes** pour vous préparer.
2. **Les vagues** : 3 vagues au début, jusqu'à 5 pour une ville très avancée, avec 30 secondes de répit entre deux. Chaque vague peut arriver d'un côté différent. Les assaillants sont d'autant plus nombreux que la ville est avancée et que des joueurs sont connectés.
3. **Une barre rouge** en haut de l'écran suit le siège : vague en cours, direction, assaillants restants, temps restant.
4. **La fin** : vous avez **20 minutes** pour repousser toutes les vagues.

### Qui attaque ?

Selon le siège, Valmont fait face à **des hordes de monstres** ou à **l'armée d'une faction rivale**, qui marche bannière en tête. Plus la ville grandit, plus ses ennemis sont redoutables. Dans les sièges les plus durs, **un champion** peut mener la dernière vague…

Les ennemis s'en prennent d'abord **aux habitants et aux gardes**, puis marchent sur la **mairie**. Bonne nouvelle : les soldats ennemis **n'ouvrent pas les portes**, et une maison bien fermée protège ses habitants.

### Votre rôle pendant un siège

- ⚠️ **Pendant un siège, vous pouvez être blessé, même en ville.**
- **Aucun bloc n'est jamais endommagé** : pas de porte enfoncée, pas d'incendie, pas d'explosion.
- **La garde se met en ligne** sur le côté attaqué pendant l'alerte, puis **sort à la rencontre de l'ennemi** à l'arrivée de chaque vague.
- Les monstres que vous abattez comptent pour vos **contrats de chasse** auprès des artisans.

### Victoire ou défaite

| | Résultat |
|---|---|
| 🏆 **Victoire** | Fanfare, cloches et **feux d'artifice** au-dessus de la mairie. La caisse reçoit **150 coins + 50 par chapitre** (350 coins au chapitre IV), et le capitaine de la garde gagne de l'expérience |
| 💀 **Défaite** (temps écoulé) | Les assaillants se retirent, sans récompense |

Dans les deux cas, le chat affiche un **bilan** : les trois meilleurs défenseurs, les ennemis abattus par la garde et les pertes.

> Avant que le capitaine de la garde ne rejoigne Valmont, la défense repose entièrement sur les joueurs. Protégez vos habitants !
