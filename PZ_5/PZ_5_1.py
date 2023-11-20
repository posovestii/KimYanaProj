# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.

def string_symbol():
    length = input("Введите число символов: ")
    while (type(length) != int) or (length < 0):
        try:
            length = int(length)
            if length < 0:
                raise ValueError
        except ValueError:
            print("Вы ввели неправильно или введенное число меньше 0!")
            length = input("Введите число символов: ")

    string = "*" * length
    print("Ваша строка: ", string)


string_symbol()