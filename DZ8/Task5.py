#  Напишите функцию, которая 
#    📌 ищет json файлы в указанной директории
#    📌 сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle

def search_jsonfiles():
    file = 'doc5.json'
    with open(f'E:\Geekbrains\Immersion_in_python\DZ8\doc5.json', 'r', encoding='utf-8') as readers_dir:
        list_direct = json.load(readers_dir)
        readers_dir.close()

    with open(f'E:\Geekbrains\Immersion_in_python\DZ8\doc5.pickle', 'wb') as writes:
        writ_namefile = pickle.dump(writ_namefile, writes)        # в аргументы передать объект и файл
        writes.close()

search_jsonfiles()