#  Дана строка-предложение на русском языке.
#  Подсчитать количество содержащися в строке знаков препинания.

import string

sentence = input("Введите предложение на русском языке: ")

punctuation_count = sum([1 for char in sentence if char in string.punctuation])

print("Количество знаков препинания в предложении:", punctuation_count)
