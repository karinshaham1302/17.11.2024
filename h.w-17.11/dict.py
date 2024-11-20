israel_info = {'name': 'Israel', 'birth': 1948,
               'population_millions': 9.3, 'capital': 'Jerusalem', 'language': 'Hebrew',
               'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
               'currency': 'ILS', 'area_Kilometer': 22_145, 'gdp_billion': 450}

# a
print('The capital city is:', israel_info.get('capital'))

# b
print('All the keys in the dict:', list(israel_info.keys()))

# c
print('All the values in the dict:', list(israel_info.values()))

# d
for key, value in israel_info.items():
    print(f'{key}: {value}')

# e
new_israel_info = israel_info.copy()
print('new dict:', new_israel_info)

# f
print('removed gdp_billion:', new_israel_info.pop('gdp_billion'))
print(new_israel_info)

# g
new_dict = dict.fromkeys(israel_info.keys())

new_dict['name'] = input('Enter the country name:')
new_dict['birth'] = int(input('Enter the birthday:'))
new_dict['population_millions'] = float(input('Enter the population:'))
new_dict['capital'] = input('Enter the capital city:')
new_dict['language'] = input('Enter the language:')
new_dict['currency'] = input('Enter the currency:')
new_dict['area_Kilometer'] = int(input('Enter the area_Kilometer:'))
new_dict['gdp_billion'] = int(input('Enter the gdp_billion:'))

cities = []
for i in range(3):
    city = input(f'Enter 3 cities:, {i + 1}')
    cities.append(city)
new_dict['cities'] = cities

print('The new update dict:', new_dict)
