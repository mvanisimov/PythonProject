# 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


NUMERALS_DICT = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"} # создаем словарь для замены
RESULT_LIST = []    # лист для готового блока строк
with open("task4.txt", "r+", encoding="utf-8") as tsk:
    input_lines = tsk.readlines()

    for line in input_lines:
        splitted_line = line.split(" — ")       # разделяем строки
        # если слово совпадает с ключом в словаре, то меняем значение.
        if splitted_line[0] in NUMERALS_DICT:
            word = NUMERALS_DICT[splitted_line[0]]
            number = splitted_line[1]
            RESULT_LIST.append(word + " - " + number)

with open("task4_final.txt", "w", encoding="utf-8") as tsk_final:
    tsk_final.writelines(RESULT_LIST) # добавляем готовый лист в файл
