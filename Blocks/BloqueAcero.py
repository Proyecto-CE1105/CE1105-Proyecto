import pygame
from pygame.sprite import Sprite

class BloqueAcero(Sprite):  
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Assets/Blocks/SteelBlock.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def cambioEstado(self):
        pass

    def update(self,x,y):
        self.rect.x=x
        self.rect.y=y