import pygame
import sys
import random
from character import Character

class Item:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


    def check_collision(self, character_rect):
        return self.rect.colliderect(character_rect)
