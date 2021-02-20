# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class Nulldivision:

    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:

            return divider / denominator

        except:

            return "Division by null is not acceptable"


div = Nulldivision(10, 100)
print(Nulldivision.divide_by_null(10, 0))
print(Nulldivision.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
