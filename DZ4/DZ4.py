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


# Возьмите задачу о банкомате из семинара 2. Разбейте её 
# на отдельные операции — функции. Дополнительно сохраняйте 
# все операции поступления и снятия средств в список.

BANKTAX = 0.015
BANKTAXMIN = 30
BANKTAXMAX = 600
BANKPERCENT = 1.03
COUNTRYTAX = 0.1
RICH = 5000000


logDict = {}

def menu():
    print()
    print(f'Вывести остаток на счете, нажмите : 1')
    print(f'Снять со счета, нажмите : 2')
    print(f'Внести на счет, нажмите : 3')
    print(f'История операций : 4')
    print()
    print(f'Для выхода нажмите 0')
    print()


def log(logDict, bool, opCount, cash):
    if bool : logDict[opCount] = f'на счет внесено {cash}'
    else : logDict[opCount] = f'снято со счета {cash}'
    return logDict


def putIn(money, opCount):
    while True :
        if opCount % 3 == 0: money = money * BANKPERCENT
        print(f'Сумма для внесения должна быть кратна 50')
        moneyIn = int(input('Введите сумму: '))
        if moneyIn%50 != 0 :
            print(f'Введите сумму кратную 50 ')
            continue
        elif moneyIn % 50 == 0 :
            money = money + moneyIn
            opCount +=1
            break
    log(logDict, True, opCount, moneyIn)
    return money, opCount


def takeOut(money, opCount):
    printInvoice(money)
    while True:
        if money > RICH :
            money = money - (money + money * COUNTRYTAX)
        print(f'Сколько хотите снять со счета? ')
        outMoney = float(input('Введите сумму для снятия: '))
        if outMoney > money:
            print(f'{printInvoice(money)}, введите сумму корректно')
            continue
        if BANKTAXMAX > (outMoney * BANKTAX) > BANKTAXMIN:
            money = money - (outMoney + outMoney * BANKTAX)
            break
        elif BANKTAXMIN > outMoney * BANKTAX:
            money = money - (outMoney + BANKTAXMIN)
            if money < 0 :
                print(f'Превышен лимит счета, введите заново')
                continue
            break
        else:
            money = money - outMoney - BANKTAXMAX
            if money < 0 :
                print(f'Превышен лимит счета, введите заново')
                continue
            break
    opCount +=1
    log(logDict, False, opCount, outMoney)
    return money, opCount


def printLog(logDict):
    for k,v in logDict.items():
        print (k, v)


def printInvoice(money):
    print(f'На Вашем счету - {round(money, 2)} y.e.')
money = 0
opCount = 0
while True:
    menu()
    button = input('Выберите пункт меню: ')
    if button == '1' : printInvoice(money)
    elif button == '2' : money, opCount = takeOut(money, opCount)
    elif button == '3' : money, opCount = putIn(money, opCount)
    elif button == '4' : printLog(logDict)
    elif button == '0' : break
    else: print(f'Ошибка, повторите ввод')