# Дан прямоугольник, длины сторон которого равны натуральным числам A и B.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать данный прямоугольник
# если от него каждый раз отрезать квадрат наибольшей площади.

def search_for_squares(a, b):
    squares = 0
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
        squares += 1
    return squares


A = input("Введите длину стороны A: ")
while type(A) != int or A <= 0:
    try:
        A = int(A)
        if A <= 0:
            raise ValueError
    except ValueError:
        print("Вы ввели неверно или число не является натуральным!")
        A = input("Введите длину стороны A: ")

B = int(input("Введите длину стороны B: "))
while type(B) != int or B <= 0:
    try:
        B = int(B)
        if B <= 0:
            raise ValueError
    except ValueError:
        print("Вы ввели неверно или число не является натуральным!")
        B = input("Введите длину стороны B: ")
result = search_for_squares(A, B)
print("Количество квадратов в прямоугольнике: ", result)