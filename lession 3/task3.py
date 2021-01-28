# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(count1, count2, count3):
    count_list = sorted([count1, count2, count3], reverse=True) # сортируем аргументы по возрастанию через sorted()

    summary = count_list[0] + count_list[1]  # вычисляем сумму наибольших двух
    return summary


print(my_func(4, 10, 5))
