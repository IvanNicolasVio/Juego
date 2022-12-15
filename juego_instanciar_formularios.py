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

class GeneradorFormularios():
    def __init__(self,screen,sonido) -> None:
        self.menu_principal = MenuPrincipal(name="menu_principal",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=L_VIOLET,color_border=VIOLET,active=True,nivel="",image_background=ROOT + "images\\1008904.png")
        self.menu_opciones = MenuOpciones(name="menu_opciones",master_surface = screen,x=575,y=185,w=300,h=350,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",sound=sonido,image_background=ROOT + "images\\images\\gui\\jungle\\pause\\bg.png")
        self.menu_opciones_in_game = MenuOpcionesInGame(name="opciones_in_game",master_surface = screen,x=575,y=185,w=300,h=450,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",sound=sonido,image_background=ROOT + "images\\images\\gui\\jungle\\pause\\bg.png")
        self.menu_perder = MenuPerder(name="menu_perder",master_surface = screen,x=575,y=290,w=300,h=350,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",image_background=ROOT + "images\\images\\gui\\jungle\\pause\\bg.png")
        self.menu_score = MenuScore(name="menu_score",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",image_background=ROOT + "images\\images\\gui\\jungle\\pause\\bg.png")
        self.menu_pausa = MenuPausa(name="menu_pausa",master_surface = screen,x=575,y=185,w=300,h=350,color_background=(0,255,255),color_border=(255,0,255),active=False,nivel="",image_background=ROOT + "images\\images\\gui\\jungle\\pause\\bg.png")
        self.sonido = sonido
        self.screen = screen
        self.nivel_1 = None

    def gestionar_formularios(self,lista_eventos,delta_ms,keys):
        if(self.menu_principal.active):
            self.menu_principal.update(lista_eventos)
            self.menu_principal.draw()
            self.menu_principal.bandera_nivel = True
            self.menu_perder.reiniciar_boton()
            self.sonido.cancion.stop()
        elif(self.menu_opciones.active):
            self.menu_opciones.update(lista_eventos)
            self.menu_opciones.draw()
            self.sonido.cancion.stop()
        elif(self.menu_opciones_in_game.active):
            self.menu_opciones_in_game.update(lista_eventos)
            self.menu_opciones_in_game.draw()
        elif(self.menu_perder.active):
            self.menu_perder.update(lista_eventos)
            self.menu_perder.draw()
            self.sonido.cancion.stop()
            if self.menu_perder.bandera_ingresar_nombre:
                actualizar_base_datos(self.menu_perder.text_box.nombre,self.nivel_1.player_1.score,self.nivel_1.nivel)
                self.menu_perder.bandera_ingresar_nombre = False
        elif(self.menu_score.active):
            self.menu_score.update(lista_eventos)
            self.menu_score.draw()
            self.menu_score.mostrar_nombre()
            self.menu_score.mostrar_score()
            self.menu_score.mostrar_nivel()
            self.sonido.cancion.stop()
        elif(self.menu_pausa.active):
            self.menu_pausa.update(lista_eventos)
            self.menu_pausa.draw()
            self.sonido.cancion.set_volume(0.0)
        else:
            if not self.menu_pausa.active:
                self.sonido.cancion.set_volume(0.1)
            if self.menu_principal.nivel != "":
                if self.menu_principal.bandera_nivel:
                    self.nivel_1 = Nivel(self.menu_principal.nivel,self.menu_perder,self.menu_pausa,self.screen,self.sonido,self.sonido.cancion)
                    player = self.nivel_1.generar_nivel()
                    self.menu_principal.bandera_nivel = False
                if self.nivel_1:
                    self.nivel_1.update(delta_ms,self.screen,keys,lista_eventos,lista_eventos)