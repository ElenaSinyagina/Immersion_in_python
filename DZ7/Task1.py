# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import pathlib

nameOfFile = input('Желаемое имя файла ->> ')
count = input('кол-во цифр в порядковом номере ->> ')
extOld = input('расширение файла ->> ')
extNew = input('новое расширение ->> ')

def numNum(number:int, count:int):
    sNum = '' + str(number)
    for i in range(count):
        sNum = str(0)+sNum
    return sNum

def renameFiles(nameOfFile:str, count:int, extOld:str, extNew:str):
    p = pathlib.Path('DZ7/')
    temp = []
    for i in p.iterdir():
        temp.append(i.name)
    print(temp)
    number = 0
    for i in range(len(temp)):
        name = temp[i].split('.')
        if name[1] == extOld:
            number +=1
            oldName = 'DZ7/'+name[0]+'.'+extOld
            z = pathlib.Path(oldName)
            newName = 'DZ7/'+nameOfFile+ numNum(number, count) + '.' +extNew
            n = pathlib.Path(newName)
            z.rename(n)

path = 'E:/Geekbrains/Immersion_in_python/DZ7/'
nameOfFile ='document'
count = 3
extOld = 'xml'
extNew = 'txt'
renameFiles(nameOfFile, count, extOld, extNew)