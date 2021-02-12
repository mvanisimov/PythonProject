# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    # создаем базовый класс с конструктором
    def __init__(self, name: str, surname: str, position: str, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}  # защищенный словарь с атрибутами зарплаты и премии


class Position(Worker):  # создаем класс на базе родительского класса Worker

    def get_full_name(self):
        return f"{self.name} {self.surname}"  # метод возвращает строку имени и фамилии

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]  # метод возвращает зарплату сотрудника с учетом бонусов


petya = Position("Petya", "Ivanov", "Manager", 100000, 15000)   # проверяем
print("сотрудник: " + petya.get_full_name())
print(f"работает в должности: {petya.position}")
print(f"его зарплата составила: {petya.get_total_income()}")
