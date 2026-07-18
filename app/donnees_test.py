# ============================================================
# 1. CAS NORMAL : liste mélangée (scores dans le désordre total)
# ============================================================
liste_melangee = [
    {"pseudo": "GamerX", "score": 1500},
    {"pseudo": "ShadowWolf", "score": 320},
    {"pseudo": "NovaStrike", "score": 2750},
    {"pseudo": "PixelQueen", "score": 980},
    {"pseudo": "ByteRunner", "score": 4100},
    {"pseudo": "KnightFall", "score": 150},
    {"pseudo": "VortexAce", "score": 3300},
    {"pseudo": "EchoBlade", "score": 60},
    {"pseudo": "TitanCrush", "score": 1990},
    {"pseudo": "LunaSpark", "score": 725},
]

# ============================================================
# 2. PIRE DES CAS : liste inversée (scores triés du plus petit au plus grand)
#    -> Un tri par tas doit reconstruire l'ordre décroissant complet
# ============================================================
liste_inversee = [
    {"pseudo": "EchoBlade", "score": 60},
    {"pseudo": "KnightFall", "score": 150},
    {"pseudo": "ShadowWolf", "score": 320},
    {"pseudo": "LunaSpark", "score": 725},
    {"pseudo": "PixelQueen", "score": 980},
    {"pseudo": "GamerX", "score": 1500},
    {"pseudo": "TitanCrush", "score": 1990},
    {"pseudo": "NovaStrike", "score": 2750},
    {"pseudo": "VortexAce", "score": 3300},
    {"pseudo": "ByteRunner", "score": 4100},
]

# ============================================================
# 3. MEILLEUR DES CAS : liste déjà triée (scores du plus grand au plus petit)
# ============================================================
liste_triee = [
    {"pseudo": "ByteRunner", "score": 4100},
    {"pseudo": "VortexAce", "score": 3300},
    {"pseudo": "NovaStrike", "score": 2750},
    {"pseudo": "TitanCrush", "score": 1990},
    {"pseudo": "GamerX", "score": 1500},
    {"pseudo": "PixelQueen", "score": 980},
    {"pseudo": "LunaSpark", "score": 725},
    {"pseudo": "ShadowWolf", "score": 320},
    {"pseudo": "KnightFall", "score": 150},
    {"pseudo": "EchoBlade", "score": 60},
]


def afficher_donnees(liste, titre="Classement"):
    """Affiche proprement une liste de joueurs (dictionnaires pseudo/score)."""
    print(f"\n=== {titre} ===")
    for rang, joueur in enumerate(liste, start=1):
        print(f"{rang}. {joueur['pseudo']} - {joueur['score']} pts")


if __name__ == "__main__":
    print("########## DONNÉES DE TEST - HEAPSORT (Classement Jeu Vidéo) ##########")

    afficher_donnees(liste_melangee, "Cas normal (liste mélangée) - AVANT TRI")
    afficher_donnees(liste_inversee, "Pire des cas (liste inversée) - AVANT TRI")
    afficher_donnees(liste_triee, "Meilleur des cas (liste déjà triée) - AVANT TRI")

