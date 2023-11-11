import pygame
import sys


class Drawing:

    def __init__(self, screen):
        self.screen = screen
        self.drawColor = (99, 99, 99)
        self.radius = 20
        self.thickness = 5
        self.drawing = False
        self.points = []
        self.x = 0
        self.y = 0

    def draw(self):
        # x, y = pygame.mouse.get_cursor()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drawing = True
                    self.points = []
            elif event.type == pygame.MOUSEMOTION:
                if self.drawing:
                    (self.x, self.y) = event.pos
                self.points.append((self.x, self.y))
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drawing = False
                    self.points = []

        if len(self.points) > 2:
            pygame.draw.lines(self.screen, self.drawColor, False, self.points, self.thickness)