# Задание-1
#
# Описание:
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк, и сохраните
# в переменные, выведите на экран.
#
# Задачи:
# 1. создать несколько (мин. 1 шт) == int == переменных;
# 2. создать несколько (мин. 1 шт) == float == переменных;
# 3. создать несколько (мин. 2 шт) == str == переменных;
# 4. запросить ввод данных у пользователя (для каждой
# переменной свой запрос) и сохранить данные в соответствующих
# переменных;
#
# Ожидаемый результат:
# 1. Вывод в консоль строки ==> Hi Mir <==;
# 2. В консоли запросить у пользователя ввод == int == числа;
# 3. В консоли запросить у пользователя ввод == float == числа;
# 4. В консоли запросить у пользователя ввод == str == строки;
# 5. Результаты ввода пользователя, вывести в консоль в том же порядке;
# .

print(" ")
print("<>"*8)
print('Hi mir'.center(13))
print("<>"*8)
print(" ")

var_int =  int(input("Введите целое число (пример: _10____): "))
var_float = float(input("Введите вещественное число (пример: _10.234_): "))
var_str_v1 = str(input("Введите начало произвольной фразы (пример: _начало строки_): "))
var_str_v2 = str(input("Введите продолжение произвольной фразы (пример: _содержит продолжение_): "))
var_str_v3 = str(input("Введите завершающую часть произвольной фразы (пример: _ и свою точку._): "))
print("<>"*25)

print(" ")
print("Введено число __",var_int,"____")
print(f"Введите число __{var_float}____")
print("Введена строка " + f"__{var_str_v1}____")
print("Введена строка __%s" % var_str_v2 + "____")
print("Введена строка __%s" % var_str_v2 + "____")
print("Введена строка __" + f"{var_str_v3}" + "____")
print("<>"*25)
print(" ")
