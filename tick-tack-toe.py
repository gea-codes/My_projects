def greet():
    print("    Давай сыграем ")
    print("  в крестики-нолики! ")
    print("  ------------------ ")
    print("     Введи x, y ")
    print("  x - номер строки ")
    print("  y - номер столбца ")

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        cords = input("    Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите две координаты! ")
            continue
        x, y = cords
        if not(x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" Место занято! ")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),((0,2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print(" Победил X! ")
                return True
            if symbols == ["0", "0", "0"]:
                print(" Победил 0! ")
                return True
    return False

greet()
field = [[" "]*3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()
    if num % 2 == 1:
        field [x][y] = "X"
    else:
        field [x][y] = "0"

    if check_win():
        break
    if num == 9:
        print(" Ничья! ")
        break