import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar



class Manzana():
    '''
    clase Manzana: coleccionable utilizado para generar puntos, se dibuja y tiene animacion
    '''
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Items\\Fruits\\Apple.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 10,y + 10,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True


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

class Banana(Manzana):
    '''
    clase banana: coleccionable utilizado para generar puntos, se dibuja y tiene animacion

    hereda la clase Manzana
    '''
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Items\\Fruits\\Bananas.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 10,y + 10,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True

class Cherry(Manzana):
    '''
    clase Cherry: coleccionable utilizado para generar puntos, se dibuja y tiene animacion

    hereda la clase Manzana
    '''
    def __init__(self,x,y) -> None:
        self.idle = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Items\\Fruits\\Cherries.png",17,1)
        self.frame = 0
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect_colision = pygame.Rect(x + 15,y + 15,10,10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.recolectada = True      
        


class Frutas():
    '''
    generador automatico de las clases manzana,banana,cherry
    '''
    def __init__(self) -> None:
        self.lista_frutas = []
        self.fruta_creada = True


    def generarFrutas(self,lista_plataformas):
        '''
        itera una lista para generar 3 frutas sobre cada plataforma ingresada y las agrega a una lista

        lista_plataformas = lista con las plataformas donde se quiere generar las frutas
        '''
        for plataforma in lista_plataformas:
            self.lista_frutas.append(Manzana(plataforma.rect.x + 10,plataforma.rect.y - 30))
            self.lista_frutas.append(Banana(plataforma.rect.x + 70,plataforma.rect.y - 30))
            self.lista_frutas.append(Cherry(plataforma.rect.x + 140,plataforma.rect.y - 30))
        

    def update(self,lista_plataformas,screen):
        '''
        llama a la funcion para generar frutas
        y luego las dibuja hasta que chocan con el jugador

        lista_plataformas = lista con las plataformas donde se quiere generar las frutas
        screen = pantalla donde se ejecuta el juego

        retorna la lista de frutas
        '''
        if self.fruta_creada:
            self.generarFrutas(lista_plataformas)
            self.fruta_creada = False
        for fruta in self.lista_frutas:
            if fruta.recolectada:
                fruta.update(screen)
            else:
                self.lista_frutas.remove(fruta)    
            
        return self.lista_frutas
            
