# Задание-7.
#
# Описание:
#
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
#
# .


""


class ComplexClass:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __add__(self, other):
        return f'Сумма чисел complex_1 и complex_2: {self.__a + other.a} + {self.__b + other.b}i'

    def __mul__(self, other):
        return f'Произведение complex_1 и complex_2: {self.__a*other.a - (self.__b*other.b)} + {self.__b*other.a}i'

    def __str__(self):
        return f'Комплексное число: {self.__a} + {self.__b}i'


complex_1 = ComplexClass(2, 5)
complex_2 = ComplexClass(8, -4)
print(complex_1)
print(complex_2)

sum_complex = complex_1 + complex_2
print(sum_complex)

mult_complex = complex_1*complex_2
print(mult_complex)
