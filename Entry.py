import pygame, sys
from pygame import *

class Entry:
    def __init__(self, colorActive, colorPassive, color, text, activeness):
        self.colorActive = colorActive
        self.colorPassive = colorPassive
        self.color = color
        self.text = text
        self.activeness = activeness
        self.font = pygame.font.Font(None, 30)
        self.input_user = pygame.Rect(300, 300, 140, 32)

    def drawEntry(self, window):
        pygame.draw.rect(window, self.color, self.input_user, 1)
        textSurface = self.font.render(self.text, True, (255, 255, 255))
        window.blit(textSurface, (self.input_user.x + 5, self.input_user.y + 5))
    def is_clicked(self, mouse_pos):
        return self.input_user.x < mouse_pos[0] < self.input_user.x + self.input_user.width and self.input_user.y < mouse_pos[1] < self.input_user.y + self.input_user.height
