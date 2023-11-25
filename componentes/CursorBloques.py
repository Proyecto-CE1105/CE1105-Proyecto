import pygame
from pygame.sprite import Sprite

class CursorBloques(Sprite):
    def __init__(self,mainWindow):
        self.image=pygame.transform.scale(pygame.image.load("Assets/Cursor/block_cursor.png"),(50,50))
        self.screen=mainWindow
        self.cursor_x=0
        self.cursor_y=0
        self.cursor_position=(self.cursor_x,self.cursor_y)
    
    def update(self,screen):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.cursor_y>=0:
            self.cursor_y-=50
        elif keys[pygame.K_DOWN] and self.cursor_y+50<=screen.get_height():
            self.cursor_y+=50
        elif keys[pygame.K_RIGHT] and self.cursor_x+50<=screen.get_width():
            self.cursor_x+=50
        elif keys[pygame.K_LEFT] and self.cursor_x>=0:
            self.cursor_x-=50
        
        self.cursor_position=(self.cursor_x,self.cursor_y)