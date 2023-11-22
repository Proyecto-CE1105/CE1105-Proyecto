# Importación de las bibliotecas necesarias
import pygame
import sys
from pygame.locals import *

# Configuraciones generales del programa
ANCHO_CONTADOR = 180
ALTO_CONTADOR = 60
ANCHO_BLOQUE = 50
ALTO_BLOQUE = 20
ESPACIO_ENTRE_BLOQUES = 5
DISTANCIA_AL_BORDE = 20
RECARGA_ACERO_TIEMPO = 30000  # 30 segundos en milisegundos
RECARGA_MADERA_TIEMPO = 30000  # 30 segundos en milisegundos
RECARGA_LADRILLO_TIEMPO = 30000  # 30 segundos en milisegundos
MENSAJE_TIEMPO = 3000  # 3 segundos en milisegundos
MOSTRAR_MENSAJE_EVENTO = pygame.USEREVENT + 1

# Variables para rastrear la recarga de bloques de acero
tiempo_ultima_recarga = pygame.time.get_ticks()
bloques_recargados = 0

# Diccionarios que almacenan la cantidad de bloques y sus colores
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

# Función para recargar bloques de acero y mostrar un mensaje
def recargar_acero(cantidad):
    global bloques_recargados, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['acero'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_ACERO_TIEMPO:
        cantidad['acero'] += 1
        bloques_recargados += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje

# Función para recargar bloques de madera y mostrar un mensaje
def recargar_madera(cantidad):
    global bloques_recargados, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['madera'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_MADERA_TIEMPO:
        cantidad['madera'] += 1
        bloques_recargados += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje
# Función para recargar bloques de ladrillo y mostrar un mensaje
def recargar_ladrillo(cantidad):
    global bloques_recargados, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['ladrillo'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_LADRILLO_TIEMPO:
        cantidad['ladrillo'] += 1
        bloques_recargados += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje
