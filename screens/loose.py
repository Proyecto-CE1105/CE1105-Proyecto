import pygame
from pygame import *
import sys,time
from interfaces.intPantallas import Pantallas
import PodioJsonController

class GameOver(Pantallas):
    def __init__(self,controller,name,points):
        self.point=points
        self.name=name
        self.controler=controller
        self.MainWindow=controller.screen
        self.initial_time=time.time()


        pygame.display.set_caption("Atacante Ganador")

        self.font = pygame.font.Font(None, 36)
        self.pointsLabel = self.font.render("Ganó el atacante con un tiempo de : " + str(self.point) + " segundos", 0, (250, 250, 250))
        self.podioJson = PodioJsonController.PodioControllerUsers("podio")
        self.podio = self.font.render("Entro al podio: "+str(self.podioJson.verifyPodio(self.name,self.point)),0,(250,250,250))

        self.addPodio=self.podioJson.addResult(self.name,self.point,"musica")
        #self.background_image = pygame.image.load("imagenes/gameoverScreen.jpg")
        #self.background_image = pygame.transform.scale(self.background_image, (1200, 650))

        print("segundos: "+ str(points))

    def runner(self):
        self.MainWindow.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.MainWindow.blit(self.pointsLabel, (300, 50))
        self.MainWindow.blit(self.podio,(400,300))

        
        if time.time()-self.initial_time>5:
            self.change()

        

    def change(self):
        print("cambio a menu")
        self.controler.backMenu()