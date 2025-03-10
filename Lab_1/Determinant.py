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

def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_by_chio(multiplier, matrix):
    n = matrix.size()[0]

    if matrix.size() == (2, 2):
        return multiplier * determinant_2x2(matrix)
    
    elif matrix[0][0] == 0:
        # for i in range(n + 1):
        #     if matrix[i][0] != 0:
        #         matrix[0][:], matrix[i][:] = matrix[i][:], matrix[0][:]
        #         multiplier = multiplier * (-1)
        #         break
        i = 0
        while i <= n and matrix[i][0] == 0:
            i += 1

        if i <= n:
            matrix[0][:], matrix[i][:] = matrix[i][:], matrix[0][:]
            multiplier = multiplier * (-1)
    
    new_multiplier = multiplier * (1 / (matrix[0][0] ** (n -2)))

    submatrix = [[determinant_2x2(Matrix([[matrix[0][0], matrix[0][j + 1]],
                                          [matrix[i + 1][0], matrix[i + 1][j + 1]]])) for j in range(matrix.size()[0] - 1)] for i in range(n - 1)]
    
    return determinant_by_chio(new_multiplier, Matrix(submatrix))

def transpose(matrix):
    result = []
    for _ in range(matrix.size()[1]):
        row = [0] * matrix.size()[0]
        result.append(row)

    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            result[j][i] = matrix[i][j]
    result = Matrix(result)
    return result

def chio_method(matrix):
    return determinant_by_chio(1, matrix)

def main():
    matrix1 = Matrix([[5, 1, 1, 2, 3],
                      [4, 2, 1, 7, 3],
                      [2, 1, 2, 4, 7],
                      [9, 1, 0, 7, 0],
                      [1, 4, 7, 2, 2]])

    result1 = chio_method(matrix1)
    print("Wyznacznik pierwszej macierzy:", result1)

    matrix2 = Matrix([[0, 1, 1, 2, 3],
                      [4, 2, 1, 7, 3],
                      [2, 1, 2, 4, 7],
                      [9, 1, 0, 7, 0],
                      [1, 4, 7, 2, 2]])

    result2 = chio_method(matrix2)
    print("Wyznacznik drugiej macierzy:", result2)

if __name__ == "__main__":
    main()