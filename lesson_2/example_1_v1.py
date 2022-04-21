# Задание-1
#
# Описание:
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
# Ожидаемый результат:
# var_float = 2/5 ==>> 0.4 ==>> type(var_float) ==>> <class 'float'>
# var_complex = complex(2,5) ==>> (2+5j) ==>> type(complex(2,5)) == <class 'complex'>
# var_string = "it's_my_best_string" ==>> it's_my_best_string ==>> type(var_string) ==>> <class 'str'>
# my_list = list("mylist") ==>> ['m', 'y', 'l', 'i', 's', 't'] ==>> type(my_list) ==>> <class 'list'>
# var_bool = True ==>> True ==>> type(var_bool) ==>> <class 'bool'>
#
# и т.д.
#
# Задачи:
# 1. создать переменные различных типов и присвоить им соответствующие значения:
#   - int (в различных системах счисления: int\bin\oct\hex)
#   - float
#   - complex
#   - string
#   - bool
#   - list
#   - tuple
#   - set
#   - frozenset
#   - dict
#   - bytes
#   - bytearray
#   - None
#   - exception;
#
# 2. Разместить значения переменных в списке;
# 3. Создать цикл с обработкой исключений и применением функции == type() ==
#   для проверки и вывода значений типа созданных переменных;
#


my_number = 25

var_int_2 = bin(my_number)
var_int_8 = oct(my_number)
var_int_10 = int(my_number)
var_int_16 = hex(my_number)
var_float = int(str(my_number)[0])/int(str(my_number)[1])
var_complex = complex(int(str(my_number)[0]),int(str(my_number)[1]))
var_string = "it's_my_best_string"
var_bool = True

# Список
str_4_list = "mylist"
my_list = list(str_4_list)

# Кортеж == не изменяемый Cписок
my_tuple = ("the","_stings_","of_","eternity","_tend_","to_","infinity")
my_tuple_v1 = tuple("строки Вечности стремятся к бесконечности")

# Множество.
# Множество с изменяемым типом данных
my_set = set("it's very big line")
my_set_v1 = {1,2,3,345,4,True,3,5,345,True}
# Множество с НЕизменяемым типом данных
my_frozenset = frozenset("it's very big line")

# Словарь.
my_dict = {"var_int_2": var_int_2, "var_int_8": var_int_8, "var_int_10": var_int_10, "var_int_16": var_int_16, 2: 500, 5: None}
my_dict_v1 = dict(var_int_2='var_int_2', var_int_8='var_int_8', )

# Байты
# Единица хранения информации (текстовой \ графической \ звуковой).
# Байтовое представление похоже на строковое, но с рядом отличий
var_bytes = bytes(234)

# Байт-массив представляет собой изменяемый тип данных
var_byte_array = bytearray(b"234 yps")


var_None = None


my_best_list = [var_int_2,
                var_int_8,
                var_int_10,
                var_int_16,
                var_float,
                var_complex,
                var_string,
                my_list,
                my_tuple,
                my_set,
                my_frozenset,
                my_dict,
                my_dict_v1,
                var_bool,
                var_bytes,
                var_byte_array,
                var_None]

print("<>"*35)

try:

    for c, k in enumerate(my_best_list):

        if type(k) == str:


            if k == var_int_2:

                print(f"my_best_list || index ={c} || ==>> bin__{k} <-><-><-><-> Type__{type(k)}")

            elif k == var_int_8:
                print(f"my_best_list || index ={c} || ==>> oct__{k} <-><-><-><-> Type__{type(k)}")

            elif k == var_int_16:
                print(f"my_best_list || index ={c} || ==>> hex__{k} <-><-><-><-> Type__{type(k)}")

            else:
                print(
                    f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == int:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == complex:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == bool:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == float:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == list:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == tuple:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == set:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == frozenset:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == dict:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) == bytes:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) is bytearray:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__\"{k}\" <-><-><-><-> Type__{type(k)}")

        elif type(k) is not None:

            print(
                f"my_best_list || index ={c} || ==>> {str(type(k)).split(' ') [1].rstrip('>')}__{k} <-><-><-><-> Type__{type(k)}")


    var_except = 123/0

except (ZeroDivisionError, IndentationError):

    print("<>"*25)

    try:

        print(f"Python обнаружил ошибку \"Попытка деления на ноль{var_except}\"..., Python ругается...")

    except NameError:

        print(f"Python ругается... Python обнаружил попытку деления на ноль...")
        print("Переменная \"var_except\" не объявлена ")

print("<>"*35)
