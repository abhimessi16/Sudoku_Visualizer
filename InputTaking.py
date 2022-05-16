import pygame
from Solving import solve

class inputTaking():

    def __init__(self, window, size, mat):

        self.window = window
        self.size = size
        self.mat = mat
        self.width = size[0]
        self.height = size[1]
        self.gap = self.size[0] // 9
        self.selected = None
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

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    key = None
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    if event.key == pygame.K_KP1:
                        key = 1
                    if event.key == pygame.K_KP2:
                        key = 2
                    if event.key == pygame.K_KP3:
                        key = 3
                    if event.key == pygame.K_KP4:
                        key = 4
                    if event.key == pygame.K_KP5:
                        key = 5
                    if event.key == pygame.K_KP6:
                        key = 6
                    if event.key == pygame.K_KP7:
                        key = 7
                    if event.key == pygame.K_KP8:
                        key = 8
                    if event.key == pygame.K_KP9:
                        key = 9
                    if key and self.selected:
                        x, y = self.selected
                        num = self.font.render(str(key), 1, (0, 0, 0))
                        self.createRect(self.selected, (200, 200, 200))
                        self.window.blit(num, (x + self.gap // 4, y + self.gap // 4))
                        self.mat[x // self.gap][y // self.gap] = key
                        pygame.display.update()
                        key = None
                        self.selected = None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.getPos(pygame.mouse.get_pos())
                    if pos[1] == self.height:
                        if pos[0] >= self.width // 2:
                            running = False
                            solve(self.window, self.size, self.mat)
                    if self.selected:
                        self.createRect(self.selected, (200, 200, 200))
                    self.selected = pos
                    self.createRect(pos, (200, 225, 225))
                    pygame.display.update()
