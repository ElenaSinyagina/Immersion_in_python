# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения 
# внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

import csv
from random import randint
from statistics import mean
import pandas as pd
from csv import writer
import os

class check_input_data:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not(value.isalpha() and value[0].isupper()):
            raise TypeError("Данные должны содержать: только буквы/первая заглавная")
        else:
            setattr(instance, self.name, value)

class students:
    lastname = check_input_data()
    name = check_input_data()
    patronymic = check_input_data()

    def __init__(self, lastname, name, patronymic, *args, **kwargs):
        self.lastname, self.name, self.patronymic = lastname, name, patronymic

    def list_lessons(self):
        with open("lessons.csv", "r", encoding="utf-8") as file:
            lines = csv.DictReader(file)
            list_temp = []
            for line in lines:
                list_temp.append(line["Lesson"])
        return list_temp

    def list_grades(self):
        try:
            os.remove('temp.csv')
        except:
            pass
        temp_list_headlines = ['Предмет', 'Ball', 'AVG_B', 'Test', 'AVG_T']
        with open('temp.csv', 'a', newline='', encoding='utf-8') as file_temp:
            csv_write = csv.DictWriter(file_temp, fieldnames=[*temp_list_headlines])
            csv_write.writeheader()
            writer_object = writer(file_temp)
            for i in self.list_lessons():
                ball = [randint(2, 5) for i in range(1, randint(2, 5))]
                test = [randint(0, 100) for i in range(1, randint(2, 5))]
                temp_list_values = [i, ball, round(mean(ball), 2), test, round(mean(test), 2)]
                writer_object.writerow(temp_list_values)
            file_temp.close()

    def data_print(self):
        print(f'\n{self.lastname} {self.name} {self.patronymic}')
        self.list_grades()
        table = pd.read_csv('temp.csv', delimiter=',')
        print(table)

if __name__ == '__main__':
    try:
        os.remove('lessons.csv')
    except:
        pass

    lesson_list = [{"Lesson": "Алгебра"},
                   {"Lesson": "Физика"},
                   {"Lesson": "Химия"},
                   {"Lesson": "История"},
                   {"Lesson": "Геометрия"}]

    with open("lessons.csv", 'w', newline='', encoding='utf-8') as file:
        csv_write = csv.DictWriter(file, fieldnames=[*lesson_list[0]])
        csv_write.writeheader()
        csv_write.writerows(lesson_list)

    Peoples = (('Петров', 'Петр', 'Петрович'),
               ('Ольгина', 'Ольга', 'Олеговна'),
               ('Сидоров', 'Сидор', 'Сидорович'),
               ('Маринина', 'Марина', 'Михайловна'),
               ('Иванов', 'Иван', 'Иванович'))

    for people in Peoples:
        students(*people).data_print()