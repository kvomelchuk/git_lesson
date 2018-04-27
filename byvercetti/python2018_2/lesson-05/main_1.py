# Модули и пакеты

# 1. Импорт модуля "целиком"
import os.path
import square_shapes

# 2. Частичный импорт
from square_shapes import (
    calculate_rectangle_area,
    calculate_circle_area as calc_circle_area
)
from os import path as Path

# 3. Импорт * (все имена из модуля)
from square_shapes import *

print(square_shapes.calculate_square_area(5))
print(square_shapes.calculate_rectangle_area(4, 3))

os.path.basename('/home/itmo/1.txt')

print(calculate_rectangle_area(7, 8))


if __name__ == '__main__':
    print('Будет работать только если модуль используется как исполняемый (главный)')



