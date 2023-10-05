import pygame
import sys
from pygame.locals import *
from pygame.sprite import Group
from Bomb import Bomb

pygame.init()

width, height = 500, 400
fps = 60
clock = pygame.time.Clock()

blanco = (255, 255, 255)
negro = (0, 0, 0)

icono = pygame.image.load("Assets/Logo_Game.jpg")
tanque = pygame.image.load("Assets/Tank_Image.png")

pantalla = pygame.display.set_mode((width, height))

pygame.display.set_caption("Eagle Defender")

pantalla.fill(negro)
pygame.display.set_icon(icono)

sprites = Group()
bombs = []  # List to store bombs

font = pygame.font.Font(None, 36)  # Font for the counter

def mostrar_contador_bombas(contador):
    """
    Display the bomb counter on the screen.

    Args:
        contador (int): The bomb count.

    Returns:
        None
    """
    # Clear the counter area
    pygame.draw.rect(pantalla, negro, (width - 150, 0, 150, 30))
    texto = font.render(f'Bombas: {contador}', True, blanco)
    pantalla.blit(texto, (width - texto.get_width() - 10, 10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if Bomb.can_place_bomb():
                bomb = Bomb()
                bomb.place_bomb(pygame.mouse.get_pos())
                sprites.add(bomb)
                bombs.append(bomb)

    clock.tick(fps)

    sprites.update()
    sprites.draw(pantalla)
    mostrar_contador_bombas(Bomb.bomb_count)  # Display bomb counter
    pygame.display.update()

    # Remove bombs that have gone off-screen
    bombs_to_remove = []
    for bomb in bombs:
        if bomb.rect.bottom < 0:
            bombs_to_remove.append(bomb)
            Bomb.bomb_count += 1

    for bomb in bombs_to_remove:
        bombs.remove(bomb)
