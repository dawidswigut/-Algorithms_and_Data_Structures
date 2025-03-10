# SKOŃCZONE

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


def main():
    m1 = Matrix([[1, 0, 2],
                 [-1, 3, 1]])
    
    m2 = Matrix((2, 3), fill_value=1)

    m3 = Matrix([[3, 1],
                 [2, 1],
                 [1, 0]])

    print(transpose(m1))
    print(m1 + m2)
    print(m1 * m3)

if __name__ == "__main__":
    main()