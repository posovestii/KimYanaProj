#  Дана строка.
#  Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.

text = input("Введите строку: ")
latin_count = 0
cyrillic_count = 0

for char in text:
    if char.isalpha():
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            latin_count += 1
        elif 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            cyrillic_count += 1

S = latin_count + cyrillic_count
print("Общее количество латинских букв:", latin_count)
print("Общее количество русских букв:", cyrillic_count)
