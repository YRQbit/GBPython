# Задание-1.
#
# Описание:
# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
#
# .


""
from random import randint

"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-4
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""

class Matrix:

    def __init__(self, matrix_lists):
        self.len_matrix = len(matrix_lists)
        if 0 <= self.len_matrix < 2:
            self.matrix_list = matrix_lists
        else:
            self.list_matrix = matrix_lists

    def __str__(self):
        if hasattr(self,'list_matrix'):

                print(f"Размерность {self.len_matrix}x{len(self.list_matrix[0])}")
                return str("".join(f"{k}\n" for k in self.list_matrix)).replace("[",'').replace(",",'').replace("]",'')
        else:
            print(f"Размерность {self.len_matrix}x{len(self.matrix_list[0])}")
            s,*d = self.matrix_list [ 0 ]
            return f"{s} "+" ".join(str(d_num) for d_num in d)

    def __add__(self, other):
        # Складывать матрицы можно только одинаковой размерности!
        if hasattr(self, 'list_matrix'):
            if (self.len_matrix == len(other.list_matrix)) and (len(self.list_matrix[0]) == len(other.list_matrix[0])):
                result = [ [ self.list_matrix [ i ] [ j ] + other.list_matrix [ i ] [ j ] for j in range(len(self.list_matrix [ 0 ])) ] for i in range(len(other.list_matrix)) ]
                return str("".join(f"{res}\n" for res in result)).replace("[", '').replace(",", '').replace("]",'')  # f"Матрицы одинаковой размерности, можно складывать..."
            else:
                return f"Суммирование матриц разной формы не допускается"
        else:
            try:
                if (self.len_matrix == len(other.matrix_list)) and (len(self.matrix_list[0]) == len(other.matrix_list[0])):
                    result = [ [ self.matrix_list [ i ] [ j ] + other.matrix_list [ i ] [ j ] for j in range(len(self.matrix_list [ 0 ])) ] for i in range(len(other.matrix_list)) ]
                    return str("".join(f"{res}\n" for res in result)).replace("[", '').replace(",", '').replace("]",'')  # f"Матрицы одинаковой размерности, можно складывать..."
                else:
                    return f"Суммирование матриц разной формы не допускается"
            except AttributeError:
                return f"Суммирование матриц разной формы не допускается"


row_count_1 = int(input("Укажите количество строк матрицы №_1: "))
col_count_1 = int(input("Укажите количество столбцов матрицы №_1: "))

row_count_2 = int(input("Укажите количество строк матрицы №_2: "))
col_count_2 = int(input("Укажите количество столбцов матрицы №_2: "))

list_num_1 = [ [ randint(0, 100) for i in range(0, col_count_1) ] for k in range(0, row_count_1) ]
list_num_2 = [ [ randint(-50, 50) for j in range(0, col_count_2) ] for q in range(0, row_count_2) ]


print("")
print("<>"*25)

matrix_class_obj_1 = Matrix(list_num_1)
print("matrix_class_obj_1 == ",matrix_class_obj_1)

matrix_class_obj_2 = Matrix(list_num_2)
print("matrix_class_obj_2 == ",matrix_class_obj_2)

matrix_str = matrix_class_obj_1 + matrix_class_obj_2
print("Сумма матриц == \n", matrix_str)




