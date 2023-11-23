import pygame
import sys
from pygame.locals import *

width, height = 500, 400
class Water(pygame.sprite.Sprite):
    water_count = 5
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("imagenes/wwaterball.png")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y -= 1
        if self.rect.bottom < 0:
            self.kill()

    def place_water(self, mouse_position):
        if Water.can_place_water():
            self.rect.center = mouse_position
            Water.water_count -= 1
    @staticmethod
    def can_place_water():
        return Water.water_count > 0
    def get_left(self):
        return self.rect.left
    def get_right(self):
        return self.rect.right
    def get_top(self):
        return self.rect.top
    def get_bottom(self):
        return self.rect.bottom
