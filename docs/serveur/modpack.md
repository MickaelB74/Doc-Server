---
title: Installer le modpack
description: Télécharger l'archive des mods de MyCivilisation et l'installer, avec un launcher ou le launcher officiel de Minecraft.
---

# Installer le modpack

Pour rejoindre MyCivilisation, votre jeu doit avoir **les mêmes mods que le serveur**. Ils sont tous réunis dans une seule archive : préparez Minecraft avec NeoForge, copiez les mods, et c'est prêt.
{ .chapeau }

[Télécharger l'archive des mods](https://mega.nz/file/a1p0BBSC#MVPOLpJXNfgisEHr8nsketEz0Y3jvv_eqjSwgzxvJuY){ .md-button .md-button--primary }

L'archive est hébergée sur **MEGA** : le lien ouvre sa page de téléchargement, dans votre navigateur.

| | |
|---|---|
| **Adresse du serveur** | `92.159.232.157:25567` |
| **Minecraft** | 1.21.1 |
| **Chargeur de mods** | NeoForge 21.1.219 |
| **Contenu** | Tous les mods nécessaires pour jouer, détaillés dans la [liste des mods](liste-des-mods.md) |

## 1. Préparer Minecraft avec NeoForge

=== "Avec un launcher (conseillé)"

    Dans Prism Launcher, l'application CurseForge ou Modrinth App, créez une nouvelle instance (ou un nouveau profil) **Minecraft 1.21.1** avec le chargeur de mods **NeoForge**, version **21.1.219**. Le launcher installe lui-même Minecraft et NeoForge.

=== "Avec le launcher officiel"

    1. Téléchargez l'[installateur NeoForge 21.1.219](https://maven.neoforged.net/releases/net/neoforged/neoforge/21.1.219/neoforge-21.1.219-installer.jar).
    2. Ouvrez-le (Java doit être installé sur votre ordinateur), choisissez **Install client** et validez.
    3. Dans le launcher Minecraft, lancez une première fois le profil **NeoForge** qui vient d'apparaître, puis quittez le jeu : les dossiers nécessaires sont créés.

## 2. Ajouter les mods

1. Téléchargez l'archive avec le bouton ci-dessus et décompressez-la.
2. Ouvrez le dossier **`mods`** de votre jeu :
    - avec un launcher, ouvrez le dossier de l'instance (tous proposent un bouton pour cela), puis son dossier `mods` ;
    - avec le launcher officiel, appuyez sur ++win+r++, tapez `%appdata%\.minecraft\mods` et validez.
3. Copiez-y **tous les fichiers `.jar`** de l'archive.

!!! warning "Un dossier `mods` propre"

    Le dossier `mods` ne doit contenir que les mods de l'archive : retirez-en les mods d'autres serveurs ou d'anciennes versions, sinon le jeu risque de ne pas démarrer.

!!! tip "La mémoire du jeu"

    Avec autant de mods, le jeu a besoin de plus de mémoire qu'en « vanilla ». En général, accorder **au moins 4 à 6 Go** à l'instance (ou au profil, dans les options du launcher) évite les plantages et les ralentissements.

## 3. Se connecter

Lancez le jeu, puis suivez les étapes de [Rejoindre le serveur](index.md#se-connecter) : ajouter l'adresse du serveur et accepter le pack de ressources « Valmont ».

## Les mods facultatifs

Six mods de l'archive ne sont pas indispensables pour se connecter. Vous pouvez les retirer du dossier `mods` si vous n'en voulez pas :

- **JourneyMap**, la carte du monde. Il est **conseillé** : c'est sur sa carte que s'affichent les parcelles de la ville ;
- **Sodium**, **Iris** (shaders), **EntityCulling**, **LambDynamicLights** et **Leawind's Third Person**, pour l'affichage et les performances. Iris a besoin de Sodium.

Le détail de chaque mod est dans la [liste des mods](liste-des-mods.md).

## Quand le modpack change

Quand l'équipe ajoute, retire ou met à jour un mod sur le serveur, une nouvelle archive est publiée et le bouton en haut de cette page pointe vers elle. Téléchargez-la, **videz** votre dossier `mods`, puis copiez-y le contenu de la nouvelle archive. Si le jeu refuse la connexion en signalant des mods manquants ou différents, c'est en général le signe que votre archive n'est plus à jour.
