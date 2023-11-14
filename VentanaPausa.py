import pygame
from pygame import *
from pygame.locals import *

rect_surface=pygame.Surface((1200,650),pygame.SRCALPHA)

def draw_pause(ventana,width,height):
    pygame.draw.rect(rect_surface,(128,128,128,150),[0,0,width,height])
    pygame.draw.rect(rect_surface, 'dark gray', [200,150,600,50],0,10)
    reset=pygame.draw.rect(rect_surface,'white',[200,220,280,50],0,10)
    save=pygame.draw.rect(rect_surface,'white',[520,220,280,50],0,10)
    '''rect_surface.blit(fuente.render('Juego en Pausa: Presione Escape para continuar',True,'black'),(220,160))
    rect_surface.blit(fuente.render('Salir',True,'black'),(220,230))
    rect_surface.blit(fuente.render('Guardar',True,'black'),(540,230))'''
    ventana.blit(rect_surface,(0,0))