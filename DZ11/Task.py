# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix():
    def __init__(self, data):
        self.data = data

    def size(self):
        size = (len(self.data), len(self.data[0]))
        return size

    def printMtx(self):
        print("\n".join([" ".join(map(str, i)) for i in self.data]))
        print()
   
    def __eq__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            return True
        else: return False

    def __add__(self, other):
        outData = []
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            for i in range(len(self.data)):
                myList = [self.data[i][j]+other.data[i][j] for j in range(len(self.data[i]))]
                outData.append(myList)
            return Matrix(outData)
        else:
            print('Матрицы имеют разные размерности')
            return None

    def __mul__(self, other):
        outData = []
        if (len(self.data) == len(other.data[0])) and (len(self.data[0]) == len(other.data)):
            for i in range(len(self.data)):
                x= []
                for j in range(len(self.data[0])):
                    x.append(self.data[i][j] * other.data[j][i])
                outData.append(x)
            return Matrix(outData)
        else :
            print("Матрицы не согласованы")
            return None



m = Matrix([[1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
            [4, 4, 4]])
m2 = Matrix([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]])
m3 = Matrix([[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
m4 = Matrix([[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]])


print(m4.size())
m.printMtx()
m2.printMtx()

print(m == m2)
x = m+m2
x.printMtx()

m3.printMtx()
print(m == m3)
m4.printMtx()
z = m4*m3
z.printMtx()