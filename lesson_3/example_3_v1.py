# Задание-3.
#
# Описание:
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
#
# Ожидаемый результат:
# 1. Пользователь запускает Python-скрипт на выполнение
# 2. Python выводит в консоль запрос на ввод трех значений в одной строке (через пробел)
# 3. Python выполняет поиск двух наибольших значений
# 4. Python суммирует два наибольших значения
# 5. Python выводит результат суммирования в консоль
# 6. Python завершает выполнение кода
#

value_1, value_2, value_3 = input("Укажите 3 целочисленных значения: ").split()

def max_val(val1, val2, val3):
    """Функция-1 "Сумма двух наибольших значений из трех"
    Функция выполняет:
        - принимает значения через обязательные параметры
        - размещает полученные значение в элементах Списка
        - находит минимальный элемент в списке
        - удаляет минимальный элемент из списка
        - суммирует значения двух оставшихся элементов """

    val_list = [val1,val2,val3]
    print(min(val_list))

    for index, val_znach in enumerate(val_list):

        if int(min(val_list)) == int(val_znach):

            val_list.pop(index)
            print(f"Сумма двух наибольших значений: {sum(val_list)}")

max_val(int(value_1),int(value_2),int(value_3))
    # Вызываем Функцию-1 "Сумма двух наибольших значений из трех"
    # из основной ветки кода с позиционными аргументами обязательных параметров

