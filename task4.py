# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

number = int(input("Введите целое положительное число:"))
temp = number % 10  # берем последнюю цифру числа
number = number // 10  # берем оставшуюся часть числа

while number > 0:  # сравниваем в цикле temp и последнюю цифру в оставшейся части числа.
    if number % 10 > temp:  # если последняя цифра оставшейся части числа больше, то записываем ее.
        temp = number % 10

    number = number // 10

print("Самая большая цифра в числе:", temp)
