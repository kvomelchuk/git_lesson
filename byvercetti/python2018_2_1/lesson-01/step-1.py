# Однострочный комментарий

'''
Многострочный комментарий
'''

"""
Многострочный комментарий
"""

# 1. Как объявить переменную?
""" Переменная - поименованная область оперативной памяти
                 из которой данные можно прочитать
                 или в которую их можно записать
PEP-8
"""

username = 'root' # присвоить значение переменной
print(username)

username = 'toor' # присвоить новое значение
print(username)


# Какие типы данных существуют в Python?

"""
Тип данных переменной является ее характеристикой
и описывает следующее:
- кол-во памяти
- диапазон допустимых значений
- допустимые операции над переменной
- формат отображения (для человека)
-

1. Простые или скалярные типы данных
- в один момент времени хранят одно значение
  - int     - целое число
  - float   - число с плавающей точкой
  - bool    - логическое значение
  - complex - комплексное число
  - str     - строка
  - bytes   - only Py3 - байтовая строка
2. Структурные (составные, сложные) типы данных
- в один момент времени хранят
  любое кол-во значений любого типа
  - tuple - кортеж
  - list  - список
  - set   - множество
  - dict  - словарь
  - object - объекты
3. Специальные типы данных
  - None - пустота, отсутствие значения
"""

a = None


# bool    - логическое значение
flag1 = True
flag2 = False


# int     - целое число
i1 = 666
i2 = 0b10101
i3 = 0o755
i4 = 0xaf

# float
f1 = 1.23
f2 = 1e-3 # 0.001
f3 = 1e6  # 1000000.0

# complex
c1 = 3.14j


# str

s1 = 'str"ing'
s2 = "str\"ing \\!!! \\n"
s3 = '''
    Много"стр'очная строка

'''
s4 = """
    Многострочная строка
"""

s5 = r'^\d+$' # сырая строка (raw)
s6 = u'Unicode in Python 2'

# bytes

s7 = b'Hello'


# tuple - кортежи
t1 = (1, 1.5, True, 'string', (1, 2, 3))
print(t1[3])
t2 = (546,)

# list - списки
l1 = [(1,), [2], 'str']
print(l1[0])    # => (1,)
print(l1[0][0]) # => 1
l1[0] = False
print(l1[0])    # => False

# set - множества
s1 = {1, 1, 2, 2, 3, 3}
s2 = set() # пустое множество

# dict - словари
d1 = {
    'id': 1,
    'name': 'Linus',
    'is_developer': True,
    'skills': ('C++', 'Linux'),
    'address': {
        'street': s2
    }
}
print(d1['id'])   # => 1
print(d1['name']) # => Linus
print(d1['address']['street'])
d1['any'] = 123


# Как определить тип данных переменной?
print(type(d1))


# Как выполнить явное приведение переменой к типу?
i = '666'
i = int(i)
print(i, type(i)) # 666, int


"""
Типы данных бывают изменяемые и неизменяемые
immutable (неизменяемые):
- bool, int, float, str, complex, bytes, tuple
mutable (изменяемые):
- list, dict, set, object
"""


# Какие операторы существуют в Python?
"""
Арифметические:  + - * / % ** //
Сравнения:       == != <> > < >= <=
Присваивания:    = += -= *= %= **= //=
Логические:      and or not
Побитовые:       & | ~ ^ << >>
Принадлежности:  in
                 not in
Тождественности: is
                 not is
"""


# Ветвление

a = 1
b = 2

if a < b:
    print('a < b')
elif a == b:
    print('a = b')
elif a is b:
    pass # пустой блок кода
else:
    print('a > b')


# Тернарный оператор

if True:
    username = 'Вася'
else:
    username = 'Петя'

username = ['Вася'] if True else 'Петя'

# Циклы

i = 0

while 1:
    i += 1

    if i % 2:
        continue # пропускает текущую итерацию

    print(i)

    if i == 10:
        break # мгновенное завершение цикла


lst = [1, 2, 3]

for i in lst:
    print('Элемент списка:', i)


for key, value in enumerate(range(10, 21, 2)):
    print(key, value)


for key, value in d1.items():
    print(key, value)



"""
Функции для работы со списками и методы списков
len(l) - длина списка
l.append(e) - добавить элемен в конец списка
l.insert(index, e) - добавить элемент в указанную позицию
"""

lst = list(range(10))
print('Длина списка:', len(lst))
lst.append(10)
lst.insert(0, -1)
lst.insert(1000, -1)
print(lst)


s = []

for c in range(ord('a'), ord('z') + 1):
    s.append(chr(c))

print(''.join(s))

int(input())



