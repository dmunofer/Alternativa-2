sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def resolver(sudoku):
    find = encontrar_vacia(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valido(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if resolver(sudoku):
                return True

            sudoku[row][col] = 0

    return False

def valido(sudoku, num, pos):
    # Check row
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sudoku[i][j] == num and (i,j) != pos:
                return False

    return True

def mostrar_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")