# Задание-3
#
# Описание:
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
#
# Ожидаемый результат:
#
# 1. Python выводит в консоль приглашения на ввод := "Введите число месяца: ";
# 2. Пользователь вводит числовое значение месяца;
# 3. Python выполняет валидацию ввода и значения;
# 3. Python сопоставляет полученное значение с соответствующим названием из Списка "Названия месяцев";
# 4. Python выводит в консоль соответсвующее название месяца из Списка "Названия месяцев"
# 5. Python сопоставляет полученное значение с соответствующим названием из Словаря "Названия месяцев";
# 6. Python выводит в консоль соответсвующее название месяца из Словаря "Названия месяцев"
# 7. Python завершает выполнение кода;
#
# Пример:
#   - Python ==>> Введите число месяца:
#   - Пользователь вводит ==>> 1
#   - Python ==>> январь
#
#   - Python ==>> Введите число месяца:
#   - Пользователь вводит ==>> 3
#   - Python ==>> март
#
# Задачи:
# 1. Создать объект Списка, содержащий значения с наименованиями месяцев;
# 2. Создать объект Словаря, содержащий значения с наименованиями месяцев;
# 3. Вывести в консоль запрос на ввод данных "Введите число месяца: ";
# 4. Выбрать из Списка месяц, соответствующий числовому значению, полученному от Пользователя:
# 5. Вывести в консоль полученное из Списка значение месяца;
# 6. Выбрать из Словаря месяц, соответствующий числовому значению, полученному от Пользователя:
# 7. Вывести в консоль полученное из Словаря значение месяца;
#


# Решение через Python-Список == list ==
month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]

# Решение через Python-Словарь == dict ==
month_dict = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}

while True:
    try:
        var_month = int(input("Введите число месяца: "))

        if 0 < var_month <= 12:

            for c, i in enumerate(month_list):
                if c + 1 == var_month:
                    print("Значение в Списке ==>> ", i)

            print("Значение в Словаре ==>> ", month_dict [ var_month ])
            exit()

        else:
            print("Указано не верное значение месяца, повторите ввод...")

    except ValueError:
        print("Ошибка в значении, нужно числовое значение ( от 1 до 12 )")

# Тест
#
# Введите число месяца: 010
# Значение в Списке ==>>  октябрь
# Значение в Словаре ==>>  октябрь
#
# Введите число месяца: 020
# Указано не верное значение месяца, повторите ввод...
# Введите число месяца: 012
# Значение в Списке ==>>  декабрь
# Значение в Словаре ==>>  декабрь
# /