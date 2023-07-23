from pathlib import Path
import os
import json
import csv
import pickle

def folder_Size(path):
    folder_size = 0
    for file in Path(path).rglob('*'):
        if (os.path.isfile(file)):
            folder_size += os.path.getsize(file)
    return folder_size

def recursive_folder_traversal(path, level = 1):
    for j in (os.listdir(path)):
        file_size = os.path.getsize(path + '\\' + j)
        folder_size = folder_Size(path + '\\' + j)
        path_file_or_folder = path + '\\' + j
        if os.path.isfile(path_file_or_folder):
            list_data.append({
                'type': 'file',
                'name': j,
                'path': path,
                'size': file_size
            })

        else:
            list_data.append({
                'type': 'folder',
                'name': j,
                'path': path,
                'size': folder_size
            })

    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            recursive_folder_traversal(path + '\\' + i, level + 1)


def write_To_Files(list_data):
    with open('test.json', 'w') as f_json:
        json.dump(list_data, f_json, indent=2, ensure_ascii=False)
    with open('test.csv', 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.DictWriter(f_csv, fieldnames=[*list_data[0]])
        csv_write.writeheader()
        csv_write.writerows(list_data)
    with open('test.pickle', 'wb') as f_pickle:
        pickle.dump(list_data, f_pickle)


if __name__ == '__main__':
    path = 'E:\Geekbrains\Immersion_in_python\DZ8'
    list_data = []
    recursive_folder_traversal(path)
    write_To_Files(list_data)