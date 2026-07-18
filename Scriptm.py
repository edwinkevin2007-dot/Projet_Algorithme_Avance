def entasser(liste, taille, i):
    plus_grand = i
    gauche = 2 * i + 1
    droite = 2 * i + 2

    if gauche < taille and liste[gauche] > liste[plus_grand]:
        plus_grand = gauche

    if droite < taille and liste[droite] > liste[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        print(f"  Échange : {liste[i]} <-> {liste[plus_grand]}")
        liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
        entasser(liste, taille, plus_grand)


def heapsort(liste):
    n = len(liste)
    print(f"Liste de départ : {liste}\n")

    print("Étape 1 : construction du tas max")
    for i in range(n // 2 - 1, -1, -1):
        entasser(liste, n, i)
    print(f"Tas max obtenu : {liste}\n")

    print("Étape 2 : extraction du maximum, un par un")
    for i in range(n - 1, 0, -1):
        print(f"Le plus grand élément est {liste[0]}, on le place à la position {i}")
        liste[0], liste[i] = liste[i], liste[0]
        entasser(liste, i, 0)
        print(f"  Liste actuelle : {liste}\n")

    print(f"Liste triée : {liste}")


if __name__ == "__main__":
    heapsort([45, 7, 12, 90, 15, 3])