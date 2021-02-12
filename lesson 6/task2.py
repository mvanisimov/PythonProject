# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, length: float, width: float):  # конструктор для переменных
        self._length = length
        self._width = width

    # метод для расчета массы асфальта по формуле. Принимает переменные толщины асфальта и
    # масса асфальта для покрытия одного кв метра дороги асфальтом
    def total_asphalt_mass(self, asphalt_thickness: float, sqm_asphalt_mass: float):
        asphalt_mass = self._length * self._width * asphalt_thickness * sqm_asphalt_mass
        print(f"Масса асфальта для покрытия этой дороги: {asphalt_mass / 1000} тонн")


rally_road = Road(5000, 20)
rally_road.total_asphalt_mass(0.05, 25)
