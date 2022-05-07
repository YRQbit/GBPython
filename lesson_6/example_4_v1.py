# Задание-4.
#
# Описание:
# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
#
# .


""
import curses
import random
"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-1
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

ВНИМАНИЕ! ВНИМАНИЕ! ВНИМАНИЕ! ВНИМАНИЕ!

Для выполнения Скрипта, необходимо перейти в консоль и расширить 
ее минимум до 10 строк. Лучше и проще, полностью развернуть окно
терминала.
 
После этого перейти в директорию размещения скрипта и выполнить его
запуск командой: python ./example_4_v1.py

Эти требования связаны с применением псевдографического интерфейса,
реализованного с помощью библиотеки Curses.

P.S.
Чуть-чуть увлекся... о_О и... немного вышел за рамки ПЗ :))  
   
"""

color_class_var = ['красный',"синий","белый","желтый" ]
name_class_var = ['УАЗ Патриот','RSM-2375','ГАЗель Next Citiline','Лада НИВА']


""" Определение классов и методов """

class Car:
    # Базовый Класс

    speed = 0
    color = color_class_var
    name = name_class_var
    _is_police = False



    def go(self):
        """ Метод """
        speed_plus = self.speed + 1

        if 0 < speed_plus < 2:
            myscreen.addstr(4, 75, f"   Движение  ")
            myscreen.addstr(5, 75, f"  [ НАЧАЛО ]  ")
        elif 2 < speed_plus < 4:
            myscreen.addstr(4, 75, f"              ")
            myscreen.addstr(5, 75, f"              ")

        Car.speed = speed_plus
        return self.speed



    def stop(self):
        """ Метод """
        speed_minus = self.speed - 1

        if 0 >= speed_minus:
            Car.speed = 0
            speed_minus = 0
            myscreen.addstr(4, 75, f"   Движение  ")
            myscreen.addstr(5, 75, f"  [  СТОП  ]  ")
            return speed_minus
        else:
            Car.speed = speed_minus
            return self.speed



    def show_speed(self):
        """ Метод выводит результат скорости в псевдографический
        интерфейс Сприпта, сформированный через "curses"
        """
        myscreen.addstr(1, 77, f"[ {self.speed} км\ч ]    ")
        myscreen.addstr(2, 77, " Скорость CarClass")



    def turn(self, direction):
        """ Метод принимает отрицательное \ положительное значение
        после чего формирует значение угла поворота
        """
        turn_side = direction
            # получем значение параметра direction (сторона поворота)
            # .

        if turn_side < 0:
            # В случае отрицательного значения,
            # пониманием, что вызов Метода
            # выполнен с запросом на левый поворот...
            # .
            myscreen.addstr(4, 75, f"   Движение  ")
            myscreen.addstr(5, 75, f"  [ ВЛЕВО  ]  ")
            if turn_side + 1 == 0:
                myscreen.addstr(4, 75, f"   Движение   ")
                myscreen.addstr(5, 75, f"  [  ПРЯМО ]  ")
            return abs(turn_side + 1) # abs(turn_left + 1)
                # первое нажатие клавиши (вызов Метода)
                # обнулит показатель. При этом не важно,
                # когда нажата клавиша, - в первый раз
                # с момента запуска Скрипта, или первый
                # раз после поворота вправо\влево.
                # Такое решение применяется для получения
                # нулевых значений между переключениями
                # влево\вправо, т.о. мы получаем прямолинейное
                # движение.
                # Обнуление второго показателя (противоположного),
                # выполняется в основном блоке кода, обнулением
                # переменных:
                # left_key_press = 0 и right_key_press = 0
                # соответственно
                # .

        elif turn_side > 0:
            # В случае положительного значения,
            # понимаем, что вызов Метода выполнен
            # с запросом на правый поворот...
            # .
            myscreen.addstr(4, 75, f"   Движение  ")
            myscreen.addstr(5, 75, f"  [ ВПРАВО ]  ")
                #
                # .
            if turn_side - 1 == 0:
                myscreen.addstr(4, 75, f"   Движение  ")
                myscreen.addstr(5, 75, f"  [  ПРЯМО  ]  ")
                    #
                    # .
            return turn_side - 1
                # первое нажатие клавиши (вызов Метода)
                # обнулит показатель.
                # Подробнее, см. комментарии к return abs(turn_side + 1)
                # .



class TownCar(Car):
    """ Переопределить метод def show_speed(self):
    при превышении скорости свыше 60 км\ч выводить
    сообщение о превышении скорости
    """

    def show_speed(self):
        """ Метод """
        colorid = random.randrange(len(self.color))
        colorizer = self.color[colorid]
            #
            # .
        myscreen.addstr(8, 55, f"[  {colorizer}  ]    ")
            # мечта шпиона))
            # .
        myscreen.addstr(8, 75, "[  городской  ]")
            #
            # .
        myscreen.addstr(8, 95, f"[  {self.name [ 2 ]}  ]    ")
            #
            # .

        if self.speed > 60:
            myscreen.addstr(4, 75, f"  Превышение  ")
            myscreen.addstr(5, 75, f"  [ {self.speed - 60} км\ч ]  ")
        elif self.speed > 3:
            myscreen.addstr(4, 75, f"              ")
            myscreen.addstr(5, 75, f"              ")



class SportCar(Car):

    def sport_car(self):
        """
        обработка Метода в основном блоке кода :
        SportCar_class_obj = SportCar()
        if car_select == 3:
        if keyses == 52: SportCar_class_obj.sport_car()
        """
        colorid = random.randrange(len(self.color))
        colorizer = self.color [ colorid ]

        myscreen.addstr(8, 55, f"[  {colorizer}  ]    ")
            # мечта шпиона))
            # .
        myscreen.addstr(8, 75, "[ спортивный ]   ")
            #
            # .
        myscreen.addstr(8, 95, f"[  {self.name [ 0 ]}  ]    ")
            #
            # .



class WorkCar(Car):
    """ Переопределить метод def show_speed(self):
    при превышении скорости свыше 40 км\ч
    выводить сообщение о превышении скорости
    """

    def show_speed(self):
        """ Метод """
        colorid = random.randrange(len(self.color))
        colorizer = self.color [ colorid ]
            #
            # .
        myscreen.addstr(8, 55, f"[  {colorizer}  ]    ")
            # мечта шпиона))
            # .
        myscreen.addstr(8, 75, "[   рабочий   ]")
            #
            # .
        myscreen.addstr(8, 95, f"[  {self.name [ 1 ]}  ]    ")
            #
            # .

        if self._is_police == False:
            # обработка атрибута выполняется исключительно
            # в академических целях...

            if self.speed > 40:
                myscreen.addstr(4, 75, f"  Превышение  ")
                myscreen.addstr(5, 75, f"  [ {self.speed - 40} км\ч ]  ")
            elif self.speed > 3:
                myscreen.addstr(4, 75, f"              ")
                myscreen.addstr(5, 75, f"              ")

        else:
            if self.speed > 3:
                myscreen.addstr(4, 75, f"              ")
                myscreen.addstr(5, 75, f"              ")


class PoliceCar(Car):

    def police_car(self):
        """ Метод """
        colorid = random.randrange(len(self.color))
        colorizer = self.color [ colorid ]
            #
            # .
        myscreen.addstr(8, 55, f"[  {colorizer}  ]    ")
            # мечта шпиона))
            # .
        myscreen.addstr(8, 75, "[ полицейский ]   ")
            #
            # .
        myscreen.addstr(8, 95, f"[  {self.name [ 3 ]}  ]    ")
            #
            # .


""" Основной блок кода """


myscreen = curses.initscr()

car_class_obj =  Car()
WorkCar_class_obj = WorkCar()
TownCar_class_obj = TownCar()
PoliceCar_class_obj = PoliceCar()
SportCar_class_obj = SportCar()



def keys_map():
    myscreen.addstr(1, 2,"Клавиши управления: ")
    myscreen.addstr(2, 2,"    Увеличить скорость [стрелка вверх ]")
    myscreen.addstr(3, 2,"    Повернуть вправо   [стрелка вправо]")
    myscreen.addstr(4, 2,"    Повернуть влево    [стрелка влево ] ")
    myscreen.addstr(5, 2,"    Снизить скорость   [стрелка вниз  ]")
    myscreen.addstr(7, 2, "Выбрать тип транспорта [пробел] ")
    myscreen.addstr(8, 2, "Выход [q] ")



def car_type_menu():
    myscreen.addstr(1, 2, "Тип транспорта:      ")
    myscreen.addstr(2, 2, "    Рабочий транспорт     [ 1 ]        ")
    myscreen.addstr(3, 2, "    Городской транспорт   [ 2 ]        ")
    myscreen.addstr(4, 2, "    Полицейский транспорт [ 3 ]        ")
    myscreen.addstr(5, 2, "    Спортивный транспорт  [ 4 ]        ")
    myscreen.addstr(7, 2, "Вернуться [ESC]                 ")
    myscreen.addstr(8, 2, "Выход [q]       ")



def priborka(car_speed=0,left_side=0, right_side=0):
    myscreen.addstr(1, 77, f"[ {car_speed} км\ч ]    ")
    myscreen.addstr(2, 77, " Скорость")
    myscreen.addstr(4, 60, f"  [ {left_side} град ]    ")
    myscreen.addstr(5, 60, "Угол поворота")
    myscreen.addstr(4, 91, f" [ {right_side} град ]    ")
    myscreen.addstr(5, 91, "Угол поворота")
    myscreen.addstr(7, 77, " Транспорт")


right_key_press = left_key_press = 0

try:

    myscreen.border(0)
    keys_map()
    priborka(car_class_obj.speed)
    car_select = 0

    while True:
        keyses = myscreen.getch(1,23)
        myscreen.addstr(1, 23, " "*3)
            #
            # .

        if keyses != 113:
            #
            # .
            if keyses == 65:
                #
                # .
                myscreen.refresh()
                myscreen.addstr(6, 3, " "*25)
                car_class_obj.go()
                    #
                    # .

                if car_select == 1:
                    WorkCar_class_obj.show_speed()
                if car_select == 2:
                    TownCar_class_obj.show_speed()
                if car_select == 3:
                    PoliceCar_class_obj.police_car()
                if car_select == 4:
                    SportCar_class_obj.sport_car()
                        #
                        # .

                car_class_obj.show_speed()
                    #
                    # .

            if keyses == 66:
                #
                # .
                myscreen.refresh()
                myscreen.addstr(6, 3, " "*25)
                car_class_obj.stop()
                    #
                    # .

                if car_select == 1:
                    WorkCar_class_obj.show_speed()
                if car_select == 2:
                    TownCar_class_obj.show_speed()
                        #
                        # .

                car_class_obj.show_speed()
                    #
                    # .

            if keyses == 67:
                myscreen.refresh()
                myscreen.addstr(6, 3, " "*25)
                right_key_press += 1
                    #
                    # .

                if right_key_press > 0:
                    left_right = car_class_obj.turn(right_key_press)
                    left_key_press = 0
                        # обнуляем значения показателя левого поворота
                        # в основном блоке кода. Это позволяет сбросить
                        # точку отсчета, при нажатии на левую клавишу
                        # т.о. отсчет будет продолжаться не с == -3 ==,
                        # а с нуля...
                        # т.е. при следующем вызове Метода == turn ==,
                        # при очередном нажатии левой клавиши, после того
                        # как мы несколько раз нажали на правую, отсчет
                        # угла поворота будет начинаться с нуля..
                        # .

                priborka(right_side= left_right)
                    # Передаем полученное значение в Функцию "Приборная панель"
                    # .
                car_class_obj.show_speed()
                    #
                    # .

            if keyses == 68:
                myscreen.refresh()
                myscreen.addstr(6, 3, " "*25)
                left_key_press -= 1
                    #
                    # .

                if left_key_press < 0:
                    left_right = car_class_obj.turn(left_key_press)
                    right_key_press = 0
                        #
                        # .

                priborka(left_side = left_right)
                car_class_obj.show_speed()
                    #
                    # .

            if keyses == 32:
                car_type_menu()
                    #
                    # .

            if keyses == 27:
                keys_map()
                    #
                    # .

            if keyses == 49:
                car_select = 1
                WorkCar_class_obj.show_speed()
            if keyses == 50:
                car_select = 2
                TownCar_class_obj.show_speed()
            if keyses == 51:
                car_select = 3
                PoliceCar_class_obj.police_car()
            if keyses == 52:
                car_select = 4
                SportCar_class_obj.sport_car()
                    #
                    # .
            else:
                myscreen.refresh()
                #
                # .
        elif keyses == 113:
            myscreen.addstr(8, 2, f"For EXIT press [ENTER]:        ")
            gs = myscreen.getch(8, 26)
                #
                # .

            if gs == 10:
                break
                #
                # .
            else:
                myscreen.addstr(8, 3, " "*35)
                myscreen.addstr(8,3, "Продолжаем... жмем на кнопки!")
                keyses = myscreen.getch(9, 35)
                myscreen.refresh()
                continue

finally:
    #
    # .
    myscreen.refresh()
    myscreen.clear()
    curses.endwin()
        #
        # .

