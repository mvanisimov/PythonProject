# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

SUBJECTS = {}

with open("task6.txt", encoding="utf-8") as tsk:
    lines = tsk.readlines()  # считываем строки с файла
    # заменяем скобку "(" рядом с числом на пробел, чтобы корректно разделить строку функцией .split, и разделяем.
    for line in lines:
        tmp = line.replace('(', ' ').split()

        # записываем в словарь в ключ имя предмета[0] без двоеточия[:-1], и записываем в значение сумму чисел.
        SUBJECTS[tmp[0][:-1]] = sum(
            int(i) for i in tmp if i.isdigit())  # проверяем символы, если это число, то прибавляем к сумме.

print(SUBJECTS)

# проще решить через регулярные выражения, но мы их пока не проходили :)