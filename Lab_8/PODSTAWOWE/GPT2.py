import polska

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return self.key


class AdjacencyMatrixGraph:
    def __init__(self, init_value=0):
        self.vertices = []
        #self.num_vertices = len(vertices)
        self.matrix = [[init_value] * self.num_vertices for _ in range(len(self.vertices))]

    def is_empty(self):
        return self.num_vertices == 0

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            #self.num_vertices += 1
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.vertices))

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.vertices.index(vertex1)
        idx2 = self.vertices.index(vertex2)
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.vertices:
            idx = self.vertices.index(vertex)
            del self.vertices[idx]
            #self.num_vertices -= 1
            del self.matrix[idx]
            for row in self.matrix:
                del row[idx]

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.vertices.index(vertex1)
        idx2 = self.vertices.index(vertex2)
        self.matrix[idx1][idx2] = 0
        self.matrix[idx2][idx1] = 0

    def neighbours(self, vertex_id):
        idx = self.vertices.index(vertex_id)
        for i, edge in enumerate(self.matrix[idx]):
            if edge != 0:
                yield self.vertices[i], edge

    def vertices(self):
        return self.vertices

    def get_vertex(self, vertex_id):
        return vertex_id


class AdjacencyListGraph:
    def __init__(self):
        self.vertices = {}

    def is_empty(self):
        return len(self.vertices) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = edge
            self.vertices[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    del self.vertices[v][vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                del self.vertices[vertex1][vertex2]
            if vertex1 in self.vertices[vertex2]:
                del self.vertices[vertex2][vertex1]

    def neighbours(self, vertex_id):
        if vertex_id in self.vertices:
            for neighbour, edge in self.vertices[vertex_id].items():
                yield neighbour, edge

    def vertices(self):
        return self.vertices.keys()

    def get_vertex(self, vertex_id):
        return vertex_id


# def build_graph(graph_class, edges):
#     graph = graph_class()
#     for edge in edges:
#         graph.insert_vertex(Vertex(edge[0]))
#         graph.insert_vertex(Vertex(edge[1]))
#         graph.insert_edge(Vertex(edge[0]), Vertex(edge[1]))
#     return graph


# if __name__ == "__main__":
#     import polska

#     adjacency_matrix_graph = build_graph(AdjacencyMatrixGraph, polska.graf)
#     adjacency_list_graph = build_graph(AdjacencyListGraph, polska.graf)

#     adjacency_matrix_graph.delete_vertex(Vertex('M'))
#     adjacency_matrix_graph.delete_edge(Vertex('M'), Vertex('L'))

#     adjacency_list_graph.delete_vertex(Vertex('M'))
#     adjacency_list_graph.delete_edge(Vertex('M'), Vertex('L'))

#     polska.draw_map(adjacency_matrix_graph)
#     polska.draw_map(adjacency_list_graph)

def graph_testing(przykladowy_graf):
    for i in polska.graf:
        przykladowy_graf.insert_edge(Vertex(i[0]), Vertex(i[1]))

    przykladowy_graf.delete_edge(Vertex('W'), Vertex('E'))
    przykladowy_graf.delete_vertex(Vertex('K'))
    polska.draw_map(przykladowy_graf)

def main():
    macierz = AdjacencyMatrixGraph()
    lista = AdjacencyListGraph()
    graph_testing(macierz)
    graph_testing(lista)

if __name__ == "__main__":
    main()