# Дан список A размера N.
# Вывести его элементы в следующем порядке: A1, AN, A2, AN-1, A3, AN-2,...

import random


def sorting(listarr):
    num = []
    n = len(a)
    i = 0
    while i < n//2:
        num.append(a[i])
        num.append(a[n - i - 1])
        i += 1
    if n % 2 != 0:
        num.append(a[n // 2])
    return num


N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")

a = [random.randint(1, 100) for _ in range(N)]

print("Исходный список:", a)
arr = sorting(a)
print("Список после сортировки:", arr)
