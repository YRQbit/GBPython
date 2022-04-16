# Задание-6
#
# Описание:
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
#
# Задачи:
# 1. запросить в консоли ввод результата (дистанция в км.) пробежки в первый день тренировки;
# 2. запросить в консоли ввод ожидаемого результата пробежки (дистанция в км.);
# 3. задать параметры по-умолчанию и выполнить расчет показателя прогресса;
# 4. выполнить расчет прогресса по каждому дню пробежки с учетом 10%-го увеличения результата, относительно предыдущего;
# 5. вычислить день, в который показатель прогресса превысит значения ожидаемого результата;
# 6. вывести результаты вычислений в консоль;
#
#
# Ожидаемый результат:
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
# .


first_day_result_km = float(input("Сколько километров вы пробежали в первый день? (по-умолчанию 2): "))
need_me_result = float(input("Укажите максимальную дистанцию, в километрах, которую планируете пробежать ?(минимум 50 км) : "))

def prognosis_result(need_result_km=3,fact_percent = 10.0,count_day=0,):

    progress = float((first_day_result_km/100 * fact_percent))
    plan_progress = first_day_result_km

    print(" \n"+"<>"*26)
    print("<><><><> план прогресса тренировок по бегу <><><><>")
    print("<>" * 26,'\n' )

    while plan_progress < float(need_result_km) + 1:
        count_day += 1

        if 0 < count_day < 2:

            if dig_count(str(first_day_result_km)) < 1:
                print(f"день {count_day}-й ==> {int(first_day_result_km)} км")

                if first_day_result_km == need_result_km:
                    print(" ")
                    print("Примите наши поздравления! Вы достигли своего рекорда!")

                    break

                plan_progress = (first_day_result_km + progress)

            else:
                print(f"день {count_day}-й => {round(first_day_result_km, 2)} км")

                if first_day_result_km == need_result_km:
                    print(" ")
                    print("Примите наши поздравления! Вы достигли своего рекорда!")

                    break

                plan_progress = (first_day_result_km + progress)

        else:
            if plan_progress < float(need_result_km):

                if dig_count(str(plan_progress)) < 1:
                    print(f"день {count_day}-й ==> {round(plan_progress, 0)} км")

                    plan_progress = plan_progress + (plan_progress / 100 * fact_percent)

                else:
                    print(f"день {count_day}-й ==> {round(plan_progress, 2)} км")

                    plan_progress = plan_progress + (plan_progress / 100 * fact_percent)

            elif plan_progress >= need_result_km:

                if dig_count(str(plan_progress)) < 1 :
                    print(f"день {count_day}-й ==> {round(plan_progress, 2)} км")

                    break

                else:
                    print(f"день {count_day}-й ==> {round(plan_progress, 2)} км")

                    break

    print(" \n"+"<>"*26)
    print("<><><><> Прогноз достижений <><><><>"+ '\n' )
    print(f"Достижение показателя пробежки не менее чем {need_result_km} км \nв день тренировки, "
          f"возможно на {round(count_day, 2)} день тренировок, \nпри соблюдении плана прогресса "
          f"регулярного увеличения \nдистанции пробежки на {fact_percent}%")
    print("<>" * 26, '\n')

def dig_count(val_num):

    if "." in val_num:
        return len(val_num.split(".")[1].rstrip("0"))

    else:
        return 0

prognosis_result(need_result_km=need_me_result)
