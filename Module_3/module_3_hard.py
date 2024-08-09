data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def open1():
    global w, q, e, r, t, len_c, len_d, hello
    for item1 in data_structure:
        if item1 == data_structure[0]:
            q = data_structure[0]
        if item1 == data_structure[1]:
            w = data_structure[1]
            e = data_structure[1]
        if item1 == data_structure[2]:
            r, t = data_structure[2]
            len_c, len_d = t
        if item1 == data_structure[3]:
            hello = data_structure[3]
        if item1 == data_structure[4]:
            a = data_structure[4]
            list_ = []
            s, d = a
            f = set(*d)
            g = list(*f)
            z = [*g]
            x = list(z[2])
            print(len(w) + sum(q)
                  + e.get('b')
                  + e.get('a')
                  + r
                  + len(len_c)
                  + len(len_d)
                  + t.get(len_c)
                  + t.get(len_d)
                  + len(hello)
                  + z[0]
                  + len(z[1])
                  + len(x[0])
                  + x[1])


open1()
