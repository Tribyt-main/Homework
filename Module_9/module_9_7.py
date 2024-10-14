def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, (result // 2) + 1):
            if result % i == 0:
                return f'Составное\n{result}'
            else:
                return f'Простое\n{result}'

    return wrapper


@is_prime
def sum_three(*args):
    it = list(args)
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
