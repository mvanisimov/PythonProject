# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

from json import dumps  # импортируем dumps

company_list = []  # обьявляем лист для сохранения данных
total_profit = 0  # обьявляем переменную для расчета общей прибыли
i = 0  # обьявляем счетчик прибыльных компаний для расчета средней прибыли
with open("task7.txt", encoding="utf-8") as tsk:  # открываем файл
    for line in tsk:
        name, state, proceeds, costs = line.split()  # через .split разбиваем, считываем строку, сохраняем в переменные
        profit = int(proceeds) - int(costs)  # считаем прибыль
        if profit >= 0:  # исключаем убыточные компании, считаем общую прибыль
            total_profit += profit
            i += 1

        company_list.append({name: profit})  # добавляем вначале по шаблому компании и их прибыль\убыток

    avg_profit = int(total_profit / i)  # затем рассчитываем и добавляем среднюю прибыль
    company_list.append({"average_profit": avg_profit})

with open("task7.json", "w", encoding="utf-8") as tskj:  # записываем в json
    tskj.write(dumps(company_list))
