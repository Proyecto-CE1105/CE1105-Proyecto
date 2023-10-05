import pygame
from pygame.locals import *

widht,height=500,400

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        #Heredación del init de la clase Sprite de Pygame
        super().__init__()
        #Rectángulo (Bomba)
        self.original_image=pygame.image.load("Assets/Bomb_Image.webp").convert()
        self.rect=self.original_image.get_rect()
        #Escalar la imagen
        self.image=pygame.transform.scale(self.original_image,(50,50))
        #Obtención del rectángulo (sprite)
        self.rect=self.image.get_rect()
        #Posición inicial fuera de la pantalla
        self.rect.x=-self.rect.width
        self.rect.y=-self.rect.height
    
    def update(self):
        #Mover hacia arriba (desaparece cuando sale de la pantalla)
        self.rect.y -=1
        if self.rect.bottom<0:
            #Si la bomba sale de la pantalla, se resetea la posición afuera de la pantalla
            self.rect.x= -self.rect.width
            self.rect.y= -self.rect.height
    
    def place_bomb(self,mouse_position):
        #Colocar la bomba en la posición del ratón
        self.rect.center=mouse_position