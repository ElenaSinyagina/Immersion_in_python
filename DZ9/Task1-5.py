import json
from functools import wraps
# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

# def add_one():
#     numb = int(input("Введите число от 1 до 100 для загадывания: "))
#     count = int(input("Введите число от 1 до 10 - количество попыток для угадывания: "))
#
#     def add_two():
#         nonlocal count
#         while count > 0:
#             n = int(input("Какое число? "))
#             if n != numb:
#                 count -= 1
#                 continue
#             else:
#                 print("Вы угадали")
#                 break
#
#     return add_two
#
#
# h = add_one()
# h()


# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random
from typing import Callable


def deco1(func: Callable):
    @wraps(func)
    def wrapper(a, b, *arg, **args):
        # if not 1 <= a >= 100:
        #     a = random.randint(1, 100)
        # if not 1 <= b >= 100:
        #     b = random.randint(1, 10)
        # x = random.randint(1, a)
        result = func(a, b)
        return result

    return wrapper


# @deco
# def fuTwo(count,x):
#     while count > 0:
#         number = int(input('введите число ->> '))
#         if number < x:
#             print('Искомое больше ')
#         elif number > x:
#             print('Искомое меньше ')
#         else:
#             print('Bingo!')
#             return count
#         count -= 1
#     return count
#
# if __name__ == "__main__":
#     fuTwo(-100,10)

# Задание №3
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

def deco2(func: Callable):
    @wraps(func)
    def wrapper(a, b, *arg, **args):
        print('Оборачиваемая функция: {}'.format(func))
        fileName = str('{}'.format(func))[1:-1]
        ind1 = str('{}'.format(func))[1:-1].index(' ')
        ind2 = str('{}'.format(func))[1:-1].index(' ', ind1 + 1)
        # print(fileName[ind1+1:ind2])
        fileName = fileName[ind1 + 1:ind2]
        # print(fileName)
        # if not 1 <= a >= 100:
        #     a = random.randint(1, 100)
        # if not 1 <= b >= 100:
        #     b = random.randint(1, 10)
        # x = random.randint(1, a)
        result = func(a, b)
        with open('{}'.format(fileName) + '.json', "a") as file:
            myDict = {}
            myDict['a'] = a
            myDict['b'] = b
            myDict.update(**args)
            json.dump(myDict, file)
        return result

    return wrapper


# @deco1
# def fuTwo(count,x):
#     while count > 0:
#         number = int(input('введите число ->> '))
#         if number < x:
#             print('Искомое больше ')
#         elif number > x:
#             print('Искомое меньше ')
#         else:
#             print('Bingo!')
#             return count
#         count -= 1
#     return count
#
# if __name__=="__main__":
#     fuTwo(10,2, c=5)

# Задание №4. Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
def count(num: int = 1):
    def deco(func: Callable):
        counter = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter

        return wrapper

    return deco


@count(10)
@deco1
@deco2
def rnd(a: int, b: int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    return random.randint(a, b)


print(rnd(1, 5))

help(rnd)
