import polska
class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return repr(self.key)


class NeighbourList:
    def __init__(self):
        self.graph = {}
        self.neighbours_d = {}

    def is_empty(self):
        if self.graph == {}:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = vertex
            self.neighbours_d[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.neighbours_d[vertex1][vertex2] = edge
        self.neighbours_d[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        del self.graph[vertex]
        del self.neighbours_d[vertex]
        for neighbours in self.neighbours_d.values():
            neighbours.pop(vertex, None)

    def delete_edge(self, vertex1, vertex2):
        del self.neighbours_d[vertex1][vertex2]
        del self.neighbours_d[vertex2][vertex1]

    def get_vertex_id(self, vertex):
        return vertex

    def get_vertex(self, vertex_id):
        return self.graph.get(vertex_id)

    def neighbours(self, vertex_id):
        return self.neighbours_d.get(vertex_id, {}).items()

    def vertices(self):
        return self.graph.keys()

class NeighbourMatrix:
    def __init__(self, init_v=0):
        self.graph = []
        self.neighbours = []
        self.init_v = init_v

    def __str__(self):
        out = ""
        for i in self.graph:
            out = str(i) + ", "
        return out[:-2]

    def is_empty(self):
        if self.graph is []:
            return True
        else:
            return False

    def get_vertex(self, vertex_id):
        return self.graph[vertex_id]

    def get_vertex_id(self, vertex):
        ind = 0
        for elem in self.graph:
            if elem == vertex:
                return ind
            else:
                ind += 1

    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.append(vertex)
            size = len(self.graph)
            for row in self.neighbours:
                row.append(self.init_v)
            self.neighbours.append([self.init_v] * size)

    def insert_edge(self, vertex1, vertex2, edge=1):
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)

        self.neighbours[id1][id2] = edge
        self.neighbours[id2][id1] = edge

    def delete_vertex(self, vertex):
        idx = self.get_vertex_id(vertex)
        if idx is not None:
            del self.graph[idx]
            for row in self.neighbours:
                del row[idx]
            del self.neighbours[idx]

    def delete_edge(self, vertex1, vertex2):
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)

        if id1 is not None and id2 is not None:
            self.neighbours[id1][id2] = 0
            self.neighbours[id2][id1] = 0

    def neighbours(self, vertex_id, edge=1):
        out = []
        for index in range (len(self.graph)):
            elem = self.graph[vertex_id][index]
            if elem == edge:
                out.append((index, elem))
        return out

    def vertices(self):
        out = []
        for i in range(len(self.graph)):
            out.append(i)
        return out


def main():
    edges = polska.graf
    pol = polska.polska
    vertices = []
    for i in edges:
        if Node(i[0]) not in vertices:
            vertices.append(Node(i[0]))
        if Node(i[1]) not in vertices:
            vertices.append(Node(i[1]))


    list = NeighbourList()
    matrix = NeighbourMatrix()
    for vertex in vertices:
        list.insert_vertex(vertex)
        matrix.insert_vertex(vertex)


    for edge in edges:
        n1 = Node(edge[0])
        n2 = Node(edge[1])
        list.insert_edge(n1, n2)
        matrix.insert_edge(n1, n2)

    list.delete_vertex(Node('K'))
    matrix.delete_vertex(Node('K'))
    list.delete_edge(Node('W'), Node('E'))
    matrix.delete_edge(Node('W'), Node('E'))

    pol = [(e[2], e[2]) for e in pol if Node(e[2]) in list.vertices()]

    polska.draw_map(list, pol)
    polska.draw_map(matrix, pol)


main()