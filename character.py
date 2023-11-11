import pygame
import sys
import random

class Character:
    # character object
    def __init__(self):
        self.player = pygame.Rect(50, 250, 30, 30)
        self.color = (255, 0, 0)

        # for jumping
        self.movement = [0,0]
        self.jump_speed = -11
        self.gravity = 0.3
        self.on_ground = True


    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.jump()
                if event.key == pygame.K_a:
                    self.movement[0] = -5
                if event.key == pygame.K_d:
                    self.movement[0] = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.movement[0] = 0
                if event.key == pygame.K_d:
                    self.movement[0] = 0

    def jump(self):
        if self.on_ground == True:
            self.movement[1] = self.jump_speed  # Adjust the jump velocity as needed
            self.on_ground = False

    def border_collision(self,screen_width, screen_height):
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > screen_width:
            self.player.right = screen_width
        if self.player.top < 0:
            self.player.top = 0
        if self.player.bottom > screen_height:
            self.player.bottom = screen_height
            self.on_ground = True

    def horizontal_movement_collision(self, immovable_items):
        self.player.x += self.movement[0]
        for item in immovable_items:
            if self.player.colliderect(item.rect):
                if self.movement[0] > 0:
                    self.player.right = item.rect.left
                elif self.movement[0] < 0:
                    self.player.left = item.rect.right

    def vertical_movement_collision(self, immovable_items):
        self.apply_gravity()
        for item in immovable_items:
            if self.player.colliderect(item.rect):
                if self.movement[1] > 0:
                    self.player.bottom = item.rect.top
                    self.movement[1] = 0
                    self.on_ground = True
                elif self.movement[1] < 0:
                    self.player.top = item.rect.bottom
                    self.movement[1] = 0
                    self.on_ground = True

        if self.on_ground and self.movement[1] < 0 or self.movement[1] > 1:
            self.on_ground = False

    def apply_gravity(self):
        self.movement[1] += self.gravity
        self.player.y += self.movement[1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.player)
