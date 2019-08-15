# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 2):
        if cells[0][i] == cells[1][i] == cells[2][i] != 'O':
            return True
            print("'O' wins!")
            break
    return False

def check_row(cells):
    for i in range(0, 2):
        if cells[i][0] == cells[i][1] == cells[i][2] != 'O':
            return True
            print("'O' wins!")
            break
    return False

def check_diag(cells):
    for i in range(0, 2):
        if cells[i][j] == cells[i + 1][j + 1] == cells[i + 2][j + 2] != 'O':
            return True
            print("'O' wins!")
            break
    return False

def check_col(cells):
    for i in range(0, 2):
        if cells[0][i] == cells[1][i] == cells[2][i] != 'X':
            return True
            print("'X' wins!")
            break
    return False

def check_row(cells):
    for i in range(0, 2):
        if cells[i][0] == cells[i][1] == cells[i][2] != 'X':
            return True
            print("'X' wins!")
            break
    return False

def check_diag(cells):
    for i in range(0, 2):
        if cells[i][j] == cells[i + 1][j + 1] == cells[i + 2][j + 2] != 'X':
            return True
            print("'X' wins!")
            break
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
        break
    return False

turn = 0
    
cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)
while True:
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] == 'O':
        print("It is taken already")
    elif cells[row][col] == 'X':
        print("It is taken already")
    elif cells[row][col] == (3, 100000000):
        print("Wrong input")
    else:
        if turn == 0:
            cells[row][col] = 'X'
            turn = 1
        elif turn == 1:
            cells[row][col] = 'O'
            turn = 0
        printcell(cells)
        else:
            if cells = []:
                print("Draw...")
                break
