import pygame
from pygame.locals import *

width, height = 500, 400

class Bomb(pygame.sprite.Sprite):

    bomb_count = 0  # Variable para contar la cantidad de bombas colocadas
    
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("Assets/Bomb_Image.webp").convert()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y -= 1
        if self.rect.bottom < 0:
            self.kill()

    def place_bomb(self, mouse_position):
        if Bomb.can_place_bomb():
            self.rect.center = mouse_position
            Bomb.bomb_count += 1

    @staticmethod
    def can_place_bomb():
        return Bomb.bomb_count < 5
