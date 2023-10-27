import threading
from random import randint
import pygame, sys, Button, Entry, Label, FilesController, JsonController, Player, Aguila
from pygame import *
from pygame.sprite import Group
from pygame.locals import *
import Bomb
import Music
import time

class Screens:
    def __init__(self):
        pygame.init()

        self.icono = pygame.image.load("imagenes/logo.jpg")
        pygame.display.set_icon(self.icono)
        pygame.display.set_caption('Eagle Defender')

        self.MainWindow = pygame.display.set_mode((1200, 650))
        self.bg = pygame.image.load("imagenes/Background.png")
        self.buttonSignIn = Button.Button(650, 300, 150, 50, 'Sign In', (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.buttonSignUp = Button.Button(850, 300, 150, 50, 'Sign Up', (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)

        self.buttonRegisterUser = Button.Button(740, 550, 150, 50, 'Register User', (111, 84, 247), (78, 42, 255), (111, 84, 247), 25)
        self.buttonSelectSong = Button.Button(760, 450, 100, 25, 'Select Music', (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonSelectPhoto = Button.Button(760, 500, 100, 25, 'Select Photo', (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        self.user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.email_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry = Entry.Entry(750, 350, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.rol_entry = Entry.Entry(750, 400, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.user_entry_signIn = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry_signIn = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.labelUser = Label.Label('User:', 20, 675, 250, (0, 0, 0))
        self.labelEmail = Label.Label('Email:', 20, 675, 300, (0, 0, 0))
        self.labelPassword = Label.Label('Password:', 20, 675, 350, (0, 0, 0))
        self.labelMusic = Label.Label('Music:', 20, 675, 450, (0, 0, 0))
        self.labelPhoto = Label.Label('Photo:', 20, 675, 500, (0, 0, 0))
        self.labelRol = Label.Label('Rol:', 20, 675, 400, (0, 0, 0))
        self.labelUser_signIn = Label.Label('User:', 20, 675, 250, (0, 0, 0))
        self.labelPassword_signIn = Label.Label('Password:', 20, 675, 300, (0, 0, 0))
        self.labelCharacter_singIn = Label.Label('Atacante', 60, 700, 180, (0, 0, 0))
        self.labelCharacterInScreen = Label.Label('Player', 30, 650, 20, (0, 0, 0))

        self.userFile = JsonController.JsonControllerUsers("users")

        self.SteelButton = Button.Button(915, 0, 150, 50, 'Steel', (111, 84, 247), (78, 42, 255), (111, 84, 247), 25)
        self.steel_selection = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.playerName = ""
        self.favoriteSong = ""
    def signInScreen(self):

        Atacante = True
        Defensor = False
        running = True
        while(running):
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
                        #Screens.playScreen(self)
                        if self.userFile.verifyUser(self.user_entry_signIn.text, self.password_entry_signIn.text) and Defensor==False:
                            Atacante = False
                            Defensor = True
                            self.labelCharacter_singIn.update_text("Defensor")
                            self.playerName = self.user_entry_signIn.text
                            self.favoriteSong = str(self.userFile.selectSong(self.user_entry_signIn.text))
                            self.user_entry_signIn.text = ''
                            self.password_entry_signIn.text = ''

                        elif self.userFile.verifyUser(self.user_entry_signIn.text, self.password_entry_signIn.text):
                            self.playScreen()
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

                pygame.display.update()

    def signUpScreen(self):
        userFile = JsonController.JsonControllerUsers
        FileDialog = FilesController.FileControllers("","")

        running = True
        while (running):
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
                        running = False
                        self.mainScreen()

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

                pygame.display.update()

    def mostrar_contador_bombas(self, contador, MainWindow):
        """
        Display the bomb counter on the screen.

        Args:
            contador (int): The bomb count.

        Returns:
            None
        """
        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        # Clear the counter area
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(MainWindow, negro, (1200 - 150, 0, 150, 30))
        texto = font.render(f'Bombas: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 10))

    def playScreen(self):
        fps = 60
        clock = pygame.time.Clock()
        tiempo_inicial = pygame.time.get_ticks()
        tanque = pygame.image.load("imagenes/Tank_Image.png")
        sprites = Group()
        bombs = []  # List to store bombs
        destroyedBlocks = 0
        points = 0

        SteelButtonClicked = False
        steelBlock = 10

        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        font = pygame.font.Font(None, 36)

        self.fondosDisponibles=[pygame.transform.scale(pygame.image.load("imagenes/fondo2.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo3.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo4.jpg"),(1920,1920))]
        self.fondo=self.fondosDisponibles[0]

        tanqueSprite = Group()
        mitanque = Player.Player(self.MainWindow)
        tanqueSprite.add(mitanque)

        aguila = Aguila.Aguila(self.MainWindow)
        aguila.set_position(0,200)


        music = Music.Music(self.MainWindow, self.favoriteSong)
        music.playSong()
        musicStartTime = time.time()

        self.labelCharacterInScreen.update_text(self.playerName)

        running = True
        while(running):
            self.SteelButton.drawButton(self.MainWindow)
            self.MainWindow.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_g:
                    self.fondo = self.fondosDisponibles[randint(0,len(self.fondosDisponibles)-1)]
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if Bomb.Bomb.can_place_bomb():
                        bomb = Bomb.Bomb()
                        bomb.place_bomb(pygame.mouse.get_pos())
                        sprites.add(bomb)
                        bombs.append(bomb)
                # elif event.type==KEYDOWN:
                # interfaz_bloques.cambiar_bloque_seleccionado(event.key)
                    elif self.SteelButton.is_clicked(mouse.get_pos()):
                        print("button steel clicked")
                        print(self.SteelButton.seeActiveness(mouse.get_pos(), self.MainWindow))

                        self.SteelButton.seeActiveness(mouse.get_pos(), self.MainWindow)
                        '''
                        if self.SteelButton.seeActiveness(mouse.get_pos(), self.MainWindow)) == False:
                            self.SteelButton.color = self.steel_selection.colorActive
                            self.SteelButton.activeness = True
                        else:
                            self.SteelButton.color = self.steel_selection.colorPassive
                            self.SteelButton.activeness = False
                            '''
                elif event.type == music.songEnd:
                    # Aquí puedes ejecutar el código que deseas cuando la canción termine
                    print("La canción ha terminado de reproducirse.")
                    #running = False  # Puedes agregar tu propia lógica para continuar después de la canción
                    self.winScreen(points)


            self.MainWindow.blit(self.fondo,(0,0))
            clock.tick(fps)

            tanqueSprite.update(self.MainWindow)
            tanqueSprite.draw(self.MainWindow)

            sprites.update()
            sprites.draw(self.MainWindow)
            self.mostrar_contador_bombas(Bomb.Bomb.bomb_count, self.MainWindow)

            self.labelCharacterInScreen.draw(self.MainWindow)

            elapsed_time = time.time() - musicStartTime

            # Actualiza la pantalla
            text = font.render(f'Tiempo: {int(elapsed_time)} / {int(music.duration)} segundos', True, (0, 0, 0))
            self.MainWindow.blit(text, (100, 100))
            #pygame.display.flip()
            # Timer
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicial) // 1000
            timerLabel = font.render("Time: " + str(tiempo_transcurrido), True, (63, 176, 224))
            self.MainWindow.blit(timerLabel, (20, 10))

            # Showing the destroyed blocks
            desBlocksLabel = font.render("Destroyed blocks: " + str(destroyedBlocks), 0, (63, 176, 224))
            self.MainWindow.blit(desBlocksLabel, (120, 10))

            # Points
            pointsLabel = font.render("Points: " + str(points), 0, (63, 176, 224))
            self.MainWindow.blit(pointsLabel, (400, 10))

            self.MainWindow.blit(aguila.image, aguila.rect)

            self.SteelButton.drawButton(self.MainWindow)

            pygame.display.update()

            # Remove bombs that have gone off-screen
            bombs_to_remove = []
            for bomb in bombs:
                # Saber si la bomba toca el aguila
                if mitanque.rect.colliderect(bomb.rect):
                    #self.gameoverScreen(points)
                    print("collide")
                    aguila.update()

                if bomb.rect.bottom < 0:
                    bombs_to_remove.append(bomb)
                    bomb.bomb_count += 1

            for bomb in bombs_to_remove:
                bombs.remove(bomb)
    def winScreen(self, points):
        fps = 60
        clock = pygame.time.Clock()

        pygame.display.set_caption("You Win!")

        background_color_hex = 0x008aff

        background_color = (
        background_color_hex >> 16 & 255, background_color_hex >> 8 & 255, background_color_hex & 255)
        self.MainWindow.fill(background_color)

        background_image = pygame.image.load("imagenes/gamewinScreen.jpg")
        background_image = pygame.transform.scale(background_image, (1000, 650))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.MainWindow.blit(background_image, (100, 0))

            font = pygame.font.Font(None, 36)
            pointsLabel = font.render("Points Obtained: " + str(points), 0, (0, 0, 0))
            self.MainWindow.blit(pointsLabel, (600, 50))
            #reproducir cancion elegida

            #salon de la fama

            pygame.display.update()

    def gameoverScreen(self, points):
        fps = 60
        clock = pygame.time.Clock()

        pygame.display.set_caption("You Lost!")
        background_image = pygame.image.load("imagenes/gameoverScreen.jpg")
        background_image = pygame.transform.scale(background_image, (1200, 650))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            font = pygame.font.Font(None, 36)
            pointsLabel = font.render("Points Obtained: " + str(points), 0, (0, 0, 0))
            self.MainWindow.blit(pointsLabel, (600, 50))

            self.MainWindow.blit(background_image, (0, 0))

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

                self.buttonSignUp.seeActiveness(mouse.get_pos(), self.MainWindow)
                self.buttonSignIn.seeActiveness(mouse.get_pos(), self.MainWindow)

                pygame.display.update()


