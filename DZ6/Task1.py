# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from datetime import datetime
import calendar

def funcDate():
    text = input('Введите дату в формате DD.MM.YYYY ->>> ')
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1]
    if int(text[0]) <= days and int(text[1]) <= 12:
        print('Нормальная дата')
        return True
    else:
        print('не коректная дата')
        return False

def _vysYear(year):
    if calendar.monthrange(year, 2) == 29: return True
    else: return False
    
if __name__=='__main__':
    print(funcDate())