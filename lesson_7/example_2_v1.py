# Задание-2.
#
# Описание:
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
#
# .


""
"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-1
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def sizer(self):
        pass

class Clothes_dicts():

    _coat_size = 0
    _costume_size = 0
    def __init__(self,Clothing_names,usr_size):
        self.Clothing_names = Clothing_names
        self.size = usr_size
        self.Clothing_dict = {"Пальто":
                                   ["Английское",
                                    "Балмакаан",
                                    "Британская шинель",
                                    "Бушлат",
                                    "Даблфейс",
                                    "Даффлкот",
                                    "Запашное пальто",
                                    "Инвернесс",
                                    "Кафтан"],
                               "Костюм":
                                   ["Визитка",
                                    "Полуфрак",
                                    "Смокинг",
                                    "Фрак",
                                    "Английский",
                                    "Итальянский",
                                    "Американский",
                                    "Европейский",
                                    "Французский",
                                    "Немецкий"]}


class Total_Cloth_Coat(Clothes,Clothes_dicts):

    @property
    def sizer(self):

        if self.Clothing_names in self.Clothing_dict [ "Пальто" ]:
            Clothes_dicts._coat_size = round(float(self.size)/6.5 + 0.5, 2)
            return round(float(self.size)/6.5 + 0.5, 2)

class Total_Cloth_Costume(Clothes,Clothes_dicts):

    @property
    def sizer(self):
        if self.Clothing_names in self.Clothing_dict [ "Костюм" ]:
            self.rost = self.size
            Clothes_dicts._costume_size = round(2*float(self.rost) + 0.3)
            return round(2*float(self.rost) + 0.3) # self.size_of_rost

class Cloth_Calculate(Clothes,Clothes_dicts):

    def sizer(self):
        return Clothes_dicts._costume_size + Clothes_dicts._coat_size


usr_input_coat = "Бушлат"
usr_input_coat_size = 10
print("Количество ткани на пальто: ",Total_Cloth_Coat(usr_input_coat,usr_input_coat_size).sizer)

usr_input_costume = "Фрак"
usr_input_costume_size = 30
print("Количество ткани на костюм: ",Total_Cloth_Costume(usr_input_costume,usr_input_costume_size).sizer)

total_calculate = Cloth_Calculate(usr_input_coat,usr_input_coat_size)
print("Общее количество ткани: ",total_calculate.sizer())