# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month_number = int(input("введите номер месяца: "))

month_list = ['winter', 'spring', 'summer', 'autumn']
month_dict = {1: "winter", 2: 'spring', 3: 'summer', 4: 'autumn'}

if month_number == 12 or month_number == 1 or month_number == 2:
    print(month_list[0])
    print(month_dict.get(1))
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(month_list[1])
    print(month_dict.get(2))
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(month_list[2])
    print(month_dict.get(3))
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(month_list[3])
    print(month_dict.get(4))
else:
    print('this month does not exist')
