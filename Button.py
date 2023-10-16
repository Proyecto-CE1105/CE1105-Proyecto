import pygame
from pygame import *

class Button:
    def __init__(self, posX, posY, width, height, text, color, sizeFont):
        self.x = posX
        self.y = posY
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.textColor = (255,255,255)
        self.font = pygame.font.Font(None, sizeFont)
    def drawButton(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        textSurface = self.font.render(self.text, True, self.textColor)
        textRect = textSurface.get_rect()
        textRect.center = (self.x + self.width//2, self.y + self.height//2)
        window.blit(textSurface, textRect)
    def is_clicked(self, mouse_pos):
        return self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height
