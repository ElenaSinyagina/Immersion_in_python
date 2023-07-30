# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов 
# методов экземпляра.

import random
import csv
import math
import json

coeff_file = 'Test1.csv'
roots_file = 'Test2.json'

def decorator(funcion):
    def wrapper(self, *args, **kwargs):
        print('__________________________________________')
        return funcion(self, *args, **kwargs)
    return wrapper

class create_coefficient:
    def __int__(self, *args, **kwargs):

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
        obtaining_coefficients().__int__()

class quadratic_equation:

    @decorator
    def __int__(self, *args, **kwargs):

        koef_a, koef_b, koef_c = args
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

        write_To_Files().__int__(koef_a, koef_b, koef_c, discr, x1, x2)
        

class obtaining_coefficients(quadratic_equation):
    def __int__(self, *args, **kwargs):
        with open(roots_file, 'w') as json_file:
            json_file.write('[]')
        with open(coeff_file, encoding='utf-8') as r_file:
            file = csv.reader(r_file, delimiter=",")
            for row in file:
                try:
                    super().__int__(int(row[0]), int(row[1]), int(row[2]))
                except:
                    continue

class write_To_Files:
    def __int__(self, *args, **kwargs):
        result = args
        keys_tuple = ('a', 'b', 'c', 'discr', 'x1', 'x2')
        myDict = dict(zip(keys_tuple, result))
        with open(roots_file, 'r') as file:
            obj = json.load(file)
            obj.append(myDict)
        with open(roots_file, 'w') as file:
            json.dump(obj, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    create_coefficient().__int__()