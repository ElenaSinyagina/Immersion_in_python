# Задача 1:
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

import random

MAX = 1000
MIN = -1000

def file_with_nums(nums, file):
    for i in range(nums):
        num_int = random.randint(MIN, MAX)
        num_float = random.uniform(MIN, MAX)
        with open(file, 'a', encoding="utf-8") as f:
            f.write(f'{num_int} | {num_float} \n')

if __name__ == '__main__':
    print('Сколько строк с числами необходимо создать в файле?')
    number_lines = int(input('-> '))
    print('Введите имя файла: ')
    file = input('-> ')
    file_with_nums(number_lines, file)
    
    
#Задача 2:
# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# полученные имена сохраните в файл.

import random

def create_random_name():
    length = random.randint(4, 7)
    low_letters = 'абвгдежзийклмнопрстуфхцчшщьэюя'
    up_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЭЮЯ'
    random_name = ''.join(random.sample(up_letters, 1)) + ''.join(random.sample(low_letters, length))
    return random_name

def filling_file_with_names(nums, file):
    for i in range(nums):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(f'{create_random_name()} \n')

if __name__ == '__main__':
    print('Сколько псевдоимен необходимо создать?')
    number_lines = int(input('-> '))
    print('Введите имя файла: ')
    file = input('-> ')
    filling_file_with_names(number_lines, file)
    
    
# Задача3:
# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя,
# записанное строчными буквами и произведение по модулю,
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

from random import randint, choice

DIC1 = "AIEYUO"
DIC2 = "QWRTPSDFHGKL"


def multiply():
    with (
        open('hulu.txt', 'r', encoding='utf-8') as numbers,
        open('hdori.txt', 'r', encoding='utf-8') as liter,
        open('both_files', 'a', encoding='utf-8') as r
    ):
        while res_n := numbers.readline():
            a = res_n.replace(' \n', '').split(" | ")

            if a == ['\n']:
                continue
            print(a)
            mult_ = int(a[0]) * float(a[1])
            res_l = ''
            if mult_ < 0:
                res_l = liter.readline().replace(' \n', '')
                r.write(f'{res_l.lower(), abs(mult_)} \n')
            elif mult_ >= 0:
                r.write(f'{res_l.upper(), round(mult_)} \n')


multiply()


# Задача 4 :
# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from random import *

DIC1 = 'abcdefghijklm'
DIC2 = 'nopqrstuvwxyz'

def function(text, a=5, b=30, c= 7, d=256, n = 42):
    for _ in range(n):
        name = ""
        for i in range(randint(6, 30)):
            name += choice(DIC1)
            if len(name) >= 30: break
            name += choice(DIC2)
        name = name + '.' + text              # формируется название файла
        with open(name, 'w', encoding='utf-8') as new_f:
            g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
            new_f.write(f'{g}')



function("txt", a=5, b=30, c= 7, d=256, n = 42)


# Задача 5:
# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи

from random import *

DIC1 = 'abcdefghijklm'
DIC2 = 'nopqrstuvwxyz'

def function(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):         # формируем файлы в количестве, указанном в словаре для каждого расширения
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function(dic, a=5, b=30, c=7, d=256)


# Задача 6:
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import *

DIC1 = 'abcdefghijklm'
DIC2 = 'nopqrstuvwxyz'

def function(dic, a=5, b=30, c=7, d=256):
    for key in dic:
        for _ in range(dic[key]):
            name = ""
            for i in range(randint(6, 30)):
                name += choice(DIC1)
                if len(name) >= 30: break
                name += choice(DIC2)
            name = name + '.' + key
            if Path(name).is_file():
                continue
            with open(name, 'w', encoding='utf-8') as new_f:
                g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
                new_f.write(f'{g}')


dic = {"txt": 5, "doc": 3}
function(dic, a=5, b=30, c=7, d=256)


def dir(text):    # создание директории
    if isinstance(text, str):
        a = Path(text)  # преобразование в class 'pathlib.WindowsPath'
    else:
        a = text
    if not a.is_dir():
        a.mkdir(parents=True)
    chdir(a)
    function(dic, a=5, b=30, c=7, d=256)


dir('DZ7')


# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import chdir
from pathlib import Path

def sort_file(dict_file_extension, dir_name):
    if isinstance(dir_name, str):
        dir_name = Path(dir_name)
    else:
        dir_name = dir_name
    chdir(dir_name)
    for key in dict_file_extension:
        a = Path(key)
        if not a.is_dir():
            a.mkdir(parents=True)

    p = Path(Path().cwd())
    for obj in p.iterdir():
        for key in dict_file_extension:
            if obj.suffix in dict_file_extension[key]:
                obj.replace(p / key / obj.name)

put = 'E:\Geekbrains\Immersion_in_python\DZ7'
dict_file_extension = {'video': ['.mov', '.avi', '.doc', '.mp4'], 'docum': ['.txt']}
sort_file(dict_file_extension, put)