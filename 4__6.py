"""Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. """
from itertools import count, cycle
from sys import argv

name, arg, slovo = argv
arg = int(arg)

for el in count(arg):
    if el > 15:
        break
    else:
        print(el)

с = 0
for el in cycle(slovo):
    if с > 10:
        break
    print(el)
    с += 1

