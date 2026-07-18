# -------------------
# Zone pour Mendrika
# -------------------

from structures.max_heap import MaxHeap

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

class Joueur:
    def __init__(self, pseudo, score):
        self.pseudo = pseudo
        self.score = score
        
    def __gt__(self, autre):
        return self.score > autre.score

def afficher_donnees(liste, titre="Classement"):
    print(f"\n=== {titre} ===")
    for rang, joueur in enumerate(liste, start=1):
        if isinstance(joueur, Joueur):
            print(f"{rang}. {joueur.pseudo} - {joueur.score} pts")
        else:
            print(f"{rang}. {joueur['pseudo']} - {joueur['score']} pts")

def lancer_simulation(choix_liste: int):
    if choix_liste == 1:
        donnees = liste_melangee
        titre = "Cas normal (Liste mélangée)"
    elif choix_liste == 2:
        donnees = liste_inversee
        titre = "Pire des cas (Liste inversée)"
    else:
        donnees = liste_triee
        titre = "Meilleur des cas (Liste déjà triée)"
        
    afficher_donnees(donnees, f"{titre} - AVANT TRI")
    
    liste_joueurs = [Joueur(d["pseudo"], d["score"]) for d in donnees]

    tri_tas = MaxHeap()
    resultat_tri = tri_tas.heapsort(liste_joueurs)
    
    resultat_tri.reverse()
    
    afficher_donnees(resultat_tri, "CLASSEMENT OFFICIEL (APRÈS TRI)")
