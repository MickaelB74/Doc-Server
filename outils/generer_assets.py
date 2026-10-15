"""Génère et copie les images du thème « Valmont » de la documentation.

Deux tâches :
1. Copier dans docs/assets/ les éléments d'interface du pack de ressources
   (dossier Contexte/Pixel-arts, non versionné) utilisés par les pages.
2. Dessiner, pixel par pixel, les images propres au site : textures de bois,
   de parchemin et de pierre, blason de Valmont, favicon et panorama d'accueil.

Toutes les images générées sont des créations originales (aucune ressource
Mojang). Elles sont dessinées à leur taille réelle et agrandies par le
navigateur avec `image-rendering: pixelated`, comme les menus en jeu.

Utilisation (depuis la racine du dépôt, Pillow requis : pip install pillow) :
    python outils/generer_assets.py
"""

from __future__ import annotations

import math
import random
import shutil
from pathlib import Path

from PIL import Image

RACINE = Path(__file__).resolve().parent.parent
SOURCE_PIXEL_ARTS = RACINE / "Contexte" / "Pixel-arts"
ASSETS = RACINE / "docs" / "assets"

# --- Palette reprise des menus en jeu (échantillonnée sur les PNG du pack) ---
BOIS_CONTOUR = (0x1E, 0x12, 0x0A)
BOIS_TRES_SOMBRE = (0x2C, 0x1A, 0x0D)
BOIS = (0x3A, 0x23, 0x12)
BOIS_MOYEN = (0x55, 0x34, 0x1B)
BOIS_CLAIR = (0x6E, 0x45, 0x24)
OR_CONTOUR = (0x4A, 0x30, 0x06)
OR_SOMBRE = (0x9A, 0x6A, 0x14)
OR = (0xC9, 0x9A, 0x2A)
OR_CLAIR = (0xEF, 0xC4, 0x52)
OR_ECLAT = (0xFF, 0xED, 0xA0)
ROUGE_SOMBRE = (0x86, 0x1E, 0x1E)
ROUGE = (0xB4, 0x30, 0x30)
ROUGE_CLAIR = (0xDE, 0x50, 0x50)
CREME = (0xF6, 0xEB, 0xCD)
SABLE = (0xC9, 0xAE, 0x7C)


# =============================================================================
# 1. Copie des éléments du pack de ressources
# =============================================================================

# Dossier source (dans Pixel-arts) -> dossier cible (dans docs/assets)
COPIES = {
    "Apercus_ecrans": "ecrans",
    "Elements_interface_x4/Icones": "ui/icones",
    "Elements_interface_x4/Badges": "ui/badges",
    "Elements_interface_x4/Anneaux_statut": "ui/anneaux",
    "Elements_interface_x4/Etoiles_rang": "ui/etoiles",
    "Elements_interface_x4/Boutons_menus": "ui/boutons",
    "Elements_interface_x4/Boutons_maire": "ui/boutons",
    "Elements_interface_x4/Boutons_quetes": "ui/boutons",
    "Elements_interface_x4/Rubans_titres": "ui/rubans",
    "Elements_interface_x4/Decors_portraits": "ui/decors",
    "Elements_interface_x4/Onglets_journal": "ui/onglets",
    "Elements_interface_x4/Positions_panneau": "ui/positions",
}


def copier_pack() -> None:
    """Copie les PNG du pack de ressources vers docs/assets (écrase l'existant)."""
    if not SOURCE_PIXEL_ARTS.exists():
        print(f"! {SOURCE_PIXEL_ARTS} introuvable : copie du pack ignorée.")
        return
    for source, cible in COPIES.items():
        dossier_cible = ASSETS / cible
        dossier_cible.mkdir(parents=True, exist_ok=True)
        for png in sorted((SOURCE_PIXEL_ARTS / source).glob("*.png")):
            shutil.copy2(png, dossier_cible / png.name)
    print("- éléments du pack copiés")


# =============================================================================
# 2. Outils de dessin
# =============================================================================

def nouvelle_image(largeur: int, hauteur: int, fond=(0, 0, 0, 0)) -> Image.Image:
    return Image.new("RGBA", (largeur, hauteur), fond)


