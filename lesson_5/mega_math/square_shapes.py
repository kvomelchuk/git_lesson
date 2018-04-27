"""
Модуль вычисления площадей геометрических фигур
"""
from math import pi as PI # создание псевдонима через "as <PName>"

# специальные переменные для решения проблем со * в вызывающем модуле:
_all_ = [
    'calculate_square_area', 
    'calculate_rectangle_area',
    'calculate_triangle_area',
    'calculate_circle_area', 
]

def calculate_square_area(a):
    """Возвращает площадь квадрата""" # комментарий документации
    return a ** 2


def calculate_rectangle_area(a, b):
    return a * b


def calculate_triangle_area(a, b, c):
    """Формула Герона"""
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0,5


def calculate_circle_area(r):
    return PI * r ** 2 # возведение в степень имеет более высокий приоритет

"""
если переменная пользуется как константа то пишется через КАПС в псевдониме
"""
