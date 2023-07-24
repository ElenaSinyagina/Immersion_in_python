# Вспоминаем задачу 3 из прошлого семинара: 
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.

#  Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
#  Имена пишите с большой буквы. 
#  Каждую пару сохраняйте с новой строки.

import json


def toJson():
    myDict = {}
    with open(f"E:\Geekbrains\Immersion_in_python\DZ8\doc1.txt", "r", encoding="utf-8") as nf :
        while res := nf.readline():
            myList = res.replace("\n", "").upper().split(' | ')
            myDict[myList[0]] = myList[1]
        nf.close()
    print(myDict)
    with open(f"E:\Geekbrains\Immersion_in_python\DZ8\doc1.json", 'w', encoding="utf-8") as f:
        result = json.dumps(myDict, indent=2, separators=(',', ':'), sort_keys=True)
        f.write(result)
        f.close()

toJson()