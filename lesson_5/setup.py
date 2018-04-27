"""
name         - название пакета
version      - версия пакета (0.0.0)
description  -
url          - URL-адрес сайта
license      - Лицензия (BSD, Apache, GPL etc.)
author       -
author_email - E-mail автора
packages     - пакеты, которые нужно скопировать
            (без рекурсии, необходимо указать явно вложенные пакеты)
py_modules   - модули, которые нужно скопировать (без пакета)

scripts      - запускаемые из командной строки скрипты

install_requires - зависимости пакета от других пакетов (в первую очередь для пакетного менеджера)



запуск установки: утилита
Пакетный менеджер - pip
"""

from setuptools import setup

setup(
    name='mega-math',
    version='0.0.1',
    description='Collection of math formulas',
    url='',
    license='Apache-2.0',
    author='Konstantin Omelchuk'
    author_email=''
    packages=[
        'mega_math',
    ]
)    


"""
если что то не ставится через pip - первым делом обновлять pip
если ошибка осталась - разбираться с ошибкой
"""
