import pygame
import sys
from pygame.locals import *


width, height = 500, 400

class Aguila(pygame.sprite.Sprite):

    def __init__(self, MainWindow):

        super().__init__()
        self.original_image = pygame.image.load("imagenes/aguila.png")
        self.image = pygame.transform.scale(self.original_image, (70, 70))

        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def update(self):
        print("y: " + str(self.rect.y))
        print("x: " + str(self.rect.x))

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def reducir_vida(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0  # Asegura que la vida no sea negativa

    def obtener_vida(self):
        return self.vida

    def esta_vivo(self):
        return self.vida > 0




