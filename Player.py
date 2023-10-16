import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group


class Player(pygame.sprite.Sprite):
    def __init__(self, MainWindow):
        super().__init__()
        self.time = 0
        self.image = pygame.transform.scale(pygame.image.load("imagenes/Tank_Image.png"), (75, 75))

        self.rect = self.image.get_rect()
        self.rect.center = (MainWindow.get_width() // 14, MainWindow.get_height() // 2)

    def update(self, MainWindow):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.top >= 0:
                self.rect.y -= 4
        if keys[pygame.K_s]:
            if self.rect.bottom <= MainWindow.get_height():
                self.rect.y += 4
        if keys[pygame.K_a]:
            if self.rect.left >= 0:
                self.rect.x -= 4
        if keys[pygame.K_d]:
            if self.rect.right <= MainWindow.get_width():
                self.rect.x += 4
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()