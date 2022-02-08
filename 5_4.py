"""Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
dict ={
    'One':'Один',
    'Two':'Два',
    'Three':'Три',
    'Four':'Четыре'}
try:
    with open("file4.txt", 'r', encoding='utf-8') as f1_obj:
        with open('file_4.txt','w',encoding='utf-8') as f2_obj:
            for i in f1_obj.readlines():
                my_list = (i.split(' '))
                my_list[0] = dict[my_list[0]]
                f2_obj.writelines(my_list)
except IOError:
    print('Произошла ошибка ввода - вывода!')

