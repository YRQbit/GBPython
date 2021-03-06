# Задание-2
#
# Описание:
# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды, и выведите в формате чч:мм:сс. Используйте
# форматирование строк
#
# Задачи:
# 1. запросить в консоли ввод числа секунд от пользователя;
# 2. перевести время в часы, и вывести в консоль используя форматирование строк;
# 3. перевести время в минуты, и вывести в консоль используя форматирование строк;
# 4. перевести время в секунды, и вывести в консоль используя форматирование строк;
# 5. вывести часы, минуты и секунды в формате чч:мм:сс;
#
#
# Ожидаемый результат:
# 1. Вывод в консоль приглашения на ввод "Введите произвольное количество секунд: ";
# 2. Вывод в консоль результата ==>> "Указанному времени соответствует _N_ час(а\ов) _N_ года";
# 3. Вывод в консоль результата ==>> "Указанному времени соответствует _N_ мин. _N_ года";
# 4. Вывод в консоль результата ==>> "Указанному времени соответствует _N_ сек. _N_ года";
# 5. Вывод в консоль результата ==>> "Указанному времени в формате чч:мм:сс, соответствует: __:__:__ _N_ года";
# .

import datetime as datetime_mod
import time as time_mod

print("Текущее время в секундах ==>> ", time_mod.time())

userSecTime = float(input("Введите произвольное количество секунд: "))

userTimeCount = userSecTime

k=0

while True:

    if (userTimeCount > 0) and (k < 1):

        print("<><><><> Обратный отсчет <><><><>")

        k += 1

    elif userTimeCount > 0.0:

        print("Текущее значение ==> ", userTimeCount)

    else:

        print(" ")
        print(" Python думает... Python решает... пожалуйста, подождите... ")
        time_mod.sleep(3)

        print(" ")
        print("<>"*28)

        sysTimeVal = datetime_mod.datetime.fromtimestamp(userSecTime)

        print(f"Указанному времени соответствует {sysTimeVal.hour} час. {sysTimeVal.year} года")
        print(f"Указанному времени соответствует {sysTimeVal.minute} мин. {sysTimeVal.year} года")
        print(f"Указанному времени соответствует {sysTimeVal.second} сек. {sysTimeVal.year} года")
        print("<>" * 28)
        print(" ")

        print(f"Указанному времени в формате чч:мм:сс, соответствует: {sysTimeVal.time()} ({sysTimeVal.year} года)")
        print("<>" * 38)
        break


    userTimeCount = int(userTimeCount) - (userTimeCount * 0.5)
