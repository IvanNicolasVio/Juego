import pygame
import sys
from constantes import *
from player import Player
from plataforma import *
from enemigos_2 import *   
from disparos_3 import *
from coleccionables import *
from mostrables import *
from generador_enemigos import *
from finalizador_juego import *

tiempo_acumulado = 0

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\first_images\\locations\\city\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


lista_plataformas = []
lista_plataformas.append(Platform(100,500,200,50,1))#1 x,y,w,h
lista_plataformas.append(Platform(500,500,200,50,1))#1
lista_plataformas.append(Platform(800,500,200,50,1))#1
lista_plataformas.append(Platform(1200,500,200,50,1))#1
lista_plataformas.append(Platform(300,400,200,50,1))#2
lista_plataformas.append(Platform(1000,400,200,50,1))#2
lista_plataformas.append(Platform(100,290,200,50,1))#3
lista_plataformas.append(Platform(500,290,200,50,1))#3
lista_plataformas.append(Platform(800,290,200,50,1))#3
lista_plataformas.append(Platform(1200,290,200,50,1))#3
lista_plataformas.append(Platform(300,190,200,50,1))#4
lista_plataformas.append(Platform(1000,190,200,50,1))#4
lista_plataformas.append(Platform(500,70,200,50,1))#5
lista_plataformas.append(Platform(700,70,200,50,1))#5
lista_plataformas.append(Platform(900,70,100,50,1))#5

player_1 = Player(x=0,y=591,speed_walk=4,speed_run=8,gravity=8,jump_power=25,frame_rate_ms=80,move_rate_ms=10,jump_height=150,vidas=3)

lista_de_balas = lista_balas(5)
lista_de_balas_enemigos = lista_balas_enemigas(1)
frutas = Frutas()
trunk = Generador_trunk(5,8)
radish = Generador_radish(3,1800,590,8,0,ANCHO_VENTANA,8)
items_en_pantalla  = items_pantalla(0,0,player_1.vidas)
finalizador_juego = Finalizador()

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
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    finalizador = finalizador_juego.update(delta_ms,screen)

    if not finalizador or player_1.vidas == 0:
        pass
    else:
        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        lista_frutas = frutas.update(lista_plataformas,screen)
        lista_trunk = trunk.update(lista_plataformas,screen,delta_ms,player_1)
        lista_radish = radish.update(delta_ms,lista_plataformas,screen,player_1)

        for enemigo in lista_trunk:
            lista_balas_de_enemigo = lista_de_balas_enemigos.update(enemigo,screen,player_1,lista_trunk,delta_ms)

        if player_1.vitality:
            player_1.events(keys)
            player_1.update(delta_ms,lista_plataformas,lista_trunk,lista_frutas,lista_radish,lista_balas_de_enemigo)
            player_1.draw(screen)
            lista_para_contar_balas = lista_de_balas.update(player_1,events,screen,lista_trunk,lista_radish)

        items_en_pantalla.update(screen,player_1,delta_ms)


        
    pygame.display.flip()

