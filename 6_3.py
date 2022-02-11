"""Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность),
income (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
премии (get_total_income); проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров."""
class Worker:
    def __init__(self, name, surname, position, wage:[int,float],bonus:[int,float]):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": wage, "Премия": bonus}
class Position(Worker):
    def get_full_name(self):
        try:
            print(f"Полное имя сотрудника: {self.name} {self.surname}")
        except TypeError:
            return None
    def get_total_income(self):
        print(f'Доход с учётом премии {sum(self._income.values())}')

info_1 = Position('Mike', 'Leonov', 'Director', 500000, 15000)
info_1.get_full_name()
info_1.get_total_income()
print(info_1.position)
info_2 = Position('Kate', 'Golubenko', 'Cleaner', 30000, 1000)
info_2.get_total_income()