import sys
import pygame
from Drawing import Drawing

pygame.init()
screen_width, screen_height = 400, 600
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

draw = Drawing(DISPLAYSURF)

while True:
    draw.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
