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
