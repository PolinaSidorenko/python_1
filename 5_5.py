"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""
def summa():
    try:
        with open("file5.txt", 'w', encoding='utf-8') as f_obj:
            vvod = input('Введите чиcла, разделённые пробелами:\n')
            f_obj.writelines(vvod)
            my_list = vvod.split(' ')
            print('Сумма введённых чисел равна: ', sum(map(int, my_list)))
    except IOError:
        print('Ошибка в файле!')
    except ValueError:
        print('Ошибка ввода-вывода!')
summa()