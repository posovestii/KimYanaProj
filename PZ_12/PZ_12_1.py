# В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов

import random

n = 10
num = [random.randint(-100, 100) for _ in range(n)]
max_positive = max(filter(lambda x: x > 0, num), default=None)
min_negative = min(filter(lambda x: x < 0, num), default=None)

prod = 1
for elem in num:
    prod *= elem

print("Последовательность чисел:", num)
print("Максимальное положительное число:", max_positive)
print("Минимальное отрицательное число:", min_negative)
print("Произведение всех элементов:", prod)
