﻿# Однострочный комментарий

'''
Многострочный комментарий
'''

"""
Многострочный комментарий
"""

# 1. Как объявить переменную?
"""Переменная - поименованная область оперативной памяти,
				из которой данные можно прочитать
				или в которую их можно записать
a
A
это разные переменные

PEP-8 - прочесть - правила хорошего кода
				
"""

#на имена переменных накладываются ограничения - only латиница, цифры, _, не с цифры

username = 'root' # присвоить значение переменной
print(username)

username = 'kilemal' # присвоить новое значение
print(username)


# Какие типы данных существуют в Python?

"""
Тип данных переменной является ее характеристикой
и описывает следующее:
- количество памяти
- диапазон допустимых значений
- допустимые операции над переменной
- формат отображения (для человека)
- 

1. Простые типы данных (скалярные)
- в один момент времени хранят одно значение
    - int     - целое число
	- float   - число с плавающей точкой
	- bool    - логическое значение
	- complex - комплексное число - узнать что это и для чего предназначены
	- str     - строка
	- bytes   - (Py3) - байтовая строка
2. Структурные (составные, сложные) типы данных
- в один момент времени хранят любое количество значений любого типа
    - tuple  - кортеж
	- list   - список
	- set    - множество
	- dict   - словарь
	- object - объект
3. Специальные типы данных
    - None - пустота, отсутствие значения
"""

# декларация и инициализация, нельзя просто декларировать, всегда нужно инициализировать, как написано ниже строкой

a = None


# bool - логическое значение
flag1 = True
flag2 = False

# int
i1 = 666
i2 = 0b011001 # пример записи двоичного числа (конструкция 0b)
i3 = 0o743    # пример записи 8- числа (конструкция 0o)
i4 = 0xaf     # 16

# float
f1 = 1.22
f2 = 1e-3 # экспонента для записи длинных чисел (с минусом дробное, количество нулей после запятой, без знака - количество нулей до запятой)

# complex
c1 = 3.14j


# str

s1 = 'str"ing'
s2 = "str\"ing \\\!!!"    # знак \ - знак экранирования
s3 = '''
	много"стр'очная 
	строка
'''
print(s3)

s4 = """
helka
belka
"""

# регулярные выражения для сложных примеров
s5 = r'^\d+jglsb' # сырая строка (raw)
print(s5)

s6 = u'Unicode in Python 2'

# bytes

s7 = b'Hello' # байты, поток данных без кодировки