# Задание-5
#
# Описание:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее, запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете
# на одного сотрудника.
#
# Задачи:
# 1. запросить в консоли ввод значения выручки и издержек компании;
# 2. Вычислить финансовый результат и вывести в консоль;
# 3. Финансовый результат "Прибыль" ==>
#    вывести в консоль результат с комментарием "Прибыль компании составляет"__значение полученной прибыли__;
# 4. Финансовый результат "Убытки" ==>
#    вывести в консоль результат с комментарием "Убытки компании составляет"__значение полученных убытков__;
# 5. В случае, когда значение прибыли положительное ==>
#    вычислить значение рентабельности (соотношение прибыли к выручке) и вывести это значение в консоль;
# 6. запросить в консоли ввод численности сотрудников компании;
# 7. Выполнить расчет прибыли компании в расчете на одного сотрудника и вывести результат в консоль;
#
# Ожидаемый результат:
# 1. Вывод в консоль приглашения на ввод "Укажите выручку за текущий год: ";
# 1. Вывод в консоль приглашения на ввод "Укажите сумму издержек за текущий год: ";
# 3. В случае, когда значение прибыли положительное ==>
#    Вывод в консоль результата ==>>
#       - "Прибыль компании составляет" __значение полученной прибыли__
#       - "Рентабельность компании составляет" __значение рентабельности__;
# 4. Вывод в консоль приглашения на ввод "Укажите численность сотрудников в компании:";
# 5. Вывод в консоль результата ==>>
#       - "Прибыль в расчете на одного сотрудника составляет:";
# .

import datetime
import sys

print(f" ")
print("<><><><> Расчет финансовых результатов компании <><><><>")  # выводим в консоль заголовок нашей формы расчета

company_name = str(input("Наименование компании: "))
receipt = float(input("Выручка за текущий год:"))
costs = float(input("Сумма издержек за текущий год:"))

year_result = datetime.datetime.now().year

print("<>" * 28)
print(f" ")


if receipt >= costs:
    print(f"Прибыль компании {company_name},за {year_result} год, "
          f"составляет: {round((receipt - costs), 2)} руб.")

else:
    print(f"Убытки компании составляют: {round((receipt - costs), 2)} руб.")

print(f" ")
print("<>" * 28)

number_of_staff = int(input("Укажите количество сотрудников в компании :"))

print(f" ")


if number_of_staff <= 0:
    print("Упс... что-то пошло не так, попробуйте позже...")
    sys.exit()

else:
    print(f"Прибыль компании в расчете на одного сотрудника: {round((receipt - costs) / number_of_staff, 2)} руб.")
    print(f" ")
    print("ВНИМАНИЕ! Рентабельность ОТРИЦАТЕЛЬНА! ")
    print(f" ")

    if receipt > costs:
        print("Рентабельность : ", "{:.2%}".format((receipt - costs) / receipt))
        print(f" ")
