from pygame import *
from pygame.sprite import Group
import pygame
import time
import sys
from random import randint
from componentes import button,Label,Music,Aguila,BloqueAcero,BloqueLadrillo,BloqueMadera,Player,CursorBloques
from interfaces.intPantallas import Pantallas
from weapons.Bomb import Bomb 
from weapons.Water import Water
from weapons.Fire import Fire
from componentes.ContadorBloques import dibujar_contador

class GameScreen(Pantallas):
    def __init__(self,controlador,jugador1,jugador2,musica1,musica2):

        self.controlador=controlador
        self.pantalla=controlador.screen
        self.MainWindow=controlador.screen
        self.i18n=controlador.i18n
        self.jugador1=jugador1
        self.jugador2=jugador2
        self.musica1=musica1
        self.musica2=musica2
        pygame.display.set_caption('Pantalla1')
        self.buttonEnter = button.Button(740, 350, 100, 50, 'Enter', (86, 140, 255), (2, 82, 253), (86, 140, 255), 20)

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.tiempo_inicial = pygame.time.get_ticks()
        self.tanque = pygame.image.load("imagenes/Tank_Image.png")
        self.destroyedBlocks = 0
        self.points = 0

        self.font = pygame.font.Font(None, 36)

        self.fondosDisponibles=[pygame.transform.scale(pygame.image.load("imagenes/fondo2.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo3.jpg"),(1920,1920)),pygame.transform.scale(pygame.image.load("imagenes/fondo4.jpg"),(1920,1920))]
        self.fondo=self.fondosDisponibles[0]

        self.tanqueSprite = Group()
        self.mitanque = Player.Player(self.MainWindow)
        self.tanqueSprite.add(self.mitanque)

        self.aguila = Aguila.Aguila(self.MainWindow)
        self.aguilaSprite = Group()
        self.aguilaSprite.add(self.aguila)
        self.aguila.set_position(0,200)

        self.cursorSprite=Group()
        self.cursor=CursorBloques.CursorBloques(self.MainWindow)
        self.cursorSprite.add(self.cursor)

        self.steelSprite=Group()
        self.steel=BloqueAcero.BloqueAcero(self.MainWindow)
        self.steelSprite.add(self.steel)
        self.bloques_acero=[]

        self.brickSprite=Group()
        self.brick=BloqueLadrillo.BloqueLadrillo(self.MainWindow)
        self.brickSprite.add(self.brick)
        self.bloques_ladrillo=[]

        self.woodSprite=Group()
        self.wood=BloqueMadera.BloqueMadera(self.MainWindow)
        self.woodSprite.add(self.wood)
        self.bloques_madera=[]

        self.bombSprite = Group()
        self.fireSprite = Group()
        self.waterSprite = Group()
        self.bombs = []
        self.fires = []
        self.waters = []

        self.music = Music.Music(self.MainWindow, self.musica1)
        self.music.playSong()
        self.musicStartTime = time.time()
        self.pauseTime = 0

        self.labelCharacterInScreen = Label.Label(self.i18n.t("player"), 30, 650, 20, (0, 0, 0))
        self.labelCharacterInScreen.update_text(self.jugador1)

        self.anchoVentana=self.MainWindow.get_width()
        self.altoVentana=self.MainWindow.get_height()
        self.rect_surface=pygame.Surface((self.anchoVentana,self.altoVentana),pygame.SRCALPHA)

        self.cantidadBloques={'acero':10, 'madera':10, 'ladrillo':10}

        self.image_change_time = pygame.time.get_ticks() + 1000

        self.pausa = False
        self.paused_rect = pygame.Surface((self.anchoVentana, self.altoVentana), pygame.SRCALPHA)
        self.paused_rect.fill((128, 128, 128, 128)) 

        self.ayuda = False

        
    def mostrar_contador_bombas(self, contador, MainWindow):
        blanco = (255, 255, 255)
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bombas: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 0))
        
    def mostrar_contador_agua(self, contador, MainWindow):
        blanco = (255, 255, 255)
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bolas de Agua: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 30))

    def mostrar_contador_fuego(self, contador, MainWindow):
        blanco = (255, 255, 255)
        font = pygame.font.Font(None, 36)
        texto = font.render(f'Bolas de Fuego: {contador}', True, blanco)
        MainWindow.blit(texto, (1200 - texto.get_width() - 10, 60))

    def runner(self):
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif not self.pausa:
                if event.type == KEYDOWN:
                    if event.key==K_p:
                        self.pausa = True
                        self.music.pause()

                    elif event.key == K_g:
                        self.fondo = self.fondosDisponibles[randint(0, len(self.fondosDisponibles) - 1)]

                    elif event.key == K_b:
                        if Bomb.can_place_bomb():
                            bombDir = self.mitanque.getDirection()
                            tankRect = self.mitanque.getRect()
                            bomb = Bomb(bombDir, tankRect, self.MainWindow)
                            bomb.place_bomb()
                            self.bombSprite.add(bomb)
                            self.bombs.append(bomb)
                            current_time = pygame.time.get_ticks()
                            if current_time >= self.image_change_time:
                                if self.mitanque.image == self.mitanque.skins[1]:
                                    self.mitanque.image =self.mitanque.skins[0]
                                else:
                                    self.mitanque.image = self.mitanque.skins[1]
                    
                    elif event.key == K_m:
                        if Water.can_place_water():
                            waterDir = self.mitanque.getDirection()
                            tankRect = self.mitanque.getRect()
                            water = Water(waterDir, tankRect, self.MainWindow)
                            water.place_water()
                            self.waterSprite.add(water)
                            self.waters.append(water)
                            current_time = pygame.time.get_ticks()
                            if current_time >= self.image_change_time:
                                if self.mitanque.image == self.mitanque.skins[1]:
                                    self.mitanque.image = self.mitanque.skins[0]
                                else:
                                    self.mitanque.image = self.mitanque.skins[1]
                    
                    elif event.key == K_n:
                        if Fire.can_place_fire():
                            fireDir = self.mitanque.getDirection()
                            tankRect = self.mitanque.getRect()
                            fire = Fire(fireDir, tankRect, self.MainWindow)
                            fire.place_fire()
                            self.fireSprite.add(fire)
                            self.fires.append(fire)
                            current_time = pygame.time.get_ticks()
                            if current_time >= self.image_change_time:
                                if self.mitanque.image == self.mitanque.skins[1]:
                                    self.mitanque.image = self.mitanque.skins[0]
                                else:
                                    self.mitanque.image = self.mitanque.skins[1]

                    elif event.key == K_1 and self.cantidadBloques['acero'] > 0:
                        self.cantidadBloques['acero'] -= 1
                        bloque_acero = BloqueAcero.BloqueAcero(self.MainWindow)
                        bloque_acero.rect.topleft = self.cursor.get_pos()
                        self.bloques_acero.append(bloque_acero)

                    elif event.key == K_2 and self.cantidadBloques['madera'] > 0:
                        self.cantidadBloques['madera'] -= 1
                        bloque_madera = BloqueMadera.BloqueMadera(self.MainWindow)
                        bloque_madera.rect.topleft=self.cursor.get_pos()
                        self.bloques_madera.append(bloque_madera)
                        
                    elif event.key == K_3 and self.cantidadBloques['ladrillo'] > 0:
                        self.cantidadBloques['ladrillo'] -= 1
                        bloque_ladrillo = BloqueLadrillo.BloqueLadrillo(self.MainWindow)
                        bloque_ladrillo.rect.topleft=self.cursor.get_pos()
                        self.bloques_ladrillo.append(bloque_ladrillo)

                elif event.type == self.music.songEnd:
                    # Aquí puedes ejecutar el código que deseas cuando la canción termine
                    print("La canción ha terminado de reproducirse.")
                    running = False  # Puedes agregar tu propia lógica para continuar después de la canción
                    ##################################################################################
                    #self.winScreen(self.points)

            elif self.pausa:
                if event.type == KEYDOWN and event.key == K_p:
                    self.pausa = False
                    self.ayuda = False
                    self.music.unpause()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1: 
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (500 <= mouse_x <= 600) and (200 <= mouse_y <= 250): 
                        self.pausa = False
                        self.ayuda=False
                        self.music.unpause()
                    elif (200 <= mouse_x <= 300) and (200 <= mouse_y <= 250):
                        self.ayuda = True
                    elif (self.anchoVentana - 150 <= mouse_x <= self.anchoVentana - 50) and (self.altoVentana - 50 <= mouse_y <= self.altoVentana):
                        self.ayuda = False
        
        if self.pausa:
            self.MainWindow.blit(self.paused_rect, (0, 0))

            ayuda_button = pygame.draw.rect(self.MainWindow, (255, 255, 255), (200, 200, 100, 50))
            podio_button = pygame.draw.rect(self.MainWindow, (255, 255, 255), (350, 200, 100, 50))
            salir_button = pygame.draw.rect(self.MainWindow, (255, 255, 255), (500, 200, 100, 50))

            mouse_x, mouse_y = pygame.mouse.get_pos()

            ayuda_color = (150, 150, 150) if ayuda_button.collidepoint(mouse_x, mouse_y) else (255, 255, 255)
            podio_color = (150, 150, 150) if podio_button.collidepoint(mouse_x, mouse_y) else (255, 255, 255)
            salir_color = (150, 150, 150) if salir_button.collidepoint(mouse_x, mouse_y) else (255, 255, 255)

            pygame.draw.rect(self.MainWindow, ayuda_color, (200, 200, 100, 50))
            pygame.draw.rect(self.MainWindow, podio_color, (350, 200, 100, 50))
            pygame.draw.rect(self.MainWindow, salir_color, (500, 200, 100, 50))

            ayuda_text = self.font.render('Ayuda', True, (0, 0, 0))
            podio_text = self.font.render('Podio', True, (0, 0, 0))
            salir_text = self.font.render('Salir', True, (0, 0, 0))

            ayuda_rect = ayuda_text.get_rect(center=ayuda_button.center)
            podio_rect = podio_text.get_rect(center=podio_button.center)
            salir_rect = salir_text.get_rect(center=salir_button.center)

            self.MainWindow.blit(ayuda_text, ayuda_rect.topleft)
            self.MainWindow.blit(podio_text, podio_rect.topleft)
            self.MainWindow.blit(salir_text, salir_rect.topleft)

            if self.ayuda:
                pygame.draw.rect(self.MainWindow, (0, 0, 0), (0, 0, self.anchoVentana, self.altoVentana))

                salir_button = pygame.draw.rect(self.MainWindow, (255, 255, 255), (self.anchoVentana - 150, self.altoVentana - 50, 100, 50))
                salir_text = self.font.render('Salir', True, (0, 0, 0))
                salir_rect = salir_text.get_rect(center=salir_button.center)

                salir_color = (150, 150, 150) if salir_button.collidepoint(mouse_x, mouse_y) else (255, 255, 255)
                pygame.draw.rect(self.MainWindow, salir_color, (self.anchoVentana - 150, self.altoVentana - 50, 100, 50))

                joystick_up = pygame.transform.scale(pygame.image.load("Assets/Keys/JoystickUp.png"),(50,50))
                joystick_down = pygame.transform.scale(pygame.image.load("Assets/Keys/JoystickDown.png"),(50,50))
                joystick_right = pygame.transform.scale(pygame.image.load("Assets/Keys/JoystickRight.png"),(50,50))
                joystick_left = pygame.transform.scale(pygame.image.load("Assets/Keys/JoystickLeft.png"),(50,50))

                self.MainWindow.blit(joystick_up, (self.anchoVentana // 2 - 25, 100))
                self.MainWindow.blit(joystick_down, (self.anchoVentana // 2 - 25, 200))
                self.MainWindow.blit(joystick_right, (self.anchoVentana // 2 - 25, 300))
                self.MainWindow.blit(joystick_left, (self.anchoVentana // 2 - 25, 400))

                font = pygame.font.Font(None, 30)
                text_up = font.render('Moverse Arriba (Atacante/Defensor)', True, (255, 255, 255))
                text_down = font.render('Moverse Abajo (Atacante/Defensor)', True, (255, 255, 255))
                text_right = font.render('Moverse Derecha (Atacante/Defensor)', True, (255, 255, 255))
                text_left = font.render('Moverse Izquierda (Atacante/Defensor)', True, (255, 255, 255))

                self.MainWindow.blit(text_up, (self.anchoVentana // 2 - text_up.get_width() // 2, 160))
                self.MainWindow.blit(text_down, (self.anchoVentana // 2 - text_down.get_width() // 2, 260))
                self.MainWindow.blit(text_right, (self.anchoVentana // 2 - text_right.get_width() // 2, 360))
                self.MainWindow.blit(text_left, (self.anchoVentana // 2 - text_left.get_width() // 2, 460))

                self.MainWindow.blit(salir_text, salir_rect.topleft)

            pygame.display.update()
            return

        self.MainWindow.blit(self.fondo, (0, 0))
        self.clock.tick(self.fps)
        dibujar_contador(self.MainWindow, self.cantidadBloques)

        if not self.pausa:
            for bloque_acero in self.bloques_acero:
                bloque_acero.update()

                bombs_hit = pygame.sprite.spritecollide(bloque_acero, self.bombSprite, True)
                for bomb in bombs_hit:
                    bloque_acero.health-=100
                    Bomb.bomb_count += 1

                fires_hit = pygame.sprite.spritecollide(bloque_acero, self.fireSprite, True)
                for fire in fires_hit:
                    bloque_acero.health-=100
                    Fire.fire_count += 1

                waters_hit = pygame.sprite.spritecollide(bloque_acero, self.waterSprite, True)
                for water in waters_hit:
                    bloque_acero.health-=50
                    Water.water_count += 1

                if bloque_acero.health <= 0:
                    self.bloques_acero.remove(bloque_acero)

                self.MainWindow.blit(bloque_acero.image, bloque_acero.rect)

            for bloque_madera in self.bloques_madera:
                bloque_madera.update()

                bombs_hit = pygame.sprite.spritecollide(bloque_madera, self.bombSprite, True)
                for bomb in bombs_hit:
                    bloque_madera.health-=100
                    Bomb.bomb_count += 1

                fires_hit = pygame.sprite.spritecollide(bloque_madera, self.fireSprite, True)
                for fire in fires_hit:
                    bloque_madera.health-=100
                    Fire.fire_count += 1

                waters_hit = pygame.sprite.spritecollide(bloque_madera, self.waterSprite, True)
                for water in waters_hit:
                    bloque_madera.health-=100
                    Water.water_count += 1

                if bloque_madera.health <= 0:
                    self.bloques_madera.remove(bloque_madera)

                self.MainWindow.blit(bloque_madera.image, bloque_madera.rect)

            for bloque_ladrillo in self.bloques_ladrillo:
                bloque_ladrillo.update()

                bombs_hit = pygame.sprite.spritecollide(bloque_ladrillo, self.bombSprite, True)
                for bomb in bombs_hit:
                    bloque_ladrillo.health-=100
                    Bomb.bomb_count += 1

                fires_hit = pygame.sprite.spritecollide(bloque_ladrillo, self.fireSprite, True)
                for fire in fires_hit:
                    bloque_ladrillo.health-=50
                    Fire.fire_count += 1

                waters_hit = pygame.sprite.spritecollide(bloque_ladrillo, self.waterSprite, True)
                for water in waters_hit:
                    bloque_ladrillo.health-=33.34
                    Water.water_count += 1

                if bloque_ladrillo.health <= 0:
                    self.bloques_ladrillo.remove(bloque_ladrillo)

                self.MainWindow.blit(bloque_ladrillo.image, bloque_ladrillo.rect)

            self.tanqueSprite.update(self.MainWindow)
        self.tanqueSprite.draw(self.MainWindow)

        if not self.pausa:
            self.cursorSprite.update(self.MainWindow)
        self.cursorSprite.draw(self.MainWindow)

        self.aguilaSprite.draw(self.MainWindow)
        if not self.pausa:
            self.bombSprite.update()
        self.bombSprite.draw(self.MainWindow)
        if not self.pausa:
            self.fireSprite.update()
        self.fireSprite.draw(self.MainWindow)
        if not self.pausa:
            self.waterSprite.update()
        self.waterSprite.draw(self.MainWindow)

        self.mostrar_contador_bombas(Bomb.bomb_count, self.MainWindow)
        self.mostrar_contador_agua(Water.water_count, self.MainWindow)
        self.mostrar_contador_fuego(Fire.fire_count, self.MainWindow)

        self.labelCharacterInScreen.draw(self.MainWindow)

        if not self.pausa:
            elapsed_time = time.time() - self.musicStartTime

            text = self.font.render(f'Tiempo: {int(elapsed_time)} / {int(self.music.duration)} segundos', True, (0, 0, 0))

            tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_inicial) // 1000
            timerLabel = self.font.render("Time: " + str(tiempo_transcurrido), True, (63, 176, 224))

            desBlocksLabel = self.font.render("Destroyed blocks: " + str(self.destroyedBlocks), 0, (63, 176, 224))

            pointsLabel = self.font.render("Points: " + str(self.points), 0, (63, 176, 224))

        self.MainWindow.blit(text, (100, 100))
        self.MainWindow.blit(timerLabel, (20, 10))
        self.MainWindow.blit(desBlocksLabel, (120, 10))
        self.MainWindow.blit(pointsLabel, (400, 10))


        if not self.pausa:
            pygame.display.update()

            if not self.pausa:
                bombs_to_remove = []
                for bomb in self.bombs:
                    if bomb.rect.bottom < 0 or bomb.rect.top> self.MainWindow.get_height() or bomb.rect.left > self.MainWindow.get_width() or bomb.rect.right < 0:
                        bombs_to_remove.append(bomb)
                        Bomb.bomb_count += 1
                    if self.aguila.rect.colliderect(bomb.rect):
                        self.gameoverScreen(self.points)
                for bomb in bombs_to_remove:
                    self.bombs.remove(bomb)

                waters_to_remove = []
                for water in self.waters:
                    if water.rect.bottom < 0:
                        waters_to_remove.append(water)
                        Water.water_count += 1
                    if self.aguila.rect.colliderect(water.rect):
                        self.gameoverScreen(self.points)
                for water in waters_to_remove:
                    self.waters.remove(water)

                fires_to_remove = []
                for fire in self.fires:
                    if fire.rect.bottom < 0:
                        fires_to_remove.append(fire)
                        Fire.fire_count += 1
                    if self.aguila.rect.colliderect(fire.rect):
                        self.gameoverScreen(self.points)
                        print("collide")
                for fire in fires_to_remove:
                    self.fires.remove(fire)
                     
        
                    

    
    def change(self,newPantalla):
         self.controlador.cambio(newPantalla)