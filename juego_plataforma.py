import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar




class Platform:
    
    def __init__(self,x,y,w,h,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "first_images\\tile\\sheet1.png",8,8)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ancho = w
        self.alto = h
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)

        screen.blit(self.image,self.rect)

        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)


class creadorPlataformas():
    def __init__(self,x,y,cantidad,alto,ancho) -> None:
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.cantidad = cantidad
        self.lista_plataformas = []
        
    def primer_mosaico(self):
        for i in range(self.cantidad):
            self.lista_plataformas.append(Platform(self.x + 50,self.y + 500,self.alto,self.ancho))

        return self.lista_plataformas

    def draw(self,screen):
        for elemento in self.lista_plataformas:
            elemento.draw(screen)
        return self.lista_plataformas