"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее
реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица."""


class Matrix:
    def __init__(self, list_1, list_2 = False):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        self.matr = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        if len(self.list_1) == len(self.list_2):
            for i in range(len(self.list_1)):
                for j in range(len(self.list_2[i])):
                    self.matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))
        else:
            print('Введенные матрицы не удовлетворяют указанным требованиям!')

    def __str__(self):
        self.matr = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(3):
                self.matr[i][j] = self.list_1[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])
matrr = Matrix([[5, 18, 11],
                [6, 17, 23],
                [41, 50, 9]])

print(my_matrix.__add__(),'\n')
print(matrr.__str__())