# Напишите функцию для транспонирования матрицы

def Transposition(matr):
    for i in range(len(matr)):
        for j in range(i, len(matr[i])):
            temp = matr[i][j]
            matr[i][j] = matr[j][i]
            matr[j][i] = temp
    return matr
matr = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3],[4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
for i in matr:
    print(i)
print()
matr = Transposition(matr)
for i in matr:
    print(i)