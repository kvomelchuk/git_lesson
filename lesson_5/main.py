#Пакеты

#полностью
import mega_math.square_shapes

#частично (как правило из пакетов импорты частичные)
from mega_math import square_shapes
square_shapes.calculate_circle_area(10)

from mega_math.square_shapes import calculate_triangle_area
calculate_triangle_area(1, 2, 3)


#относительный импорт (позже)
#не работает в исполняемом (главном) модуле!
# from . import module_name
# from .module_name import func_name
# from ..parent_module import class_name

from mega_math import calculate_rectangle_area


# как делиться пакетами и получать сторонние пакеты - нужен файл-манифест setup.py
