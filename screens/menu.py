import sys
import pygame
from pygame import *
from interfaces.intPantallas import Pantallas
from componentes import button

class menuPrincipal(Pantallas):
    def __init__(self,manager):
        self.manager=manager
        self.i18n=manager.i18n
        self.buttonSignIn = button.Button(650, 300, 150, 50, self.i18n.t("login"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.buttonSignUp = button.Button(850, 300, 150, 50, self.i18n.t("singup"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.buttonPodio = button.Button(650, 500, 150, 50, "Podio", (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.buttonIdioma = button.Button(850, 500, 150, 50, "Cambiar Idioma", (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.bg = pygame.image.load("imagenes/Background.png")
        pygame.display.set_caption('Eagle Defender - Menu Principal')


    def runner(self):
        for event in pygame.event.get():
            self.manager.screen.blit(self.bg, (0, 0))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.buttonSignIn.is_clicked(mouse.get_pos()):
                    print("Login clicked")
                    self.change("SignIn")

                if self.buttonSignUp.is_clicked(mouse.get_pos()):
                    print("singup clicked")
                    self.change("SignUp")
                if self.buttonPodio.is_clicked(mouse.get_pos()):
                    print("podio clicked")
                    self.change("podio")
                if self.buttonIdioma.is_clicked(mouse.get_pos()):
                    print("singup clicked")
                    pass


            self.buttonSignUp.seeActiveness(mouse.get_pos(), self.manager.screen)
            self.buttonSignIn.seeActiveness(mouse.get_pos(), self.manager.screen)
            self.buttonPodio.seeActiveness(mouse.get_pos(), self.manager.screen)
            self.buttonIdioma.seeActiveness(mouse.get_pos(), self.manager.screen)

    def change(self,newPantalla):
        self.manager.cambio(newPantalla)