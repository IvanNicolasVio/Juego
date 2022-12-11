import pygame
from pygame.locals import *
import sys
from constantes import *
from form import *
from player import Player
from plataforma import *
from enemigos_2 import *   
from disparos_3 import *
from coleccionables import *
from mostrables import *
from generador_enemigos import *
from finalizador_juego import *
from generador_nivel import *
from boton import *


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

menu_principal = MenuPrincipal(name="menu_principal",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=L_VIOLET,color_border=VIOLET,active=True,nivel="")
menu_opciones = MenuOpciones(name="menu_opciones",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")
menu_perder = MenuPerder(name="menu_perder",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")
menu_score = MenuScore(name="menu_score",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")
menu_pausa = MenuPausa(name="menu_pausa",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")


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

    if(keys[pygame.K_p]):
        menu_pausa.active = True # fix
        print("entro en la pausa")

    delta_ms = clock.tick(FPS)
    
    if(menu_principal.active):
        menu_principal.update(lista_eventos)
        menu_principal.draw()
        menu_principal.bandera_nivel = True
    elif(menu_opciones.active):
        menu_opciones.update(lista_eventos)
        menu_opciones.draw()
    elif(menu_perder.active):
        menu_perder.update(lista_eventos)
        menu_perder.draw()
    elif(menu_score.active):
        menu_score.update(lista_eventos)
        menu_score.draw()
    elif(menu_pausa.active):
        menu_pausa.update(lista_eventos)
        menu_pausa.draw()
    else:
        if menu_principal.nivel != "":
            if menu_principal.bandera_nivel:
                nivel_1 = Nivel(menu_principal.nivel,menu_perder,menu_pausa,screen)
                nivel_1.generar_nivel()
                menu_principal.bandera_nivel = False
            nivel_1.update(delta_ms,screen,keys,lista_eventos,lista_eventos)
            

    pygame.display.flip()