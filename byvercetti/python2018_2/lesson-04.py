# Как объявить функцию?
# Функция - это блок кода,
# который можно вызывать многократно.

def hello():
    print('Hello!')

print(type(hello))
hello() # вызов функции
hello()

say_hello = hello
say_hello()


# Зачем функции аргументы?

def hello_username(name):
    print('Hello,', name)


hello_username('Python')
hello_username('JavaScript')
hello_username('Вася')

def summa(a, b):
    print(a + b)

summa(1, 3)
summa(5, 5)

# Передача значений аргументов по ссылке
def parse(src, output):
    src = src.strip('.')

    for i in src.split():
        output.append(i)

src = 'Python is programming language.'
lst = []

print(src, lst)
parse(src, lst)
print(src, lst)




# Как задать значение аргумента по умолчанию?
def poww(x, p=2):
    print(x ** p)

poww(5)
poww(2, 3)


def f(i, l=None):
    l = l or []


# Как вернуть значение из функции?

def minus(a, b):
    return a - b
    a = a * b # никогда не выполнится!!!

r = minus(1, 2)
r2 = minus(b=10, a=90)
print(r)

def f2():
    return 1, 2, 3

a, b, c = f2()


# Переменное количество аргументов в описании функции
def demo_func(i, *args, **kwargs):
    """
    args   - кортеж
    kwargs - словарь
    """
    print(i, args, type(args))
    print(kwargs, type(kwargs))


demo_func(1, 2, 3, j=4)
demo_func('10', '20', k=True, e=456)

def f3(i, *args, j=1, **kwargs):
    print(i, j, args)

f3(2, 5, 5, j=2, d={})

# Переменное количество аргументов при вызове функции
def f4(i, j, k, a=None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a': 10,
    'b': 20,
    'c': 30,
}
f4(*args, **kwargs)


# Анонимная функция

sqrt = lambda x: x ** 0.5
# lambda: pass
# lambda x, y: pass
print(sqrt(9))

def f5(x, cb):
    return cb(x)

print(f5(25, lambda x: x ** 0.5))
print(f5(25, lambda x: x ** x))


# Замыкания

# Функция каррирования
def trim(chars=None):
    # Область видимости (локальная) функции trim
    # Замкнутая область
    # def f(s):
    #     # Область видимости (локальная) функции f
    #     return s.strip(chars)
    # return f
    return lambda s: s.strip(chars)

spaces_trim = trim()
slashes_trim = trim('/\\')

print(spaces_trim('    Hello   '))
print(slashes_trim('////url//\\\\//'))


# Рекурсивная функция
# 5! = 1 * 2 * 3 * 4 * 5
def factorial(x):
    # Прямая рекурсия
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5))


# Косвенная рекурсия
# def a():
#     b()
#
# def b():
#     a()





g = 666

def wrapper():
    external = 777

    def func():
        global g
        nonlocal external

        g += 1
        external += 1

    func()

    print(g, external)

wrapper()




