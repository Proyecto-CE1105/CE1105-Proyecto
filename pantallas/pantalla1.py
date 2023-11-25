import pygame
from interfaces.intPantallas import Pantallas
from componentes import button
from pygame import MOUSEBUTTONDOWN, mouse

class menu(Pantallas):
    def __init__(self,manager):
        self.controlador=manager
        self.pantalla=manager.screen
        pygame.display.set_caption('Pantalla1')
        self.buttonEnter = button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        font = pygame.font.Font('freesansbold.ttf', 32)
 

        self.text = font.render('Texto', True, "red")
 
        self.textRect = self.text.get_rect()

        self.textRect.center = (self.pantalla.get_width() // 2, self.pantalla.get_height() // 2)
        
    def runner(self):
        self.pantalla.fill("green")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controlador.running = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_2:
                         self.change("Register")
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.buttonEnter.is_clicked(mouse.get_pos()):
                        self.change("Register")
                     
        self.buttonEnter.drawButton(self.pantalla)
        self.pantalla.blit(self.text, self.textRect)             
        pygame.display.flip()
    
    def change(self,newPantalla):
         self.controlador.cambio(newPantalla)