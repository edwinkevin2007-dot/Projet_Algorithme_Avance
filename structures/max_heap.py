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

        largest = index

        while True:
            left = self.get_left_child_index(index)
            right = self.get_right_child_index(index)

            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.swap(index, largest)
            index = largest
    
    # -----------------
    # Zone pour Rindra
    # -----------------
    def build_heap(self, data_list: list):
  
        self.heap = data_list.copy()
        n = len(self.heap)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
    
    def heapsort(self, data_list: list) -> list:
   
        self.build_heap(data_list)

        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.swap(0, i)
            self.heapify(i, 0)
        
        return self.heap
