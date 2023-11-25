import pygame
from pygame import *
import sys,time
from interfaces.intPantallas import Pantallas

class winScreen(Pantallas):
    def __init__(self,controller,points,player):
        self.controler=controller
        self.MainWindow=controller.screen
        self.points=points
        self.player=player

        pygame.display.set_caption("You Win!")

        self.background_color_hex = 0x008aff

        self.background_color = (
        self.background_color_hex >> 16 & 255, self.background_color_hex >> 8 & 255, self.background_color_hex & 255)
        self.MainWindow.fill(self.background_color)

        self.background_image = pygame.image.load("imagenes/gamewinScreen.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 650))

    def runner(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.MainWindow.blit(self.background_image, (100, 0))

        font = pygame.font.Font(None, 36)
        pointsLabel = font.render("Points Obtained: " + str(self.points), 0, (0, 0, 0))
        self.MainWindow.blit(pointsLabel, (600, 50))