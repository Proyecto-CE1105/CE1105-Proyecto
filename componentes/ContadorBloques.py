import pygame
import sys
from pygame.locals import *

ANCHO_CONTADOR = 180
ALTO_CONTADOR = 60
ANCHO_BLOQUE = 50
ALTO_BLOQUE = 20
ESPACIO_ENTRE_BLOQUES = 5
DISTANCIA_AL_BORDE = 20
RECARGA_ACERO_TIEMPO = 30000  
RECARGA_MADERA_TIEMPO = 30000  
RECARGA_LADRILLO_TIEMPO = 30000  
MENSAJE_TIEMPO = 3000  
MOSTRAR_MENSAJE_EVENTO = pygame.USEREVENT + 1

tiempo_ultima_recarga = pygame.time.get_ticks()
bloques_recargados = 0

COLORES_BLOQUES = {
    'acero': (169, 169, 169),  # Gris
    'madera': (139, 69, 19),    # Café
    'ladrillo': (255, 0, 0)    # Rojo
}
COLOR_TEXTO = (0, 0, 0)  # Color del texto (Negro)
FUENTE = "Arial"
TAMANO_FUENTE = 20

# Función para dibujar el contador de bloques en la ventana
def dibujar_contador(ventana,cantidad):
    x, y = ventana.get_size()
    contador_x = x - (ANCHO_CONTADOR + ESPACIO_ENTRE_BLOQUES)
    contador_y = y - (ALTO_CONTADOR + ESPACIO_ENTRE_BLOQUES)

    espacio_entre_bloques = 10

    for tipo in cantidad:
        pygame.draw.rect(ventana, COLORES_BLOQUES[tipo],
                         (x - DISTANCIA_AL_BORDE - ANCHO_BLOQUE, contador_y + ALTO_CONTADOR - espacio_entre_bloques - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE))
        fuente = pygame.font.SysFont(FUENTE, TAMANO_FUENTE)
        texto = fuente.render(str(cantidad[tipo]), True, COLOR_TEXTO)
        texto_rect = texto.get_rect(midtop=(x - DISTANCIA_AL_BORDE - ANCHO_BLOQUE // 2, contador_y + ALTO_CONTADOR - espacio_entre_bloques - ALTO_BLOQUE))
        ventana.blit(texto, texto_rect)
        contador_y -= (ALTO_BLOQUE + ESPACIO_ENTRE_BLOQUES)
