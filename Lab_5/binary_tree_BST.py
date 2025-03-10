# SKOŃCZONE

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.search_recurrent(self.root, key)
    
    def search_recurrent(self, node, key):
        if node is None or node.key == key:
            return node.data if node else None
        elif key < node.key:
            return self.search_recurrent(node.left_child, key)
        elif key > node.key:
            return self.search_recurrent(node.right_child, key)

    def insert(self, key, data):
        self.root = self.insert_recurrent(self.root, key, data)
    
    def insert_recurrent(self, node, key, data):
        if node is None:
            return Node(key, data)
        elif key < node.key:
            node.left_child = self.insert_recurrent(node.left_child, key, data)
            return node
        elif key > node.key:
            node.right_child = self.insert_recurrent(node.right_child, key, data)
            return node
        else:
            node.data = data
            return node
        
    def delete(self, key):
        self.root = self.delete_recurrent(self.root, key)

    def delete_recurrent(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left_child = self.delete_recurrent(node.left_child, key)
        elif key > node.key:
            node.right_child = self.delete_recurrent(node.right_child, key)
        else:
            # Case 1: usunięcie węzła, który nie posiada węzłów dzieci (child nodes
            if node.left_child is None and node.right_child is None:
                return None
            # Case 2: usunięcie węzła z jednym dzieckiem
            elif node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            # Case 3: usunięcie węzła, który posiada dwa węzły dzieci - 
            #         usuwany węzeł zastępujemy minimalnym kluczem z prawego 
            #         poddrzewa (ang. right subtree) - successor node
            else:
                successor_parent = node
                successor = node.right_child
                while successor.left_child is not None:
                    successor_parent = successor
                    successor = successor.left_child

                node.key = successor.key
                node.data = successor.data

                if successor_parent == node:
                    node.right_child = self.delete_recurrent(node.right_child, successor.key)
                else:
                    successor_parent.left_child = self.delete_recurrent(successor, successor.key)
        return node
    
    def print(self):
        if self.root is not None:
            self.print_recurrent(self.root)
            print()

    def print_recurrent(self, node):
        if node is not None:
            self.print_recurrent(node.left_child)
            print(f"{node.key} {node.data}", end=",")
            self.print_recurrent(node.right_child)


    def height(self):
        return self.height_recurrent(self.root)

    def height_recurrent(self, node):
        if node is None:
            return 0
        left_height = self.height_recurrent(node.left_child)
        right_height = self.height_recurrent(node.right_child)
        return 1 + max(left_height, right_height)
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right_child, lvl+5)
            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left_child, lvl+5)

def main():
    # utworzenie pustego drzewa BST
    bst = BinaryTree()

    # dodanie kolejno elementy klucz:wartość -- 
    # {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'},
    # tworząc drzewo o podanej strukturze, jak na rysunku:
    data_dict = {50: 'A',
                 15: 'B',
                 62: 'C',
                 5: 'D',
                 20: 'E',
                 58: 'F',
                 91: 'G',
                 3: 'H',
                 8: 'I',
                 37: 'J',
                 60: 'K',
                 24: 'L'}

    for key, data in data_dict.items():
        bst.insert(key, data)
    
    # wypisz drzewo 2D (funkcją print_tree)
    bst.print_tree()

    # wyświetl zawartość drzewa jako listę elementów ułożonych od najmniejszego 
    # do największego klucza wypisanych w postaci klucz wartość
    bst.print()

    # znajdź klucz 24 i wypisz wartość
    print(bst.search(24))

    #zaktualizuj wartość "AA" dla klucza 20
    bst.insert(20, 'AA')

    # dodaj element 6:M
    bst.insert(6, 'M')
    
    # usuń element o kluczu 62
    bst.delete(62)
    
    # dodaj element 59:N
    bst.insert(59, 'N')
    
    # dodaj element 100:P
    bst.insert(100, 'P')
    
    # usuń element o kluczu 8
    bst.delete(8)
    
    # usuń element o kluczu 15
    bst.delete(15)
    
    # wstaw element 55:R
    bst.insert(55, 'R')
    
    # usuń element o kluczu 50
    bst.delete(50)
    
    # usuń element o kluczu 5
    bst.delete(5)
    
    # usuń element o kluczu 24
    bst.delete(24)
    
    # wypisz wysokość drzewa
    print(bst.height())
    
    # wyświetl zawartość drzewa jako listę elementów
    bst.print()
    
    # wyświetl drzewo 2D
    bst.print_tree()

if __name__ == '__main__':
    main()