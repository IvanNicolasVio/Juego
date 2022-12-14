import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar



class Saw():
    '''
    clase Saw: Cierra utilizada como trampa,estatica que lastima al jugador
    '''
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Recursos_pixel\\Traps\\Saw\\On (38x38).png",8,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_colision = pygame.Rect(self.rect.x + 5,self.rect.y + 5,28,28)
        self.vitality = True


    def do_animation(self): #Hace la animacion
        '''
        anima el objeto dibujado utiliza las funciones de la carpeta auxiliar
        '''
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        '''
        dibuja el objeto en la pantalla de juego

        screen = pantalla donde se ejecuta el juego
        '''
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,RED,self.rect_colision)
            #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def update(self,screen):
        '''
        llama a la funcion para dibujar y a la funcion para animar

        screen = pantalla donde se ejecuta el juego
        '''
        self.draw(screen)
        self.do_animation()
