import copy
import itertools
from random import randint
n=5
arr=[0]*n
for i in range (n):
    arr[i]=randint(-100, 0)
# Функция, которая возвращает все возможные варианты массива, заменяя отрицательные числа на нечетных позициях их модулями
def array_variants(arr):
    variants = []
    negative_indices = [i for i in range(0, len(arr), 2) if arr[i] < 0]

    for i in range(len(negative_indices) + 1):
        for combination in itertools.combinations(negative_indices, i):
            variant = copy.deepcopy(arr)
            for index in combination:
                variant[index] = abs(variant[index])
            variants.append(variant)
    return variants


# Получаем все возможные варианты
variants = array_variants(arr)

# Выводим варианты
for variant in variants:
    print(variant)
