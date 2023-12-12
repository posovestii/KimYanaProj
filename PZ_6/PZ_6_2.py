# Дан целочисленный список размера N, все элементы которого упорядочены (по возр или убыв)
# Найти количество различных элементов в данном списке.

import random


def unique(listarr):
    n = len(a)
    i = 1
    count = 1
    while i < n:
        if a[i] != a[i-1]:
            count += 1
        i += 1
    return count


N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")

a = [random.randint(1, 10) for _ in range(N)]
print("Исходный список:", a)
a.sort()
print("Список после сортировки:", a)
print("Количество уникальных элементов:", unique(a))
