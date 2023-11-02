import pygame
import sys
from pygame.locals import *

# Configuraciones
ANCHO_CONTADOR = 180
ALTO_CONTADOR = 60
ANCHO_BLOQUE = 50
ALTO_BLOQUE = 20
ESPACIO_ENTRE_BLOQUES = 5
DISTANCIA_AL_BORDE = 20
RECARGA_ACERO_TIEMPO = 30000  # 30 segundos en milisegundos

CANTIDAD_BLOQUES = {
    'acero': 5,    # Cantidad de bloques de acero
    'madera': 3,   # Cantidad de bloques de madera
    'ladrillo': 8  # Cantidad de bloques de ladrillo
}
COLORES_BLOQUES = {
    'acero': (169, 169, 169),  # Gris
    'madera': (139, 69, 19),    # Café
    'ladrillo': (255, 0, 0)    # Rojo
}
COLOR_TEXTO = (0, 0, 0)  # Negro
FUENTE = "Arial"
TAMANO_FUENTE = 20

# Función para dibujar el contador
def dibujar_contador(ventana):
    x, y = ventana.get_size()
    contador_x = x - (ANCHO_CONTADOR + ESPACIO_ENTRE_BLOQUES)
    contador_y = y - (ALTO_CONTADOR + ESPACIO_ENTRE_BLOQUES)

    espacio_entre_bloques = 10

    for tipo in CANTIDAD_BLOQUES:
        pygame.draw.rect(ventana, COLORES_BLOQUES[tipo],
                         (x - DISTANCIA_AL_BORDE - ANCHO_BLOQUE, contador_y + ALTO_CONTADOR - espacio_entre_bloques - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE))
        fuente = pygame.font.SysFont(FUENTE, TAMANO_FUENTE)
        texto = fuente.render(str(CANTIDAD_BLOQUES[tipo]), True, COLOR_TEXTO)
        texto_rect = texto.get_rect(midtop=(x - DISTANCIA_AL_BORDE - ANCHO_BLOQUE // 2, contador_y + ALTO_CONTADOR - espacio_entre_bloques - ALTO_BLOQUE))
        ventana.blit(texto, texto_rect)
        contador_y -= (ALTO_BLOQUE + ESPACIO_ENTRE_BLOQUES)

# Función para recargar bloques de acero
def recargar_acero():
    if CANTIDAD_BLOQUES['acero'] < 5:
        CANTIDAD_BLOQUES['acero'] += 1

# Configuración de Pygame
pygame.init()
VENTANA_ANCHO, VENTANA_ALTO = 800, 600
ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
pygame.display.set_caption("Contador de Bloques")

# Bucle principal
reloj = pygame.time.Clock()
ultimo_tiempo_acero = pygame.time.get_ticks()

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_1:
                if CANTIDAD_BLOQUES['acero'] > 0:
                    CANTIDAD_BLOQUES['acero'] -= 1
            elif evento.key == K_2:
                if CANTIDAD_BLOQUES['ladrillo'] > 0:
                    CANTIDAD_BLOQUES['ladrillo'] -= 1
            elif evento.key == K_3:
                if CANTIDAD_BLOQUES['madera'] > 0:
                    CANTIDAD_BLOQUES['madera'] -= 1

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo_acero >= RECARGA_ACERO_TIEMPO:
        recargar_acero()
        ultimo_tiempo_acero = tiempo_actual

    ventana.fill((255, 255, 255))  # Fondo blanco
    dibujar_contador(ventana)  # Dibuja el contador en la ventana
    pygame.display.flip()
    reloj.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
