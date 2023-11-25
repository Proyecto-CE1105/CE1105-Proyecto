import pygame
from interfaces.intPantallas import Pantallas

class register(Pantallas):
    def __init__(self,manager):
        self.controlador=manager
        self.pantalla=manager.screen
        pygame.display.set_caption('Pantalla2')
        
    def runner(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controlador.running = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                         self.change("main")
                     
        self.pantalla.fill("blue")
        pygame.display.flip()
    
    def change(self,newPantalla):
         self.controlador.cambio(newPantalla)