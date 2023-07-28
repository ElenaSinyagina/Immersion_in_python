# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


from typing import Callable
from functools import wraps
import random
import csv
import math
import json

coeff_file = 'Test1.csv'
roots_file = 'Test2.json'

# def decorator(funcion):
#     def wrapper(self, *args, **kwargs):
#         print('********************************************')
#         return funcion(self, *args, **kwargs)
#     return wrapper

def decor(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        keys_tuple = ('a', 'b', 'c', 'discr', 'x1', 'x2')
        myDict = dict(zip(keys_tuple, result))
        with open(roots_file, 'r') as file:
            obj = json.load(file)
            obj.append(myDict)
        with open(roots_file, 'w') as file:
            json.dump(obj, file, indent=2, ensure_ascii=False)
        return func(self, *args, **kwargs)
    return wrapper

class find_quadratic_equation:
    def csv_file_generation(self):

        list_data = []
        for j in range(100):
            list_data.append({
               'a': random.randint(-50, 50),
               'b': random.randint(-50, 50),
               'c': random.randint(-50, 50),
                })
        with open(coeff_file, 'w', newline='') as f_csv:
            csv_write = csv.DictWriter(f_csv, fieldnames=[*list_data[0]])
            csv_write.writeheader()
            csv_write.writerows(list_data)
        self.obtaining_coefficients()

    @decor
    def quadratic_equation(self, koef_a, koef_b, koef_c):

        discr = koef_b ** 2 - 4 * koef_a * koef_c
        print("Дискриминант D = %.3f" % discr)

        if discr > 0:
            x1 = (-koef_b + math.sqrt(discr)) / (2 * koef_a)
            x2 = (-koef_b - math.sqrt(discr)) / (2 * koef_a)
            print(f"Уравнение {koef_a}x^2 + {koef_b}x + {koef_c} = 0 имеет следующие корни:\nx1 = {x1} \nx2 = {x2}")
        elif discr == 0:
            x1 = -koef_b / (2 * koef_a)
            x2 = None
            print(f"Уравнение {koef_a}x^2 + {koef_b}x + {koef_c} = 0 имеет один корень:\nx1 = {x1}")
        else:
            x1 = None
            x2 = None
            print(f"Уравнение {koef_a}x^2 + {koef_b}x + {koef_c} = 0 не имеет корней")

        return (koef_a, koef_b, koef_c, discr, x1, x2)
        
    def obtaining_coefficients(self):
        with open(roots_file, 'w') as json_file:
            json_file.write('[]')
        with open(coeff_file, encoding='utf-8') as r_file:
            file = csv.reader(r_file, delimiter=",")
            for row in file:
                try:
                    self.quadratic_equation(int(row[0]), int(row[1]), int(row[2]))
                except:
                    continue

    # def write_To_Files(self, list_data):
    #     with open('roots.json', 'w') as f_json:
    #         json.dump(list_data, f_json, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    f_q_e = find_quadratic_equation()
    f_q_e.csv_file_generation()