import cv2
import numpy as np
import graf_mst
import matplotlib as plt

class Vertex:
    def __init__(self, value, color=0):
        self.value = value
        self.color = color

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value

    def __str__(self):
        return str(self.value)
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

class Graph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.list:
            return
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge = None):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.list[vertex1][vertex2] = edge
        self.list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.list:
            del self.list[vertex]
            for vertices in self.list.values():
                vertices.pop(vertex, None)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.list and vertex2 in self.list:
            self.list[vertex1].pop(vertex2, None)
            self.list[vertex2].pop(vertex1, None)

    def neighbours(self, vertexidx):
        return self.list[vertexidx].items()

    def vertices(self):
        return self.list.keys()

    def get_vertex(self, vertexidx):
        return vertexidx

    def get_vertex_id(self, value):
        for vertex in self.list:
            if vertex.value == value:
                return vertex

def prim(graph: Graph):
    mst = Graph()

    intree = {vertex: 0 for vertex in graph.vertices()}
    distance = {vertex: float('inf') for vertex in graph.vertices()}
    parent = {vertex: None for vertex in graph.vertices()}

    v = next(iter(graph.vertices()))
    tree_length = 0

    while intree[v] == 0:
        intree[v] = 1

        for neighbour, weight in graph.neighbours(v):
            if weight < distance[neighbour] and not intree[neighbour]:
                distance[neighbour] = weight
                parent[neighbour] = v

        unprocessed_vertices = [v for v in graph.vertices() if intree[v] == 0]
        if unprocessed_vertices:
            v = min(unprocessed_vertices, key = lambda x: distance[x])

            if parent[v] is not None:
                mst.insert_edge(v, parent[v], distance[v])
                tree_length += distance[v]
        else:
            break

    return mst

def visualize_segmentation(image, mst, removed_edge):
    XX, YY = image.shape[1], image.shape[0]
    IS = np.zeros((YY,XX), dtype='uint8')

    # Przechodzenie po obu drzewach
    for tree in [mst, removed_edge]:
        stack = [next(iter(tree.vertices()))]  # Rozpocznij od korzenia
        while stack:
            vertex = stack.pop()
            vertex_id = vertex.value
            y, x = divmod(vertex_id, XX)  # Oblicz współrzędne piksela
            IS[y, x] = 100 if tree is mst else 200  # Ustaw kolor w zależności od drzewa
            for neighbour, _ in tree.neighbours(vertex):
                if neighbour.get_color() == 0:  # Jeśli sąsiad nie był odwiedzony
                    neighbour.set_color(1)
                    stack.append(neighbour)

    plt.imshow("Segmented Image", IS)
    #cv2.waitKey(0)

def main():
    # Wczytaj obraz
    image = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Nie udało się wczytać obrazu.")
        return

    # Stwórz graf na podstawie obrazu
    graph = Graph()
    height, width = image.shape
    for y in range(height):
        for x in range(width):
            vertex = Vertex(y * width + x)
            graph.insert_vertex(vertex)
            # Dodaj krawędzie do sąsiadów
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if 0 <= y + dy < height and 0 <= x + dx < width and (dy != 0 or dx != 0):
                        neighbour_vertex = Vertex((y + dy) * width + (x + dx))
                        graph.insert_edge(vertex, neighbour_vertex, abs(int(image[y, x]) - int(image[y + dy, x + dx])))

    # Wykonaj algorytm Prima
    mst = prim(graph)

    # Znajdź i usuń krawędź o najwyższej wadze
    max_weight = -1
    max_edge = None
    for v1 in mst.vertices():
        for v2, weight in mst.neighbours(v1):
            if weight > max_weight:
                max_weight = weight
                max_edge = (v1, v2)
    if max_edge:
        mst.delete_edge(max_edge[0], max_edge[1])

    # Wizualizuj segmentację
    visualize_segmentation(image, mst, Graph())  # Drugi argument to drzewo MST, trzeci - puste drzewo dla usuniętej krawędzi

if __name__ == '__main__':
    main()
