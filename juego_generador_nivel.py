import pygame
import json
from juego_constantes import *
from juego_player import Player
from juego_plataforma import *
from juego_enemigos import *   
from juego_disparos import *
from juego_coleccionables import *
from juego_mostrables import *
from juego_generador_enemigos import *
from juego_finalizador import *
from juego_boton import *
from juego_form import *
from juego_sounds import *
from trampas import *


class Nivel():
    def __init__(self,nivel,menu_perder,menu_pausa,screen,sonido,cancion) -> None:
        self.nivel = nivel
        self.configuraciones_completas = self.leer_archivo()
        self.lista_plataformas = []
        self.lista_trampas = []
        self.parametro_imagen_fondo = PATH_IMAGE + self.configuraciones_completas[nivel]["imagen_fondo"]
        self.parametro_plataformas = self.configuraciones_completas[nivel]["parametros_plataformas"]
        self.parametro_trampas = self.configuraciones_completas[nivel]["parametros_trampas"]
        self.parametro_player_1 = self.configuraciones_completas[nivel]["player_1"]
        self.parametro_balas = self.configuraciones_completas[nivel]["cantidad_balas"]
        self.parametro_trunk = self.configuraciones_completas[nivel]["trunk"]
        self.parametro_radish = self.configuraciones_completas[nivel]["radish"]
        self.player_1 = Player(self.parametro_player_1["x"],self.parametro_player_1["y"],self.parametro_player_1["speed_walk"],self.parametro_player_1["speed_run"],self.parametro_player_1["gravity"],self.parametro_player_1["jump_power"],self.parametro_player_1["frame_rate_ms"],self.parametro_player_1["move_rate_ms"],self.parametro_player_1["jump_height"],self.parametro_player_1["vidas"])
        self.lista_de_balas = lista_balas(self.parametro_balas["jugador"])
        self.lista_de_balas_enemigos = lista_balas_enemigas(self.parametro_balas["enemigo"])
        self.frutas = Frutas()
        self.trunk = Generador_trunk(self.parametro_trunk["speed_walk"],self.parametro_trunk["gravity"])
        self.radish = Generador_radish(self.parametro_radish["cantidad"],self.parametro_radish["x"],self.parametro_radish["y"],self.parametro_radish["speed"],self.parametro_radish["tope_izq"],self.parametro_radish["tope_der"],self.parametro_radish["gravity"])
        self.items_en_pantalla  = items_pantalla(0,0,self.player_1.vidas)
        self.finalizador_juego = Finalizador(self.configuraciones_completas[nivel]["tiempo_juego"])
        self.imagen_fondo = pygame.image.load(self.parametro_imagen_fondo)
        self.menu_perder = menu_perder
        self.boton1 = ButtonScreen(master=screen,x=1150,y=20,w=50,h=50,color_background=BLACK,color_border=BLACK,on_click=menu_pausa.on_click_boton1,on_click_param="menu_pausa",text=" P",font="Verdana",font_size=30,font_color=WHITE)
        self.sonido = sonido
        self.cancion = cancion
        self.lista_trunk = [0]
        self.lista_frutas = [1]



    def leer_archivo(self):
        with open("nivel_1.json", "r",encoding="utf-8") as configuraciones:
            return json.load(configuraciones)

    def crear_plataformas(self):
        for parametro in self.parametro_plataformas:
            self.lista_plataformas.append(Platform(parametro[0],parametro[1],parametro[2],parametro[3],parametro[4]))

    def crear_trampas(self):
       for parametro in self.parametro_trampas:
            self.lista_trampas.append(Saw(parametro[0],parametro[1])) 

    def generar_nivel(self):

        #imagen_fondo = pygame.image.load(self.parametro_imagen_fondo)
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


        self.crear_plataformas()
        self.crear_trampas()
        self.sonido.play_music(self.cancion)
        crear_base_datos()
        
        return self.player_1

    def update(self,delta_ms,screen,keys,events,lista_eventos):
        
        screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())
        finalizador = self.finalizador_juego.update(delta_ms,screen)

        if (not finalizador or self.player_1.vidas == 0) or (self.lista_frutas == [] and self.lista_trunk == []):
            fuente = pygame.font.SysFont("Arial",100)
            texto = fuente.render("Score: {0}".format(self.player_1.score),True,RED)
            screen.blit(texto,(500,130))
            self.menu_perder.active = True
            #self.bandera_nivel_terminado = True
            self.sonido.stop_music(self.cancion)
        else:

            for plataforma in self.lista_plataformas:
                plataforma.draw(screen)

            for trampa in self.lista_trampas:
                trampa.update(screen)

            lista_frutas = self.frutas.update(self.lista_plataformas,screen)
            lista_trunk = self.trunk.update(self.lista_plataformas,screen,delta_ms,self.player_1)
            lista_radish = self.radish.update(delta_ms,self.lista_plataformas,screen,self.player_1)
            self.lista_frutas = lista_frutas
            self.lista_trunk = lista_trunk 

            for enemigo in lista_trunk:
                self.lista_balas_de_enemigo = self.lista_de_balas_enemigos.update(enemigo,screen,self.player_1,lista_trunk,delta_ms,self.sonido)

            if self.player_1.vitality:
                self.player_1.events(keys)
                self.player_1.update(delta_ms,self.lista_plataformas,lista_trunk,lista_frutas,lista_radish,self.lista_balas_de_enemigo,self.sonido,self.lista_trampas)
                self.player_1.draw(screen)
                lista_para_contar_balas = self.lista_de_balas.update(self.player_1,events,screen,lista_trunk,lista_radish,self.sonido)

            self.items_en_pantalla.update(screen,self.player_1,delta_ms)

        self.boton1.update(lista_eventos)
        self.boton1.draw(screen)