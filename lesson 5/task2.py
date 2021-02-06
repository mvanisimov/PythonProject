# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

line_list = ['new line 1', 'new line 2'] # лист строк для добавления

with open("task2.txt", "a", encoding='utf-8') as txt:
    txt.writelines("\n".join(line_list))     # добавляем строки в конец файла из списка

with open("task2.txt", "r", encoding='utf-8') as txt: #подсчитываем
    lines = 0
    words = 0
    for line in txt:
        lines += 1
        for word in line:
            words += 1

    print(f"количество строк: {lines} , количество слов: {words}")
