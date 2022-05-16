import pygame, time

class solve:

    def __init__(self, window, size, mat):
        self.window = window
        self.size = size
        self.gap = size[0] // 9
        self.mat = mat
        self.width = size[0]
        self.height = size[1]
        self.font = pygame.font.SysFont('consolas', 40)

        self.main()
    
    def createRect(self, pos, color):
        X, Y = pos
        x, y = X // self.gap, Y // self.gap
        x1 = 3 if x % 3 == 0 else 1
        x2 = 1 if (x + 1) % 3 == 0 else 0
        y1 = 3 if y % 3 == 0 else 1
        y2 = 1 if (y + 1) % 3 == 0 else 0
        if x == 0:
            x1 = 0
        if y == 0:
            y1 = 0
        pygame.draw.rect(self.window, color, (X + x1, Y + y1, self.gap - x2 - x1, self.gap - y2 - y1))
        pygame.display.update()
    
    def getPos(self, pos):
        x, y = pos
        x //= self.gap
        y //= self.gap
        return x * self.gap, y * self.gap
    
    def solveSudoku(self):
        
        def nextValid():
            for i in range(9):
                for j in range(9):
                    if self.mat[i][j] == 0:
                        return i, j
            return -1, -1

        def validate(ch, row, col):
            for i in range(9):
                if self.mat[i][col] == ch and row != i:
                    return False
            
            for i in range(9):
                if self.mat[row][i] == ch and col != i:
                    return False
            
            row //= 3
            col //= 3

            for i in range(row * 3, row * 3 + 3):
                for j in range(col * 3, col * 3 + 3):
                    if self.mat[i][j] == ch and (row, col) != (i, j):
                        return False
            return True

        def solveIt():
            row, col = nextValid()
            #no unassigned position is found, puzzle solved
            if row == -1 and col == -1:
                return True
            for num in range(1, 10):
                if validate(num, row, col):
                    self.mat[row][col] = num
                    self.createRect((row * self.gap, col * self.gap), (150, 150, 150))
                    Num = self.font.render(str(num), 1, (0, 0, 0))
                    self.window.blit(Num, (row * self.gap + self.gap // 4, col * self.gap + self.gap // 4))
                    pygame.display.update()
                    if solveIt():
                        return True
                    self.mat[row][col] = 0
                    self.createRect((row * self.gap, col * self.gap), (150, 150, 150))
                    pygame.display.update()
            return False

        def print_board(bo):
            for i in range(len(bo)):
                if i % 3 == 0 and i != 0:
                    print("- - - - - - - - - - - - - ")

                for j in range(len(bo[0])):
                    if j % 3 == 0 and j != 0:
                        print(" | ", end="")

                    if j == 8:
                        print(bo[i][j])
                    else:
                        print(str(bo[i][j]) + " ", end="")
        
        solveIt()
        print_board(self.mat)

    def main(self):
        self.solveSudoku()
        