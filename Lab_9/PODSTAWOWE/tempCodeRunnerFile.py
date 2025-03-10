def prim(graph: Graph):
#     mst = Graph()

#     intree = {vertex: 0 for vertex in graph.vertices()}
#     distance = {vertex: float('inf') for vertex in graph.vertices()}
#     parent = {vertex: None for vertex in graph.vertices()}

#     # Inicjalizacja zmiennych dla pierwszego wierzchołka
#     start_vertex = next(iter(graph.vertices()))
#     distance[start_vertex] = 0

#     # Inicjalizacja zmiennej dla sumy wag krawędzi w MST
#     total_weight = 0

#     # Pętla wykonująca się, dopóki istnieją wierzchołki spoza drzewa MST
#     while not all(intree[vertex] for vertex in graph.vertices()):
#         # Znalezienie wierzchołka spoza drzewa o najmniejszej odległości
#         current_vertex = min((vertex for vertex in graph.vertices() if not intree[vertex]), key=lambda x: distance[x])
#         intree[current_vertex] = 1

#         # Dodanie bieżącego wierzchołka do drzewa MST
#         mst.insert_vertex(current_vertex)

#         # Dodanie krawędzi do drzewa MST, jeśli istnieje parent
#         if parent[current_vertex] is not None:
#             mst.insert_edge(current_vertex, parent[current_vertex], distance[current_vertex])
#             total_weight += distance[current_vertex]

#         # Przeglądanie sąsiadów bieżącego wierzchołka
#         for neighbour, weight in graph.neighbours(current_vertex):
#             # Aktualizacja odległości dla sąsiadów, jeśli jest mniejsza
#             if weight < distance[neighbour] and not intree[neighbour]:
#                 distance[neighbour] = weight
#                 parent[neighbour] = current_vertex

#     return mst