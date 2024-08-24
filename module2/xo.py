def creat_field(x, y):
    field = []
    for i in range(x):
        field.append ([])
        for j in range(y):
            field[i].append('.')
    return field

def draw_field(field):
    print()
    for line in field:
        print(*line)
    print()

def check_win(field, size, player):
    #по строкам
    for line in field:
        win = True
        for item in line:
            if item != player:
                win = False
                break;
        if win:
            return True
    #по столбцам
    for col in range(size):
        win = True
        for row in range(size):
            if field[row][col] != player:
                win = False
                break;
        if win:
            return True
    #по диагонали
    win1 = True
    win2 = True
    for i in range(size):
        if field[i][i] != player:
            win1 = False
        if field[size - 1 - i][i] != player:
            win2 = False
    if win1 or win2:
        return True
    return False

def chech_step(field, x, y):
    if field[x][y] != '.':
        return False
    return True

size = 3
field = creat_field(size, size)

player = 'O'
while not check_win(field, size, player):
    draw_field(field)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    print(f'Ход {player}')
    while True:
        row = int(input('Номер строки: '))
        row_ = row - 1
        col = int(input('Номер столбца: '))
        col_ = col - 1
        if row_ > size or col_ > size:
            print(f'Поле {row}-{col} не найдено')
            continue
        if chech_step(field, row_, col_):
            break
        print(f'Поле {row}-{col} занято')
    field[row_][col_] = player

draw_field(field)
print(f'Выйграли {player}')