import os

os.system('clear')

cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ').lower()

if tourists[0]['city'].lower() == city:
    counter = int(0)
elif tourists[1]['city'].lower() == city:
    counter = int(1)
elif tourists[2]['city'].lower() == city:
    counter = int(2)

city = city[:1].upper() + city[1:]

print(f"Турист {users[counter]['name']}, возраст {users[counter]['age']}. Посетил город {city}.")
