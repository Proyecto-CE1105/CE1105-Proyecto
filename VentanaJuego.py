#Importación de paquetes
import pygame,sys
from pygame.locals import *

#Inicialización de Pygame
pygame.init()

#Creación de la pantalla
patalla= pygame.display.set_mode((500,400))

#Especificación de título
pygame.display.set_caption("Eagle Defender")

#Bucle de ejecución
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

