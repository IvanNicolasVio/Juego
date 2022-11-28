import pygame
from constantes import *

class Finalizador():
    def __init__(self) -> None:
        self.bandera_finalizador = True
        self.tiempo_transcurrido = 0
        self.tiempo_de_juego = 30
        self.retorno = True

    def finalizar_juego(self,delta_ms):
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > 3400:
            self.tiempo_de_juego -= 1
            self.tiempo_transcurrido = 0


        if self.tiempo_de_juego > 0:
            self.retorno = True
        else:
            self.retorno = False
            self.tiempo_de_juego = 0
        
        return self.retorno


    def update(self,delta_ms,screen):

        self.finalizar_juego(delta_ms)

        fuente = pygame.font.SysFont("Arial",30)
        texto = fuente.render("Tiempo restante: {0}".format(self.tiempo_de_juego),True,(0,0,0))
        screen.blit(texto,(1200,30))