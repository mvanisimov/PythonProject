# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

numbers_list = [el for el in range(20, 241) if el % 21 == 0 or el % 20 == 0]

print(numbers_list)
