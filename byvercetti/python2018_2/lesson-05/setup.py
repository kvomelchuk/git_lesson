"""
name         - название пакета
version      - версия пакета (0.0.0)
description  - описание пакета
url          - URL-адрес сайта
license      - Лицензия
author       - Имя автора
author_email - E-Mail автора

packages   - пакеты, который нужно скопировать
             (без рекурсии, необходимо указать вложенные пакеты)
py_modules - модули, которые нужно скопировать

scripts    - запускаемые из командной строки скрипты

install_requires - зависимости пакета от других пакетов


Утилита
Пакетный менеджер - PIP
"""

from setuptools import setup

setup(
    name='mega-math',
    version='0.0.1',
    description='Collection of mathematical formulas.',
    url='https://github.com/user/mega-math',
    license='Apache-2.0',
    author='Kirill Vercetti',
    autho_email='office@kyzima-spb.com',
    packages=[
        'mega_math',
    ]
)