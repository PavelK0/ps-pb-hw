import os

os.system('clear')

def plural_form(quantity, form1, form2, form3):

    if 10 <= quantity % 100 <= 19 or 5 <= quantity % 10 <= 9 or 10 <= quantity <= 19:
        print(f'{quantity} {form3}')
    elif 2 <= quantity % 10 <= 4:
        print(f'{quantity} {form2}')
    elif quantity % 10 == 1 and not 10 <= quantity <= 20:
        print(f'{quantity} {form1}')
    else:
        print(f'{quantity} {form3}')

for i in range(0,139):  
    plural_form(i, 'яблоко', 'яблока', 'яблок') 
  