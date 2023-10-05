#Importación de paquetes
import pygame,sys
from pygame.locals import *
from pygame.sprite import Group
from Bomb import Bomb

#Inicialización de Pygame
pygame.init()

#Variables para la pantalla
widht,height=500,400
fps=60
reloj=pygame.time.Clock()

#Colores
blanco=(255,255,255)
negro=(0,0,0)

#Assets para usar a lo largo del proyecto
icono=pygame.image.load("Assets/Logo_Game.jpg")
tanque=pygame.image.load("Assets/Tank_Image.png")

#Creación de la pantalla
pantalla= pygame.display.set_mode((widht,height))

#Especificación de título
pygame.display.set_caption("Eagle Defender")

pantalla.fill(negro)
pygame.display.set_icon(icono)

#Grupo de sprites, instanciación del objeto bomba
sprites=Group()
bomb=Bomb()
sprites.add(bomb)

#Bucle de ejecución
while True:
    #Cerrar el juego
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN and event.button==1:
            #Si se realiza click izquierdo, coloca una bomba en la posicón del mouse
            bomb.place_bomb(pygame.mouse.get_pos())
            
    #Control FPS
    reloj.tick(fps)
    #Actualización de la bomba
    sprites.update()
    #Dibujar el sprite en la pantalla
    sprites.draw(pantalla)
    #Actualización de la ventana
    pygame.display.update()
