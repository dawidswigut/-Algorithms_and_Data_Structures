# SKOŃCZONE

import graf_mst

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

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    graph = Graph()

    for edge in graf_mst.graf:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])
        graph.insert_edge(vertex1, vertex2, edge[2])

    mst = prim(graph)
    printGraph(mst)
if __name__ == '__main__':
    main()