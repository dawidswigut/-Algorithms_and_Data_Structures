# SKOŃCZONE

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data
    
    def __str__(self):
        return f"{self.key}:{self.data}"

class HashTable:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash_function(self, key):
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        key = key % self.size
        return key

    def search(self, key):
        idx = self.hash_function(key)
        i = 0
        while i < self.size:
            if self.tab[idx] is not None and self.tab[idx].key == key:
                return self.tab[idx].data
            i += 1
            idx = self.open_addressing(key, i)
        return None
        
    def insert(self, key, data):
        idx = self.hash_function(key)
        i = 0
        while i < self.size:
            idx = self.open_addressing(key, i)
            if self.tab[idx] is None:
                self.tab[idx] = Element(key, data)
                return
            if self.tab[idx].key is (key):
                self.tab[idx].data = data
                return
            i += 1
        print("Brak miejsca")
        return None

    def open_addressing(self, key, i):
        idx = self.hash_function(key)
        return (idx + self.c1 * i + self.c2 * i**2) % self.size

    def remove(self, key):
        idx = self.hash_function(key)
        i = 0
        while i < self.size:
            
            if self.tab[idx] is not None and self.tab[idx].key is key:
                self.tab[idx] = None
                return
            i += 1
            idx = self.open_addressing(key, i)
        print("Brak danej")
        return None

    def __str__(self):
        elements = ', '.join(str(item) for item in self.tab)
        return "{" + elements + "}"

def functionality_test_1(size, c1=1, c2=0):
    # utworzenie pustej tablicy o rozmiarze 13 i próbkowaniem liniowym
    hash_table = HashTable(size, c1, c2)
    
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14 ,15]
    data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    
    # użycie insert do wpisana do niej 15 danych
    for idx in range(len(keys)):
        hash_table.insert(keys[idx], data[idx])

    # wypisanie tablicy
    print(hash_table)

    # użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(hash_table.search(5))
    
    # użycie search do wyszukania (i wypisania) danej o kluczu 14
    print(hash_table.search(14))
    
    # użycie insert do nadpisania wartości dla klucza 5 wartością 'Z'
    hash_table.insert(5, 'Z')
    
    # użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(hash_table.search(5))
    
    # użycie remove do usunięcia danej o kluczu 5
    hash_table.remove(5)
    
    # wypisanie tablicy
    print(hash_table)
    
    # użycie search do wyszukania (i wypisania) danej o kluczu 31
    print(hash_table.search(31))
    
    # wprowadzenie do tablicy insertem daną o wartości 'W' z kluczem 'test' i wypisanie tablicy
    hash_table.insert('test', 'W')
    print(hash_table)


def functionality_test_2(size, c1=0, c2=1):
    # utworzenie pustej tablicy o rozmiarze 13 i próbkowaniem liniowym
    hash_table = HashTable(size, c1, c2)
    
    data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        hash_table.insert(13 * i, data[i - 1])
    print(hash_table)

def main():
    print()
    # uruchomienie pierwszej funkcji z próbkowniem liniowym
    functionality_test_1(13, 1, 0)
    print("\n")
    
    # uruchomienie drugiej fukcji z próbkowaniem liniowym
    functionality_test_2(13, 1, 0)
    print("\n")
    
    # uruchomienie drugiej funkcji z próbkowaniem KWADRATOWYM
    functionality_test_2(13, 0, 1)
    print("\n")
    
    # uruchomienie pierwszej funkcji z próbkowaniem KWADRATOWYM
    functionality_test_1(13, 0, 1)
    print()

if __name__ == '__main__':
    main()