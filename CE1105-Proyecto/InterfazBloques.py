import pygame
from pygame.locals import *
import BloqueAcero, BloqueConcreto, BloqueMadera

width, height = 500, 400
class InterfazBloques:
    def __init__(self):
        self.bloques = [BloqueAcero(), BloqueMadera(), BloqueConcreto()]
        self.bloque_seleccionado = 0
        self.selected_block_rects = []  # Rectángulos para mostrar selección visual
        self.create_selected_block_rects()

    def create_selected_block_rects(self):
        # Crea los rectángulos para mostrar la selección visual
        block_width, block_height = 50, 50
        x_offset = 10
        y_offset = height - block_height - 10

        for i in range(len(self.bloques)):
            rect = pygame.Rect(x_offset, y_offset, block_width, block_height)
            self.selected_block_rects.append(rect)
            x_offset += block_width + 10

    def display(self, pantalla):
        # Muestra los bloques en la interfaz y la selección visual
        for i, bloque in enumerate(self.bloques):
            pantalla.blit(bloque.image, self.selected_block_rects[i])
            if i == self.bloque_seleccionado:
                pygame.draw.rect(pantalla, (100, 100, 100), self.selected_block_rects[i], 4)

    def cambiar_bloque_seleccionado(self, key):
        # Cambia el bloque seleccionado según la tecla presionada
        if key == pygame.K_1:
            self.bloque_seleccionado = 0
        elif key == pygame.K_2:
            self.bloque_seleccionado = 1
        elif key == pygame.K_3:
            self.bloque_seleccionado = 2

    def bloque_seleccionado_actual(self):
        # Devuelve el bloque seleccionado
        return self.bloques[self.bloque_seleccionado]