class MaxHeap:
    def __init__(self):
        self.heap = []
       
    # ---------------- 
    # Zone pour Edwin
    # ----------------
    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2
    
    def get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1
    
    def get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2
    
    def swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    # ------------------
    # Zone pour Nathan
    # ------------------
    def heapify(self, size: int, index: int):
        """
        Fait descendre l'élément à 'index' à sa bonne place pour que
        la propriété de Max-Heap soit respectée.
        Nathan code ici.
        """
        
        # Tu écris un algorithme qui comparee l'élément
        # avec ses enfants gauche/droit et l'échange si un enfant est plus grand.
        pass # Enlève cette ligne et écris ton code ici
    
    # -----------------
    # Zone pour Rindra
    # -----------------
    def build_heap(self, data_list: list):
        """
        Prend une liste brute et transforme la en Max-Heap.
        Rindra, tu codes de ce côté.
        """
        self.heap = data_list.copy()
        n = len(self.heap)
        
        # Tu dois faire une boucle en partant du milieu de la liste
        # jusqu'à l'index 0 et appeler heapify() à chaque fois.
        pass # Enlève cette ligne et code ici
    
    def heapsort(self, data_list: list) -> list:
        """
        C'est ici que l'algorithme principal du Tri par Tas passe.
        Rindra, tu codes aussi de ce côté là.
        """
        # D'abord, tu appelles build_heap() pour transformer la liste en tas. Déjà fait là.
        self.build_heap(data_list)
        n = len(self.heap)
        
        # Puis, c'est ici que tu dois faire une boucle de tri, qui
        # va échanger la racine (le plus grand) avec le dernier élément,
        # réduire la taille du tas virtuel de 1, et ré-entasser (heapify).
        # Tu codes ici
        
        return self.heap
