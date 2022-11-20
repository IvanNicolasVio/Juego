#from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
import pygame
import sys
from constantes import *
from player import Player
from plataforma import *
from enemigo import *
from disparos import *




screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\first_images\\locations\\city\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(x=0,y=591,speed_walk=4,speed_run=8,gravity=8,jump_power=25,frame_rate_ms=80,move_rate_ms=10,jump_height=150)
dust_1 = Dust(x=500,y=590,speed_walk=5,tope_izq=0,tope_derecho=ANCHO_VENTANA,gravity=8)
lista_de_balas = lista_balas(5)
lista_de_balas_enemigos = lista_balas_enemigas(5)
lista_enemigos = []
lista_enemigos.append(TrunkPatrulla(x=150,y=450,speed_walk=4,tope_izq=100,tope_derecho=200,gravity=8))
lista_enemigos.append(TrunkPatrulla(x=550,y=450,speed_walk=4,tope_izq=500,tope_derecho=600,gravity=8))
lista_enemigos.append(TrunkPatrulla(x=850,y=450,speed_walk=4,tope_izq=800,tope_derecho=900,gravity=8))
lista_enemigos.append(TrunkPatrulla(x=1250,y=450,speed_walk=4,tope_izq=1200,tope_derecho=1300,gravity=8))
lista_plataformas = []
lista_plataformas.append(Platform(100,500,200,50,1))#1
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

    for plataforma in lista_plataformas:
        plataforma.draw(screen)

    player_1.events(keys)
    player_1.update(delta_ms,lista_plataformas,lista_enemigos)
    player_1.draw(screen)
    lista_de_balas.update(player_1,events,screen,lista_enemigos)
    dust_1.update(lista_plataformas,screen)
    for enemigo in lista_enemigos:
        enemigo.update(delta_ms,lista_plataformas,screen,player_1)
        lista_de_balas_enemigos.update(enemigo,screen,player_1)
    
    pygame.display.flip()

