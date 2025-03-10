# SKOŃCZONE

class Vertex:
    def __init__(self, value, color=0):
        self.value = value
        self.color = color

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)
    
class Edge:
    def __init__(self, capacity, is_residual = False):
        self.capacity = capacity
        self.is_residual = is_residual
        self.flow = 0 if not is_residual else capacity
        self.residual = 0 if is_residual else capacity

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.is_residual}"

class Graph:
    def __init__(self):
        self.list = {}

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.list:
            return
        self.list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, capacity):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.list[vertex1][vertex2] = Edge(capacity)
        self.list[vertex2][vertex1] = Edge(capacity, is_residual = True)

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
        for vertex in self.vertices():
            if vertex.value == vertexidx:
                return vertex

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def BFS(graph, start):
    visited = set()
    parent = {}
    queue = []
    visited.add(start)
    queue.append(start)

    while queue:
        current_vertex = queue.pop(0)

        for neighbor, edge in graph.neighbours(current_vertex):
            if neighbor not in visited and edge.residual > 0:
                visited.add(neighbor)
                parent[neighbor] = current_vertex
                queue.append(neighbor)

    return parent

def find_min_capacity(graph, source, target, parent):
    min_capacity = float('inf')
    current_vertex = target

    if target not in parent:
        return 0

    while current_vertex != source:
        parent_vertex = parent[current_vertex]
        edge = graph.list[parent_vertex][current_vertex]
        min_capacity = min(min_capacity, edge.residual)
        current_vertex = parent_vertex

    return min_capacity

def update_flow(graph, source, target, parent, min_capacity):
    current_vertex = target

    while current_vertex != source:
        parent_vertex = parent[current_vertex]
        edge = graph.list[parent_vertex][current_vertex]

        if not edge.is_residual:
            edge.flow += min_capacity
            edge.residual -= min_capacity
        else:
            edge.flow -= min_capacity
            edge.residual += min_capacity
            
        current_vertex = parent_vertex
    
    return graph

def ford_fulkerson_edmonds_karp(graph, source='s', target='t'):
    max_flow = 0
    
    while True:
        parent = BFS(graph, source)
        
        if target not in parent:
            break

        min_capacity = find_min_capacity(graph, source, target, parent)
        graph = update_flow(graph, source, target, parent, min_capacity)
        max_flow += min_capacity

    return max_flow

def main():
    grafy = [[('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)],
             [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)],
             [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]]

    for idx, graf in enumerate(grafy):
        graph = Graph()
        
        for i in graf:
            vertex1 = Vertex(i[0])
            vertex2 = Vertex(i[1])
            graph.insert_edge(vertex1, vertex2, i[2])

        max_flow = ford_fulkerson_edmonds_karp(graph, graph.get_vertex('s'), graph.get_vertex('t'))
        print(f"Maksymalny przepływ dla grafu {idx}: {max_flow}\n")
        printGraph(graph)
        print()

if __name__ == '__main__':
    main()