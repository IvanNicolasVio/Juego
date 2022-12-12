import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar



class Manzana():
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Items\\Fruits\\Apple.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 10,y + 10,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True


    def do_animation(self): #Hace la animacion
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,RED,self.rect_colision)
            #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def update(self,screen):
        self.draw(screen)
        self.do_animation()

class Banana(Manzana):
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Items\\Fruits\\Bananas.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 10,y + 10,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True

class Cherry(Manzana):
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Items\\Fruits\\Cherries.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 15,y + 15,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True      
        


class Frutas():
    def __init__(self) -> None:
        self.lista_frutas = []
        self.fruta_creada = True


    def generarFrutas(self,lista_plataformas):
        for plataforma in lista_plataformas:
            self.lista_frutas.append(Manzana(plataforma.rect.x + 10,plataforma.rect.y - 30))
            self.lista_frutas.append(Banana(plataforma.rect.x + 70,plataforma.rect.y - 30))
            self.lista_frutas.append(Cherry(plataforma.rect.x + 140,plataforma.rect.y - 30))
        

    def update(self,lista_plataformas,screen):
        if self.fruta_creada:
            self.generarFrutas(lista_plataformas)
            self.fruta_creada = False
        for fruta in self.lista_frutas:
            if fruta.recolectada:
                fruta.update(screen)
            else:
                self.lista_frutas.remove(fruta)    
            
        return self.lista_frutas
            
