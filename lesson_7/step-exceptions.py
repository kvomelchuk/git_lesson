# Exception - исключение


try:
    i = int(input())
    # print(i[0])

except ValueError:
    print('Переделывай, некорреткное число!')
except:
    print('Любое исключение было отловлено')
finally:
    print('Выполняется всегда')

    
raise KeyError('Мое сообщение об ошибке')
