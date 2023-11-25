import pygame
from pygame import *
import sys,time
from interfaces.intPantallas import Pantallas

class GameOver(Pantallas):
    def __init__(self,controller,points):
        self.point=points
        self.controler=controller
        self.MainWindow=controller.screen
        self.initial_time=time.time()

        pygame.display.set_caption("You Lost!")
        self.background_image = pygame.image.load("imagenes/gameoverScreen.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1200, 650))

        print("segundos: "+ str(points))

    def runner(self):
        if time.time()-self.initial_time>5:
            self.change()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        font = pygame.font.Font(None, 36)
        pointsLabel = font.render("Points Obtained: " + str(self.point), 0, (0, 0, 0))
        self.MainWindow.blit(pointsLabel, (600, 50))

        self.MainWindow.blit(self.background_image, (0, 0))
        

    def change(self):
        print("cambio a menu")
        self.controler.backMenu()