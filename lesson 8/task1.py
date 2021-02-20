# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:

    def __init__(self, data: str):
        self.data = str(data)

    @classmethod
    def extract_data(cls, data):
        date = data.split("-")

        return int(date[0]), int(date[1]), int(date[2])

    def __str__(self):
        return f'Текущая дата {Data.extract_data(self.data)}'

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return 'date is valid'
                else:
                    return 'wrong year'
            else:
                return 'wrong month'
        else:
            return 'wrong day'


today_date = Data("20-02-2021")

print(today_date)
print(Data.validate(11, 10, 2030))
print(today_date.validate(11, 13, 2013))
print(Data.extract_data('12-12-2020'))
print(today_date.extract_data('12-12-2020'))
print(Data.validate(1, 11, 2000))
