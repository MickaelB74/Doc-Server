# Documentation serveur

Sources de la documentation du serveur, générée avec [Zensical](https://zensical.org/)
et publiée en site statique sur [Render](https://render.com/).

## Arborescence

| Élément            | Rôle                                                        |
| ------------------ | ----------------------------------------------------------- |
| `docs/`            | Pages Markdown de la documentation (+ `docs/assets/` pour les images) |
| `docs/stylesheets/valmont.css` | Thème médiéval « Valmont » (bois, parchemin, or, pixel art) |
| `overrides/`       | Surcharges du thème Zensical (chargement des polices)       |
| `outils/generer_assets.py` | Copie les pixel arts du pack et génère textures, blason et panorama |
| `zensical.toml`    | Configuration du site (nom, navigation, thème, extensions)  |
| `requirements.txt` | Version de Zensical utilisée pour le build                  |
| `render.yaml`      | Blueprint Render : build et publication automatique         |
| `Contexte/`        | Matière première locale, **non versionnée** (voir `.gitignore`) |

## Organisation des pages

| Dossier de `docs/` | Rubrique (onglet) |
| ------------------ | ----------------- |
| `serveur/`         | Le serveur : connexion, pack de ressources, mods et plugins, règles d'or |
| `histoire/`        | L'histoire : récit sans spoiler, Chroniques de Valmont, lexique |
| `guide/`           | Guide du joueur : premiers pas, trame, territoire, bâtiments, commerce, habitants, garde, sièges, interfaces, ambiances |
| `personnages/`     | Galerie, recrutement, artisans, ateliers, puis une fiche par personnage (`survivants/`, `legendes/`, `alderic.md`) |
| `aide/`            | Aide-mémoire, commandes, FAQ, fonctionnalités à venir |

Les informations encore manquantes (adresse du serveur, modpack, règlement…)
sont signalées dans les pages par des encadrés `!!! equipe` et des étiquettes
« à compléter » / « à vérifier » : `grep -rn "equipe\|à vérifier\|à compléter" docs/`.

## Le thème « Valmont »

Le style reprend les menus du pack de ressources en jeu (palette échantillonnée
sur les PNG). Composants disponibles dans les pages Markdown :

| Syntaxe | Rendu |
| ------- | ----- |
| `!!! dialogue "Nom"` | Réplique d'un personnage (style barre d'action) |
| `??? spoiler "Titre"` | Bloc violet replié pour ce qui dévoile l'histoire |
| `??? chronique "Titre"` | Page de livre (Chroniques de Valmont) |
| `!!! equipe "Titre"` | Information à compléter par l'équipe |
| `!!! nouveau "Titre"` | Fonctionnalité récente, susceptible d'évoluer |
| `{ .lettrine }` après un paragraphe | Grande initiale dorée |
| `<span class="vm-badge vm-badge--vert">…</span>` | Étiquette (vert, bleu, violet, orange, rouge, turquoise, gris, or) |
| `![](…/ui/boutons/btn_vendre.png){ .vm-ui }` | Bouton du jeu en ligne ; `.vm-icone`, `.vm-anneau`, `.vm-etoiles` pour les petites images |
| `<div class="vm-fiche" markdown>` | Fiche d'identité (voir `docs/personnages/survivants/bastien.md`) |
| `<ol class="vm-frise" markdown>` | Étapes numérotées en chiffres romains sur cartouches dorés |

Pour régénérer les images (Pillow requis, et le dossier `Contexte/` présent) :

```powershell
pip install pillow
python outils/generer_assets.py
```

## Travailler en local (Windows / PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

zensical serve                    # aperçu sur http://localhost:8000 avec rechargement auto
zensical build --clean            # même build que Render, à lancer avant de merger dans main
```

## Branches

| Branche   | Rôle                                                              |
| --------- | ----------------------------------------------------------------- |
| `main`    | Production : **chaque commit est publié automatiquement** par Render |
| `develop` | Rédaction en cours ; merge dans `main` quand le contenu est prêt  |

Flux conseillé : travailler sur `develop` (ou une branche `doc/<sujet>` issue de
`develop`), vérifier avec `zensical build --clean`, puis merger dans `main`.

## Mise en ligne automatique (Render)

Le dépôt n'est encore relié à **aucun remote**. Pour brancher la publication :

1. Créer le dépôt distant (GitHub, GitLab ou Bitbucket) puis le relier :

    ```powershell
    git remote add origin <url-du-depot>
    git push -u origin main develop
    ```

2. Dans Render : **New > Blueprint**, sélectionner le dépôt. Render lit
   `render.yaml`, crée le site statique `doc-serveur` et installe un webhook sur
   le dépôt.
3. À partir de là, chaque push / merge sur `main` déclenche
   `pip install -r requirements.txt && zensical build --clean` (commande de
   build documentée par Zensical) puis la publication du dossier `site/`. Si le build échoue, la version en ligne reste
   inchangée.
4. Mettre à jour `site_url` dans `zensical.toml` avec l'URL réelle du site
   (`https://<service>.onrender.com/` ou domaine personnalisé), et renseigner
   `repo_url` / `repo_name` si souhaité.

### Variante : déclenchement par Deploy Hook

Si le déploiement doit être piloté par une CI (par exemple après des tests),
passer `autoDeployTrigger: off` dans `render.yaml`, récupérer l'URL **Deploy
Hook** dans *Settings* du service Render (URL secrète, à stocker en secret CI)
et l'appeler en fin de pipeline sur `main` :

```bash
curl -fsS -X POST "$RENDER_DEPLOY_HOOK_URL"
```
