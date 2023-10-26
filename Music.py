import pygame
import time

pygame.init()

class Music:

    def __init__(self, MainWindow):
        self.font = pygame.font.Font(None, 36)
        self.songPath = 'Songs/Maps.mp3'
        self.songEnd = pygame.USEREVENT +1
        self.duration = pygame.mixer.Sound.get_length(pygame.mixer.Sound(self.songPath))
        self.MainWindow = MainWindow
        self.startTime = time.time()

    def playSong(self):
        pygame.mixer.music.set_endevent(self.songEnd)
        pygame.mixer.music.load(self.songPath)
        pygame.mixer.music.play()

