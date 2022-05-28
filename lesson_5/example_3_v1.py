# Задание-3.
#
# Описание:
# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
#
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#

""
import os
"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
ВАРИАНТ-1
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""

path2file = r'./less5_test_files' # указываем путь для размещения файлов с данными
if not os.path.exists(path2file): # проверяем, создана директория по указанному пути или нет, если нет, тогда...
    os.mkdir(path2file) # создаем директорию по указанному пути
    print("Директория создана")
else:
    print("Создание директории не требуется")

file_test = os.path.join(path2file,"lesson_test_3.txt")
    # объединяем путь до локации и наименование файла, который планируем обрабатывать

with open(file_test,'r',encoding="utf-8") as file_str: # открываем файл в режиме только чтение, с указанием его пути
    file_str.seek(0)
        # переводим курсор на начало файла
        # .
    file_text = file_str.readlines()
        # считываем данные из файла и размещаем в объекте типа Строка
        # .
list_salary=[]
    # подготавливаем Список для сбора показателей ЗП сотрудников,
    # .
list_name4min=[]
    # подготавливаем Список для сбора фамилий сотрудников,
    # чья ЗП ниже 20.000
    # .

def find_results(vals):
    """ Функция-1 "Расчет зарплаты" """

    result_line = vals.replace('\t','').replace('\n','')#.replace('-',' ')
    result_line = result_line.split('-')
        # выполнили очистку полученной строки, и ее разбиение по разделителю "-"
        # результат размещаем в объекте Списка
        # .
    salary = float(str(result_line [ 1 ]).replace(',', '.'))
        # подготавливаем строку и выполяем преобразование,
        # полученного значения в вещественный тип
        # .

    if salary < 20000.00:
        # Проверяем показатели зарплат == salary == сотрудников
        # в случаях, когда ЗП ниже 20.000, выполняем блок if
        # .
        list_name4min.append(result_line[0])
            # формируем список из фамилий сотрудников,
            # зарплата которых ниже 20.000
            # .

    list_salary.append(salary)
        # добавляем полученные значения зарплат в Список
        # .
    return
        # функция возвращает None
        # .

list(map(find_results, file_text))
    # через функцию map перебираем элементы Списка == file_text ==
    # и передаем их функции el_format
    # .
print("")
print("СПИСОК СОТРУДНИКОВ С ЗАРПЛАТОЙ МЕНЕЕ 20.000")
print("<>"*25)
for k in list_name4min: print(k)
    # выводим в консоль фамилии всех сотрудников,
    # зарплата которых, менее 20.000
    # .

print("")
print("<>"*25)
print("Средняя величина дохода сотрудников == ", round(sum(list_salary)/len(list_salary),2))
    # выполняем вычисление количества элементов в списке list_salary
    # (там собраны значения всех зарплат)
    # суммируем все значения в списке list_salary и вычисляем
    # среднюю величину ДОХОДА сотрудников
    # Результаты вычислений выводим в консоль
    # .