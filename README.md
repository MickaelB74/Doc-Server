# Documentation serveur

Sources de la documentation du serveur, générée avec [Zensical](https://zensical.org/)
et publiée en site statique sur [Render](https://render.com/).

## Arborescence

| Élément            | Rôle                                                        |
| ------------------ | ----------------------------------------------------------- |
| `docs/`            | Pages Markdown de la documentation (+ `docs/assets/` pour les images) |
| `zensical.toml`    | Configuration du site (nom, navigation, thème, extensions)  |
| `requirements.txt` | Version de Zensical utilisée pour le build                  |
| `render.yaml`      | Blueprint Render : build et publication automatique         |
| `Contexte/`        | Matière première locale, **non versionnée** (voir `.gitignore`) |

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
