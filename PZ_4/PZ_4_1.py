# Дано вещественное число A и целое число N(>0).
# Используя один цикл, найти сумму 1 + A + A^2 + A^3 + ... + A^N.

A = input("Введите вещественное число A: ")
while type(A) != float:  # обработка исключений
    try:
        A = float(A)
    except ValueError:
        print("Вы ввели неправильно!")
        A = input("Введите число A: ")

N = input("Введите целое число N (>0): ")
while (type(N) != int) or (N <= 0):  # обработка исключений
    try:
        N = int(N)
        if N <= 0:
            raise ValueError
    except ValueError:
        print("Вы ввели неправильно!")
        N = input("Введите число N (>0): ")

S = 1
i = 1

while i <= N:
    S += A ** i
    i += 1
print("Сумма равна:", S)
