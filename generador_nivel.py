import pygame
import json
from constantes import *
from player import Player
from plataforma import *
from enemigos_2 import *   
from disparos_3 import *
from coleccionables import *
from mostrables import *
from generador_enemigos import *
from finalizador_juego import *

class Nivel():
    def __init__(self,nivel) -> None:
        self.nivel = nivel
        self.configuraciones_completas = self.leer_archivo()
        self.lista_plataformas = []
        self.parametro_imagen_fondo = self.configuraciones_completas[nivel]["imagen_fondo"]
        self.parametro_plataformas = self.configuraciones_completas[nivel]["parametros_plataformas"]
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
        self.finalizador_juego = Finalizador()
        self.imagen_fondo = pygame.image.load(self.parametro_imagen_fondo)

        
    def leer_archivo(self):
        with open("nivel_1.json", "r",encoding="utf-8") as configuraciones:
            return json.load(configuraciones)

    def crear_plataformas(self):
        for parametro in self.parametro_plataformas:
            self.lista_plataformas.append(Platform(parametro[0],parametro[1],parametro[2],parametro[3],parametro[4]))

    def generar_nivel(self,screen):

        #imagen_fondo = pygame.image.load(self.parametro_imagen_fondo)
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


        self.crear_plataformas()

    def update(self,delta_ms,screen,keys,events):
        
        screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())
        finalizador = self.finalizador_juego.update(delta_ms,screen)

        if not finalizador or self.player_1.vidas == 0:
            fuente = pygame.font.SysFont("Arial",100)
            texto = fuente.render("Score: {0}".format(self.player_1.score),True,(0,0,0))
            screen.blit(texto,(500,330))

        else:
            for plataforma in self.lista_plataformas:
                plataforma.draw(screen)

            lista_frutas = self.frutas.update(self.lista_plataformas,screen)
            lista_trunk = self.trunk.update(self.lista_plataformas,screen,delta_ms,self.player_1)
            lista_radish = self.radish.update(delta_ms,self.lista_plataformas,screen,self.player_1)

            for enemigo in lista_trunk:
                lista_balas_de_enemigo = self.lista_de_balas_enemigos.update(enemigo,screen,self.player_1,lista_trunk,delta_ms)

            if self.player_1.vitality:
                self.player_1.events(keys)
                self.player_1.update(delta_ms,self.lista_plataformas,lista_trunk,lista_frutas,lista_radish,lista_balas_de_enemigo)
                self.player_1.draw(screen)
                lista_para_contar_balas = self.lista_de_balas.update(self.player_1,events,screen,lista_trunk,lista_radish)

            self.items_en_pantalla.update(screen,self.player_1,delta_ms)

        
