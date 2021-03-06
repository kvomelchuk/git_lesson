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

is1 = 'str"ing'
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


# tuple - кортежи - неоднородные данные, описание сущности, его характеристик (есть индекс)

t1 = (1, 1.5, True, 'string', (1, 2, 3))
print(t1[3])

t2 = (444,)

# list - списки - для однородных данных
l1 = [(1,), [2], 'str']
print(l1[0])     # => (1,)
print(l1[0][0])   # => 1
l1[0] = False
print(l1[0])     # => False


# set  - множество
s1 = {1, 2, 3, 3, 2}


# dict - словари (самые быстрые в питоне) словари из переменных
d1 = {
    'id': 1,
    'name': 'Linus',
    'skills': ('C++', 'Linux'),
    'address': {
        'street': ''
    }
}
print(d1['id'])    # => 1
print(d1['name'])  # => Linus
print(d1['address']['street'])
d1['any'] = 123



# Как определить тип данных переменной?
print(type(d1))


# Как выполнить явное приведение переменной к типу?

i = '666'
i = int(i)
print(i, type(i)) # 666, int

"""
# Типы данных бывают изменяемые и неизменяемые
# immutable (неизменяемые):
- bool, int, float, str, complex, bytes, tuple
- mutable (изменяемые):
- list, dict, set, object


- склеивание символов - 1. сначала список символов, 2. склеивание
"""

# Какие операторы существуют в python?
"""
операторы позволяют выполнять операции над переменными

Арифметические: + - * / %() **(степень) //(часть от деления)
Сравнения:      == != <> < > <= >=
Присваивания:   = +=(+1) -=(-1) *= %= **= //=

(++i, --i - унарные операции смены знака)

Логические:     and or not
Побитовые:      &(and) |(or) ~(not) ^(xor) << >> (сдвиги) (джипеги, mp3 и тд)
Принадлежности: in
                not in

-- проверка ключа в словаре - очень быстрая операция через in/not in
Тождественности:is - True если ссылка на одно и то же значение, и одна переменная = другая переменная
                нельзя писать для переменной None через ==, только через is
                not is
"""

# Ветвление

a = 1
b = 2
if a < b:           # обязательный блок
    print('a < b')
elif a == b:        # необязательный блок
    print('a = b')
# если нужен пустой блок кода:
elif a is b:
    pass # пустой блок кода
else:               # необязательный блок
    print('fuck off')



# Тернарный оператор
if True:
    username = 'Вася'
else:
    username = 'Petya'

username = 'Vasya' if True else 'Petya' # использовать в простых инструкциях



# Циклы
"""
только циклы с предусловием
"""

i = 0
while 1:            # явно писать не нужно условие, здесь 0 или <пусто> это False, все остальное True
    if i % 1:
        continue # пропускает текущую итерацию (не приветствуется)
    print(i)
    if i == 10:
        break # мгновенное завершение цикла (когда неизвестен момент завершения цикла - обработка завершения работы цикла)
    i += 1



lst = [1, 2, 3]
for i in lst:               # перебор списка
    print('Элемент списка:', i)


for i in range(10): # десятка в промежуток не включается
    print(i)
    

for i in range(10, ): # 15 в промежуток не включается
    print(i)

for i in range(10, 21, 2): # с шагом 2 (start, end, шаг)
    print(i)

for i in enumerate(range(10, 21, 2)): # с шагом 2 (start, end, шаг)
    print(i)


# for key, value in enumerate # распаковка кортежа в переменные и уже действовать с переменными
      
for i in d1:
    print(i, d1[i]) # не питон

for key, value in d1.items():
    print(key, value)



# Срезы
"""
s[first_index:last_index]
we can delete first_index [:m] when cut from first to some
similar for last_index - [n:] for cutting from end
and step (third position in []
-1 step - playback of string
"""

l = [1, 2, 3, 4, 5]

l = list(range(10))
"""
cutting for lists is like cutting for
"""

"""
Функции дл рвботы со списками и методы списков
len(l) - длина списка
l.append(e) - добавить элемент в конец списка
l.insert(index, e) - добавить элемент в указанную позицию

подсказка: лучше воткнуть в конец списка и перевернуть один раз

как превратить список в строку (пользоваться всегда): print(''.join(s)) # '' - символ разделителя
join принимает как список последовательность (строку)


связка append и pop работает со списком как со стеком

Методы списков:
https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html



Строковые функции - домашнее изучение
Домашнее задание:
1. Сделать отдельный репозиторий для ДЗ
2. Вся ДЗ проверяется через Git
3. Система баллов - каждая задача имеет стоимость в баллах
4. Табель на GoogleDocs
5. 3-4 задачи на каждую ДЗ
6. Система автопроверки - можно самому проверить

int(input())
Для себя - надо изучить библиотеки
"""

