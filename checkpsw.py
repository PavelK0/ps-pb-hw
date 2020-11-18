psw = input('Введите пароль: ')

try:
    check = 1/len(psw)
    int(psw)
    print('Ваш пароль состоит только из цифр.')
except ZeroDivisionError:
    print('Вы ввели пустой пароль.')
except ValueError:
    print('Требования к паролю соблюдены.')
    
