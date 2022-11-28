import pygame
from constantes import *

class PrimeraVida():
    def __init__(self,x,y) -> None:
        self.image = pygame.image.load("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\images\\corazon_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect_vida = pygame.Rect(x,y,30,30)
        


    def draw(self,screen):
            if(DEBUG):
                #pygame.draw.rect(screen,RED,self.rect)
                pygame.draw.rect(screen,RED,self.rect_vida)
                #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
            #self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect_vida)

    def update(self,screen):
        self.draw(screen)

    
class items_pantalla():
    def __init__(self,x,y,cantidad) -> None:
        self.lista_vidas = []
        self.vida_creada = True
        self.x = x
        self.y = y
        self.cantidad = cantidad
        self.bandera_muerte = False
        self.acompañante_x = 30
        self.tiempo_transcurrido = 0
        self.tiempo_de_juego = 30
        

    def generarVida(self):
        for i in range(self.cantidad):
            self.lista_vidas.append(PrimeraVida(self.x + self.acompañante_x,self.y))
            self.acompañante_x += 30
            

    def restarVida(self,jugador,delta_ms):
        for vida in self.lista_vidas:
            self.tiempo_transcurrido += delta_ms
            if jugador.bandera_restar_vidas and self.tiempo_transcurrido >= 1800:
                self.tiempo_transcurrido = 0
                jugador.bandera_restar_vidas = False
                self.lista_vidas.remove(vida)

    def tiempo_de_nivel(self,delta_ms,screen):
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > 3400:
            self.tiempo_de_juego -= 1
            self.tiempo_transcurrido = 0
        fuente = pygame.font.SysFont("Arial",30)
        texto = fuente.render("Tiempo restante: {0}".format(self.tiempo_de_juego),True,(0,0,0))
        screen.blit(texto,(1200,30))
           
    

    def update(self,screen,jugador,delta_ms):
        if self.vida_creada:
            self.generarVida()
            self.vida_creada = False

        for vida in self.lista_vidas:
            if not self.bandera_muerte:
                vida.update(screen)  

        self.restarVida(jugador,delta_ms)

        fuente = pygame.font.SysFont("Arial",30)
        texto = fuente.render("Score: {0}".format(jugador.score),True,(0,0,0))
        screen.blit(texto,(1200,0))

        self.tiempo_de_nivel(delta_ms,screen)
            
        return self.lista_vidas
        

