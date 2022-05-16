'''
this is the main class where the main window for sudoku solving will be initialised
its dimensions, colors, etc

here i will import the input-taking class and solving class
'''

import pygame
from InputTaking import inputTaking
from Solving import solve

class Sudoku:
    
    def __init__(self, width, height):

        pygame.init()
        pygame.display.set_caption('Sudoku Visualizer')

        self.width = width
        self.height = height
        self.mat = [[0] * 9 for _ in range(9)]
        self.gap = width // 9
        self.size = (width, height)
        self.sizeSudoku = (width, height * 0.90)
        self.window = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont('consolas', 40)

        self.selected = None

        self.main()
    
    def createStructure(self):
        self.window.fill((200, 200, 200))
        x, y = self.sizeSudoku
        for i in range(1, 10):
            if i % 3 == 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.window, (0, 0, 0), (0, self.gap * i), (x, self.gap * i), width = thick)
            pygame.draw.line(self.window, (0, 0, 0), (self.gap * i, 0), (self.gap * i, y), width = thick)
        
        reset = self.font.render('...Reset...', 1, (0, 0, 0))
        solve = self.font.render('...Solve...', 1, (0, 0, 0))

        self.window.blit(reset, (0, self.size[1] - self.gap * 3 // 4))
        self.window.blit(solve, (self.width // 2, self.size[1] - self.gap * 3 // 4))

        pygame.display.update()
    
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

    def main(self):
        self.createStructure()
        inputTaking(self.window, self.sizeSudoku, self.mat)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[1] > self.sizeSudoku[1]:
                        if pos[0] < self.width // 2:
                            self.createStructure()
                            inputTaking(self.window, self.sizeSudoku, self.mat)
                        else:
                            self.createStructure()
                            solve(self.window, self.sizeSudoku, self.mat)
        pygame.quit()

sudoku = Sudoku(540, 600)
