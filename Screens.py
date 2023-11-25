import i18n
i18n.load_path.append('./translation/')
i18n.set('locale', 'es')
i18n.set('file_format', 'json')
i18n.set('filename_format', '{locale}.{format}')

import threading
from random import randint
import pygame, sys, Button, Entry, Label, FilesController, JsonController, Player, Aguila
from ContadorBloquesTest import dibujar_contador, recargar_acero, recargar_madera, recargar_ladrillo
from pygame import *
from pygame.sprite import Group
from pygame.locals import *
from VentanaPausa import draw_pause
from Weapons.Bomb import Bomb
from Weapons.Water import Water
from Weapons.Fire import Fire
import Music
import time

anchoVentana, altoVentana =1200, 650

anchoContador=180
altoContador=60
anchoBloque=50
altoBloque=20
espacioEntreBloques=5
distanciaBorde=20
recargaBloqueAcero=30000
recargaBloqueMadera=30000
recargaBloqueLadrillo=30000
mensajeTiempo=3000
mostrarMensajeEvento=pygame.USEREVENT +1

tiempo_ultima_recarga_Acero = pygame.time.get_ticks()
tiempo_ultima_recarga_Madera = pygame.time.get_ticks()
tiempo_ultima_recarga_Ladrillo = pygame.time.get_ticks()
bloques_recargados=0

cantidadBloques={'acero':5, 'madera':10, 'ladrillo':8}
coloresBloques={'acero':(169, 169, 169), 'madera': (139,69,19), 'ladrillo': (255,0,0)}

colorTexto=(0,0,0)
fuente="Arial"
tamanoFuente=20

rect_surface=pygame.Surface((anchoVentana,altoVentana),pygame.SRCALPHA)


