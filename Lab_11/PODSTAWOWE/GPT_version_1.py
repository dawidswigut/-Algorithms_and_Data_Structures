import itertools

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __str__(self):
        return str(self.key)

class NeighborhoodMatrix:
    def __init__(self, default_value=0):
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

    def insert_edge(self, vertex1, vertex2, edge=1):
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

class Matrix:
    def __init__(self, size, fill_value=0):
        if isinstance(size, tuple):
            rows, columns = size
            self.matrix = []
            for _ in range(rows):
                row = [fill_value] * columns
                self.matrix.append(row)
        else:
            self.matrix = size

    def __add__(self, other):
        if self.size() == other.size():
            rows, columns = self.size()
            result = []
            for _ in range(rows):
                row = [0] * columns
                result.append(row)
            for i in range(rows):
                for j in range(columns):
                    result[i][j] = self.matrix[i][j] + other[i][j]
            return Matrix(result)
        else:
            raise Exception("Matrix dimensions do not match!")

    def __mul__(self, other):
        if self.size()[1] == other.size()[0]:
            rows1, columns1 = self.size()
            rows2, columns2 = other.size()
            result = []
            for _ in range(rows1):
                row = [0] * columns2
                result.append(row)
            for i in range(rows1):
                for j in range(columns2):
                    for k in range(rows2):
                        result[i][j] += self.matrix[i][k] * other[k][j]
            return Matrix(result)
        else:
            raise Exception("Matrix dimensions do not match!")
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __str__(self):
        output = ""
        for row in self.matrix:
            output += " | " + " ".join(map(str, row)) + " |\n"
        return output

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def transpose(self):
        rows, columns = self.size()
        result = []
        for _ in range(columns):
            row = [0] * rows
            result.append(row)
        for i in range(rows):
            for j in range(columns):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)

    def __eq__(self, other):
        return self.matrix == other.matrix

    def deepcopy(self):
        return Matrix([row[:] for row in self.matrix])

def sprawdz_izomorfizm(M, P, G):
    MT = M.transpose()
    P_m = Matrix(P.list)
    G_m = Matrix(G.list)
    product = M * (G_m * MT)
    return product == P_m

def create_M0(P, G):
    rows = len(P.values)
    cols = len(G.values)
    M0 = Matrix((rows, cols), 0)
    for i in range(rows):
        for j in range(cols):
            if len(P.neighbours(i)) <= len(G.neighbours(j)):
                M0.matrix[i][j] = 1
    return M0

def ullmann(uzywane, aktualny_wiersz, macierz_M, P, G, poprawne_izomorfizmy, wywolania):
    wywolania[0] += 1
    if aktualny_wiersz == len(macierz_M.matrix):
        # Sprawdzenie izomorfizmu
        if sprawdz_izomorfizm(macierz_M, P, G):
            poprawne_izomorfizmy.append(macierz_M.deepcopy())
        return
    
    for c in range(len(macierz_M.matrix[0])):
        if not uzywane[c]:
            uzywane[c] = True
            for row in range(len(macierz_M.matrix[aktualny_wiersz])):
                macierz_M.matrix[aktualny_wiersz][row] = 0
            macierz_M.matrix[aktualny_wiersz][c] = 1
            ullmann(uzywane, aktualny_wiersz + 1, macierz_M, P, G, poprawne_izomorfizmy, wywolania)
            uzywane[c] = False


def ullmann_v2(uzywane, aktualny_wiersz, macierz_M, P, G, poprawne_izomorfizmy, wywolania):
    wywolania[0] += 1
    if aktualny_wiersz == len(macierz_M.matrix):
        if sprawdz_izomorfizm(macierz_M, P, G):
            poprawne_izomorfizmy.append(macierz_M.deepcopy())
        return
    
    M_kopia = macierz_M.deepcopy()
    for c in range(len(macierz_M.matrix[0])):
        if not uzywane[c] and macierz_M.matrix[aktualny_wiersz][c] != 0:
            uzywane[c] = True
            for row in range(len(macierz_M.matrix[aktualny_wiersz])):
                M_kopia.matrix[aktualny_wiersz][row] = 0
            M_kopia.matrix[aktualny_wiersz][c] = 1
            ullmann_v2(uzywane, aktualny_wiersz + 1, M_kopia, P, G, poprawne_izomorfizmy, wywolania)
            uzywane[c] = False



def prune(M, P, G):
    zmiana = True
    while zmiana:
        zmiana = False
        for i in range(len(M.matrix)):
            for j in range(len(M.matrix[0])):
                if M.matrix[i][j] == 1:
                    neighbours_P = P.neighbours(i)
                    neighbours_G = G.neighbours(j)
                    if not all(any(M.matrix[x][y] == 1 for y, _ in neighbours_G) for x, _ in neighbours_P):
                        M.matrix[i][j] = 0
                        zmiana = True

def ullmann_v3(uzywane, aktualny_wiersz, macierz_M, P, G, poprawne_izomorfizmy, wywolania):
    wywolania[0] += 1
    if aktualny_wiersz == len(macierz_M.matrix):
        if sprawdz_izomorfizm(macierz_M, P, G):
            poprawne_izomorfizmy.append(macierz_M.deepcopy())
        return
    
    M_kopia = macierz_M.deepcopy()
    prune(M_kopia, P, G)
    for c in range(len(macierz_M.matrix[0])):
        if not uzywane[c] and macierz_M.matrix[aktualny_wiersz][c] != 0:
            uzywane[c] = True
            for row in range(len(macierz_M.matrix[aktualny_wiersz])):
                M_kopia.matrix[aktualny_wiersz][row] = 0
            M_kopia.matrix[aktualny_wiersz][c] = 1
            ullmann_v3(uzywane, aktualny_wiersz + 1, M_kopia, P, G, poprawne_izomorfizmy, wywolania)
            uzywane[c] = False

graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

G = NeighborhoodMatrix()
P = NeighborhoodMatrix()

for u, v, w in graph_G:
    G.insert_edge(Vertex(u), Vertex(v), w)

for u, v, w in graph_P:
    P.insert_edge(Vertex(u), Vertex(v), w)

# Version 1.0
wywolania_1 = [0]
poprawne_izomorfizmy_1 = []
M = Matrix((len(P.values), len(G.values)), 0)
ullmann([False] * len(G.values), 0, M, P, G, poprawne_izomorfizmy_1, wywolania_1)
print(f"Wersja 1.0: Liczba izomorfizmów: {len(poprawne_izomorfizmy_1)}, Liczba wywołań rekurencyjnych: {wywolania_1[0]}")

# Version 2.0
wywolania_2 = [0]
poprawne_izomorfizmy_2 = []
M0 = create_M0(P, G)
ullmann_v2([False] * len(G.values), 0, M0, P, G, poprawne_izomorfizmy_2, wywolania_2)
print(f"Wersja 2.0: Liczba izomorfizmów: {len(poprawne_izomorfizmy_2)}, Liczba wywołań rekurencyjnych: {wywolania_2[0]}")

# Version 3.0
wywolania_3 = [0]
poprawne_izomorfizmy_3 = []
M0_v3 = create_M0(P, G)
ullmann_v3([False] * len(G.values), 0, M0_v3, P, G, poprawne_izomorfizmy_3, wywolania_3)
print(f"Wersja 3.0: Liczba izomorfizmów: {len(poprawne_izomorfizmy_3)}, Liczba wywołań rekurencyjnych: {wywolania_3[0]}")
