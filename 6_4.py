"""Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar
 и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self, color, name, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.direction = ''

    def go(self, speed):
        self.speed = float(speed)
        print(f'Машина поехала со скоростью {self.speed}')

    def stop(self):
        print ('Машина остановилась!')

    def turn(self, direction):
        if direction not in ('направо', 'налево'):
            print(f"'{direction}'  - неверное направление")
            return
        if not self.speed:
            print(f"'Нельзя повернуть {direction}', стоя на месте! Скорость равна нулю.")
            return
        self.direction = direction
        print("Машина повернула: ", self.direction)

    def show_speed(self):
        print(f'Машина движется со скоростью: {self.speed} км/ч')
        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Скорость превышена на  {self.speed - self._max_granted_speed} км/ч')


class TownCar(Car):
    _max_granted_speed = 60

class SportCar(Car):
    pass

class WorkCar(Car):
    _max_granted_speed = 40

class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)

a = TownCar('Yellow', 'Aston Martin Cygnet')
b = SportCar('Green', 'BMW M3')
c = WorkCar('White', 'VAZ 2106')
d = PoliceCar('Red', 'Ford Crown Victoria')

print(a.name)
print(b.speed)
print(c.color)
d.turn('налево')
a.go(20)
a.show_speed()
a.stop()
a.go(120)
a.show_speed()
print(d.is_police)