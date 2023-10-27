import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group

pygame.init()

#reloj de pantalla (se usa para fps)
fps = 60
clock = pygame.time.Clock()

#icono para tanque tomado de "Assets/Logo_Game.jpg"
tanque = pygame.image.load("Assets/Tank_Image.png")

#Se defienen las propiedades de pantalla
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Eagle Defender")
screen.fill("#FFFFFF")

#Clase de tanque con sus propiedades de posicion y metodo de movimientos
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.time=0
        self.image=pygame.transform.scale(pygame.image.load("Assets/Tank_Image.png"),(75,75))

        self.rect=self.image.get_rect()
        self.rect.center=(screen.get_width()//14,screen.get_height()//2)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.top>=0:
                self.rect.y -=4
        if keys[pygame.K_s]:
            if self.rect.bottom<=screen.get_height():
                self.rect.y +=4
        if keys[pygame.K_a]:
            if self.rect.left>=0:
                self.rect.x -=4
        if keys[pygame.K_d]:
            if self.rect.right<=screen.get_width():
                self.rect.x +=4
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()
    
tanqueSprite=Group()
mitanque=Player()
tanqueSprite.add(mitanque)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(pygame.image.load("Assets/Backgrounds/mapBack.jpg"),(500,400)),(0,00))
    clock.tick(fps)

    tanqueSprite.update()
    tanqueSprite.draw(screen)

 # Mostrar 
    pygame.display.update()

    # Elimina las bombas que han salido de la pantalla