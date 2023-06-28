# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex 
# используйте для проверки своего результата.

num = int(input("Введите число: "))

print("Проверка hex(): ", hex(num))

str = ''
digits = '0123456789ABCDEF'
 
while num > 0:
    str = digits[num % 16] + str
    num = num // 16
 
# print("Результат вычислений: ", str)


# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

numerator1 = int(input("Введите числитель первой дроби "))
denominator1 = int(input("Введите знаменатель первой дроби "))
numerator2 = int(input("Введите числитель второй дроби "))
denominator2 = int(input("Введите знаменатель второй дроби "))

if denominator1 == denominator2:
    number1 = numerator1 + numerator2 # Числитель дроби в результате сложения
    number2 = denominator1 # Знаменатель дроби в результате сложения
else:
    number1 = (numerator1 * denominator2) + (numerator2 * denominator1) # Числитель дроби в результате сложения
    number2 = denominator1 * denominator2 # Знаменатель дроби в результате сложения

print(f'Сумма {number1}/{number2}')
print(f'Произведение {numerator1 * numerator2}/{denominator1 * denominator2}')

firstfraction = fractions.Fraction(numerator1, denominator1)
secondfraction = fractions.Fraction(numerator2, denominator2)
result1 = firstfraction + secondfraction
result2 = firstfraction * secondfraction

print(f'Проверка результатов: сумма {result1}, произведение {result2}')