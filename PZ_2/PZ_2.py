# ввод трехзначного числа и вывод его средней и последней цифры
while True:  # обработка исключений
    try:
        num = int(input("Введите трехзначное число: "))
        if num <= 99 or num >= 1000:
            print("Ошибка! Вы ввели не трехзначное число!")
            continue
        break
    except ValueError:
        print("Вы ввели не число!")
last_digit = num % 10
second_digit = num//10 % 10
print("Последняя цифра:", last_digit)
print("Средняя цифра:", second_digit)
