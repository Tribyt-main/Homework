my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
item = 0
while True:
    if my_list[item] == 0:
        item = item + 1
    elif my_list[item] < 0:
        break
    else:
        print(my_list[item])
        item = item + 1
