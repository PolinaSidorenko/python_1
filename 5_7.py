"""Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
"""
from json import dumps
info = [{},{}]
try:
    with open('file7.txt', 'r', encoding='utf-8') as f_obj1:
        lines = f_obj1.readlines()
    for line in lines:
        name, smth,proceeds, expenses = line.split()
        info[0][name] = int(proceeds) - int(expenses)
    info[1]['average_profit'] = sum(profit for i, profit in info[0].items() if profit > 0) / len(info[0])
    with open('file_7.json', "w", encoding='utf-8') as f_obj2:
        f_obj2.write(dumps(info))
except IOError:
    print('Ошибка в файле!')
except ValueError:
    print('Ошибка ввода-вывода!')

