first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zp = zip(first, second)
first_result = (len(item[0]) - len(item[1]) for item in zp if
                len(item[0]) != len(item[1]) and len(item[0]) > len(item[1]))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
