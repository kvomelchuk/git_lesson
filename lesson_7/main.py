# Базы данных - SQLite3

import sqlite3

# 1. подключение к БД
conn = sqlite3.connect('db.sqlite')


# 2. создание объекта курсора
cursor = conn.cursor()

# 3. Выполнить SQL-запрос к БД
sql = '''
    CREATE TABLE shortener (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL DEFAULT '',
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
'''
#cursor.execute(sql)

#conn.commit()

sql = '''
    INSERT INTO shortener (
        original_url
    ) VALUES (?)  
'''
#колонки перечисляются через запятую
#символ ?
#все данные необходимо очищать, т.к. можно пропустить sql-injection

cursor.execute(sql, ('http://profi.itmo.ru',)) # признак кортежа - ','
# указанное в курсоре значение встанет на место '?'
conn.commit()

sql = '''
    SELECT
        id, original_url, short_url, created
    FROM
        shortener
'''

cursor.execute(sql)


result = cursor.fetchall()
print(result)

# закрытие соединения после работы с бд
conn.close()





# Контекстный менеджер!!!

with sqlite3.connect('db.sqlite') as conn:
    sql = 'SELECT * FROM shortener'
    cursor = conn.execute(sql)
    print(cursor.fetchall())
