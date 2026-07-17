# Projet d'Algorithme Avancé
Sujet 5 : Tri par Tas (Heapsort)

## Notre équipe et les tâches pour chacun
Chaque membre a un rôle précis.

*   **Edwin :** Architecture globale de la classe `MaxHeap`, calculs des index enfants/parents et gestion du dépôt GitHub.
*   **Nathan :** Programmation de la fonction essentielle `heapify(size, index)` dans `structures/max_heap.py`.
*   **Rindra :** Programmation des fonctions `build_heap()` et `heapsort()` dans `structures/max_heap.py`.
*   **Mendrika :** Gestion du classement de joueurs de jeux vidéo par score dans `app/application.py`.
*   **Ritso :** Gestion du menu interactif dans `main.py` et enregistrement de la vidéo de démonstration (Vokoscreen).
*   **Tantely :** Rédaction du rapport PDF final (théorie, répartition des tâches, captures d'écran).

## Structure du Projet

```text
Projet_Algorithme_Avance/
│
├── app/
│   ├── __init__.py          # NE PAS TOUCHER (Laisser vide)
│   └── application.py       # Mendrika (Application sur le classement de joueurs de jeux vidéo par score.)
│
├── structures/
│   ├── __init__.py          # NE PAS TOUCHER (Laisser vide)
│   └── max_heap.py          # Edwin, Nathan et Rindra (Logique du Tri par Tas (Heapsort))
│
├── main.py                 # Ritso (Menu interactif de démo avec Vokoscreen)
└── README.md               # Petit Guide
```
