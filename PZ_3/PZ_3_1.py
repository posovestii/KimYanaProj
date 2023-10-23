# Даны три целых числа A, B, C
# Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное.»
A = input("Введите число A: ")
while type(A) != int:  # обработка исключений
    try:
        A = int(A)
    except ValueError:
        print("Вы ввели неправильно!")
        A = input("Введите число A: ")

B = input("Введите число B: ")
while type(B) != int:  # обработка исключений
    try:
        B = int(B)
    except ValueError:
        print("Вы ввели неправильно!")
        B = input("Введите число B: ")

C = input("Введите число C: ")
while type(C) != int:   # обработка исключений
    try:
        C = int(C)
    except ValueError:
        print("Вы ввели неправильно!")
        C = input("Введите число C: ")

count_positive = 0
if A > 0:
    count_positive += 1
if B > 0:
    count_positive += 1
if C > 0:
    count_positive += 1
if count_positive == 1:
    print("Высказывание истинно")
else:
    print("Высказывание ложно")

