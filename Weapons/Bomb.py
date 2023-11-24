import pygame
import sys
from pygame.locals import *


width, height = 500, 400

class Bomb(pygame.sprite.Sprite):
    
    bomb_count = 5

    def __init__(self,bombDir,tankRect,MainWindow):
        
        super().__init__()
        self.direccion = bombDir
        self.tankPos = tankRect
        self.pantalla =MainWindow
        self.original_image = pygame.image.load("imagenes/Bomb_Image.webp")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
       
        if self.direccion=="up":
            self.rect.y -= 1
            if self.rect.bottom < 0:
                self.kill()
        elif self.direccion=="down":
            self.rect.y += 1
            if self.rect.top > self.pantalla.get_height():
                self.kill()
        elif self.direccion=="left":
            self.rect.x -= 1
            if self.rect.right < 0:
                self.kill()
        elif self.direccion=="right":
            self.rect.x += 1
            if self.rect.left > self.pantalla.get_width():
                self.kill()


    def place_bomb(self):
        
        if Bomb.can_place_bomb():
            self.rect.center = self.tankPos.center
            Bomb.bomb_count -= 1

    @staticmethod
    def can_place_bomb():
        
        return Bomb.bomb_count > 0

    # Getters to obtain positions of bomb image's sides
    def get_left(self):
        return self.rect.left

    def get_right(self):
        return self.rect.right

    def get_top(self):
        return self.rect.top

    def get_bottom(self):
        return self.rect.bottom