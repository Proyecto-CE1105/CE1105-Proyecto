from interfaces.intPantallas import Pantallas
from pantallas import pantalla1,secundaria
from screens import menu,singUp,login,game,loose,win,podio
from pygame import *
from pygame.sprite import Group
from pygame.locals import *
import pygame
from componentes import Music
import i18n as inter

class Main:
    def __init__(self):
        #internacionalizacion
        self.i18n=inter
        self.i18n.load_path.append('./translation/')
        self.i18n.set('locale', 'es')
        self.i18n.set('file_format', 'json')
        self.i18n.set('filename_format', '{locale}.{format}')


        #inicializadores
        pygame.init()
        pygame.font.init()

        #Atributos globales
        self.icono = pygame.image.load("imagenes/logo.jpg")
        pygame.display.set_icon(self.icono)
        pygame.display.set_caption('Eagle Defender')
        self.screen = pygame.display.set_mode((1200,650))
        self.clock = pygame.time.Clock()
        self.running=True
        self.pantalla:Pantallas=menu.menuPrincipal(self)

        #Estado del control de pantalla [menu,partida,finalizado,podio]
        self.status="menu"
        self.music = Music.Music(self.screen, "Environment.ogg")

        #run (no añadir atributos despues del run)
        self.run()
    

    def cambio(self,newPantalla):
        temp=self.pantalla
        if newPantalla=="menu":
            self.pantalla=menu.menuPrincipal(self)
        elif newPantalla=="SignUp":
            self.pantalla=singUp.signUpScreen(self)
        elif newPantalla=="SignIn":
            self.pantalla=login.signInScreen(self)
        elif newPantalla=="podio":
            self.pantalla=podio.Podio(self)
        del temp
    
    def empezarPartida(self,jugador1,jugador2,musica1,musica2):
        self.status="partida"
        self.music.stop()
        self.pantalla=game.GameScreen(self,jugador1,jugador2,musica1,musica2)
    
    def gameOver(self,puntaje,jugadorNombre):
        self.status="gameOver"
        self.pantalla=loose.GameOver(self,jugadorNombre,puntaje)
    
    def winGame(self,puntaje,player):
        self.status="Ganado"
        self.pantalla=win.winScreen(self,puntaje,player)
    
    def backMenu(self):
        self.status="menu"
        self.pantalla=menu.menuPrincipal(self)
        self.music.playSong()

    def run(self):
        self.music.playSong()
        while self.running:
            self.pantalla.runner()
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()
    

Main()