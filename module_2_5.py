def get_matrix(n, m, value):
    matrix = []
    for i in n, m, value:
        if i == m:
            matrix = [value]*m
    for j in n, m, value:
        if j == n:
            matrix = [matrix] * n
            print(matrix)
            break
get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
