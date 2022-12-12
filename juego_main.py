import pygame
from pygame.locals import *
import sys
from juego_constantes import *
from juego_form import *
from juego_player import Player
from juego_plataforma import *
from juego_enemigos import *   
from juego_disparos import *
from juego_coleccionables import *
from juego_mostrables import *
from juego_generador_enemigos import *
from juego_finalizador import *
from juego_generador_nivel import *
from juego_boton import *
from juego_sounds import *
from juego_sqlite import *


flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
sonido = Sound(PATH_IMAGE + "Sonidos\\Alexander_Nakarada_-_The_Return.mp3")
menu_principal = MenuPrincipal(name="menu_principal",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=L_VIOLET,color_border=VIOLET,active=True,nivel="")
menu_opciones = MenuOpciones(name="menu_opciones",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",sound=sonido)
menu_opciones_in_game = MenuOpcionesInGame(name="opciones_in_game",master_surface = screen,x=575,y=185,w=300,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",sound=sonido)
menu_perder = MenuPerder(name="menu_perder",master_surface = screen,x=575,y=290,w=300,h=300,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")
menu_score = MenuScore(name="menu_score",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="")
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

    delta_ms = clock.tick(FPS)
    
    if(menu_principal.active):
        menu_principal.update(lista_eventos)
        menu_principal.draw()
        menu_principal.bandera_nivel = True
        sonido.cancion.stop()
    elif(menu_opciones.active):
        menu_opciones.update(lista_eventos)
        menu_opciones.draw()
        sonido.cancion.stop()
    elif(menu_opciones_in_game.active):
        menu_opciones_in_game.update(lista_eventos)
        menu_opciones_in_game.draw()
    elif(menu_perder.active):
        menu_perder.update(lista_eventos)
        menu_perder.draw()
        sonido.cancion.stop()
        if menu_perder.bandera_ingresar_nombre:
            print("Entro aca")
            actualizar_base_datos(menu_perder.text_box.nombre,nivel_1.player_1.score,nivel_1.nivel)
            menu_perder.bandera_ingresar_nombre = False
    elif(menu_score.active):
        menu_score.update(lista_eventos)
        menu_score.draw()
        menu_score.mostrar_puntaje()
        sonido.cancion.stop()
    elif(menu_pausa.active):
        menu_pausa.update(lista_eventos)
        menu_pausa.draw()
        sonido.cancion.set_volume(0.0)
    else:
        if not menu_pausa.active:
            sonido.cancion.set_volume(0.1)
        if menu_principal.nivel != "":
            if menu_principal.bandera_nivel:
                nivel_1 = Nivel(menu_principal.nivel,menu_perder,menu_pausa,screen,sonido,sonido.cancion)
                player = nivel_1.generar_nivel()
                menu_principal.bandera_nivel = False
            nivel_1.update(delta_ms,screen,keys,lista_eventos,lista_eventos)
            

    pygame.display.flip()