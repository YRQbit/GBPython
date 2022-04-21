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
# 7. Python сопоставляет полученное значение со значением из списка "Время года";
# 8. Python выводит в консоль соответсвующее название времени года из Списка "Врем года";
# 9. Python завершает выполнение кода;
#
# Пример:
#   - Python ==>> Введите число месяца:
#   - Пользователь вводит ==>> 1
#   - Python ==>> январь
#   - Python ==>> зима
#
#   - Python ==>> Введите число месяца:
#   - Пользователь вводит ==>> 3
#   - Python ==>> март
#   - Python ==>> весна
#
#   - Python ==>> Введите число месяца:
#   - Пользователь вводит ==>> 6
#   - Python ==>> июнь
#   - Python ==>> лето
#
# Задачи:
# 1. Создать объект Списка, содержащий значения с наименованиями месяцев;
# 2. Создать объект Списка, содержащий значения с наименованиями времен года;
# 3. Создать объект Словаря, содержащий значения с наименованиями месяцев;
# 4. Вывести в консоль запрос на ввод данных "Введите число месяца: ";
# 5. Выбрать из Списка месяц, соответствующий числовому значению, полученному от Пользователя:
# 6. Вывести в консоль полученное из Списка значение месяца;
# 7. Выбрать из Словаря месяц, соответствующий числовому значению, полученному от Пользователя:
# 8. Вывести в консоль полученное из Словаря значение месяца;
# 9. Выбрать из списка время года, соответствующее числовому значению, полученному от Пользователя:
# 10. Вывести в консоль полученное из списка значение времени года;


# Решение через Python-Список == list ==
month_list = [ "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
               "декабрь" ]

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
            break

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
#

var_season = {"зима": (12, 1, 2),
            "весна": (3, 4, 5),
            "лето": (6, 7, 8),
            "осень": (9, 10, 11)
            }

for time_year, season in var_season.items():
    if var_month in season:
        print("Время года ==>> ", time_year)