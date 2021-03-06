# Задание-6.
#
# Описание:
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
#
""
def gen_list_func():
    """Функция-1 "Создание списка значений в указанном диапазоне"
    Функция предназначена для вызова в качестве функции модуля"""
    from itertools import count
    usr_num_v1 = int(input("Укажите начальное число: "))
    usr_num_v2 = int(input("Укажите конечное число: "))

    gen_list = []
    for k in count(usr_num_v1):
        if k > usr_num_v2:
            break
        else:
            gen_list.append(k)

    return gen_list
