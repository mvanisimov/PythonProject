# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и
# до n!. Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial  # импортируем функцию факториала из math


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)  # берем факториал


input_number = input("please enter number of factorials: ")
try:  # обрабатываем исключение
    v = int(input_number)
except ValueError:
    print("not a number!")

for el in fact(v):
    print(el)