def rect(img: Image.Image, x0: int, y0: int, x1: int, y1: int, couleur) -> None:
    """Remplit le rectangle [x0, x1] x [y0, y1] (bornes incluses, coupé au cadre)."""
    px = img.load()
    for y in range(max(0, y0), min(img.height, y1 + 1)):
        for x in range(max(0, x0), min(img.width, x1 + 1)):
            px[x, y] = couleur if len(couleur) == 4 else (*couleur, 255)


def point(img: Image.Image, x: int, y: int, couleur) -> None:
    if 0 <= x < img.width and 0 <= y < img.height:
        img.load()[x, y] = couleur if len(couleur) == 4 else (*couleur, 255)


def bruit_valeur(largeur: int, hauteur: int, cellule: int, graine: int) -> list[list[float]]:
    """Bruit de valeur périodique (raccord parfait en mosaïque), valeurs 0..1."""
    rng = random.Random(graine)
    nx, ny = largeur // cellule, hauteur // cellule
    grille = [[rng.random() for _ in range(nx)] for _ in range(ny)]

    def lisse(t: float) -> float:
        return t * t * (3 - 2 * t)

    champ = []
    for y in range(hauteur):
        ligne = []
        gy, fy = divmod(y / cellule, 1)
        gy = int(gy)
        for x in range(largeur):
            gx, fx = divmod(x / cellule, 1)
            gx = int(gx)
            a = grille[gy % ny][gx % nx]
            b = grille[gy % ny][(gx + 1) % nx]
            c = grille[(gy + 1) % ny][gx % nx]
            d = grille[(gy + 1) % ny][(gx + 1) % nx]
            sx, sy = lisse(fx), lisse(fy)
            ligne.append((a * (1 - sx) + b * sx) * (1 - sy) + (c * (1 - sx) + d * sx) * sy)
        champ.append(ligne)
    return champ


# =============================================================================
# 3. Textures (mosaïques)
# =============================================================================

def texture_planches(base, veine_claire, veine_sombre, joint, graine: int) -> Image.Image:
    """Planches horizontales façon Minecraft : 32 x 32 px, raccord en mosaïque."""
    rng = random.Random(graine)
    img = nouvelle_image(32, 32)
    hauteur_planche = 8
    for rangee in range(4):
        y0 = rangee * hauteur_planche
        # Chaque rangée a une teinte très légèrement différente.
        teinte = rng.choice([base, base, veine_sombre if rangee % 2 else base])
        rect(img, 0, y0, 31, y0 + hauteur_planche - 2, teinte)
        # Veines du bois : courts traits horizontaux.
        for _ in range(7):
            x = rng.randrange(32)
            y = y0 + rng.randrange(hauteur_planche - 1)
            longueur = rng.randrange(3, 9)
            couleur = veine_claire if rng.random() < 0.5 else veine_sombre
            for i in range(longueur):
                point(img, (x + i) % 32, y, couleur)
        # Joint horizontal sous la planche, et joint vertical décalé.
        rect(img, 0, y0 + hauteur_planche - 1, 31, y0 + hauteur_planche - 1, joint)
        x_joint = (rangee * 13 + 5) % 32
        rect(img, x_joint, y0, x_joint, y0 + hauteur_planche - 2, joint)
        point(img, (x_joint + 1) % 32, y0, veine_claire)
    return img


def texture_parchemin(couleurs, graine: int) -> Image.Image:
    """Parchemin moucheté discret : 64 x 64 px, 4 tons quantifiés, raccord parfait."""
    rng = random.Random(graine)
    champ = bruit_valeur(64, 64, 16, graine)
    fin = bruit_valeur(64, 64, 4, graine + 1)
    img = nouvelle_image(64, 64)
    clair, base, sombre, tache = couleurs
    for y in range(64):
        for x in range(64):
            v = champ[y][x] * 0.7 + fin[y][x] * 0.3 + (rng.random() - 0.5) * 0.12
            if v > 0.72:
                c = clair
            elif v < 0.24:
                c = tache
            elif v < 0.36:
                c = sombre
            else:
                c = base
            point(img, x, y, c)
    return img


