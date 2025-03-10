# SKOŃCZONE

class Queue:
    def __init__(self):
        self.size = 5
        self.tab = [None for i in range(5)]
        self.write_idx = 0
        self.read_idx = 0

    def is_empty(self):
        return self.write_idx == self.read_idx
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read_idx]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.tab[self.read_idx]
            self.read_idx = (self.read_idx + 1) % self.size
            return data

    def enqueue(self, data):
        self.tab[self.write_idx] = data
        self.write_idx = (self.write_idx + 1) % self.size
        
        if self.write_idx == self.read_idx:
            self.tab = self.realloc(self.tab, self.size * 2)
            idx = self.size + self.read_idx
            self.tab[idx:] = self.tab[self.read_idx : self.size]
            for i in range(self.read_idx, self.size):
                self.tab[i] = None
            self.read_idx = idx
            self.size *= 2
        

    def realloc(self, tab, size):
        oldSize = len(tab)
        return [tab[i] if i < oldSize else None  for i in range(size)]
    
    def get_tab(self):
        return self.tab

    def __str__(self):
        queue_elements = []
        idx = self.read_idx
        while idx != self.write_idx:
            queue_elements.append(self.tab[idx])
            idx = (idx + 1) % self.size
        return "[" + ", ".join(str(element) for element in queue_elements) + "]"

def main():
    # utworzenie pustej kolejki
    queue = Queue()

    # użycie enqueue do wpisana do niej  4 danych - kolejnych liczb od 1 do 4
    for i in range(1,5):
        queue.enqueue(i)

    # użycie dequeue do odczytu pierwszej wpisanej danej i wypisanie jej
    print(queue.dequeue())

    # użycie  peek do odczytu drugiej  wpisanej danej i wypisanie jej
    print(queue.peek())

    # testowe wypisanie aktualnego stanu kolejki (wpisanych danych od początku kolejki (indeks odczytu) do jej końca (indeks zapisu))
    print(queue)

    # użycie enqueue do wpisana do kolejki następnych 4 danych - kolejnych liczb od 5 do 8
    for i in range(5,9):
        queue.enqueue(i)

    # testowe wypisanie aktualnego stanu tablicy (czyli wewnętrznej reprezentacji)
    print(queue.get_tab())

    # opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    while(not queue.is_empty()):
        print(queue.dequeue())

    # wypisanie kolejki (powinna być pusta)
    print(queue)

if __name__ == '__main__':
    main()