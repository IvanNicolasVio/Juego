import pygame
from pygame.locals import *
import sys
from juego_constantes import *
from juego_sounds import *
from juego_instanciar_formularios import *


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
sonido = Sound(ROOT + "Sonidos\\Alexander_Nakarada_-_The_Return.mp3")
formularios = GeneradorFormularios(screen,sonido)


while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)

    formularios.gestionar_formularios(lista_eventos,delta_ms,keys)
    
    pygame.display.flip()