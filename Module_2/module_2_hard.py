import random
random_number = random.randint(15, 15)
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = ''
for x in numbers_1:
    for i in numbers_1:
        if random_number % (x + i) == 0 and x < i:
            a += str(x) + str(i)
            # if x != i:
            #     if x > i:
print(random_number, '-', a)

15 - 1214114232133124115106978