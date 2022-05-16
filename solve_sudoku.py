mat = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

dirsX = [0, 0, 1, -1]
dirsY = [1, -1, 0, 0]

def nextValid():
    for i in range(9):
        for j in range(9):
            if mat[i][j] == ".":
                return i, j
    return -1, -1

def validate(ch, row, col):
    for i in range(9):
        if mat[i][col] == ch and row != i:
            return False
    
    for i in range(9):
        if mat[row][i] == ch and col != i:
            return False
    
    row //= 3
    col //= 3

    for i in range(row * 3, row * 3 + 3):
        for j in range(col * 3, col * 3 + 3):
            if mat[i][j] == ch and (row, col) != (i, j):
                return False
    return True

def solveIt(mat):
    row, col = nextValid()
    #no unassigned position is found, puzzle solved
    if row == -1 and col == -1:
        return True
    for num in range(1, 10):
        if validate(str(num), row, col):
            mat[row][col] = str(num)
            if solveIt(mat):
                return True
            mat[row][col] = "."
    return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(mat)
print(solveIt(mat))
print()
print_board(mat)