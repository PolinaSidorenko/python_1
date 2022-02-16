"""2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность
 (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте
 относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды
использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу
декоратора @property."""


class Cloths:
    def __init__(self, v, h):
        self.v = float(v)
        self.h = float(h)

    def coat_square(self):
        return self.v / 6.5 + 0.5

    def costume_square(self):
        return self.h * 2 + 0.3

    @property
    def total_square(self):
        return str(f'Всего затрачено:\n'
                   f' {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)} метров ткани')


class Coat(Cloths):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.coat_sq = round(float(v) / 6.5 + 0.5)

    def __str__(self):
        return f'Потрачено метров ткани на пальто: {self.coat_sq}'


class Costume(Cloths):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.costume_sq = round(float(h) * 2 + 0.3)

    def __str__(self):
        return f'Потрачено метров ткани на костюм: {self.costume_sq}'


coat = Coat(2, 4)
costume = Costume(1,5)
print(coat)
print(costume)
print(coat.total_square)
print(costume.total_square)
print(costume.costume_square())
print(costume.coat_square())
