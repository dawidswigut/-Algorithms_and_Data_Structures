#skonczone
import copy

class Matrix:
    def __init__(self, argument, elements = 0):
        if(isinstance(argument, tuple)):
            self.__matrix = [[elements for i in range(argument[1])] for j in range(argument[0])]
        else:
            self.__matrix = argument

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
    
    def __add__(self, matrix):
        selfRows, selfCols = self.size()[0], self.size()[1]
        if(selfCols == matrix.size()[1] and selfRows == matrix.size()[0]):
            result = [[0 for i in range(selfCols)] for j in range(selfRows)]
            for i in range(selfRows):
                for j in range(selfCols):
                    result[i][j] = self.__matrix[i][j] + matrix[i][j]
            return Matrix(result)
        else:
            return None

    def __mul__(self, matrix):
        selfRows, selfCols = self.size()[0], self.size()[1]
        matrixRows, matrixCols = matrix.size()[0], matrix.size()[1]
        if(selfCols == matrixRows):
            result = [[0 for i in range(matrixCols)] for j in range(selfRows)]
            for i in range(selfRows):
                for j in range(matrixCols):
                    for k in range(matrixRows):
                        result[i][j] += self.__matrix[i][k] * matrix[k][j]
            return Matrix(result)
        else:
            return None

    def __getitem__(self, index):
        return self.__matrix[index]
    
    def __str__(self):
        string = ''
        for i in range(self.size()[0]):
            string += '|'
            for j in range(self.size()[1]):
                if self.__matrix[i][j] < 0:
                    string += str(self.__matrix[i][j])
                    string += ' '
                else:
                    string += ' '
                    string += str(self.__matrix[i][j])
                    string += ' '
            string += '|\n'
        return string
    
    def transpose(self):
        rows, cols = self.size()[0], self.size()[1]
        result = [[0 for i in range(rows)] for j in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = self.__matrix[i][j]
        return Matrix(result)
    
    def __eq__(self, other):
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if self.__matrix[i][j] != other[i][j]:
                    return False
        return True

class Graph:
    def __init__(self, default = 0):
        self.list = []
        self.values = []
        self.default = default

    def is_empty(self):
        return len(self.list) == 0

    def insert_vertex(self, vertex):
        for i in self.list:
            i.append(self.default)
        self.list.append([self.default for i in range(len(self.list) + 1)])
        self.values.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge = 1):
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        if id1 is None:
            self.insert_vertex(vertex1)
            id1 = len(self.values) - 1
        if id2 is None:
            self.insert_vertex(vertex2)
            id2 = len(self.values) - 1
        self.list[id1][id2] = edge
        self.list[id2][id1] = edge

    def get_tab(self):
        return Matrix(self.list)

    def delete_vertex(self, vertex):
        id = self.get_vertex_id(vertex)
        if id is not None:
            self.list.pop(id)
            for i in self.vertices():
                self.list[i].pop(id)
            self.values.pop(id)

    def delete_edge(self, vertex1, vertex2):
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        if id1 is not None and id2 is not None:
            self.list[id1][id2] = self.default
            self.list[id2][id1] = self.default

    def neighbours(self, vertex_id):
        return [(i, self.list[vertex_id][i]) for i in range(len(self.values)) if self.list[vertex_id][i] != self.default]
    
    def vertices(self):
        return [i for i in range(len(self.values) - 1)]

    def get_vertex(self, vertex_id):
        return self.values[vertex_id]
    
    def get_vertex_id(self, value):
        id = 0
        for i in self.values:
            if i == value:
                return id
            id += 1
        return None
        
class Vertex:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
def prune(P: Graph, G: Graph, M: Matrix):
    swapped = True
    while swapped:
        swapped = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    for x in P.neighbours(i):
                        found = False
                        for y in G.neighbours(j):
                            if M[x[0]][y[0]] == 1:
                                found = True
                                break
                        if not found:
                            M[i][j] = 0
                            swapped = True


    
def ullmann(P: Graph, G: Graph, currentRow = 0, M: Matrix = None, using = None, result = 0, iterations = 1):
    if M is None:
        M = Matrix((P.get_tab().size()[0], G.get_tab().size()[0]))
    if using is None:
        using = [False for i in range(M.size()[1])]
    if currentRow == M.size()[0]:
        if P.get_tab() == M * (M * G.get_tab()).transpose():
            result += 1
        return result, iterations
    for i in range(M.size()[1]):
        if using[i] == False:
            using[i] = True
            M[currentRow][:] = [0] * M.size()[1]
            M[currentRow][i] = 1
            result, iterations = ullmann(P, G, currentRow + 1, M, using, result, iterations)
            iterations += 1
            using[i] = False
    return result, iterations

def ullmann2(P: Graph, G: Graph, currentRow = 0, M: Matrix = None, using = None, result = 0, iterations = 0):
    iterations += 1
    if M is None:
        M = Matrix((P.get_tab().size()[0], G.get_tab().size()[0]))
    if using is None:
        using = [False for i in range(M.size()[1])]
    if currentRow == M.size()[0]:
        if P.get_tab() == M * (M * G.get_tab()).transpose():
            result += 1
        return result, iterations
    Mcopy = copy.deepcopy(M)
    for i in range(M.size()[1]):
        if using[i] == False and M[currentRow][i] != 0:
            using[i] = True
            Mcopy[currentRow][:] = [0] * M.size()[1]
            Mcopy[currentRow][i] = 1
            result, iterations = ullmann2(P, G, currentRow + 1, Mcopy, using, result, iterations)
            using[i] = False
    return result, iterations

def ullmann3(P: Graph, G: Graph, currentRow = 0, M: Matrix = None, using = None, result = 0, iterations = 0):
    iterations += 1
    if M is None:
        M = Matrix((P.get_tab().size()[0], G.get_tab().size()[0]))
    if using is None:
        using = [False for i in range(M.size()[1])]
    if currentRow == M.size()[0]:
        if P.get_tab() == M * (M * G.get_tab()).transpose():
            result += 1
        return result, iterations
    Mcopy = copy.deepcopy(M)
    prune(P, G, Mcopy)
    for i in range(M.size()[1]):
        if using[i] == False and M[currentRow][i] != 0:
            using[i] = True
            Mcopy[currentRow][:] = [0] * M.size()[1]
            Mcopy[currentRow][i] = 1
            result, iterations = ullmann3(P, G, currentRow + 1, Mcopy, using, result, iterations)
            using[i] = False
    return result, iterations

if __name__ == '__main__':
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]
    G = Graph()
    P = Graph()

    for i in graph_G:
        G.insert_edge(i[0], i[1], i[2])

    for i in graph_P:
        P.insert_edge(i[0], i[1], i[2])

    M0 = Matrix((P.get_tab().size()[0], G.get_tab().size()[0]))

    for i in range(M0.size()[0]):
        deg_vi = sum(P.get_tab()[i][:])
        for j in range(M0.size()[1]):
            deg_vj = sum(G.get_tab()[j][:])
            if deg_vi <= deg_vj:
                M0[i][j] = 1

    lista, iterations = ullmann(P, G)
    print(lista, iterations)
    lista, iterations = ullmann2(P, G, M=M0)
    print(lista, iterations)
    lista, iterations = ullmann3(P, G, M=M0)
    print(lista, iterations)