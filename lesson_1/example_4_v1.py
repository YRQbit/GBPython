# Задание-4
#
# Описание:
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
# Задачи:
# 1. запросить в консоли ввод целого положительного числа;
# 2. вычислить наибольшую цифру в числе, используя цикл while и арифметические операции;
# 3. вывести полученный результат в консоль;
#
#
# Ожидаемый результат:
# 1. Вывод в консоль приглашения на ввод "Введите произвольное число: ";
# 2. Вывод в консоль результата ==>> "Наибольшая цифра в числе ==> ";
# .

import sys


def input_int(prompt=None):

    k = 0
    while True:
        ch = input(prompt)

        try:
            return int(ch)

        except ValueError:
            if k < 2:
                print("Ошибка, нужно число, повторите пожалуйста ввод")
                print(" ")
                k+=1

            else:
                print(" ")
                print("Попробуйте в следующий раз...")
                sys.exit()

userNum_int = input_int("Введите произвольное целое число: ")

index_str_int = len(str(userNum_int))

max_val = 0

while index_str_int >= 0:

    indSymbol = int(str(userNum_int)[index_str_int-1])

    if indSymbol > max_val:

        max_val = indSymbol

    index_str_int = index_str_int - 1

print(f"Наибольшая цифра в числе ==>  {max_val}")

