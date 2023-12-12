#  Дан список размера N.
#  Осуществить циклический сдвиг элементов списка влево на одну позицию.

import random


def shift(listarr):
    n = len(listarr)
    i = 0
    while i < n-1:
        listarr[i], listarr[i+1] = listarr[i+1], listarr[i]
        i += 1
    return listarr


N = input("Введите размер списка: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")

arr = [random.randint(1, 100) for _ in range(N)]

print("Исходный список:", arr)
arr = shift(arr)
print("Список после циклического сдвига влево:", arr)
