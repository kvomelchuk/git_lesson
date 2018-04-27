# modules & packages
"""
every file with .py extension is "module"


"""

# 1. импорт модуля "целиком"
import os.path # as Path # создание псевдонима через "as <PName>"
import square_shapes

# 2. частичный импорт
from square_shapes import (
    calculate_rectangle_area,
    calculate_circle_area,
    calculate_circle_area as calc_circle_area
) # скобки необязательны, но позволяют перенести на несколько строк частичный импорт

from os import path as Path # ущу один вариант вызова


# 3. Импорт * (все имена из модуля)
from square_shapes import * # так не делать


print(square_shapes.calculate_square_area(5))
print(square_shapes.calculate_rectangle_area(4, 3))

os.path.basename('/home/itmo/1.txt')


# после импорта можно делать вызов импортированной функции:
print(calculate_rectangle_area(7, 8, 9))


# как Py находит модули?
"""
отдаваемый интерпретатору (запускаемый в shell) модуль является главным (рабочим) модулем
походы только в пределах директории (включая поддиректории (пакеты))


#Совет дня: если после правок .py программа не изменилась, то значит закэшировались файлы .pyc
нужно их удалить


opt

python3 -0 main.py
python3 -00 main.py

"""

"""
домашечное:

ВНИМАНИЕ - модуль не должен ничего запрашивать и выводить на экран

_name_ - спецпеременная
"""

if _name_ == '_main_':
    print('эта команда будет работать только если модуль используется как исполняемый (главный)'


# Лекция 5 часть 2
# Пакеты
