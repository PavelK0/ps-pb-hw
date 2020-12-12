import os

os.system('clear')

count, summ = 0, 0

for i in range(1000,20001):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        summ += i

print(f'В диапазоне [1000,20000] всего {count} чисел делятся и на 3, и на 5. Их сумма - {summ}.')
