num = int(input("Введите трехзначное число: "))
last_digit = num % 10
second_digit = num//10 % 10
print("Последняя цифра:", last_digit)
print("Средняя цифра:", second_digit)