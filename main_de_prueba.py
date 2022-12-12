import pygame
import sys
from juego_constantes import *
from juego_player import Player
from juego_plataforma import *
from juego_enemigos import *   
from juego_disparos import *
from juego_coleccionables import *
from juego_mostrables import *
from juego_generador_enemigos import *
from juego_finalizador import *
from juego_generador_nivel import *

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