import pygame
from pygame import *

class Label:
    def __init__(self, text, font_size, x, y, color=(255, 255, 255)):
        self.text = text
        self.font_size = font_size
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.surface = self.font.render(text, True, color)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)

    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(text, True, self.color)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)