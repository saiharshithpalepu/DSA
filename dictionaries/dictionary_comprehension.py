import random
city_names=['paris','london','berlin','rome','madrid']
city_temps={city:random.randint(20,30) for city in city_names}
print(city_temps)

new_dict={key:value for (key,value) in city_temps.items() if value>25}
print(new_dict)