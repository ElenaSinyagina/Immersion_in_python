# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# doctest,
# unittest,
# pytest.

import calendar

def funcDate(text):
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1] 
    if int(text[0]) <= days and int(text[1])<= 12 :
        print('Нормальная дата')
        return True
    else :
        print('не корректная дата')
        return False


if __name__=='__main__':
    funcDate("01.11.2001")