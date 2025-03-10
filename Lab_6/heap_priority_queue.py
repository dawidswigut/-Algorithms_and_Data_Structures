# SKOŃCZONE

class Element:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f"{self.__priority} : {self.__data}"

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def is_empty(self):
        return self.heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def enqueue(self, element: Element):
        if self.heap_size == len(self.heap):
            self.heap.append(element)
        elif self.heap_size < len(self.heap):
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
        self.heap[0] = self.heap[self.heap_size - 1]
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
        print(*self.heap[:self.heap_size], sep = ', ', end = ' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:           
            self.print_tree(self.right(idx), lvl + 1)
            print(2*lvl*'  ', self.heap[idx] if self.heap[idx] else None)           
            self.print_tree(self.left(idx), lvl + 1)

def main():

    # utworzenie pustej kolejki
    pq = PriorityQueue()

    # użycie w pętli enqueue do wpisana do niej elementów których priorytety będą brane
    # z listy [7, 5, 1, 2, 5, 3, 4, 8, 9], a odpowiadające im wartości będą kolejnymi
    # literami z napisu "GRYMOTYLA"
    data = "GRYMOTYLA"
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    for d, p in zip(data, priorities):
        pq.enqueue(Element(d, p))

    # wypisanie aktualnego stanu kolejki w postaci kopca
    pq.print_tree(0, 0)
    print()

    # wypisanie aktualnego stanu kolejki w postaci tablicy
    pq.print_tab()
    print()

    # użycie dequeue do odczytu  pierwszej  danej z kolejki, proszę ją zapamiętać
    first_removed = pq.dequeue()
    #print(first_removed)

    # użycie  peek do odczytu i wypisania kolejnej  danej
    print(pq.peek(),'\n')

    # wypisanie aktualnego stanu kolejki w postaci tablicy
    pq.print_tab()
    print()

    # wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    print(first_removed,'\n')

    # opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    while not pq.is_empty():
        print(pq.dequeue())

    # wypisanie opróżnionej kolejki w postaci tablicy (powinno się wypisać { } )
    pq.print_tab()

if __name__ == '__main__':
    main()