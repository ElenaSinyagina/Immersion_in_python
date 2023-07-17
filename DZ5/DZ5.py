# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def File_path(path: str) -> tuple:
    path, name = path.rsplit('\\', 1)
    name, extension = name.split('.')
    return path, name, extension

print()
file_path = r"E:\Geekbrains\Immersion_in_python\text.txt"
print(File_path(file_path))
print()


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь 
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается 
# как ставка умноженная на процент премии

employees = ['Иванов И.И.', 'Петров П.П.', 'Ольгина О.О.', 'Натальина Н.Н.', 'Сидоров С.С.', 'Антонов А.А.']
salary_rate = [30000, 35000, 27000, 32000, 48000, 50000]
premium = ['10.15', '15.25', '22.35', '10.45', '13.55', '21.65']
print({name: rank + (rank * float(prem) / 100) for name, rank, prem
       in zip(employees, salary_rate, premium)})


# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci(n):
    a, b = 0, 1
    while a < n :
        yield a
        a, b = b, a + b

print(list(fibonacci(int(input('Введите число: ')))))