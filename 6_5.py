"""Реализовать класс Stationery (канцелярская принадлежность). определить в нём атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение метода draw."""

class Stationery:
    title: str
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        title = 'Ручка'
        print('Рисунок (надпись) был(а) выполнен(а) ручкой')
class Pencil(Stationery):
    def draw(self):
        title = 'Карандаш'
        print('Рисунок (надпись)  был(а) выполнен(а) карандашом')
class Handle(Stationery):
    def draw(self):
        title = 'Маркер'
        print('Рисунок (надпись)  был(а) выполнен(а) маркером')
pen=Pen()
pen.draw()
pencil=Pencil()
pencil.draw()
handle=Handle()
handle.draw()
smth=Stationery()
smth.draw()
