# SKOŃCZONE

class LinkedList:
    
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None
    
    def add(self, node):
        new_first_node = Node(node)
        new_first_node.next = self.head
        self.head = new_first_node

    def append(self, node):
        new_last_node = Node(node)
        if self.head is None:
            self.head = new_last_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_last_node

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            previous = None
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

    def is_empty(self):
        return self.head is None

    def length(self):
        length = 0
        if self.head is None:
            return length
        else:
            iteration = self.head
            length = 1
            while iteration.next is not None:
                length += 1
                iteration = iteration.next
            return length

    def get(self):
        if self.is_empty():
            raise ("Lista jest pusta!!!")
        else:
            return self.head.data
    
    def __str__(self):
        string = "\n-> "
        elem = self.head
        while elem is not None:
            string += str(elem.data)
            elem = elem.next
            if elem is not None:
                string += ",\n-> "
        return string + "\n"

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    universities = [('AGH', 'Kraków', 1919),
                    ('UJ', 'Kraków', 1364),
                    ('PW', 'Warszawa', 1915),
                    ('UW', 'Warszawa', 1915),
                    ('UP', 'Poznań', 1919),
                    ('PG', 'Gdańsk', 1945)]
    
    #1 utwórz listę wiązaną (nazwijmy ją uczelnie) z pierwszych 3 uczelni używając dodawania na koniec
    uczelnie = LinkedList()
    for university in universities[:3]:
        uczelnie.append(university)

    #2 dołącz do listy wiązanej kolejne uczelnie używając dodawania na początek listy
    for university in universities[-3:]:
        uczelnie.add(university)

    #3 wypisz listę
    print(uczelnie)
    
    #4 wypisz długość listy
    print(uczelnie.length())
    
    #5 usuń z listy pierwszy element
    uczelnie.remove()
    
    #6 wypisz pierwszy element z listy (ten po usuniętym poprzednio)
    print(uczelnie.get())
    
    #7 usuń z listy ostatni element
    uczelnie.remove_end()
    
    #8 wypisz listę
    print(uczelnie)
    
    #9 usuń całą listę uczelnie metodą destroy i wypisz wynik is_empty dla usuniętej listy
    uczelnie.destroy()
    print(uczelnie.is_empty())

    #10 wywołaj usuwanie pierwszego elementu z listy (na pustej liście)
    uczelnie.remove()

    #11 dodaj ponownie AGH do listy używając dodawania na koniec
    uczelnie.append(universities[0])

    #12 wywołaj usuwanie ostatniego elementu z listy
    uczelnie.remove_end()
    
    #13 wypisz wynik is_empty
    print(uczelnie.is_empty())

if __name__ == "__main__":
    main()