# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


products = []
product_number = 1
title, price, amount, unit = None, None, None, None  # обьявляем характеристики
print("Please, fill the product characteristics")
while True:
    # начинаем ввод характеристик
    if title is None:
        title = input("Enter the product name: ")
        continue

    if price is None:
        price = int(input("Enter the product price: "))

        continue

    if amount is None:
        amount = int(input("Enter the product amount: "))

        continue

    if unit is None:
        unit = input("Enter the product unit: ")
        continue

    products.append(
        (product_number,
         {'title': title,
          'price': price,
          'amount': amount,
          'unit': unit}))  # добавляем все элементы в список

    title, price, amount, unit = None, None, None, None  # обнуляем характеристики после добавления в список
    product_number += 1

    print(products)
    q = input(
        "Stop forming product list? y/n :")  # запрашиваем, нужно ли закончить формирование списка( выход из цикла)
    if q.lower() == "y":
        break
    # далее цикл повторяется, если не введено y

    # формирование словаря аналитики
analytics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()}  # создаем словарь аналитики

for i, item in products:  # добавляем в словарь все элементы которые были введены
    analytics['title'].append(item['title'])
    analytics['price'].append(item['price'])
    analytics['amount'].append(item['amount'])
    analytics['unit'].add(item['unit'])

print(analytics)