def texture_pierre(graine: int) -> Image.Image:
    """Briques de pierre (remparts du pied de page) : 32 x 32 px."""
    rng = random.Random(graine)
    mortier = (0x26, 0x24, 0x2A)
    tons = [(0x4A, 0x4A, 0x52), (0x52, 0x52, 0x5A), (0x44, 0x44, 0x4C)]
    eclat, ombre = (0x5E, 0x5E, 0x68), (0x3A, 0x3A, 0x42)
    img = nouvelle_image(32, 32, (*mortier, 255))
    for rangee in range(4):
        y0 = rangee * 8
        decalage = 0 if rangee % 2 == 0 else 8
        for b in range(-1, 3):
            x0 = b * 16 + decalage
            ton = rng.choice(tons)
            for y in range(y0, y0 + 7):
                for x in range(x0, x0 + 15):
                    xx = x % 32
                    c = ton
                    if y == y0:
                        c = eclat
                    elif y == y0 + 6 or x == x0 + 14:
                        c = ombre
                    elif rng.random() < 0.08:
                        c = ombre if rng.random() < 0.5 else eclat
                    point(img, xx, y, c)
    return img


# =============================================================================
# 4. Blason de Valmont (logo) : la tour qui renaît des flammes
# =============================================================================

def blason() -> Image.Image:
    largeur, hauteur = 24, 28
    img = nouvelle_image(largeur, hauteur)
    cx = largeur / 2

    def demi_largeur(y: int) -> float:
        # Écu « français ancien » : flancs droits puis pointe arrondie.
        if y < 14:
            return 11.5
        t = (y - 14) / 13
        return 11.5 * math.cos(t * math.pi / 2) ** 0.8

    # Contour sombre, bordure d'or puis champ de gueules (rouge).
    for y in range(hauteur):
        w = demi_largeur(y)
        for x in range(largeur):
            d = abs(x + 0.5 - cx)
            if d > w:
                continue
            bord = w - d
            if y == 0 or bord < 1 or y == hauteur - 1:
                c = BOIS_CONTOUR
            elif y in (1, 2) or bord < 3 or y >= hauteur - 3:
                # Or éclairé en haut à gauche, assombri en bas à droite.
                c = OR_CLAIR if (x < cx and y < 16) or y in (1,) else OR if x < cx else OR_SOMBRE
                if y == 1 and bord >= 1:
                    c = OR_ECLAT
            else:
                c = ROUGE if x < cx else ROUGE_SOMBRE
            point(img, x, y, c)
    # Lisière intérieure sombre entre l'or et le rouge (lisibilité à petite taille).
    px = img.load()
    for y in range(3, hauteur - 3):
        for x in range(largeur):
            if px[x, y][:3] in (ROUGE, ROUGE_SOMBRE):
                voisins = [px[x + dx, y + dy][:3] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                           if 0 <= x + dx < largeur and 0 <= y + dy < hauteur]
                if any(v in (OR, OR_CLAIR, OR_SOMBRE, OR_ECLAT) for v in voisins):
                    px[x, y] = (*OR_CONTOUR, 255)

    # La tour, dessinée pixel par pixel (x 7 à 16, y 5 à 20) :
    # C = pierre claire, S = pierre ombrée, W = fenêtre éclairée, P = porte.
    tour = [
        ".CC.CC.SS.",  # merlons
        ".CC.CC.SS.",
        "CCCCCCCSSS",  # encorbellement, un peu plus large
        ".CCCCCCSS.",
        ".CCCCCCSS.",
        ".CCCWWCSS.",
        ".CCCWWCSS.",
        ".CCCCCCSS.",
        ".CCCCCCSS.",
        ".CCCCCCSS.",
        ".CCCPPCSS.",
        ".CCPPPPSS.",
        ".CCPPPPSS.",
        ".CCPPPPSS.",
    ]
    teintes_tour = {"C": CREME, "S": SABLE, "W": OR_CLAIR, "P": BOIS_CONTOUR}
    for j, ligne in enumerate(tour):
        for i, ch in enumerate(ligne):
            if ch in teintes_tour:
                point(img, 7 + i, 5 + j, teintes_tour[ch])

    # Flammes au pied de la tour : Valmont renaît de ses cendres.
    flammes = {
        19: "..F.........F...",
        20: ".FYF.F....F.FYF.",
        21: "FYYFFYF..FYFFYYF",
        22: ".FYYYOYFFYOYYYF.",
        23: "..FYOOOYYOOOYF..",
    }
    teintes = {"F": (0xE0, 0x6A, 0x1C), "Y": (0xFF, 0xD2, 0x3F), "O": (0xFF, 0xF2, 0xB8)}
    for y, motif in flammes.items():
        for i, ch in enumerate(motif):
            if ch in teintes:
                point(img, 4 + i, y, teintes[ch])
    return img


