# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Cloth(ABC):
    name = ''

    @abstractmethod
    def textile_count(self):
        """"расчет количества ткани"""


class Coat(Cloth):

    def __init__(self, size: int, name: str):
        self.name = name
        self._size = size

    def textile_count(self):
        return self._size / 6.5 + 0.5


class Suit(Cloth):

    def __init__(self, height: int, name: str):
        self.name = name
        self._height = height

    def textile_count(self):
        return 2 * self._height + 0.3


suit = Suit(175, "suit")
print(suit.textile_count())
