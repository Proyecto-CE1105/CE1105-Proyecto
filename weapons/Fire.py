import pygame
import sys
from pygame.locals import *

width, height = 500, 400
class Fire(pygame.sprite.Sprite):
    fire_count = 5
    def __init__(self,fireDir,tankRect,MainWindow):
        super().__init__()
        self.direccion = fireDir
        self.tankPos = tankRect
        self.pantalla =MainWindow
        self.original_image = pygame.image.load("Assets/Weapons/FireBall.png")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        if self.direccion == "up":
            self.rect.y -= 1
            if self.rect.bottom < 0:
                self.kill()
        elif self.direccion == "down":
            self.rect.y += 1
            if self.rect.top > self.pantalla.get_height():
                self.kill()
        elif self.direccion == "left":
            self.rect.x -= 1
            if self.rect.right < 0:
                self.kill()
        elif self.direccion == "right":
            self.rect.x += 1
            if self.rect.left > self.pantalla.get_width():
                self.kill()

    def place_fire(self):
        if Fire.can_place_fire():
            self.rect.center = self.tankPos.center
            Fire.fire_count -= 1
    @staticmethod
    def can_place_fire():
        return Fire.fire_count > 0
    def get_left(self):
        return self.rect.left
    def get_right(self):
        return self.rect.right
    def get_top(self):
        return self.rect.top
    def get_bottom(self):
        return self.rect.bottom