# Задание-7.
#
# Описание:
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
#
""
from math import factorial

def fact(usr_num):
    for k in range(1,usr_num+1):
        yield factorial(k)

n = int(input("Укажите целое положительное число: "))

if n >= 0:
    get_list = []

    for el in fact(n):
        get_list.append(el)
else:
    print("факториал отрицательного числа не может быть вычислен...")

num_list=[]

if get_list:

    for k, val_list in enumerate(get_list):

        if val_list != None:
            num_list.append(val_list)
else:
    print(f"Факториал числа _{n}_ ==> {n}")

print(f"Факториал числа {n}! = {str(num_list).rstrip(']').lstrip('[').replace(',','*').replace(' ','').rpartition('*')[0]} = {val_list}")