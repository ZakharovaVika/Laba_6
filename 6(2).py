"""Ограничение: максимальная сумма элементов массива не должна превышать некоторое число .
Целевая функция: вывести массив с максимальной  суммой элементов , не превышая данное ограничение."""
import itertools
import copy
from random import randint
n=5
arr=[0]*n
for i in range (n):
    arr[i]=randint(-100, 0)
def array_variants(arr, max_sum):
    # Максимальная сумма не может быть меньше суммы положительных элементов
    if max_sum < sum(x for x in arr if x > 0):
        raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")

    variants = []
    negative_indices = [i for i in range(1, len(arr), 2) if arr[i] < 0]

    for i in range(len(negative_indices) + 1):
        for combination in itertools.combinations(negative_indices, i):
            variant = copy.deepcopy(arr)
            for index in combination:
                variant[index] = abs(variant[index])
            print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")  # выводим каждый вариант перед проверкой
            # Проверка на соответствие максимальной сумме
            if sum(variant) <= max_sum:
                variants.append(variant)

    # Находим вариант с максимальной суммой элементов
    best_variant = max(variants[::-1], key=sum)
    return best_variant

max_sum = 10

# Получаем лучший вариант, удовлетворяющий ограничению
best_variant = array_variants(arr, max_sum)

# Выводим лучший вариант
print(best_variant)

