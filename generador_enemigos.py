import pygame
from constantes import *
from auxiliar import Auxiliar
from disparos_3 import *
import random
from enemigos_2 import *

        

class Generador_trunk():
    def __init__(self,speed_walk,gravity) -> None: #self,x,y,speed_walk,tope_izq,tope_derecho,gravity
        self.lista_trunk = []
        self.trunk_creado = True
        self.speed_walk = speed_walk
        self.gravity = gravity


    def generar_trunk(self,lista_plataformas):
        for plataforma in lista_plataformas:
            self.lista_trunk.append(TrunkPatrulla(plataforma.rect.x + 50 , plataforma.rect.y - 50 , self.speed_walk , plataforma.rect.x ,plataforma.rect.x + plataforma.ancho , self.gravity))
            #x,y,speed_walk,tope_izq,tope_derecho,gravity #100,500,200,50,1

    def update(self,lista_plataformas,screen,delta_ms,jugador):
        if self.trunk_creado:
            self.generar_trunk(lista_plataformas)
            self.trunk_creado = False
        else:
            for trunk in self.lista_trunk:
                if trunk.vitality:
                    trunk.update(delta_ms,lista_plataformas,screen,jugador)
                else:
                    self.lista_trunk.remove(trunk)    
                
        return self.lista_trunk




class Generador_radish():
    def __init__(self,cantidad,x,y,speed,tope_izq,tope_der,gravity) -> None:
        self.lista_radish = []
        self.radish_creado = True
        self.cantidad = cantidad
        self.speed = speed
        self.speed_ingresada = speed
        self.x = x
        self.y = y
        self.tope_izq = tope_izq
        self.tope_der = tope_der
        self.gravity = gravity
        self.reduccion_velocidad = 0


    
    def generar_radish(self):
        for i in range(self.cantidad):
            self.lista_radish.append(Radish(self.x,self.y,self.speed - self.reduccion_velocidad,self.tope_izq,self.tope_der,self.gravity))
            self.reduccion_velocidad += 2
            
    

    def update(self,delta_ms,lista_plataformas,screen,player):
        if self.radish_creado:
            self.generar_radish()
            self.radish_creado = False
        else:
            if self.lista_radish == []:
                self.reduccion_velocidad = 0
                self.generar_radish()
            for radish in self.lista_radish:
                if radish.vitality:
                    radish.update(delta_ms,lista_plataformas,screen,player)
                else:  
                    self.lista_radish.remove(radish)
        
        return self.lista_radish