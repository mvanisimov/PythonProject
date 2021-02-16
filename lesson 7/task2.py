# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC


# создаем абстрактный класс одежда, в котором будут переменные имени и количества ткани
class Cloth(ABC):
    _name = ''
    _text_count = 0

    # получение и запись переменной name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not type(name) == str:  # проверяем что полученная переменная - строка
            raise ValueError
        self._name = name

    # получение переменной text_count
    @property
    def textile_count(self):
        return self._text_count


# класс пальто
class Coat(Cloth):

    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size
        self._text_count = round(self._size / 6.5 + 0.5)  # рассчитываем и записываем количество ткани


# класс костюм
class Suit(Cloth):

    def __init__(self, name: str, height: float):
        self._name = name
        self._height = height
        self._text_count = round(2 * self._height + 0.3)  # рассчитываем и записываем количество ткани


# считаем общее количество ткани
def total_textile_count(text_count1, text_count2):
    return round(text_count1 + text_count2)


# проверяем
suit = Suit("suit", 1.75)
coat = Coat("coat", 56)

suit_txt_count = suit.textile_count
coat_txt_count = coat.textile_count

total_txt_count = total_textile_count(suit_txt_count, coat_txt_count)

print(f"amount of textile for suit is {suit_txt_count}")
print(f"amount of textile for coat is {coat_txt_count}")
print(f" total amount of textile needed is {total_txt_count}")
