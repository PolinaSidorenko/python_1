"""Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих
сотрудников. Выполнить подсчёт средней величины дохода сотрудников."""
all = 0
count = 0
try:
    with open("file3.txt", 'r', encoding='utf-8') as f_obj:
        for i in f_obj.readlines():
            my_list = (i.split(' '))
            my_list[1] = float(my_list[1])
            all = all + my_list[1]
            count = count + 1
            if my_list[1] < 20000:
                print(my_list[0])
        print('Средняя величина дохода сотрудников: ', round(all/count, 2) )
except IOError:
    print('Произошла ошибка ввода - вывода!')


