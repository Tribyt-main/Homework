def print_params(a=1, b='string', c=True):
    print(a, b, c)

values_list = ['ok', 1, False]
values_dict = {'a': 2, 'b': 'dict', 'c': False}
values_list_2 = [1, True]
print_params(*values_list_2, 42)
print_params(**values_dict)
print_params()
print_params(1, 2, 3)
print_params(b= 1)
print_params(c = [1, 2, 3])