# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def userdata(name, surname, year, town, email, phone):
    return " ".join([name, surname, year, town, email, phone])  # используем функцию .join с сепаратором пробела.


print(userdata(name="Max", surname="Asimov", year="1951", town="khb", email="blabla@ya.ru", phone="1231341"))
