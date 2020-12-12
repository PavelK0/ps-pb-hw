import os

os.system('clear')

fb1, fb2 = 1, 1
i_count = 2
even_count = 0

while fb2 <= 10000000:
    fb3 = fb1 + fb2
    if fb3 <= 10000000:
        fb1 = fb2
        fb2 = fb3
        i_count += 1
        if fb3 % 2 == 0:
            even_count += 1
            print(fb3)
    else:
        print(f'Всего в последовательности {i_count} элементов, из них {even_count} - чётных, предпоследний элемент последовательности - {fb1}.')
        fb2 = 10000001
