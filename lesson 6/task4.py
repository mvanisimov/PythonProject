# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:  # родительский класс car

    def __init__(self, speed: int, color: str, name: str,
                 is_police: bool):  # создаем атрибуты в кострукторе, делаем их защищенными
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
        self._direction = ''

        # создаем методы для управления и контроля авто

    def go(self, speed: int):
        self._speed = speed
        return f"{self._name}  started, accelerating to {self._speed} km/h"

    def stop(self):
        self._speed = 0
        print(f"{self._name} stopped")

    def turn(self, direction: str):
        if direction not in ('left', 'right', 'straight'):
            print("wrong direction!")
            return
        else:
            print(f"{self._name} turns {direction}")

    def show_speed(self):
        print(f"{self._name}`s speed is {self._speed}")

    # создаем дочерние классы


class TownCar(Car):
    __max_permitted_speed = 60  # разрешенная скорость

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(
            self):  # переопределяем родительский метод. Если скорость больше 60, выводится сообщение с предупреждением
        print(f"{self._name}`s speed is {self._speed}")
        if self._speed > self.__max_permitted_speed:
            print(f"Over speed limit 60 ! please slow down!")


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    __max_permitted_speed = 40  # разрешенная скорость

    def show_speed(
            self):  # переопределяем родительский метод. Если скорость больше 60, выводится сообщение с предупреждением
        print(f"{self._name}`s speed is {self._speed}")
        if self._speed > self.__max_permitted_speed:
            print(f"Over speed limit 40! please slow down!")

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

# проверяем, создавая экземпляры объектов и вызывая их методы
town_car = TownCar(0, "green", "town car", False)
print("new towncar")
town_car.go(70)
town_car.turn('left')
town_car.turn('right')
town_car.show_speed()
town_car.go(40)
town_car.show_speed()
town_car.stop()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

sport_car = SportCar(0, "red", "sports car", False)
print("new sportcar!")
sport_car.go(70)
sport_car.turn('left')
sport_car.turn('right')
sport_car.show_speed()
sport_car.go(40)
sport_car.show_speed()
sport_car.stop()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

work_car = WorkCar(0, "blue", "work car", False)
print('new workcar')
work_car.go(70)
work_car.turn('left')
work_car.turn('right')
work_car.show_speed()
work_car.go(30)
work_car.show_speed()
work_car.stop()
work_car.show_speed()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

police_car = PoliceCar(0, "black", "Police", True)
print('new police car')
police_car.go(110)
police_car.turn('left')
police_car.turn('right')
police_car.show_speed()
police_car.stop()
police_car.show_speed()
