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
MENSAJE_TIEMPO = 3000  # 3 segundos en milisegundos
MOSTRAR_MENSAJE_EVENTO = pygame.USEREVENT +1

# Variable para rastrear la recarga de bloques de acero
tiempo_ultima_recarga = pygame.time.get_ticks()
bloques_recargados = 0

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

# Función para recargar bloques de acero y mostrar un mensaje
def recargar_acero():
    global bloques_recargados, tiempo_ultima_recarga, mensaje_tiempo_inicio
    tiempo_actual = pygame.time.get_ticks()
    if CANTIDAD_BLOQUES['acero'] < 5 and tiempo_actual - tiempo_ultima_recarga >= RECARGA_ACERO_TIEMPO:
        CANTIDAD_BLOQUES['acero'] += 1
        bloques_recargados += 1
        tiempo_ultima_recarga = tiempo_actual
        mensaje_tiempo_inicio = tiempo_actual  # Establece el tiempo de inicio del mensaje

# Configuración de Pygame
pygame.init()
VENTANA_ANCHO, VENTANA_ALTO = 800, 600
ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
pygame.display.set_caption("Contador de Bloques")

# Cargar la imagen del bloque de acero
steelblock = pygame.image.load("Assets/Blocks/SteelBlock.png")
steelblock = pygame.transform.scale(steelblock, (50, 50))

# Bucle principal
reloj = pygame.time.Clock()
ultimo_tiempo_acero = pygame.time.get_ticks()
mensaje_tiempo_inicio = None  # Variable para almacenar el tiempo de inicio del mensaje

bloques_acero = []  # Lista para almacenar los bloques de acero

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_1 and CANTIDAD_BLOQUES['acero'] > 0:
                CANTIDAD_BLOQUES['acero'] -= 1
                x, y = pygame.mouse.get_pos()
                bloque_acero = (x - 25, y - 25)
                bloques_acero.append(bloque_acero)
                ultimo_tiempo_acero = pygame.time.get_ticks()
                mensaje_tiempo_inicio = tiempo_ultima_recarga  # Establece el tiempo de inicio del mensaje para mostrarlo 3 segundos

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - tiempo_ultima_recarga >= RECARGA_ACERO_TIEMPO:
        recargar_acero()
        mensaje_tiempo_inicio = pygame.time.get_ticks()  # Inicia el tiempo del mensaje de recarga

    ventana.fill((255, 255, 255))  # Fondo blanco
    dibujar_contador(ventana)  # Dibuja el contador en la ventana

    for bloque_acero in bloques_acero:
        ventana.blit(steelblock, bloque_acero)  # Coloca los bloques de acero en la posición almacenada

    if mensaje_tiempo_inicio is not None and tiempo_actual - mensaje_tiempo_inicio < MENSAJE_TIEMPO:
        fuente_mensaje = pygame.font.SysFont(FUENTE, TAMANO_FUENTE)
        texto_mensaje = fuente_mensaje.render("Bloque de acero recargado", True, COLOR_TEXTO)
        texto_mensaje_rect = texto_mensaje.get_rect(midbottom=(VENTANA_ANCHO // 2, VENTANA_ALTO - 20))
        ventana.blit(texto_mensaje, texto_mensaje_rect)

    pygame.display.flip()
    reloj.tick(60)  # 60 FPS