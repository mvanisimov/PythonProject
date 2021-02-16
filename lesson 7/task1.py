# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from typing import List


class Matrix:
    # создаем класс Matrix, который принимает матрицу(список списков) в аргументе.
    def __init__(self, matrix: list):
        self._matrix = matrix

    # переопределяем __str__ чтобы при вызове корректно выводилось содержимое матрицы. Используем функцию map,
    # чтобы конвертировать с помощью str каждый ряд в матрице в строку. Используем '\t' для разделения чисел табуляцией,
    # \n для перевода строки
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self._matrix)

    # переопределяем __add__

    def __add__(self, other):  # принимает на вход other - другую матрицу
        result = []  # создаем список, куда будем добавлять результат сложения.
        # используем zip, чтобы создать итератор из парных кортежей для удобной парной итерации.
        # используем sum для суммирования элементов
        for item in zip(self._matrix, other._matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)  # возвращаем объект типа Matrix с аргументом в виде готовой матрицы


# проверяем
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8, 9],
           [10, 11, 12]]

mx_obj1 = Matrix(matrix1)
mx_obj2 = Matrix(matrix2)

result_matrix = mx_obj1 + mx_obj2

print(result_matrix)
