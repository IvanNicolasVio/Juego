import pygame
from juego_constantes import *

class Finalizador():
    '''
    objeto que finaliza el juego, dibuja el tiempo en el nivel
    '''
    def __init__(self,tiempo_juego) -> None:
        self.bandera_finalizador = True
        self.tiempo_transcurrido = 0
        self.tiempo_de_juego = tiempo_juego
        self.retorno = True

    def finalizar_juego(self,delta_ms):
        '''
        pone el retorno en false cuando el tiempo termina
        es usado en el generador de nivel

        delta_ms = tiempo para medir el tiempo estipulado
        '''
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > 2400:
            self.tiempo_de_juego -= 1
            self.tiempo_transcurrido = 0


        if self.tiempo_de_juego > 0:
            self.retorno = True
        else:
            self.retorno = False
            self.tiempo_de_juego = 0
        
        return self.retorno


    def tiempo_de_nivel(self,screen):
        '''
        muestra el tiempo en el nivel

        screen = pantalla donde muestra el tiempo
        '''
        fuente = pygame.font.SysFont("Arial",30)
        texto = fuente.render("Tiempo restante: {0}".format(self.tiempo_de_juego),True,(0,0,0))
        screen.blit(texto,(1200,30))


    def update(self,delta_ms,screen):
        '''
        utiliza la funcion de mostrar el tiempo en el nivel y la de terminarlo

        delta_ms = tiempo para medir el tiempo estipulado
        screen = pantalla donde muestra el tiempo

        retorna False si el tiempo llega a 0
        '''

        self.tiempo_de_nivel(screen)
        self.retorno = self.finalizar_juego(delta_ms)
        return self.retorno