class Screens:
    def __init__(self):

        pygame.init()

        self.icono = pygame.image.load("imagenes/logo.jpg")
        pygame.display.set_icon(self.icono)
        pygame.display.set_caption('Eagle Defender')

        self.MainWindow = pygame.display.set_mode((anchoVentana, altoVentana))
        self.bg = pygame.image.load("imagenes/Background.png")
        self.buttonSignIn = Button.Button(650, 300, 150, 50, i18n.t("login"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)
        self.buttonSignUp = Button.Button(850, 300, 150, 50, i18n.t("singup"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 30)

        self.buttonRegisterUser = Button.Button(740, 550, 150, 50, i18n.t("register"), (111, 84, 247), (78, 42, 255), (111, 84, 247), 25)
        self.buttonSelectSong = Button.Button(760, 450, 100, 25, i18n.t("selec_music"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonSelectPhoto = Button.Button(760, 500, 100, 25, i18n.t("select_picture"), (86, 140, 255), (2, 82, 253), (86, 140, 255), 23)
        self.buttonEnter = Button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        self.user_entry = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.email_entry = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry = Entry.Entry(750, 350, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.rol_entry = Entry.Entry(750, 400, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.user_entry_signIn = Entry.Entry(750, 250, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)
        self.password_entry_signIn = Entry.Entry(750, 300, (8, 42, 79), (12, 76, 143), (12, 76, 143), '', False)

        self.labelUser = Label.Label(i18n.t('user'), 20, 675, 250, (0, 0, 0))
        self.labelEmail = Label.Label(i18n.t('email'), 20, 675, 300, (0, 0, 0))
        self.labelPassword = Label.Label(i18n.t('password'), 20, 675, 350, (0, 0, 0))
        self.labelMusic = Label.Label(i18n.t('music'), 20, 675, 450, (0, 0, 0))
        self.labelPhoto = Label.Label(i18n.t('photo'), 20, 675, 500, (0, 0, 0))
        self.labelRol = Label.Label(i18n.t('rol'), 20, 675, 400, (0, 0, 0))
        self.labelUser_signIn = Label.Label(i18n.t('user'), 20, 675, 250, (0, 0, 0))
        self.labelPassword_signIn = Label.Label(i18n.t("password"), 20, 675, 300, (0, 0, 0))
        self.labelCharacter_singIn = Label.Label(i18n.t("attacker"), 60, 700, 180, (0, 0, 0))
        self.labelCharacterInScreen = Label.Label(i18n.t("player"), 30, 650, 20, (0, 0, 0))

        self.userFile = JsonController.JsonControllerUsers("users")

        self.playerName = ""
        self.favoriteSong = ""

        self.music = Music.Music(self.MainWindow, "Environment.ogg")

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
                        # Screens.playScreen(self)
                        if self.userFile.verifyUser(self.user_entry_signIn.text,
                                                    self.password_entry_signIn.text) and Defensor == False:
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
        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        # Clear the counter area
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bombas: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 0))
    def mostrar_contador_agua(self, contador, MainWindow):
        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bolas de Agua: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 30))
    def mostrar_contador_fuego(self, contador, MainWindow):
        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bolas de Fuego: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 60))

    def playScreen(self):
        pausa = False

        fps = 60
        clock = pygame.time.Clock()
        tiempo_inicial = pygame.time.get_ticks()
        sprites = Group()
        bombs = []
        waters = []
        fires = []
        destroyedBlocks = 0
        points = 0

        font = pygame.font.Font(None, 36)

        self.fondosDisponibles=[pygame.transform.scale(pygame.image.load("imagenes/fondo2.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo3.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo4.jpg"),(1920,1920))]
        self.fondo=self.fondosDisponibles[0]

        tanqueSprite = Group()
        mitanque = Player.Player(self.MainWindow)
        tanqueSprite.add(mitanque)

        aguila = Aguila.Aguila(self.MainWindow)
        aguilaSprite = Group()
        aguilaSprite.add(aguila)
        aguila.set_position(0,200)

        music = Music.Music(self.MainWindow, self.favoriteSong)
        music.playSong()
        musicStartTime = time.time()

        self.labelCharacterInScreen.update_text(self.playerName)

        steelblock = pygame.image.load("Assets/Blocks/SteelBlock.png")
        steelblock = pygame.transform.scale(steelblock,(50,50))
        woodblock = pygame.image.load("Assets/Blocks/woodblock.jpg")
        woodblock = pygame.transform.scale(woodblock, (50, 50))
        brickblock = pygame.image.load("Assets/Blocks/brickblock.jpg")
        brickblock = pygame.transform.scale(brickblock, (50, 50))

        blocks=Group()
        

        blockcursor=pygame.image.load("Assets/Cursor/Blocks_Cursor.png")
        blockcursor= pygame.transform.scale(blockcursor,(50,50))
        cursor_x=0
        cursor_y=0
        blockcursor_position=(cursor_x,cursor_y)

        mensaje_tiempo_inicio_Acero= None
        mensaje_tiempo_inicio_Madera = None
        mensaje_tiempo_inicio_Ladrillo = None
        bloques_acero=[]
        bloques_madera = []
        bloques_ladrillo = []

        image_change_time = pygame.time.get_ticks() + 1000

        running = True
        while(running):
            self.MainWindow.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif not pausa:
                    if event.type == music.songEnd:
                        print("La canción ha terminado de reproducirse.")
                        running = False 
                        self.winScreen(points)
                    elif event.type == KEYDOWN:
                        if event.type == KEYDOWN and event.key == K_g:
                            self.fondo = self.fondosDisponibles[randint(0, len(self.fondosDisponibles) - 1)]

                        elif event.key == K_1 and cantidadBloques['acero'] > 0:
                            cantidadBloques['acero'] -= 1
                            bloque_acero = (cursor_x, cursor_y)
                            bloques_acero.append(bloque_acero)
                            mensaje_tiempo_inicio_Acero = tiempo_ultima_recarga_Acero

                        elif event.key == K_2 and cantidadBloques['madera'] > 0:
                            cantidadBloques['madera'] -= 1
                            bloque_madera = (cursor_x, cursor_y)
                            bloques_madera.append(bloque_madera)
                            mensaje_tiempo_inicio_Madera = tiempo_ultima_recarga_Madera

                        elif event.key == K_3 and cantidadBloques['ladrillo'] > 0:
                            cantidadBloques['ladrillo'] -= 1
                            bloque_ladrillo = (cursor_x, cursor_y)
                            bloques_ladrillo.append(bloque_ladrillo)
                            mensaje_tiempo_inicio_Ladrillo = tiempo_ultima_recarga_Ladrillo

                        elif event.key == K_UP and cursor_y - 50 >= 0:
                            cursor_y -= 50
                            blockcursor_position = (cursor_x, cursor_y)

                        elif event.key == K_DOWN and cursor_y + 100 <= altoVentana:
                            cursor_y += 50
                            blockcursor_position = (cursor_x, cursor_y)

                        elif event.key == K_RIGHT and cursor_x + 100 <= anchoVentana:
                            cursor_x += 50
                            blockcursor_position = (cursor_x, cursor_y)

                        elif event.key == K_LEFT and cursor_x - 50 >= 0:
                            cursor_x -= 50
                            blockcursor_position = (cursor_x, cursor_y)

                        elif event.key == K_n:
                            if Fire.can_place_fire():
                                fireDir = mitanque.getDirection()
                                tankRect = mitanque.getRect()
                                fire = Fire(fireDir, tankRect, self.MainWindow)
                                fire.place_fire()
                                sprites.add(fire)
                                fires.append(fire)
                                current_time = pygame.time.get_ticks()
                                if current_time >= image_change_time:
                                    if mitanque.image == mitanque.skins[1]:
                                        mitanque.image = mitanque.skins[0]
                                    else:
                                        mitanque.image = mitanque.skins[1]
                        
                        elif event.key == K_m:
                            if Water.can_place_water():
                                waterDir = mitanque.getDirection()
                                tankRect = mitanque.getRect()
                                water = Water(waterDir, tankRect, self.MainWindow)
                                water.place_water()
                                sprites.add(water)
                                waters.append(water)
                                current_time = pygame.time.get_ticks()
                                if current_time >= image_change_time:
                                    if mitanque.image == mitanque.skins[1]:
                                        mitanque.image = mitanque.skins[0]
                                    else:
                                        mitanque.image = mitanque.skins[1]
                        
                        elif event.key == K_SPACE:
                            if Bomb.can_place_bomb():
                                bombDir = mitanque.getDirection()
                                tankRect = mitanque.getRect()
                                bomb = Bomb(bombDir, tankRect, self.MainWindow)
                                bomb.place_bomb()
                                sprites.add(bomb)
                                bombs.append(bomb)
                                current_time = pygame.time.get_ticks()
                                if current_time >= image_change_time:
                                    if mitanque.image == mitanque.skins[1]:
                                        mitanque.image = mitanque.skins[0]
                                    else:
                                        mitanque.image = mitanque.skins[1]
                        
                        elif event.key == K_p:
                            pausa = True
                            music.pause()
                            draw_pause(self.MainWindow, anchoVentana, altoVentana)
                            self.MainWindow.blit(rect_surface, (0, 0))
                    
                    elif pausa and event.key == K_p:
                            pausa = False
                            music.unpause()
                    
            if not pausa:
                tiempo_actual = pygame.time.get_ticks()

                if tiempo_actual - tiempo_ultima_recarga_Acero >= recargaBloqueAcero:
                    recargar_acero(cantidadBloques)
                    mensaje_tiempo_inicio_Acero = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultima_recarga_Madera >= recargaBloqueMadera:
                    recargar_madera(cantidadBloques)
                    mensaje_tiempo_inicio_Madera = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultima_recarga_Ladrillo >= recargaBloqueLadrillo:
                    recargar_ladrillo(cantidadBloques)
                    mensaje_tiempo_inicio_Ladrillo = pygame.time.get_ticks()

            self.MainWindow.blit(self.fondo, (0, 0))
            clock.tick(fps)
            dibujar_contador(self.MainWindow, cantidadBloques)

            self.MainWindow.blit(blockcursor,blockcursor_position)

            for bloque_acero in bloques_acero:
                self.MainWindow.blit(steelblock, bloque_acero)
            for bloque_madera in bloques_madera:
                self.MainWindow.blit(woodblock, bloque_madera)
            for bloque_ladrillo in bloques_ladrillo:
                self.MainWindow.blit(brickblock, bloque_ladrillo)

            if not pausa:
                if mensaje_tiempo_inicio_Acero is not None and tiempo_actual - mensaje_tiempo_inicio_Acero < mensajeTiempo:
                    fuente_mensaje = pygame.font.SysFont(fuente, tamanoFuente)
                    texto_mensaje = fuente_mensaje.render("Bloque de acero recargado", True, colorTexto)
                    texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(anchoVentana // 2, altoVentana - 20))
                    self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)
            if not pausa:
                if mensaje_tiempo_inicio_Madera is not None and tiempo_actual - mensaje_tiempo_inicio_Madera < mensajeTiempo:
                    fuente_mensaje = pygame.font.SysFont(fuente, tamanoFuente)
                    texto_mensaje = fuente_mensaje.render("Bloque de madera recargado", True, colorTexto)
                    texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(anchoVentana // 2, altoVentana - 20))
                    self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)
            if not pausa:
                if mensaje_tiempo_inicio_Ladrillo is not None and tiempo_actual - mensaje_tiempo_inicio_Ladrillo < mensajeTiempo:
                    fuente_mensaje = pygame.font.SysFont(fuente, tamanoFuente)
                    texto_mensaje = fuente_mensaje.render("Bloque de ladrillo recargado", True, colorTexto)
                    texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(anchoVentana // 2, altoVentana - 20))
                    self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)

            tanqueSprite.update(self.MainWindow)
            tanqueSprite.draw(self.MainWindow)

            aguilaSprite.draw(self.MainWindow)

            sprites.update()
            sprites.draw(self.MainWindow)
            self.mostrar_contador_bombas(Bomb.bomb_count, self.MainWindow)
            self.mostrar_contador_agua(Water.water_count, self.MainWindow)
            self.mostrar_contador_fuego(Fire.fire_count, self.MainWindow)

            self.labelCharacterInScreen.draw(self.MainWindow)

            if not pausa:
                elapsed_time = time.time() - musicStartTime

                # Actualiza la pantalla
                text = font.render(f'Tiempo: {int(elapsed_time)} / {int(music.duration)} segundos', True, (0, 0, 0))
                # pygame.display.flip()
                # Timer
                tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicial) // 1000
                timerLabel = font.render("Time: " + str(tiempo_transcurrido), True, (63, 176, 224))

                # Showing the destroyed blocks
                desBlocksLabel = font.render("Destroyed blocks: " + str(destroyedBlocks), 0, (63, 176, 224))

                # Points
                pointsLabel = font.render("Points: " + str(points), 0, (63, 176, 224))
            self.MainWindow.blit(text, (100, 100))
            self.MainWindow.blit(timerLabel, (20, 10))
            self.MainWindow.blit(desBlocksLabel, (120, 10))
            self.MainWindow.blit(pointsLabel, (400, 10))


            if not pausa:
                pygame.display.update()

                if not pausa:
                    # Remove bombs that have gone off-screen
                    bombs_to_remove = []
                    for bomb in bombs:
                        if bomb.rect.bottom < 0 or bomb.rect.top> self.MainWindow.get_height() or bomb.rect.left > self.MainWindow.get_width() or bomb.rect.right < 0:
                            bombs_to_remove.append(bomb)
                            Bomb.bomb_count += 1
                        if aguila.rect.colliderect(bomb.rect):
                            self.gameoverScreen(points)
                for bomb in bombs_to_remove:
                    bombs.remove(bomb)

                if not pausa:
                    # Remove water balls that have gone off-screen
                    waters_to_remove = []
                    for water in waters:
                        if water.rect.bottom < 0:
                            waters_to_remove.append(water)
                            Water.water_count += 1
                        if aguila.rect.colliderect(water.rect):
                            self.gameoverScreen(points)
                for water in waters_to_remove:
                    waters.remove(water)

                if not pausa:
                    # Remove fire balls that have gone off-screen
                    fires_to_remove = []
                    for fire in fires:
                        if fire.rect.bottom < 0:
                            fires_to_remove.append(fire)
                            Fire.fire_count += 1
                        if aguila.rect.colliderect(fire.rect):
                            self.gameoverScreen(points)
                            print("collide")
                for fire in fires_to_remove:
                    fires.remove(fire)

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
        self.music.playSong()
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