# =============================================================================
# 5. Panorama de la page d'accueil : Valmont qui renaît à l'aube
# =============================================================================

def panorama() -> Image.Image:
    largeur, hauteur = 400, 132
    rng = random.Random(1312)
    img = nouvelle_image(largeur, hauteur)

    # Ciel de l'aube en bandes tramées (dithering 2x2 entre deux bandes).
    bandes = [
        (0x1A, 0x14, 0x2E), (0x26, 0x1B, 0x3D), (0x38, 0x22, 0x4A), (0x52, 0x2C, 0x55),
        (0x74, 0x36, 0x58), (0x9A, 0x44, 0x52), (0xC0, 0x5A, 0x44), (0xDE, 0x7E, 0x3E),
        (0xF0, 0xA6, 0x4A), (0xF8, 0xC8, 0x6A),
    ]
    hauteur_ciel = 104
    for y in range(hauteur_ciel):
        t = y / hauteur_ciel * (len(bandes) - 1)
        i = int(t)
        frac = t - i
        for x in range(largeur):
            seuil = [[0.2, 0.6], [0.8, 0.4]][y % 2][x % 2]
            c = bandes[min(i + 1, len(bandes) - 1)] if frac > seuil else bandes[i]
            point(img, x, y, c)

    # Étoiles dans le haut du ciel.
    for _ in range(70):
        x, y = rng.randrange(largeur), rng.randrange(38)
        point(img, x, y, (0xF6, 0xEB, 0xCD) if rng.random() < 0.3 else (0x9C, 0x8C, 0xB8))

    # Soleil levant derrière les montagnes.
    sx, sy, r = 300, 70, 13
    for y in range(sy - r, sy + r + 1):
        for x in range(sx - r, sx + r + 1):
            d = math.hypot(x - sx, y - sy)
            if d <= r:
                point(img, x, y, (0xFF, 0xE8, 0xA8) if d < r - 2 else (0xFF, 0xD0, 0x78))

    # Dragon lointain (menace qui plane encore), silhouette sombre.
    dragon = [
        "..............XX.......",
        "XX...........XXXX......",
        ".XXX........XXXXX.....X",
        "..XXXX.....XXXXXXXXXXX.",
        "...XXXXXXXXXXXXXX......",
        "....XXXXXXXXXXX........",
        "......XXX..XX..........",
        ".....XX.....X..........",
    ]
    for j, ligne in enumerate(dragon):
        for i, ch in enumerate(ligne):
            if ch == "X":
                point(img, 70 + i, 14 + j, (0x12, 0x0C, 0x1C))

    def silhouette_relief(y_base: float, amplitude: float, frequence: float, phase: float, couleur, neige=None):
        for x in range(largeur):
            h = y_base - amplitude * (0.6 * abs(math.sin(x * frequence + phase))
                                      + 0.4 * abs(math.sin(x * frequence * 2.3 + phase * 1.7)))
            sommet = int(h)
            for y in range(sommet, hauteur):
                point(img, x, y, couleur)
            if neige and sommet < y_base - amplitude * 0.7:
                rect(img, x, sommet, x, sommet + 1, neige)

    # Montagnes lointaines (enneigées), puis collines.
    silhouette_relief(92, 34, 0.021, 0.7, (0x5A, 0x3E, 0x62), neige=(0xC8, 0xB6, 0xD2))
    silhouette_relief(104, 14, 0.035, 2.1, (0x3E, 0x2A, 0x45))

    # --- La ville, en silhouette sombre, avec fenêtres éclairées ---
    sombre = (0x1E, 0x12, 0x0A)
    sombre2 = (0x2C, 0x1A, 0x0D)
    fenetre = (0xEF, 0xC4, 0x52)
    sol = 112

    def batiment(x0: int, largeur_b: int, hauteur_b: int, toit: str = "pointe", couleur=sombre2):
        y_haut = sol - hauteur_b
        rect(img, x0, y_haut, x0 + largeur_b - 1, sol, couleur)
        if toit == "pointe":
            demi = largeur_b // 2
            for k in range(demi + 2):
                rect(img, x0 - 1 + k, y_haut - k, x0 + largeur_b - k, y_haut - k, couleur)
        elif toit == "creneaux":
            for k in range(0, largeur_b, 3):
                rect(img, x0 + k, y_haut - 2, x0 + k + 1, y_haut - 1, couleur)
        # Fenêtres éclairées, au hasard.
        for fy in range(y_haut + 3, sol - 3, 5):
            for fx in range(x0 + 2, x0 + largeur_b - 2, 4):
                if rng.random() < 0.38:
                    rect(img, fx, fy, fx, fy + 1, fenetre)

    # Remparts sur toute la largeur.
    rect(img, 0, sol - 10, largeur - 1, sol, sombre)
    for x in range(0, largeur, 4):
        rect(img, x, sol - 13, x + 1, sol - 11, sombre)

    # Maisons et tours (gauche).
    for x0, l, h, t in [(8, 12, 20, "pointe"), (24, 10, 16, "pointe"), (38, 9, 34, "creneaux"),
                        (52, 14, 22, "pointe"), (70, 11, 18, "pointe"), (86, 8, 40, "pointe"),
                        (98, 13, 24, "pointe")]:
        batiment(x0, l, h, t)

    # La cathédrale et sa rosace, au centre.
    cx = 150
    batiment(cx - 18, 36, 34, "pointe")
    batiment(cx - 26, 9, 46, "pointe")
    batiment(cx + 18, 9, 46, "pointe")
    rect(img, cx - 1, sol - 74, cx, sol - 46, sombre2)  # flèche
    rect(img, cx - 2, sol - 66, cx + 1, sol - 66, sombre2)  # croisillon
    rosace = {(0, 0): (0xF6, 0xEB, 0xCD)}
    for (dx, dy), c in {(-1, 0): (0xB4, 0x30, 0x30), (1, 0): (0x38, 0x66, 0xBA), (0, -1): (0x45, 0x92, 0x2F),
                        (0, 1): (0xEF, 0xC4, 0x52), (-1, -1): (0xEF, 0xC4, 0x52), (1, 1): (0xB4, 0x30, 0x30),
                        (1, -1): (0x78, 0x40, 0xA6), (-1, 1): (0x38, 0x66, 0xBA)}.items():
        rosace[(dx, dy)] = c
    for (dx, dy), c in rosace.items():
        point(img, cx + dx - 0, sol - 38 + dy, c)
    point(img, cx + 2, sol - 38, sombre2)

    # Le château (droite) et son donjon à bannière rouge.
    batiment(200, 40, 30, "creneaux", sombre)
    batiment(196, 10, 44, "creneaux", sombre)
    batiment(236, 10, 44, "creneaux", sombre)
    batiment(213, 14, 56, "creneaux", sombre)
    rect(img, 219, sol - 68, 219, sol - 58, sombre)  # mât
    rect(img, 220, sol - 68, 225, sol - 65, ROUGE)  # bannière de Valmont
    point(img, 222, sol - 67, OR_CLAIR)

    # Chantier de reconstruction : échafaudage et grue à roue.
    echafaudage = (0x6E, 0x45, 0x24)
    for x in (262, 268, 274):
        rect(img, x, sol - 30, x, sol, echafaudage)
    for y in (sol - 30, sol - 20, sol - 10):
        rect(img, 262, y, 274, y, echafaudage)
    batiment(276, 12, 14, "pointe")
    rect(img, 292, sol - 40, 293, sol, echafaudage)  # mât de la grue
    rect(img, 286, sol - 40, 306, sol - 39, echafaudage)  # flèche
    rect(img, 305, sol - 38, 305, sol - 26, (0x2C, 0x1A, 0x0D))  # corde
    rect(img, 303, sol - 25, 307, sol - 23, (0x55, 0x34, 0x1B))  # pierre levée

    # Maisons (droite).
    for x0, l, h, t in [(312, 12, 18, "pointe"), (328, 10, 26, "pointe"), (342, 14, 16, "pointe"),
                        (360, 9, 32, "creneaux"), (374, 12, 20, "pointe"), (390, 10, 14, "pointe")]:
        batiment(x0, l, h, t)

    # Premier plan : terre sombre et sapins.
    rect(img, 0, sol, largeur - 1, hauteur - 1, (0x16, 0x10, 0x0A))
    for x in range(0, largeur, 1):
        if rng.random() < 0.25:
            point(img, x, sol, (0x2A, 0x3A, 0x1E))
    for x0 in (0, 18, 44, 120, 178, 252, 330, 352, 384):
        hauteur_sapin = rng.randrange(10, 18)
        for k in range(hauteur_sapin):
            demi = max(0, (k * 5) // hauteur_sapin)
            rect(img, x0 + 4 - demi, hauteur - hauteur_sapin + k - 4, x0 + 4 + demi, hauteur - hauteur_sapin + k - 4,
                 (0x12, 0x1E, 0x12))
        rect(img, x0 + 4, hauteur - 4, x0 + 4, hauteur - 1, (0x12, 0x0C, 0x08))

    # Feu de camp du premier campement, au premier plan.
    for (dx, dy), c in {(0, 0): (0xFF, 0xD2, 0x3F), (-1, 1): (0xE0, 0x6A, 0x1C), (1, 1): (0xE0, 0x6A, 0x1C),
                        (0, 1): (0xFF, 0xF2, 0xB8), (0, -1): (0xE0, 0x6A, 0x1C), (-2, 2): (0x55, 0x34, 0x1B),
                        (2, 2): (0x55, 0x34, 0x1B), (-1, 2): (0x6E, 0x45, 0x24), (1, 2): (0x6E, 0x45, 0x24),
                        (0, 2): (0x55, 0x34, 0x1B)}.items():
        point(img, 100 + dx, hauteur - 8 + dy, c)
    return img


# =============================================================================
# 6. Programme principal
# =============================================================================

def enregistrer(img: Image.Image, chemin: Path, echelle: int = 1) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if echelle > 1:
        img = img.resize((img.width * echelle, img.height * echelle), Image.NEAREST)
    img.save(chemin, optimize=True)
    print(f"- {chemin.relative_to(RACINE)} ({img.width}x{img.height})")


def main() -> None:
    copier_pack()
    textures = ASSETS / "textures"
    # Bois du cadre des menus (fond du site) et bois plus sombre (en-tête).
    enregistrer(texture_planches(BOIS, BOIS_MOYEN, (0x33, 0x1F, 0x10), BOIS_TRES_SOMBRE, 7), textures / "bois.png")
    enregistrer(texture_planches(BOIS_TRES_SOMBRE, BOIS, (0x26, 0x17, 0x0B), BOIS_CONTOUR, 11),
                textures / "bois-sombre.png")
    enregistrer(texture_planches((0x1F, 0x14, 0x0C), (0x2C, 0x1C, 0x10), (0x1A, 0x10, 0x09), (0x12, 0x0B, 0x06), 5),
                textures / "bois-nuit.png")
    # Parchemin clair (jour) et parchemin de veillée (nuit).
    enregistrer(texture_parchemin([(0xF6, 0xE9, 0xC9), (0xF0, 0xE1, 0xBC), (0xE7, 0xD5, 0xAA), (0xDD, 0xC8, 0x99)], 3),
                textures / "parchemin.png")
    enregistrer(texture_parchemin([(0x33, 0x25, 0x1A), (0x2B, 0x1F, 0x15), (0x26, 0x1B, 0x12), (0x21, 0x17, 0x0F)], 4),
                textures / "parchemin-nuit.png")
    enregistrer(texture_pierre(9), textures / "pierre.png")
    # Blason (logo, en-tête), favicon et panorama de l'accueil.
    images = ASSETS / "images"
    logo = blason()
    enregistrer(logo, images / "blason.png", echelle=4)
    favicon = nouvelle_image(32, 32)
    favicon.paste(logo, (4, 2), logo)
    enregistrer(favicon, images / "favicon.png", echelle=2)
    enregistrer(panorama(), images / "panorama-valmont.png")


if __name__ == "__main__":
    main()
