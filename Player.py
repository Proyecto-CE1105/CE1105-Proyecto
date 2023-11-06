import random
import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group


class Player(pygame.sprite.Sprite):
    def __init__(self, MainWindow):
        super().__init__()
        self.direccion="left"
        self.time = 0
        self.skins=[pygame.transform.scale(pygame.image.load("imagenes/tankVerde.png"), (75, 75)),pygame.transform.scale(pygame.image.load("imagenes/tankRojo.png"), (75, 75),pygame.transform.scale(pygame.image.load("imagenes/tankAzul.png"), (75, 75)))]
        self.icon = self.skins[0]
        self.rotaciones = [pygame.transform.rotate(self.icon,0),pygame.transform.rotate(self.icon,270),pygame.transform.rotate(self.icon,180),pygame.transform.rotate(self.icon,90)]
        self.image=self.rotaciones[0]
        self.rect = self.image.get_rect()
        self.rect.center = (MainWindow.get_width() // 14, MainWindow.get_height() // 2)

    def getDirection(this):
        return this.direccion
    
    def getRect(this):
        return this.rect

    def update(self, MainWindow):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.top >= 0:
                self.rect.y -= 4
                self.direccion = "up"
                self.image=self.rotaciones[1]
        if keys[pygame.K_s]:
            if self.rect.bottom <= MainWindow.get_height():
                self.rect.y += 4
                self.direccion = "down"
                self.image=self.rotaciones[3]
        if keys[pygame.K_a]:
            if self.rect.left >= 0:
                self.rect.x -= 4
                self.direccion = "left"
                self.image=self.rotaciones[0]
        if keys[pygame.K_d]:
            if self.rect.right <= MainWindow.get_width():
                self.rect.x += 4
                self.direccion = "right"
                self.image=self.rotaciones[2]
        if keys[pygame.K_q]:
            self.cambiarSkin()

   
    def cambiarSkin(self):
        self.icon=self.skins[random.randint(0,len(self.skins)-1)]
        self.rotaciones = [pygame.transform.rotate(self.icon,0),pygame.transform.rotate(self.icon,270),pygame.transform.rotate(self.icon,180),pygame.transform.rotate(self.icon,90)]
        self.image=self.rotaciones[0]