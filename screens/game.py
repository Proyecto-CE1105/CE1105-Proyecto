from pygame import *
from pygame.sprite import Group
import pygame
import time
import sys
from random import randint
from componentes import button, Entry,Label,Music,Aguila,Bloque,BloqueAcero,BloqueConcreto,BloqueMadera,Player,VentanaPausa,ContadorBloquesTest
from interfaces.intPantallas import Pantallas
from services import JsonController,FilesController
from weapons.Bomb import Bomb 
from weapons.Water import Water
from weapons.Fire import Fire
from componentes.ContadorBloquesTest import dibujar_contador, recargar_acero, recargar_madera, recargar_ladrillo

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

        self.pausa = False

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.tiempo_inicial = pygame.time.get_ticks()
        self.tanque = pygame.image.load("imagenes/Tank_Image.png")
        self.sprites = Group()
        self.bombs = []  # List to store bombs
        self.waters = []
        self.fires = []
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

        self.music = Music.Music(self.MainWindow, self.musica1)
        self.music.playSong()
        self.musicStartTime = time.time()
        self.pauseTime = 0

        self.labelCharacterInScreen = Label.Label(self.i18n.t("player"), 30, 650, 20, (0, 0, 0))
        self.labelCharacterInScreen.update_text(self.jugador1)

        self.steelblock = pygame.image.load("Assets/Blocks/SteelBlock.png")
        self.steelblock = pygame.transform.scale(self.steelblock,(50,50))
        self.woodblock = pygame.image.load("Assets/Blocks/woodblock.jpg")
        self.woodblock = pygame.transform.scale(self.woodblock, (50, 50))
        self.brickblock = pygame.image.load("Assets/Blocks/brickblock.jpg")
        self.brickblock = pygame.transform.scale(self.brickblock, (50, 50))

        self.mensaje_tiempo_inicio_Acero= None
        self.mensaje_tiempo_inicio_Madera = None
        self.mensaje_tiempo_inicio_Ladrillo = None
        self.bloques_acero=[]
        self.bloques_madera = []
        self.bloques_ladrillo = []


        self.anchoVentana=self.MainWindow.get_width()
        self.altoVentana=self.MainWindow.get_height()
        self.rect_surface=pygame.Surface((self.anchoVentana,self.altoVentana),pygame.SRCALPHA)


        self.anchoContador=180
        self.altoContador=60
        self.anchoBloque=50
        self.altoBloque=20
        self.espacioEntreBloques=5
        self.distanciaBorde=20
        self.recargaBloqueAcero=30000
        self.recargaBloqueMadera=30000
        self.recargaBloqueLadrillo=30000
        self.mensajeTiempo=3000
        self.mostrarMensajeEvento=pygame.USEREVENT +1

        self.tiempo_ultima_recarga_Acero = pygame.time.get_ticks()
        self.tiempo_ultima_recarga_Madera = pygame.time.get_ticks()
        self.tiempo_ultima_recarga_Ladrillo = pygame.time.get_ticks()
        self.bloques_recargados=0

        self.cantidadBloques={'acero':5, 'madera':10, 'ladrillo':8}
        self.coloresBloques={'acero':(169, 169, 169), 'madera': (139,69,19), 'ladrillo': (255,0,0)}

        self.colorTexto=(0,0,0)
        self.fuente="Arial"
        self.tamanoFuente=20

        self.image_change_time = pygame.time.get_ticks() + 1000

        
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
    def runner(self):
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif not self.pausa and event.type == KEYDOWN and event.key == K_p:
                self.pausa = True
                self.music.pause()
                # pauseTime=pause_time(musicStartTime)
                self.draw_pause(self.MainWindow, self.anchoVentana, self.altoVentana)
                self.MainWindow.blit(self.rect_surface, (0, 0))
                print("Juego Pausado")
            elif not self.pausa:
                if event.type == KEYDOWN and event.key == K_g:
                    self.fondo = self.fondosDisponibles[randint(0, len(self.fondosDisponibles) - 1)]
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    if Bomb.can_place_bomb():
                        bombDir = self.mitanque.getDirection()
                        tankRect = self.mitanque.getRect()
                        bomb = Bomb(bombDir, tankRect, self.MainWindow)
                        bomb.place_bomb()
                        self.sprites.add(bomb)
                        self.bombs.append(bomb)
                        current_time = pygame.time.get_ticks()
                        if current_time >= self.image_change_time:
                            if self.mitanque.image == self.mitanque.skins[1]:
                                self.mitanque.image =self.mitanque.skins[0]
                            else:
                                self.mitanque.image = self.mitanque.skins[1]
                        print("cambia skin")
                elif event.type == KEYDOWN and event.key == K_m:
                    if Water.can_place_water():
                        waterDir = self.mitanque.getDirection()
                        tankRect = self.mitanque.getRect()
                        water = Water(waterDir, tankRect, self.MainWindow)
                        water.place_water()
                        self.sprites.add(water)
                        self.waters.append(water)
                        current_time = pygame.time.get_ticks()
                        if current_time >= self.image_change_time:
                            if self.mitanque.image == self.mitanque.skins[1]:
                                self.mitanque.image = self.mitanque.skins[0]
                            else:
                                self.mitanque.image = self.mitanque.skins[1]
                        print("cambia skin")
                elif event.type == KEYDOWN and event.key == K_n:
                    if Fire.can_place_fire():
                        fireDir = self.mitanque.getDirection()
                        tankRect = self.mitanque.getRect()
                        fire = Fire(fireDir, tankRect, self.MainWindow)
                        fire.place_fire()
                        self.sprites.add(fire)
                        self.fires.append(fire)
                        current_time = pygame.time.get_ticks()
                        if current_time >= self.image_change_time:
                            if self.mitanque.image == self.mitanque.skins[1]:
                                self.mitanque.image = self.mitanque.skins[0]
                            else:
                                self.mitanque.image = self.mitanque.skins[1]
                        print("cambia skin")

                elif event.type == self.music.songEnd:
                    # Aquí puedes ejecutar el código que deseas cuando la canción termine
                    print("La canción ha terminado de reproducirse.")
                    running = False  # Puedes agregar tu propia lógica para continuar después de la canción
                    ##################################################################################
                    #self.winScreen(self.points)
                elif event.type == KEYDOWN and event.key == K_1 and self.cantidadBloques['acero'] > 0:
                    self.cantidadBloques['acero'] -= 1
                    x, y = pygame.mouse.get_pos()
                    bloque_acero = (x - 25, y - 25)
                    self.bloques_acero.append(bloque_acero)
                    ultimo_tiempo_acero = pygame.time.get_ticks()
                    self.mensaje_tiempo_inicio_Acero = self.tiempo_ultima_recarga_Acero
                elif event.type == KEYDOWN and event.key == K_2 and self.cantidadBloques['madera'] > 0:
                    self.cantidadBloques['madera'] -= 1
                    x, y = pygame.mouse.get_pos()
                    bloque_madera = (x - 25, y - 25)
                    self.bloques_madera.append(bloque_madera)
                    self.ultimo_tiempo_madera = pygame.time.get_ticks()
                    self.mensaje_tiempo_inicio_Madera = self.tiempo_ultima_recarga_Madera
                elif event.type == KEYDOWN and event.key == K_3 and self.cantidadBloques['ladrillo'] > 0:
                    self.cantidadBloques['ladrillo'] -= 1
                    x, y = pygame.mouse.get_pos()
                    bloque_ladrillo = (x - 25, y - 25)
                    self.bloques_ladrillo.append(bloque_ladrillo)
                    ultimo_tiempo_ladrillo = pygame.time.get_ticks()
                    self.mensaje_tiempo_inicio_Ladrillo = self.tiempo_ultima_recarga_Ladrillo
            elif self.pausa and event.type == KEYDOWN and event.key == K_p:
                self.pausa = False
                self.music.unpause()
                # musicStartTime=resume_time(pauseTime)
        if not self.pausa:
            tiempo_actual = pygame.time.get_ticks()

            if tiempo_actual - self.tiempo_ultima_recarga_Acero >= self.recargaBloqueAcero:
                recargar_acero(self.cantidadBloques)
                self.mensaje_tiempo_inicio_Acero = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultima_recarga_Madera >= self.recargaBloqueMadera:
                recargar_madera(self.cantidadBloques)
                self.mensaje_tiempo_inicio_Madera = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultima_recarga_Ladrillo >= self.recargaBloqueLadrillo:
                recargar_ladrillo(self.cantidadBloques)
                self.mensaje_tiempo_inicio_Ladrillo = pygame.time.get_ticks()

        self.MainWindow.blit(self.fondo, (0, 0))
        self.clock.tick(self.fps)
        dibujar_contador(self.MainWindow, self.cantidadBloques)

        for bloque_acero in self.bloques_acero:
            self.MainWindow.blit(self.steelblock, bloque_acero)
        for bloque_madera in self.bloques_madera:
            self.MainWindow.blit(self.woodblock, bloque_madera)
        for bloque_ladrillo in self.bloques_ladrillo:
            self.MainWindow.blit(self.brickblock, bloque_ladrillo)

        if not self.pausa:
            if self.mensaje_tiempo_inicio_Acero is not None and tiempo_actual - self.mensaje_tiempo_inicio_Acero < self.mensajeTiempo:
                fuente_mensaje = pygame.font.SysFont(self.fuente, self.tamanoFuente)
                texto_mensaje = fuente_mensaje.render("Bloque de acero recargado", True, self.colorTexto)
                texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(self.anchoVentana // 2, self.altoVentana - 20))
                self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)
        if not self.pausa:
            if self.mensaje_tiempo_inicio_Madera is not None and tiempo_actual - self.mensaje_tiempo_inicio_Madera < self.mensajeTiempo:
                fuente_mensaje = pygame.font.SysFont(self.fuente, self.tamanoFuente)
                texto_mensaje = fuente_mensaje.render("Bloque de madera recargado", True, self.colorTexto)
                texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(self.anchoVentana // 2, self.altoVentana - 20))
                self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)
        if not self.pausa:
            if self.mensaje_tiempo_inicio_Ladrillo is not None and tiempo_actual - self.mensaje_tiempo_inicio_Ladrillo <self.mensajeTiempo:
                fuente_mensaje = pygame.font.SysFont(self.fuente, self.tamanoFuente)
                texto_mensaje = fuente_mensaje.render("Bloque de ladrillo recargado", True, self.colorTexto)
                texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(self.anchoVentana // 2, self.altoVentana - 20))
                self.MainWindow.blit(texto_mensaje, texto_mensaje_rect)

        self.tanqueSprite.update(self.MainWindow)
        self.tanqueSprite.draw(self.MainWindow)

        self.aguilaSprite.draw(self.MainWindow)

        self.sprites.update()
        self.sprites.draw(self.MainWindow)
        self.mostrar_contador_bombas(Bomb.bomb_count, self.MainWindow)
        self.mostrar_contador_agua(Water.water_count, self.MainWindow)
        self.mostrar_contador_fuego(Fire.fire_count, self.MainWindow)

        self.labelCharacterInScreen.draw(self.MainWindow)

        if not self.pausa:
            elapsed_time = time.time() - self.musicStartTime

            # Actualiza la pantalla
            text = self.font.render(f'Tiempo: {int(elapsed_time)} / {int(self.music.duration)} segundos', True, (0, 0, 0))
            # pygame.display.flip()
            # Timer
            tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_inicial) // 1000
            timerLabel = self.font.render("Time: " + str(tiempo_transcurrido), True, (63, 176, 224))

            # Showing the destroyed blocks
            desBlocksLabel = self.font.render("Destroyed blocks: " + str(self.destroyedBlocks), 0, (63, 176, 224))

            # Points
            pointsLabel = self.font.render("Points: " + str(self.points), 0, (63, 176, 224))
        self.MainWindow.blit(text, (100, 100))
        self.MainWindow.blit(timerLabel, (20, 10))
        self.MainWindow.blit(desBlocksLabel, (120, 10))
        self.MainWindow.blit(pointsLabel, (400, 10))


        if not self.pausa:
            pygame.display.update()

            if not self.pausa:
                # Remove bombs that have gone off-screen
                bombs_to_remove = []
                for bomb in self.bombs:
                    if bomb.rect.bottom < 0 or bomb.rect.top> self.MainWindow.get_height() or bomb.rect.left > self.MainWindow.get_width() or bomb.rect.right < 0:
                        bombs_to_remove.append(bomb)
                        Bomb.bomb_count += 1
                    if self.aguila.rect.colliderect(bomb.rect):
                        self.gameoverScreen(self.points)
            for bomb in bombs_to_remove:
                self.bombs.remove(bomb)

            if not self.pausa:
                # Remove water balls that have gone off-screen
                waters_to_remove = []
                for water in self.waters:
                    if water.rect.bottom < 0:
                        waters_to_remove.append(water)
                        Water.water_count += 1
                    if self.aguila.rect.colliderect(water.rect):
                        self.gameoverScreen(self.points)
            for water in waters_to_remove:
                self.waters.remove(water)

            if not self.pausa:
                # Remove fire balls that have gone off-screen
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