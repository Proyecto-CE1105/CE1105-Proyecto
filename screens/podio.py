import pygame
from pygame import *
import sys,time
from interfaces.intPantallas import Pantallas
import PodioJsonController
from componentes import button

class Podio(Pantallas):
    def __init__(self,controller):
        self.controller=controller
        self.MainWindow=controller.screen

        self.podioJson = PodioJsonController.PodioControllerUsers("podio")
        self.data=self.podioJson.getPodio()

        self.font = pygame.font.Font(None, 36)

        self.txt1=self.data[0]["user"]+" : "+self.data[0]["tiempo"]

        self.nombres1 = self.font.render(self.txt1, 0, (250, 250, 250))
        self.nombres2 = self.font.render(self.data[1]["user"]+" : "+self.data[1]["tiempo"], 0, (250, 250, 250))
        self.nombres3 = self.font.render(self.data[2]["user"]+" : "+self.data[2]["tiempo"], 0, (250, 250, 250))
        self.nombres4 = self.font.render(self.data[3]["user"]+" : "+self.data[3]["tiempo"], 0, (250, 250, 250))
        self.nombres5 = self.font.render(self.data[4]["user"]+" : "+self.data[4]["tiempo"], 0, (250, 250, 250))

        self.buttonPodio = button.Button(650, 500, 150, 50, "Volver", (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)



        self.indice=0
        self.font = pygame.font.Font(None, 36)
    
    def runner(self):
        self.MainWindow.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.buttonPodio.is_clicked(mouse.get_pos()):
                    print("Login back")
                    self.change("menu")

        self.MainWindow.blit(self.nombres1, (300, 50*1))
        self.MainWindow.blit(self.nombres2, (300, 50*2))
        self.MainWindow.blit(self.nombres3, (300, 50*3))
        self.MainWindow.blit(self.nombres4, (300, 50*4))
        self.MainWindow.blit(self.nombres5, (300, 50*5))

        self.buttonPodio.seeActiveness(mouse.get_pos(), self.MainWindow)


        pass
    def change(self,newPantalla):
        self.controller.cambio(newPantalla)