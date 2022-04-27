from example_6_v1 import gen_list_func
    # Импортируем функцию из ранее созданного модуля example_6_v1.py
from itertools import cycle, count

get_list = gen_list_func()
iter_cycle = cycle(get_list)

usr_recycle = int(input("Укажите количество повторений: "))

for k in range(0,usr_recycle):

    if k <= usr_recycle:
        print("")
        print(f"<><><><>Повторение №_{k+1}_<><><><>")

        for iter_i in range(0,len(get_list)):
            print(next(iter_cycle))

    else:
        break
