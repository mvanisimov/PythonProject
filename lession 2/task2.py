# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

testlist = [1, 3, 7, 4, 2, 6, 5, 4]

# поскольку мы выполняем попарную замену, берем длину списка /2 для итераций. Если список нечетный, то тип int округлит
# float до значения без точки, то есть последний элемент списка не задействован
j = 0
for i in range(int(len(testlist) / 2)):
    testlist[j], testlist[j + 1] = testlist[j + 1], testlist[j]  # меняем местами элементы
    j += 2  # переходим к следующей паре

print(testlist)
print(int(len(testlist) / 2))