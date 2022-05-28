# Задание-1.
#
# Описание:
#
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
#
# .


""


class Date:
    def __init__(self,usr_date_string:str):
        self.init_day, self.init_month, self.init_year = self.date2num(usr_date_string)

    @classmethod
    def date2num(cls,cls_date_string:str):
        str2list = str(cls_date_string).split("-")
        day2num, month2num, year2num = map(int, str2list)
        print(type(day2num), type(month2num), type(year2num))
        return day2num, month2num, year2num

    @staticmethod
    def date_validate(static_date: list):
        for k, el_eval in enumerate(static_date):

            if k == 0 and type(el_eval) != int: return f"Ошибка: значение дня недели, - ожидается int"
            if k == 0 and (31 < el_eval or el_eval < 1): return f"Ошибка: значение дня недели вне диапазона"

            if k == 1 and type(el_eval) != int:
                print(f"Ошибка: значение месяца года, - ожидается int")
                return f"Ошибка: значение месяца года, - ожидается int"
            if k == 1 and (12 < el_eval or el_eval < 1):
                print(f"Ошибка: значение месяца года вне диапазона")
                return f"Ошибка: значение месяца года вне диапазона"

            if k == 2 and type(el_eval) != int: return f"Ошибка: значение года, - ожидается int"
            if k == 2 and el_eval < 0: return f"Ошибка: значение года вне диапазона"

        return True


Date.date2num("13-05-2022")

текст_1 = Date("13-05-2022")

print(f"текст_1.init_day:__ {текст_1.init_day} type:__ {type(текст_1.init_day)}")

Date.date_validate([13,15,2022])
print(Date.date_validate([32,15,2022]))
print(Date.date_validate([13,5,-2]))
print(Date.date_validate([13,"O",-2]))

