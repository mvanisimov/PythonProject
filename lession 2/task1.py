# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

list_of_types = [None, 12, 534.1, "some text", True, {"a", "b", 2, 3}, (3, 2, 5, 1), {"dict1": 1, "dict2": 2}]

for i in list_of_types:
    print(f'{i} is {type(i)}')
