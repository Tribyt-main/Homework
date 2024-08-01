immutable_var = 1, 2, 'a', 'b', True
print(immutable_var)
# immutable_var[0] = 200
# print(immutable_var)

# Не допустимо изменять отдельные элементы в кортеже

mutable_list = [1, 2, 'a', 'b', True]
print(mutable_list)
mutable_list[0] = 64
mutable_list[-1] = False
print(mutable_list)
mutable_list = mutable_list + ['alek', False]
print(mutable_list)
mutable_list = mutable_list*2
print(mutable_list)
