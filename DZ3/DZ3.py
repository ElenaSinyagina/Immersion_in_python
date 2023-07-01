# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

import random

def Duplic():
    list_random = []

    for k in range(0, 20):
        list_random.append(random.randint(1, 20))

    print(list_random)

    list_duplic = [x for i, x in enumerate(list_random) if i != list_random.index(x)]

    print(set(list_duplic))

Duplic()

