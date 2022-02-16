"""3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать
класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение
(__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно. В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен
возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся."""

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'В итоге получилось: {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Вычитаемое больше уменьшаемого!')


    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells):
        row = ''
        for i in range(int(self.quantity / cells)):
            row += f'{"*" * cells} \\n'
        row += f'{"*" * (self.quantity % cells)}'
        return row

cells1 = Cell(15)
cells2 = Cell(7)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(14))
print(cells1.make_order(3))
print(cells1 / cells2)