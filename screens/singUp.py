from pygame import *
import pygame
import sys
from componentes import button as Button, Entry,Label
from interfaces.intPantallas import Pantallas
import JsonController,FilesController

class signUpScreen(Pantallas):
        
    def __init__(self, controlador):

        self.controlador=controlador
        self.i18n=controlador.i18n
        self.MainWindow=controlador.screen
        pygame.display.set_caption('Singup')
        self.bg = pygame.image.load("imagenes/Background.png")


        self.buttonRegisterUser = Button.Button(740, 550, 150, 50, self.i18n.t("register"), (111, 84, 247), (78, 42, 255), (111, 84, 247), 25)
        self.buttonSelectSong = Button.Button(760, 450, 100, 25, self.i18n.t("selec_music"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonSelectPhoto = Button.Button(760, 500, 100, 25, self.i18n.t("select_picture"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        self.user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.email_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry = Entry.Entry(750, 350, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.rol_entry = Entry.Entry(750, 400, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.user_entry_signIn = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry_signIn = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.labelUser = Label.Label(self.i18n.t('user'), 20, 675, 250, (0, 0, 0))
        self.labelEmail = Label.Label(self.i18n.t('email'), 20, 675, 300, (0, 0, 0))
        self.labelPassword = Label.Label(self.i18n.t('password'), 20, 675, 350, (0, 0, 0))
        self.labelMusic = Label.Label(self.i18n.t('music'), 20, 675, 450, (0, 0, 0))
        self.labelPhoto = Label.Label(self.i18n.t('photo'), 20, 675, 500, (0, 0, 0))
        self.labelRol = Label.Label(self.i18n.t('rol'), 20, 675, 400, (0, 0, 0))
        self.labelUser_signIn = Label.Label(self.i18n.t('user'), 20, 675, 250, (0, 0, 0))
        self.labelPassword_signIn = Label.Label(self.i18n.t("password"), 20, 675, 300, (0, 0, 0))
        self.labelCharacter_singIn = Label.Label(self.i18n.t("attacker"), 60, 700, 180, (0, 0, 0))
        self.labelCharacterInScreen = Label.Label(self.i18n.t("player"), 30, 650, 20, (0, 0, 0))


    def change(self,newPantalla):
        self.controlador.cambio(newPantalla)
        
    def runner(self):
        userFile = JsonController.JsonControllerUsers
        FileDialog = FilesController.FileControllers("","")

        self.MainWindow.blit(self.bg, (0, 0))
        self.labelUser.draw(self.MainWindow)
        self.labelEmail.draw(self.MainWindow)
        self.labelPassword.draw(self.MainWindow)
        self.labelMusic.draw(self.MainWindow)
        self.labelPhoto.draw(self.MainWindow)
        self.labelRol.draw(self.MainWindow)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.buttonSelectSong.is_clicked(mouse.get_pos()):
                    FileDialog.selectFile("music")
                if self.buttonSelectPhoto.is_clicked(mouse.get_pos()):
                    FileDialog.selectFile("photo")
                if self.buttonRegisterUser.is_clicked(mouse.get_pos()):
                    userFile.addUsers(0, self.user_entry.text, self.email_entry.text, self.password_entry.text, str(FileDialog.music), str(FileDialog.photo), self.rol_entry.text)
                    self.change("menu")

            self.buttonSelectSong.seeActiveness(mouse.get_pos(), self.MainWindow)
            self.buttonSelectPhoto.seeActiveness(mouse.get_pos(), self.MainWindow)
            self.buttonRegisterUser.seeActiveness(mouse.get_pos(), self.MainWindow)

            self.user_entry.seeEntryActiveness(mouse.get_pos(), self.MainWindow)
            self.password_entry.seeEntryActiveness(mouse.get_pos(), self.MainWindow)
            self.email_entry.seeEntryActiveness(mouse.get_pos(), self.MainWindow)
            self.rol_entry.seeEntryActiveness(mouse.get_pos(), self.MainWindow)


            #Write on the entries
            if event.type == pygame.KEYDOWN:
                if self.user_entry.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_entry.text = self.user_entry.text[:-1]  # Remove the last letter
                    else:
                        self.user_entry.text += event.unicode  # Add a new letter
                elif self.email_entry.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.email_entry.text = self.email_entry.text[:-1]  # Remove the last letter
                    else:
                        self.email_entry.text += event.unicode  # Add a new letter

                elif self.password_entry.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.password_entry.text = self.password_entry.text[:-1]  # Remove the last letter
                        self.password_entry.drawEntry(self.MainWindow)
                    else:
                        self.password_entry.text += event.unicode  # Add a new letter
                elif self.rol_entry.activeness:
                    if event.key == pygame.K_BACKSPACE:
                        self.rol_entry.text = self.rol_entry.text[:-1]  # Remove the last letter
                        self.rol_entry.drawEntry(self.MainWindow)
                    else:
                        self.rol_entry.text += event.unicode  # Add a new letter

        self.user_entry.drawEntry(self.MainWindow)
        self.email_entry.drawEntry(self.MainWindow)
        self.password_entry.drawEntry(self.MainWindow)
        self.rol_entry.drawEntry(self.MainWindow)

        self.buttonRegisterUser.drawButton(self.MainWindow)
        self.buttonSelectSong.drawButton(self.MainWindow)
        self.buttonSelectPhoto.drawButton(self.MainWindow)

