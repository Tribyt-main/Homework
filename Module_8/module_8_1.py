def add_everything_up(a, b):
    try:
        sum_1 = a + b
        if type(sum_1) == float:
            return f'{sum_1:.3f}'
    except TypeError:
        return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
