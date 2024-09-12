def chek_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O':
        return 'O'
    if area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O':
        return 'O'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O':
        return 'O'
    return '*'


def draw_area():
    for item in area:
        print(*item)


area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики-нолики')
print('----------------------------------')
draw_area()
for turn in range(1, 10):
    print(f'Ход {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('Ходит нолик!')
    else:
        turn_char = 'X'
        print('Ходят крестики!')
    row = int(input('Введите номер строки (1,2,3)\n')) - 1
    column = int(input('Введите номер столбца (1,2,3)\n')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
        draw_area()
    else:
        print('Ячейка уже занята, вы пропускаете ход!')
        draw_area()
        continue
    if chek_winner() == 'X':
        print('Победа крестиков!')
        break
    if chek_winner() == 'O':
        print('Победа ноликов!')
        break
    if chek_winner() == '*' and turn == 9:
        print('Ничья')
