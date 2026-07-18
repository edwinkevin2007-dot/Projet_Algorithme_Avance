from structures.max_heap import MaxHeap
from app.donnees_test import lancer_simulation

def afficher_banniere():
    print("=" * 65)
    print("       PROJET ALGORITHME AVANCÉ : TRI PAR TAS (HEAPSORT)       ")
    print("=" * 65)
    
def tri_numerique_simple():
    print("\n--- [DÉMO] Tri d'une liste de nombres basique ---")
    nombres = [45, 7, 12, 90, 15, 3]
    print(f"Liste initiale désordonnée : {nombres}")
    
    outil_tri = MaxHeap()
    resultat = outil_tri.heapsort(nombres)
    print(f"Liste triée par Heapsort   : {resultat}")
    
def menu_principal():
    while True:
        afficher_banniere()
        print("1. Exécuter un tri simple sur des nombres")
        print("2. Tester le Cas Normal (Joueurs mélangés)")
        print("3. Tester le Pire des Cas (Joueurs inversés)")
        print("4. Tester le Meilleur des Cas (Joueurs déjà triés)")
        print("5. Quitter le programme")
        print("=" * 65)
        
        choix = input("Sélectionnez votre action (1 à 5) : ")
        
        if choix == "1":
            tri_numerique_simple()
        elif choix == "2":
            lancer_simulation(1)
        elif choix == "3":
            lancer_simulation(2)
        elif choix == "4":
            lancer_simulation(3)
        elif choix == "5":
            print("\nFin de la démonstration. Merci d'avoir regardé !")
            break
        else:
            print("\n[ERRUR] Choix indisponible. Entrez un chiffre de 1 à 5.")
            
        input("\nAppuyer sur Entrée pour continuer...")
        print("\n" * 2)
        
if __name__ == "__main__":
    menu_principal()
    