# NIESKOŃCZONE

# size_tab = 5

# class Element:
#     def __init__(self):
#         self.size = size_tab
#         self.tab = [None for i in range(size_tab)]
#         self.length = len(self.tab)
#         self.next = None


# class UnrolledLinkedList:
#     def __init__(self):
#         pass

# ogolnie chuj wie czy to jest dobrze - chat to zrobił i tyle wiem

class Node:
    def __init__(self):
        self.tab = [None for _ in range(6)]
        self.fill = 0
        self.next = None

# Klasa UnrolledLinkedList reprezentująca listę wiązaną

class UnrolledLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        current = self.head
        while current:
            if index < current.fill:
                return current.tab[index]
            index -= current.fill
            current = current.next
        return None

    def insert(self, index, data):
        if not self.head:
            self.head = Node()
            self.head.tab[0] = data
            self.head.fill = 1
            return

        prev = None
        current = self.head
        while current and index >= current.fill:
            index -= current.fill
            prev = current
            current = current.next

        if not current:
            prev.next = Node()
            current = prev.next

        if current.fill < 6:
            for i in range(current.fill, index, -1):
                current.tab[i] = current.tab[i-1]
            current.tab[index] = data
            current.fill += 1
        else:
            new_node = Node()
            mid = current.fill // 2
            if index > mid:
                for i in range(mid, current.fill):
                    new_node.tab[i-mid] = current.tab[i]
                    current.tab[i] = None
                current.fill = mid
                new_node.fill = mid
                for i in range(index - mid):
                    current.tab[current.fill] = new_node.tab[i]
                    current.fill += 1
            else:
                for i in range(mid, current.fill):
                    new_node.tab[i-mid] = current.tab[i]
                    current.tab[i] = None
                current.fill = mid
                new_node.fill = mid
                for i in range(mid, index, -1):
                    current.tab[i] = current.tab[i-1]
                current.tab[index] = data
                current.fill += 1
                for i in range(mid):
                    current.tab[current.fill] = new_node.tab[i]
                    current.fill += 1
        if prev:
            prev.next = current

    def delete(self, index):
        prev = None
        current = self.head
        while current and index >= current.fill:
            index -= current.fill
            prev = current
            current = current.next

        if not current:
            return

        if current.fill > index:
            data = current.tab[index]
            for i in range(index, current.fill - 1):
                current.tab[i] = current.tab[i+1]
            current.tab[current.fill - 1] = None
            current.fill -= 1
            if current.fill < 3 and current.next:
                if current.next.fill > 3:
                    for i in range(current.fill, 3):
                        current.tab[i] = current.next.tab[i]
                        current.next.tab[i] = None
                    current.fill = 3
                    current.next.fill -= 3
                else:
                    for i in range(current.next.fill):
                        current.tab[current.fill] = current.next.tab[i]
                        current.fill += 1
                        current.next.tab[i] = None
                    current.fill -= current.next.fill
                    current.next = current.next.next
            elif current.fill == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

# Funkcja wypisująca listę

def print_list(llist):
    current = llist.head
    while current:
        print(current.tab[:current.fill], end=" -> ")
        current = current.next
    print("None")

# Testowanie implementacji

def main():
    # Zmienna reprezentująca rozmiar tablicy
    global ARRAY_SIZE
    ARRAY_SIZE = 6

    # Zadanie 2
    # Utworzenie pustej listy
    llist = UnrolledLinkedList()

    # Wpisanie kolejno 9 danych
    for i in range(1, 10):
        llist.insert(i-1, i)

    # Wypisanie elementu listy o indeksie 4
    print(llist.get(4))

    # Wstawienie danych 10 i 11 pod indeksy 1 i 8
    llist.insert(1, 10)
    llist.insert(8, 11)

    # Aktualny stan listy
    print_list(llist)

    # Usunięcie danych spod indeksów 1 i 2
    llist.delete(1)
    llist.delete(2)

    # Aktualny stan listy po usunięciu
    print_list(llist)

if __name__ == "__main__":
    main()