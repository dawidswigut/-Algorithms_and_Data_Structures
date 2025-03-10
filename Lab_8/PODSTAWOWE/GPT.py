import polska

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)


class Graph:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return len(self.graph) == 0

    def insert_vertex(self, vertex):
        self.graph[vertex] = {}

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for v in self.vertices():
                if vertex in self.graph[v]:
                    self.graph[v].pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].pop(vertex2)

        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].pop(vertex1)

    def neighbours(self, vertex):
        return self.graph[vertex].items()

    def vertices(self):
        return self.graph.keys()

    def get_vertex(self, vertex):
        return vertex

class MatrixGraph(Graph):
    def __init__(self, default_val=0):
        super().__init__()
        self.default_val = default_val

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.graph:
            self.insert_vertex(vertex1)
        if vertex2 not in self.graph:
            self.insert_vertex(vertex2)

        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge

class ListGraph(Graph):
    def __init__(self):
        super().__init__()

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 not in self.graph:
            self.insert_vertex(vertex1)
        if vertex2 not in self.graph:
            self.insert_vertex(vertex2)

        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge

def graph_testing(przykladowy_graf):
    for i in polska.graf:
        przykladowy_graf.insert_edge(Vertex(i[0]), Vertex(i[1]))

    przykladowy_graf.delete_edge(Vertex('W'), Vertex('E'))
    przykladowy_graf.delete_vertex(Vertex('K'))
    polska.draw_map(przykladowy_graf)

def main():
    macierz = MatrixGraph()
    lista = ListGraph()
    graph_testing(macierz)
    graph_testing(lista)

if __name__ == "__main__":
    main()
