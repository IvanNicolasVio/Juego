import pygame
import sys
from constantes import *
from player import Player
from plataforma import *
from enemigos_2 import *   
from disparos_3 import *
from coleccionables import *
from mostrables import *
from generador_enemigos import *
from finalizador_juego import *
from generador_nivel import *

tiempo_acumulado = 0

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
nivel_1 = Nivel("nivel_3")
nivel_1.generar_nivel(screen)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)
    
    nivel_1.update(delta_ms,screen,keys,events)

    pygame.display.flip()