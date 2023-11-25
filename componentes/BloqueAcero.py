import pygame

class BloqueAcero(pygame.sprite.Sprite):
    def __init__(self,mainWindow):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load("Assets/Blocks/SteelBlock.png"),(50,50))
        self.rect=self.image.get_rect()
        self.screen=mainWindow
        self.health=100

    def update(self):
        pass