import sys
import pygame
# import pymunk
# import pymunk.pygame_util
from character import Character
from item import Item
from Drawing import Drawing

pygame.init()
screen_width, screen_height = 400, 600
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
# control frame rate
clock = pygame.time.Clock()
# calling character class
instance_of_character = Character()
instance_of_items = [Item(200, 500), Item(0, 550)]

# add drawing feature
draw = Drawing(DISPLAYSURF)

while True:
    # Handle user input events
    instance_of_character.input()
    # instance_of_character.update(screen_width,screen_height, instance_of_character.movement, instance_of_items)

    instance_of_character.horizontal_movement_collision(instance_of_items)
    instance_of_character.vertical_movement_collision(instance_of_items)
    instance_of_character.vertical_movement_collision(instance_of_items)
    instance_of_character.border_collision(screen_width, screen_height)
    DISPLAYSURF.fill((0, 0, 0))

    instance_of_character.draw(DISPLAYSURF)
    for item in instance_of_items:
        item.draw(DISPLAYSURF)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()

# if event.type == QUIT:
# pygame.quit()
# sys.exit()