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
    

# Напишите функцию принимающую на вход только ключевые параметры 
# и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте 
# его строковое представление.

def Swap_func(**args):
    myDict = {}
    for key, value in args.items():
        if value.__hash__ == None:
            value = str(value)
        myDict[value] = key
    return myDict

print(Swap_func(a = 15, b = 'солнце', c = 3.14, d = [1, 2, 3, 4, 5], e = {1, 2, 3, 4, 5}, g = (1, 2, 3, 4, 5)))