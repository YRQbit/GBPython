# Задание-3.
#
# Описание:
#
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# .

""


class ListIntValue_Error(Exception):
    def __init__(self,list_values):
        for self.k in list_values:
            print(f"k == {self.k} and type == {type(self.k)}")
            if type(self.k) is not int:
                self.txt_err = f'Ошибка: Список содержит элемент не числового типа данных'

    def __str__(self):
        return self.txt_err

usr_val_list = []

def num_filter(list4filter):

    list4filter_double = []

    for k, item in enumerate(list4filter):
        # .
        if str(item).isdecimal():
            # .
            list4filter_double.append(int(item))

    list4filter = list4filter_double
        # .
    return list4filter


while True:
    try:

        usr_input = input("Enter value: ")

        if str(usr_input).isdecimal():
            # .
            print(f"ЧИСЛО! {usr_input}")
            usr_val_list.append(usr_input)
        else:
            # .
            raise ListIntValue_Error(usr_val_list)

    except ListIntValue_Error as myerr:
        # .
        print(myerr)
        usr_YN = input("Продолжим? [Y\\N]")

        if str(usr_YN).lower() in ["y","yes","да","д"]:
            # .
            continue
        else:
            # .
            print(usr_val_list)
            break




