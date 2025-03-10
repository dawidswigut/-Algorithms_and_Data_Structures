import time
import random

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return f"{self.key} : {self.value}"

class Heap:
    def __init__(self, elements=None):
        if elements:
            self.heap = elements
            self.heap_size = len(elements)
            for i in range(self.parent(self.heap_size - 1), -1, -1):
                self.max_heapify(i)
        else:
            self.heap = []
            self.heap_size = 0

    def is_empty(self):
        return self.heap_size == 0

    def enqueue(self, element: Element):
        if self.heap_size == len(self.heap):
            self.heap.append(element)
        else:
            self.heap[self.heap_size] = element
        self.heap_size += 1
        idx = self.heap_size - 1
        parent_idx = self.parent(idx)
        while idx > 0 and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
            parent_idx = self.parent(idx)

    def dequeue(self):
        if self.is_empty():
            return None
        max_elem = self.heap[0]
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        self.max_heapify(0)
        return max_elem

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def max_heapify(self, idx):
        l = self.left(idx)
        r = self.right(idx)
        largest = idx
        if l < self.heap_size and self.heap[l] > self.heap[idx]:
            largest = l
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.max_heapify(largest)

    def print_tab(self):
        print('{', end=' ')
        print(*self.heap[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.heap[idx] if self.heap[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)
        
class SelectionSort:
    @staticmethod
    def swap_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def shift_sort(arr):
        n = len(arr)
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if arr[index] > arr[j]:
                    index = j
            arr.insert(i, arr.pop(index))
        return arr

def main():
    # TEST 1 - ALGORYTM 1
    # W main-ie niech dana będzie lista z danymi:
    input_data = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    
    # Stwórz na jej podstawie listę (tablicę), której elementy są obiektami utworzonej na poprzednich zajęciach klasy.
    # Przykładowo może to być instrukcja:
    # [Elem(key, value) for key, value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    elements1 = [Element(key, value) for key, value in input_data]
    
    # Przekaż tak utworzoną tablicę jako parametr konstruktora przy tworzeniu kopca.
    heap = Heap(elements1)

    # Wypisz utworzony kopiec jako tablicę i jako drzewo 2D
    heap.print_tab()
    print()
    heap.print_tree(0, 0)
    print()
    
    # a następnie, po rozebraniu kopca, wypisz posortowaną tablicę (tą którą kopiec dostał jako argument przy jego tworzeniu)
    while not heap.is_empty():
        heap.dequeue()
    print(elements1)
    print("Algorytm jest niestabilny.\n")

    # TEST 2 - ALGORYTM 1
    # Wygeneruj losowo 10000 liczb w przedziale od 0 do 99 i wpisz je do tablicy
    random_numbers1 = [random.randint(0, 99) for _ in range(10000)]

    t_start1 = time.perf_counter()
    # Posortuj tę tablicę przez stworzenie i rozebranie kopca
    heap = Heap(random_numbers1)
    while not heap.is_empty():
        heap.dequeue()
    t_stop1 = time.perf_counter()

    # Wypisz czas sortowania takiej tablicy
    print("Czas obliczeń:", "{:.7f}".format(t_stop1 - t_start1),"\n")


    # TEST 1 - ALGORYTM 2 - SWAPSORT
    # stwórz  tablicę elementów i posortuj ją
    elements2 = [Element(key, value) for key, value in input_data]
    SelectionSort.swap_sort(elements2)
    print(elements2)
    print("Algorytm jest niestabilny.\n")
    
    # TEST 2 - ALGORYTM 2 - SWAPSORT
    #  Wygeneruj losowo 10000 liczb w przedziale od 0 do 99, którymi wypełnisz tablicę
    random_numbers2 = [random.randint(0, 99) for _ in range(10000)]

    t_start2 = time.perf_counter()
    SelectionSort.swap_sort(random_numbers2)
    t_stop2 = time.perf_counter()

    # Wypisz czasy sortowania takiej tablicy
    print("Czas obliczeń:", "{:.7f}".format(t_stop2 - t_start2),"\n")

    # TEST 1 - ALGORYTM 2 - SHIFTSORT
    elements3 = [Element(key, value) for key, value in input_data]
    SelectionSort.shift_sort(elements3)
    print(elements3)
    print("Algorytm jest stabilny.\n")


    # TEST 2 - ALGORYTM 2 - SHIFTSORT
    #  Wygeneruj losowo 10000 liczb w przedziale od 0 do 99, którymi wypełnisz tablicę
    random_numbers3 = [random.randint(0, 99) for _ in range(10000)]

    t_start3 = time.perf_counter()
    SelectionSort.shift_sort(random_numbers3)
    t_stop3 = time.perf_counter()

    # Wypisz czasy sortowania takiej tablicy
    print("Czas obliczeń:", "{:.7f}".format(t_stop3 - t_start3),"\n")

if __name__ == '__main__':
    main()