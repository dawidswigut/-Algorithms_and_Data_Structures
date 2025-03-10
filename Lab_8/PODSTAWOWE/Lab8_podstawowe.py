# skonczone
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

class ListwaSasiedztwa:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex1 not in self.list:
            self.list[vertex1] = {}
        self.list[vertex1][vertex2] = edge

        if vertex2 not in self.list:
            self.list[vertex2] = {}
        self.list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.list:
            self.list.pop(vertex)
            for i in self.vertices():
                if vertex in self.list[i]:
                    self.list[i].pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.list and vertex2 in self.list[vertex1]:
            self.list[vertex1].pop(vertex2)

        if vertex2 in self.list and vertex1 in self.list[vertex2]:
            self.list[vertex2].pop(vertex1)

    def neighbours(self, vertex_id):
        return self.list[vertex_id].items()

    def vertices(self):
        return self.list.keys()

    def get_vertex(self, vertex_id):
        return vertex_id

class MacierzSasiedztwa:
    def __init__(self, default_val=0):
        self.default_val = default_val
        self.list = []
        self.values = []

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        for i in self.list:
            i.append(self.default_val)

        self.list.append([self.default_val for _ in range(len(self.list) + 1)])
        self.values.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge=1):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)

        if id_1 is None:
            self.insert_vertex(vertex1)
            id_1 = len(self.values) - 1

        if id_2 is None:
            self.insert_vertex(vertex2)
            id_2 = len(self.values) - 1
        self.list[id_1][id_2] = edge
        self.list[id_2][id_1] = edge

    def delete_vertex(self, vertex):
        id = self.get_vertex_id(vertex)

        if id is not None:
            self.list.pop(id)
            for i in self.vertices():
                self.list[i].pop(id)
            self.values.pop(id)

    def delete_edge(self, vertex1, vertex2):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)
        if id_1 is not None and id_2 is not None:
            self.list[id_1][id_2] = self.default_val
            self.list[id_2][id_1] = self.default_val

    def neighbours(self, vertex_id):
        result = []
        for i in range(len(self.values)):
            if self.list[vertex_id][i] != self.default_val:
                result.append((i, self.list[vertex_id][i]))
        return result

    def vertices(self):
        return [i for i in range(len(self.values) - 1)]

    def get_vertex(self, vertex_id):
        return self.values[vertex_id]

    def get_vertex_id(self, index):
        id = 0
        for i in self.values:
            if i == index:
                return id
            id += 1
        return None


def graph_testing(przykladowy_graf):
    for i in polska.graf:
        przykladowy_graf.insert_edge(Vertex(i[0]), Vertex(i[1]))

    przykladowy_graf.delete_edge(Vertex('W'), Vertex('E'))
    przykladowy_graf.delete_vertex(Vertex('K'))
    polska.draw_map(przykladowy_graf)

def main():
    macierz = MacierzSasiedztwa()
    lista = ListwaSasiedztwa()
    graph_testing(macierz)
    graph_testing(lista)

if __name__ == "__main__":
    main()