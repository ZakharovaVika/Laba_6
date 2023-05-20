"""Вариант 4. Дан одномерный массив. Сформировать все возможные варианты данного массива путем замены отрицательных элементов на нечетных местах модулями."""
import itertools
from random import randint
n=10
arr=[0]*n
for i in range (n):
    arr[i]=randint(-100, 0)


# Функция-генератор, которая возвращает все возможные варианты массива, заменяя отрицательные числа на нечетных позициях их модулями
def array_variants(arr):
    negative_indices = [i for i in range(1, len(arr), 2) if arr[i] < 0]

    for i in range(len(negative_indices) + 1):
        for combination in itertools.combinations(negative_indices, i):
            for index in combination:
                arr[index] = abs(arr[index])
            yield arr[:]  # yield генерирует каждый вариант по очереди
            for index in combination:
                arr[index] = -abs(arr[index])  # возвращаем массив к исходному состоянию



# Получаем все возможные варианты
variants = array_variants(arr)

# Выводим варианты
for variant in variants:
    print(variant)
