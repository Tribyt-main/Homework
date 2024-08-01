# Библиотека
my_dict = {'Alek': 08.03, 'Elena': 09.05, 'Marsel': 07.04}
print(my_dict)
print(my_dict['Elena'])
print(my_dict.get('Anton'))
my_dict.update({'Oleg': 11.01,
               'Ilya': 14.02})
print(my_dict.pop('Oleg'))
# Множества
my_set = [1, 3.5, 7, 2, 8, 5, 'Ok']
print(my_set)
my_set = set(my_set)
my_set.add('no'), my_set.add(27)
my_set.discard(1)
print(my_set)
