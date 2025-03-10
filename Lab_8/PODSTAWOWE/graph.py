# SKOŃCZONE
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

class NeighborhoodList:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.list:
            return 
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge = None):
        if vertex1 not in self.list:
            self.insert_vertex(vertex1)
        if vertex2 not in self.list:
            self.insert_vertex(vertex2)

        self.list[vertex1][vertex2] = edge
        self.list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        for node in self.list:
            self.delete_edge(node, vertex)
        self.list.pop(vertex, None)

    def delete_edge(self, vertex1, vertex2):
        self.list[vertex1].pop(vertex2, None)
        self.list[vertex2].pop(vertex1, None)

    def neighbours(self, vertexidx):
        return self.list[vertexidx].items()

    def vertices(self):
        return self.list.keys()

    def get_vertex(self, vertexidx):
        return vertexidx

class NeighborhoodMatrix:
    def __init__(self, default_value = 0):
        self.list = []
        self.values = []
        self.default_value = default_value

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.values:
            return
        self.values.append(vertex)
        for row in self.list:
            row.append(self.default_value)
        self.list.append([self.default_value] * len(self.values))

    def insert_edge(self, vertex1, vertex2, edge = 1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)

        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
        
        self.list[idx1][idx2] = edge
        self.list[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.get_vertex_id(vertex)
        if idx is not None:
            self.list.pop(idx)
            for row in self.list:
                row.pop(idx)
            self.values.pop(idx)

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
        if idx1 is not None and idx2 is not None:
            self.list[idx1][idx2] = self.default_value
            self.list[idx2][idx1] = self.default_value

    def neighbours(self, vertexidx):
        result = []
        for idx, value in enumerate(self.list[vertexidx]):
            if value != self.default_value:
                result.append((idx, value))
        return result

    def vertices(self):
        return range(len(self.values))

    def get_vertex(self, vertexidx):
        return self.values[vertexidx]

    def get_vertex_id(self, idx):
        try:
            return self.values.index(idx)
        except ValueError:
            return None

def test(method):
    edges = polska.graf
    poland = polska.polska
    vertices = []
    for i in edges:
        if Vertex(i[0]) not in vertices:
            vertices.append(Vertex(i[0]))
        if Vertex(i[1]) not in vertices:
            vertices.append(Vertex(i[1]))

    for vertex in vertices:
        method.insert_vertex(vertex)

    for edge in edges:
        n1 = Vertex(edge[0])
        n2 = Vertex(edge[1])
        method.insert_edge(n1, n2)
        
    method.delete_vertex(Vertex('K'))
    method.delete_edge(Vertex('W'), Vertex('E'))

    poland = [(city[2], city[2]) for city in poland if Vertex(city[2]) in method.vertices()]

    polska.draw_map(method, poland)

def main():
    list = NeighborhoodList()
    test(list)
    matrix = NeighborhoodMatrix()
    test(matrix)

if __name__ == "__main__":
    main()