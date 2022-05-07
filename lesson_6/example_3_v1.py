# Задание-3.
#
# Описание:
# Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
#
# .

""
"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-1
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""

name_spec = input("Укажите имя сотрудника: ")
surname_spec = input("Укажите фамилию сотрудника: ")
skills = input("Количество навыков: ")
wage = input("Укажите оклад сотрудника: ")
bonus = input("Укажите премию сотрудника: ")

dict_emp_cost = {"wage":wage,"bonus":bonus}
dict_skill_cost = {"skills":skills,"skill_cost":''}


class Worker:

    def __init__(self,naming,surname,skills,income):
        self.name = naming
        self.surname = surname
        self.skills = skills
        self._income = income
        self.status_spec = ["unique specialist","best specialist","base specialist","universal"]



class Position(Worker):

    def get_full_name(self):
        """ Метод """
        return str(f"{self.name} {self.surname}")

    def get_total_income(self):
        """ Метод """
        return round(float(self._income['wage'])+float(self._income['bonus']),2)

class SkillStatus(Position):

    def get_skill_worker(self,skill_cost):
        """ Метод """
        self.skill_cost = skill_cost
        self.__average_skill_cost = float(self.get_total_income()) / float(self.skill_cost['skills'])
        self.skill_cost.update(skill_cost = round(self.__average_skill_cost,2))

        return self.skill_cost.get('skill_cost')

    def get_status_worker(self,skill_cost):
        """ Метод """
        self._skill_cost_method = self.get_skill_worker(skill_cost)

        if round(self._skill_cost_method) > 1000000 and (int(skill_cost['skills']) < 10) or int(skill_cost['skills']) > 52:
            return self.status_spec[ 0 ]

            # <><><><><><><><><><><><><><><><><><><><><><><><><>
            #
            # Сотрудник: asdfasdf asdfsadf
            # Доход сотрудника: 324523454479.0
            # self.get_skill_worker(skill_cost) == 262984971.21
            # skill_cost[0] ==  1234
            # Уровень сотрудника: unique specialist
            # Средняя стоимость навыка: 262984971.21
            # <><><><><><><><><><><><><><><><><><><><><><><><><>

            # <><><><><><><><><><><><><><><><><><><><><><><><><>
            #
            # Сотрудник: jkvndkjdns skdfnvkdsjf
            # Доход сотрудника: 972987494220.0
            # self.get_skill_worker(skill_cost) == 324329164740.0
            # skill_cost[0] ==  3
            # Уровень сотрудника: unique specialist
            # Средняя стоимость навыка: 324329164740.0
            # <><><><><><><><><><><><><><><><><><><><><><><><><>
            #
            #
            # Process finished with exit code 0

            # <><><><><><><><><><><><><><><><><><><><><><><><><>
            #
            # Сотрудник: jvnsdkfjn sdkfjvndsf
            # Доход сотрудника: 23453455590.0
            # self.get_skill_worker(skill_cost) == 1019715460.43
            # skill_cost[0] ==  23
            # Уровень сотрудника: universal
            # Средняя стоимость навыка: 1019715460.43
            # <><><><><><><><><><><><><><><><><><><><><><><><><>


        elif 20000 < round(self._skill_cost_method) < 100000 and int(skill_cost['skills']) < 13:
            return self.status_spec [ 1 ]

                # <><><><><><><><><><><><><><><><><><><><><><><><><>
                #
                # Сотрудник: фывлаи афылвофталф
                # Доход сотрудника: 95000.0
                # self.get_skill_worker(skill_cost) == 9500.0
                # skill_cost[0] ==  10
                # Уровень сотрудника: base specialist
                # Средняя стоимость навыка: 9500.0
                # <><><><><><><><><><><><><><><><><><><><><><><><><>
                #
                #
                # Process finished with exit code 0

        elif 10000 < round(self._skill_cost_method) <= 20000 and 13 <= int(skill_cost['skills']) < 26:
            return self.status_spec [ 2 ]

                # <><><><><><><><><><><><><><><><><><><><><><><><><>
                #
                # Сотрудник: sdfgkjsdnfkg sdkfgjnsdkfj
                # Доход сотрудника: 20000.0
                # self.get_skill_worker(skill_cost) == 1333.33
                # skill_cost[0] ==  15
                # Уровень сотрудника: base specialist
                # Средняя стоимость навыка: 1333.33
                # <><><><><><><><><><><><><><><><><><><><><><><><><>
                # .
        else:
            return self.status_spec [ 3 ]

                # <><><><><><><><><><><><><><><><><><><><><><><><><>
                #
                # Сотрудник: scksdlkmlc sckjsndckjas
                # Доход сотрудника: 10500.0
                # self.get_skill_worker(skill_cost) == 807.69
                # skill_cost[0] ==  13
                # Уровень сотрудника: universal
                # Средняя стоимость навыка: 807.69
                # <><><><><><><><><><><><><><><><><><><><><><><><><>


class_obj_position = Position(name_spec, surname_spec, skills, dict_emp_cost)
class_obj_skillstatus = SkillStatus(name_spec, surname_spec, skills, dict_emp_cost)

print("<>"*25 + "\n")
print(f"Сотрудник: {class_obj_position.get_full_name()}")
print(f"Доход сотрудника: {class_obj_position.get_total_income()}")
print(f"Класс сотрудника: {class_obj_skillstatus.get_status_worker(dict_skill_cost)}")
print(f"Средняя стоимость навыка: {class_obj_skillstatus.get_skill_worker(dict_skill_cost)}")
print("<>"*25 + "\n")