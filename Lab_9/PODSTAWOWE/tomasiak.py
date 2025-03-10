#skonczone
import graf_mst

class Vertex:
    def __init__(self, value, color = 0):
        self.value = value
        self._color = color

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value is other.value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, val):
        self._color = val

class Graph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge = None):
        try:
            self.list[vertex1][vertex2] = edge
        except KeyError:
            self.list[vertex1] = {}
            self.list[vertex1][vertex2] = edge
        try:
            self.list[vertex2][vertex1] = edge
        except KeyError:
            self.list[vertex2] = {}
            self.list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        try:
            self.list.pop(vertex)
            for i in self.vertices():
                try:
                    self.list[i].pop(vertex)
                except KeyError:
                    pass
        except KeyError:
           pass

    def delete_edge(self, vertex1, vertex2):
        try:
            self.list[vertex1].pop(vertex2)
        except KeyError:
            pass
        try:
            self.list[vertex2].pop(vertex1)
        except KeyError:
            pass

    def neighbours(self, vertex_id):
        return self.list[vertex_id].items()
    
    def vertices(self):
        return self.list.keys()

    def get_vertex(self, vertex_id):
        return vertex_id
        
    def get_vertex_id(self, value):
        return value


def prim(graph: Graph):
    mst = Graph()

    intree = {}
    distance = {}
    parent = {}

    for i in graph.vertices():
        intree[i] = 0
        distance[i] = float('inf')
        parent[i] = None
        mst.insert_vertex(i)

    v = list(graph.vertices())[1]
    sum = 0
    while intree[v] == 0:
        intree[v] = 1
        
        for i in graph.neighbours(v):
            if i[1] < distance[i[0]] and intree[i[0]] == 0:
                distance[i[0]] = i[1]
                parent[i[0]] = v
        
        min_distance = float('inf')

        for i in graph.vertices():
            if distance[i] < min_distance and intree[i] == 0:
                min_distance = distance[i]
                v = i

        mst.insert_edge(v, parent[v], distance[v])
        sum += distance[v]
    sum -= distance[v]
    return mst, sum

def printGraph(g: Graph):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

graph = Graph()
for i in graf_mst.graf:
    graph.insert_edge(Vertex(i[0]), Vertex(i[1]), i[2])
mst, sum = prim(graph)
printGraph(mst)
