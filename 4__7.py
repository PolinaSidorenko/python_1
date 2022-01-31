"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим
образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только
первые n чисел, начиная с 1! и до n!."""

from itertools import count
from math import factorial

def func():
    for el in count(1):
        yield factorial(el)

gen = func()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break