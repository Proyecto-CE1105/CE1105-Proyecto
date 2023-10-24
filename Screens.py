import pygame, sys, Button, Entry, Label, FilesController, JsonController, Player
from pygame import *
from pygame.sprite import Group

class Screens:
    def __init__(self, MainWindow, bg):
        self.MainWindow = MainWindow
        self.bg = bg
        self.buttonSignIn = Button.Button(650, 300, 150, 50, 'Sign In', (86, 140, 255), 30)
        self.buttonSignUp = Button.Button(850, 300, 150, 50, 'Sign Up', (86, 140, 255), 30)

        self.buttonRegisterUser = Button.Button(740, 500, 150, 50, 'Register User', (111, 84, 247), 25)
        self.buttonSelectSong = Button.Button(760, 400, 100, 25, 'Select Music', (86, 140, 255), 23)
        self.buttonSelectPhoto = Button.Button(760, 450, 100, 25, 'Select Photo', (86, 140, 255), 23)

        self.user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.email_entry = Entry.Entry(750, 350, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.labelUser = Label.Label('User:', 20, 675, 250, (0, 0, 0))
        self.labelEmail = Label.Label('Email:', 20, 675, 300, (0, 0, 0))
        self.labelPassword = Label.Label('Password:', 20, 675, 350, (0, 0, 0))
        self.labelMusic = Label.Label('Music:', 20, 675, 400, (0, 0, 0))
        self.labelPhoto = Label.Label('Photo:', 20, 675, 450, (0, 0, 0))
    def signInScreen(self):
        userFile = JsonController.JsonControllerUsers

        buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), 20)

        user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        password_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        labelUser = Label.Label('User:', 20, 675, 250, (0, 0, 0))
        labelPassword = Label.Label('Password:', 20, 675, 300, (0, 0, 0))
        labelCharacter = Label.Label('Atacante', 60, 700, 180, (0, 0, 0))

        Atacante = True
        Defensor = False
        while(True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if buttonEnter.is_clicked(mouse.get_pos()):
                        if userFile.verifyUser(0, user_entry.text, password_entry.text) and listoDefensor:
                            Atacante = False
                            Defensor = True
                            listoDefensor = False
                        elif userFile.verifyUser(0, user_entry.text, password_entry.text):
                            WantToPlay = True
                            WantToShowObjectsSignIn = False

                    if buttonEnter.is_clicked(mouse.get_pos()):
                        buttonEnter.color = user_entry.colorActive
                        buttonEnter.activeness = True
                    else:
                        buttonEnter.color = user_entry.colorPassive
                        buttonEnter.activeness = False

                    if event.type == pygame.KEYDOWN:
                        if user_entry.activeness == True:
                            if event.key == pygame.K_BACKSPACE:
                                user_entry.text = user_entry.text[:-1]  # Remove the last letter
                            else:
                                user_entry.text += event.unicode  # Add a new letter
                        elif password_entry.activeness == True:
                            if event.key == pygame.K_BACKSPACE:
                                password_entry.text = password_entry.text[:-1]  # Remove the last letter
                            else:
                                password_entry.text += event.unicode  # Add a new letter
                if Atacante:
                    labelCharacter.draw(self.MainWindow)
                if Defensor:
                    labelCharacter.update_text("Defensor")

                labelCharacter.draw(self.MainWindow)
                user_entry.drawEntry(self.MainWindow)
                password_entry.drawEntry(self.MainWindow)
                buttonEnter.drawButton(self.MainWindow)
                labelUser.draw(self.MainWindow)
                labelPassword.draw(self.MainWindow)

                pygame.display.update()

    def signUpScreen(self):
        userFile = JsonController.JsonControllerUsers
        FileDialog = FilesController.FileControllers(' ', ' ')

        self.user_entry.drawEntry(self.MainWindow)
        self.email_entry.drawEntry(self.MainWindow)
        self.password_entry.drawEntry(self.MainWindow)

        self.labelUser.draw(self.MainWindow)
        self.labelEmail.draw(self.MainWindow)
        self.labelPassword.draw(self.MainWindow)
        self.labelMusic.draw(self.MainWindow)
        self.labelPhoto.draw(self.MainWindow)

        self.buttonRegisterUser.drawButton(self.MainWindow)
        self.buttonSelectSong.drawButton(self.MainWindow)
        self.buttonSelectPhoto.drawButton(self.MainWindow)

        while (True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.buttonSelectSong.is_clicked(mouse.get_pos()):
                        FileDialog.music = FileDialog.selectFile()
                    if self.buttonSelectPhoto.is_clicked(mouse.get_pos()):
                        FileDialog.photo = FileDialog.selectFile()
                    if self.buttonRegisterUser.is_clicked(mouse.get_pos()):
                        userFile.addUsers(1, self.user_entry.text, self.email_entry.text, self.password_entry.text, FileDialog.music, FileDialog.photo)

                if self.buttonSelectSong.is_clicked(mouse.get_pos()):
                    self.buttonSelectSong.color = (2, 82, 253)
                    self.buttonSelectSong.drawButton(self.MainWindow)
                    self.buttonSelectPhoto.color = (86, 140, 255)
                    self.buttonSelectPhoto.drawButton(self.MainWindow)
                    self.buttonRegisterUser.color = (111, 84, 247)
                    self.buttonRegisterUser.drawButton(self.MainWindow)
                elif self.buttonSelectPhoto.is_clicked(mouse.get_pos()):
                    self.buttonSelectSong.color = (86, 140, 255)
                    self.buttonSelectSong.drawButton(self.MainWindow)
                    self.buttonSelectPhoto.color = (2, 82, 253)
                    self.buttonSelectPhoto.drawButton(self.MainWindow)
                    self.buttonRegisterUser.color = (111, 84, 247)
                    self.buttonRegisterUser.drawButton(self.MainWindow)
                elif self.buttonRegisterUser.is_clicked(mouse.get_pos()):
                    self.buttonSelectSong.color = (86, 140, 255)
                    self.buttonSelectSong.drawButton(self.MainWindow)
                    self.buttonSelectPhoto.color = (86, 140, 255)
                    self.buttonSelectPhoto.drawButton(self.MainWindow)
                    self.buttonRegisterUser.color = (78, 42, 255)
                    self.buttonRegisterUser.drawButton(self.MainWindow)
                else:
                    self.buttonSelectSong.color = (86, 140, 255)
                    self.buttonSelectSong.drawButton(self.MainWindow)
                    self.buttonSelectPhoto.color = (86, 140, 255)
                    self.buttonSelectPhoto.drawButton(self.MainWindow)
                    self.buttonRegisterUser.color = (111, 84, 247)
                    self.buttonRegisterUser.drawButton(self.MainWindow)

                # This checks the events related with the user_entry
                if self.user_entry.is_clicked(mouse.get_pos()):
                    self.user_entry.color = self.user_entry.colorActive
                    self.user_entry.activeness = True
                else:
                    self.user_entry.color = self.user_entry.colorPassive
                    self.user_entry.activeness = False

                # This checks the events related with the password_entry
                if self.password_entry.is_clicked(mouse.get_pos()):
                    self.password_entry.color = self.password_entry.colorActive
                    self.password_entry.activeness = True
                else:
                    self.password_entry.color = self.password_entry.colorPassive
                    self.password_entry.activeness = False

                # This checks the events related with the email_entry
                if self.email_entry.is_clicked(mouse.get_pos()):
                    self.email_entry.color = self.email_entry.colorActive
                    self.email_entry.activeness = True
                else:
                    self.email_entry.color = self.email_entry.colorPassive
                    self.email_entry.activeness = False

                #Write on the entries
                if event.type == pygame.KEYDOWN:
                    if self.user_entry.activeness:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_entry.eliminate_Text()  # Remove the last letter
                            self.user_entry.drawEntry(self.MainWindow)
                        else:
                            self.user_entry.text += event.unicode  # Add a new letter
                            self.user_entry.drawEntry(self.MainWindow)
                    elif self.email_entry.activeness:
                        if event.key == pygame.K_BACKSPACE:
                            self.email_entry.text = self.email_entry.text[:-1]  # Remove the last letter
                        else:
                            self.email_entry.text += event.unicode  # Add a new letter

                    elif self.password_entry.activeness:
                        if event.key == pygame.K_BACKSPACE:
                            self.password_entry.text = self.password_entry.text[:-1]  # Remove the last letter
                        else:
                            self.password_entry.text += event.unicode  # Add a new letter
                pygame.display.update()

    def playScreen(self):
        fps = 60
        clock = pygame.time.Clock()
        tanque = pygame.image.load("imagenes/Tank_Image.png")

        tanqueSprite = Group()
        mitanque = Player.Player(self.MainWindow)
        tanqueSprite.add(mitanque)
        while(True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                self.MainWindow.blit(pygame.transform.scale(pygame.image.load("imagenes/mapBack.jpg"), (500, 400)), (0, 00))
                clock.tick(fps)
                tanqueSprite.update(self.MainWindow)
                tanqueSprite.draw(self.MainWindow)

                pygame.display.update()

    def mainScreen(self):
        running = True
        while (running):
            self.MainWindow.blit(self.bg, (0,0))


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.buttonSignIn.is_clicked(mouse.get_pos()):
                        Screens.signInScreen(self)
                        running = False

                    if self.buttonSignUp.is_clicked(mouse.get_pos()):
                        Screens.signUpScreen(self)
                        running = False

                if self.buttonSignIn.is_clicked(mouse.get_pos()):
                    self.buttonSignIn.color = (2, 82, 253)
                    self.buttonSignIn.drawButton(self.MainWindow)
                    self.buttonSignUp.color = (86, 140, 255)
                    self.buttonSignUp.drawButton(self.MainWindow)
                elif self.buttonSignUp.is_clicked(mouse.get_pos()):
                    self.buttonSignUp.color = (2, 82, 253)
                    self.buttonSignUp.drawButton(self.MainWindow)
                    self.buttonSignIn.color = (86, 140, 255)
                    self.buttonSignIn.drawButton(self.MainWindow)
                else:
                    self.buttonSignIn.color = (86, 140, 255)
                    self.buttonSignIn.drawButton(self.MainWindow)
                    self.buttonSignUp.color = (86, 140, 255)
                    self.buttonSignUp.drawButton(self.MainWindow)
                pygame.display.update()


