# Вариант №1 с сохранением исходного url

# def get_absolute_url(url, *args, **kwargs):

#     absolute_url = url # добавляем доменное имя
    
#     for i in args[0:]: # добавляем все позиционные аргументы args через символ "/"
#         absolute_url += '/' + i

#     absolute_url = absolute_url + '?' # добавляем символ "?" в конце всех позиционных аргументов

#     for k, v in kwargs.items(): # добавляем все именованные аргументы kwargs, ключ и значение разделяем символом "=", 
#                                 # после каждой пары ключ/аргумент добавляем символ "&"
#         absolute_url += k + '=' + v + '&'

#     return absolute_url[0:-1] # удаляем лишний (последний) символ "&" и выводим абсолютный путь

# Вариант №2 без сохранения исходного url

def get_absolute_url(url, *args, **kwargs):
    
    for i in args[0:]: # добавляем все позиционные аргументы args через символ "/"
        url += '/' + i

    url = url + '?' # добавляем символ "?" в конце всех позиционных аргументов

    for k, v in kwargs.items(): # добавляем все именованные аргументы kwargs, ключ и значение разделяем символом "=", 
                                # после каждой пары ключ/аргумент добавляем символ "&"
        url += k + '=' + v + '&'

    return url[0:-1] # удаляем лишний (последний) символ "&" и выводим абсолютный путь

import os

os.system('clear')

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
