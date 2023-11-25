import pygame
from pygame.locals import *

class CursorBloques(pygame.sprite.Sprite):
    def __init__(self,mainWindow):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load("Assets/Cursor/block_cursor.png"),(50,50))
        self.screen=mainWindow
        self.rect=self.image.get_rect()
        self.time_move=500
        self.last_movement=pygame.time.get_ticks()
    
    def update(self, MainWindow):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            now = pygame.time.get_ticks()
            if self.rect.top-50 >= 0 and now-self.last_movement>self.time_move:
                self.rect.y -= 50
                self.last_movement=now
        if keys[pygame.K_DOWN]:
            now = pygame.time.get_ticks()
            if self.rect.bottom+50 <= MainWindow.get_height() and now-self.last_movement>self.time_move:
                self.rect.y += 50
                self.last_movement=now
        if keys[pygame.K_LEFT]:
            now = pygame.time.get_ticks()
            if self.rect.left-50 >= 0 and now-self.last_movement>self.time_move:
                self.rect.x -= 50
                self.last_movement=now
        if keys[pygame.K_RIGHT]:
            now = pygame.time.get_ticks()
            if self.rect.right+50 <= MainWindow.get_width() and now-self.last_movement>self.time_move:
                self.rect.x += 50
                self.last_movement=now
    
    def get_pos(self):
        return (self.rect.x, self.rect.y)
        