# SKOŃCZONE

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
        
class Matrix:
    def __init__(self, size, fill_value = 0):
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
            result = Matrix(result)
            return result
        else:
            raise Exception("Nieprawidłowe wymiary macierzy!")

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
            result = Matrix(result)
            return result
        else:
            raise Exception("Nieprawidłowe wymiary macierzy!")
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __str__(self):
        output = ""
        for i in range(self.size()[0]):
            output += " | "
            for j in range(self.size()[1]):
                output += str(self.matrix[i][j]) + " "
            output += "|\n"
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

def is_isomorphism(M, P, G):
    MT = M.transpose()
    P_m = Matrix(P.list)
    G_m = Matrix(G.list)
    product = M * (G_m * MT)
    return product == P_m

def create_M0(P, G):
    rows = len(P.values)
    columns = len(G.values)
    M0 = Matrix((rows, columns), 0)
    for i in range(rows):
        for j in range(columns):
            if len(P.neighbours(i)) <= len(G.neighbours(j)):
                M0.matrix[i][j] = 1
    return M0

def ullmann_v1(using, current_row, matrix_M, P, G, correct_isomorphism, iterations):
    iterations[0] += 1
    if current_row == len(matrix_M.matrix):
        if is_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    
    for c in range(len(matrix_M.matrix[0])):
        if not using[c]:
            using[c] = True
            for row in range(len(matrix_M.matrix[current_row])):
                matrix_M.matrix[current_row][row] = 0
            matrix_M.matrix[current_row][c] = 1
            ullmann_v1(using, current_row + 1, matrix_M, P, G, correct_isomorphism, iterations)
            using[c] = False

def ullmann_v2(using, current_row, matrix_M, P, G, correct_isomorphism, iterations):
    iterations[0] += 1
    if current_row == len(matrix_M.matrix):
        if is_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    
    M_copy = matrix_M.deepcopy()
    for c in range(len(matrix_M.matrix[0])):
        if not using[c] and matrix_M.matrix[current_row][c] != 0:
            using[c] = True
            for row in range(len(matrix_M.matrix[current_row])):
                M_copy.matrix[current_row][row] = 0
            M_copy.matrix[current_row][c] = 1
            ullmann_v2(using, current_row + 1, M_copy, P, G, correct_isomorphism, iterations)
            using[c] = False

def prune(M, P, G):
    swap = True
    while swap:
        swap = False
        for i in range(len(M.matrix)):
            for j in range(len(M.matrix[0])):
                if M.matrix[i][j] == 1:
                    neighbours_P = P.neighbours(i)
                    neighbours_G = G.neighbours(j)
                    if not all(any(M.matrix[x][y] == 1 for y, _ in neighbours_G) for x, _ in neighbours_P):
                        M.matrix[i][j] = 0
                        swap = True

def ullmann_v3(using, current_row, matrix_M, P, G, correct_isomorphism, iterations):
    iterations[0] += 1
    if current_row == len(matrix_M.matrix):
        if is_isomorphism(matrix_M, P, G):
            correct_isomorphism.append(matrix_M.deepcopy())
        return
    
    M_copy = matrix_M.deepcopy()
    prune(M_copy, P, G)
    for c in range(len(matrix_M.matrix[0])):
        if not using[c] and matrix_M.matrix[current_row][c] != 0:
            using[c] = True
            for row in range(len(matrix_M.matrix[current_row])):
                M_copy.matrix[current_row][row] = 0
            M_copy.matrix[current_row][c] = 1
            ullmann_v3(using, current_row + 1, M_copy, P, G, correct_isomorphism, iterations)
            using[c] = False

def main():
    graph_G = [('A','B',1),
               ('B','F',1),
               ('B','C',1),
               ('C','D',1),
               ('C','E',1),
               ('D','E',1)]
    
    graph_P = [('A','B',1),
               ('B','C',1),
               ('A','C',1)]
        
    G = NeighborhoodMatrix()
    P = NeighborhoodMatrix()

    for u, v, w in graph_G:
        G.insert_edge(Vertex(u), Vertex(v), w)

    for u, v, w in graph_P:
        P.insert_edge(Vertex(u), Vertex(v), w)

    # Version 1.0
    iterations_v1 = [0]
    correct_isomorphism_v1 = []
    M = Matrix((len(P.values), len(G.values)), 0)
    ullmann_v1([False] * len(G.values), 0, M, P, G, correct_isomorphism_v1, iterations_v1)
    print(len(correct_isomorphism_v1), iterations_v1[0])

    # Version 2.0
    iterations_v2 = [0]
    correct_isomorphism_v2 = []
    M0 = create_M0(P, G)
    ullmann_v2([False] * len(G.values), 0, M0, P, G, correct_isomorphism_v2, iterations_v2)
    print(len(correct_isomorphism_v2), iterations_v2[0])

    # Version 3.0
    iterations_v3 = [0]
    correct_isomorphism_v3 = []
    M0_v3 = create_M0(P, G)
    ullmann_v3([False] * len(G.values), 0, M0_v3, P, G, correct_isomorphism_v3, iterations_v3)
    print(len(correct_isomorphism_v3), iterations_v3[0])

if __name__ == '__main__':
    main()
