# Задание-5.
#
# Описание:
# Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
#
# .



""
"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-1
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""

class Stationery:

    def __init__(self):
        self.title = "Канцелярия"

    def draw(self):
        print(self.title)
        print("Запуск отрисовки в Родительском Классе == Stationery ==")

class Pen(Stationery):

    def draw(self):
        print(self.title)
        print("Запуск отрисовки в Классе == Pen ==, Дочернем Классе от == Stationery ==")


class Pencil(Stationery):

    def draw(self):
        print(self.title)
        print("Запуск отрисовки в Классе == Pencil ==, Дочернем Классе от == Stationery ==")


class Handle(Stationery):

    def draw(self):
        print(self.title)
        print("Запуск отрисовки в Классе == Handle ==, Дочернем Классе от == Stationery ==")

Stationery_class_obj = Stationery()
Stationery_class_obj.draw()
print("")
Pen_class_obj = Pen()
Pen_class_obj.draw()
print("")
Pencil_class_obj = Pencil()
Pencil_class_obj.draw()
print("")
Handle_class_obj = Handle()
Handle_class_obj.draw()