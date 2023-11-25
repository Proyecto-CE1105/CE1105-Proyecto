from pygame import *
import pygame
import sys
from componentes import button as Button, Entry,Label
from interfaces.intPantallas import Pantallas
from services import JsonController,FilesController

class signInScreen(Pantallas):

    def __init__(self,controlador):

        self.controlador=controlador
        self.MainWindow=controlador.screen
        self.i18n=controlador.i18n


        self.Atacante = True
        self.Defensor = False
        self.bg = pygame.image.load("imagenes/Background.png")

        self.buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        self.user_entry_signIn = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry_signIn = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry = Entry.Entry(750, 350, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.labelUser_signIn = Label.Label(self.i18n.t('user'), 20, 675, 250, (0, 0, 0))
        self.labelPassword_signIn = Label.Label(self.i18n.t("password"), 20, 675, 300, (0, 0, 0))
        self.labelCharacter_singIn = Label.Label(self.i18n.t("attacker"), 60, 700, 180, (0, 0, 0))
        self.labelCharacterInScreen = Label.Label(self.i18n.t("player"), 30, 650, 20, (0, 0, 0))
        

        self.userFile = JsonController.JsonControllerUsers
        self.FileDialog = FilesController.FileControllers("","")

        self.atacanteNombre=""
        self.defensorNombre=""
        self.atacanteMusica=""
        self.defensorMusica=""
        

    def change(self):
        print("iniciandoPartida")
        self.controlador.empezarPartida(self.atacanteNombre,self.defensorNombre,self.atacanteMusica,self.defensorMusica)

    def runner(self):
        self.MainWindow.blit(self.bg, (0, 0))
        self.labelCharacter_singIn.draw(self.MainWindow)
        self.user_entry_signIn.drawEntry(self.MainWindow)
        self.password_entry_signIn.drawEntry(self.MainWindow)
        self.buttonEnter.drawButton(self.MainWindow)
        self.labelUser_signIn.draw(self.MainWindow)
        self.labelPassword_signIn.draw(self.MainWindow)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if self.user_entry_signIn.is_clicked(mouse.get_pos()):
                self.user_entry_signIn.color = self.user_entry.colorActive
                self.user_entry_signIn.activeness = True
            else:
                self.user_entry_signIn.color = self.user_entry.colorPassive
                self.user_entry_signIn.activeness = False

            # This checks the events related with the password_entry
            if self.password_entry_signIn.is_clicked(mouse.get_pos()):
                self.password_entry_signIn.color = self.password_entry.colorActive
                self.password_entry_signIn.activeness = True
            else:
                self.password_entry_signIn.color = self.password_entry.colorPassive
                self.password_entry_signIn.activeness = False

            if self.buttonEnter.is_clicked(mouse.get_pos()):
                self.buttonEnter.color = self.user_entry_signIn.colorActive
                self.buttonEnter.activeness = True
            else:
                self.buttonEnter.color = self.user_entry_signIn.colorPassive
                self.buttonEnter.activeness = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.buttonEnter.is_clicked(mouse.get_pos()):
                    # Screens.playScreen(self)
                    if self.userFile.verifyUser(self.user_entry_signIn.text, self.password_entry_signIn.text) and self.Defensor == False:
                        self.Atacante = False
                        self.Defensor = True
                        self.labelCharacter_singIn.update_text("Defensor")
                        self.atacanteNombre = self.user_entry_signIn.text
                        self.atacanteMusica = str(self.userFile.selectSong(self.user_entry_signIn.text))
                        self.user_entry_signIn.text = ''
                        self.password_entry_signIn.text = ''

                    elif self.userFile.verifyUser(self.user_entry_signIn.text, self.password_entry_signIn.text):
                        self.defensorNombre = self.user_entry_signIn.text
                        self.defensorMusica = str(self.userFile.selectSong(self.user_entry_signIn.text))
                        self.change()
            if event.type == pygame.KEYDOWN:
                if self.user_entry_signIn.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_entry_signIn.text = self.user_entry_signIn.text[:-1]  # Remove the last letter
                    else:
                        self.user_entry_signIn.text += event.unicode  # Add a new letter
                elif self.password_entry_signIn.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.password_entry_signIn.text = self.password_entry_signIn.text[
                                                            :-1]  # Remove the last letter
                    else:
                        self.password_entry_signIn.text += event.unicode  # Add a new letter

        self.user_entry.drawEntry(self.MainWindow)
        self.password_entry.drawEntry(self.MainWindow)
        


