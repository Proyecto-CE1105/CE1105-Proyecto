import pygame
import sys
from pygame.locals import *

# Configuraciones generales del programa
ANCHO_CONTADOR = 180
ALTO_CONTADOR = 60
ANCHO_ARMA = 50
ALTO_ARMA = 20
ESPACIO_ENTRE_ARMAS = 5
DISTANCIA_AL_BORDE = 20
RECARGA_BOMBA_TIEMPO = 30000  # 30 segundos en milisegundos
RECARGA_AGUA_TIEMPO = 30000  # 30 segundos en milisegundos
RECARGA_FUEGO_TIEMPO = 30000  # 30 segundos en milisegundos
MENSAJE_TIEMPO = 3000  # 3 segundos en milisegundos
MOSTRAR_MENSAJE_EVENTO = pygame.USEREVENT + 1

# Variables para rastrear la recarga de armas
tiempo_ultima_recarga = pygame.time.get_ticks()
armas_recargadas = 0

# Diccionarios que almacenan la cantidad de armas y sus colores
COLORES_ARMAS = {
    'bomba': (0, 0, 0),  # Negro
    'agua': (0, 0, 255),    # Azul
    'fuego': (255, 165, 0),    # Naranja
    'acero': (169, 169, 169),
    'madera': (139, 69, 19),  # Café
    'ladrillo': (255, 0, 0)
}
COLOR_TEXTO = (0, 0, 0)  # Color del texto (Negro)
FUENTE = "Arial"
TAMANO_FUENTE = 20

# Función para dibujar el contador en la ventana
def dibujar_contador(ventana,cantidad):
    x, y = ventana.get_size()
    contador_x = x - (ANCHO_CONTADOR + ESPACIO_ENTRE_ARMAS)
    contador_y = y - (ALTO_CONTADOR + ESPACIO_ENTRE_ARMAS)

    espacio_entre_armas = 10

    for tipo in cantidad:
        pygame.draw.rect(ventana, COLORES_ARMAS[tipo],
                         (x - DISTANCIA_AL_BORDE - ANCHO_ARMA, contador_y + ALTO_CONTADOR - espacio_entre_armas - ALTO_ARMA, ANCHO_ARMA, ALTO_ARMA))
        fuente = pygame.font.SysFont(FUENTE, TAMANO_FUENTE)
        texto = fuente.render(str(cantidad[tipo]), True, COLOR_TEXTO)
        texto_rect = texto.get_rect(midtop=(x - DISTANCIA_AL_BORDE - ANCHO_ARMA // 2, contador_y + ALTO_CONTADOR - espacio_entre_armas - ALTO_ARMA))
        ventana.blit(texto, texto_rect)
        contador_y -= (ALTO_ARMA + ESPACIO_ENTRE_ARMAS)

# Función para recargar bombas y mostrar un mensaje
def recargar_bomba(cantidad):
    global armas_recargadas, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['bomba'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_BOMBA_TIEMPO:
        cantidad['bomba'] += 1
        armas_recargadas += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje

# Función para recargar bolas de agua y mostrar un mensaje
def recargar_agua(cantidad):
    global armas_recargadas, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['agua'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_AGUA_TIEMPO:
        cantidad['agua'] += 1
        armas_recargadas += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje

# Función para recargar bolas de fuego y mostrar un mensaje
def recargar_fuego(cantidad):
    global armas_recargadas, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if cantidad['fuego'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_FUEGO_TIEMPO:
        cantidad['fuego'] += 1
        armas_recargadas += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje
