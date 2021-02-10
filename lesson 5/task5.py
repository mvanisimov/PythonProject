# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

digits = "1 2 6 3 10 6 12 23 65"  # создаем набор чисел
summ = 0
with open("task5.txt", "w", encoding="utf-8") as tsk5:  # записываем числа в файл

    tsk5.write(digits)

with open("task5.txt", "r", encoding="utf-8") as tsk5:  # открываем файл и читаем числа
    input_digits = tsk5.read()

    for item in input_digits.split():  # вычисляем сумму
        summ += int(item)

print(summ)
