import pygame
from constantes import *
from auxiliar import Auxiliar

class Bala():
    def __init__(self,x,y,speed) -> None:
        self.shoot = pygame.image.load("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Skull\\Red Particle.png")
        self.rect = self.shoot.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_colide = pygame.Rect(x + 30,y + 30,5,6)
        self.speed = speed
        self.bandera_disp = False
        self.direccion_disp = DIRECTION_R

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_colide)
        screen.blit(self.shoot,self.rect_colide)
  
    def update(self,direccion):
        self.recorrido(direccion)


class lista_balas():
    def __init__(self,cantidad) -> None:
        self.cantidad_balas = cantidad
        self.lista_balas_en_cargador = self.crear_balas()
        self.lista_balas_usadas = []
        self.bandera_z = False
        

    def crear_balas(self):
        return[Bala(0,0,5) for i in range(self.cantidad_balas)]


    def recargar(self):
        self.lista_balas_en_cargador = self.crear_balas()

    def disparar_balas(self,player):
            if self.bandera_z and self.lista_balas_en_cargador:
                bala_disparada = self.lista_balas_en_cargador.pop(0)
                bala_disparada.rect_colide.x = player.rect_manos.x
                bala_disparada.rect_colide.y = player.rect_manos.y
                bala_disparada.rect.x = player.rect_manos.x
                bala_disparada.rect.y = player.rect_manos.y
                bala_disparada.bandera_disp = True
                bala_disparada.direccion_disp = player.direction
                self.bandera_z = False       
                self.lista_balas_usadas.append(bala_disparada)
                print("Disparo")
                        
    def dibujar_balas(self,screen):
        for bala in self.lista_balas_usadas:
            if bala.bandera_disp == True:
                bala.draw(screen)
                if bala.direccion_disp == DIRECTION_R:
                    bala.rect_colide.x += bala.speed
                    bala.rect.x += bala.speed
                else:
                    bala.rect_colide.x -= bala.speed
                    bala.rect.x -= bala.speed

        
    def kill(self,lista_enemigos):
        for bala in self.lista_balas_usadas:
            for enemigo in lista_enemigos:
                    if bala.rect_colide.colliderect(enemigo.rect_colision) and enemigo.vitality == True :
                        enemigo.vitality = False
                        bala.bandera_disp = False
                        self.lista_balas_usadas.remove(bala)


    def eventos(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.bandera_z = True
                if event.key == pygame.K_r:
                    self.recargar()

    def update(self,player,events,screen,lista_enemigos):
        self.eventos(events)
        self.dibujar_balas(screen)
        self.disparar_balas(player)
        self.kill(lista_enemigos)
        return self.lista_balas_usadas
        









class lista_balas_enemigas():
    def __init__(self,cantidad) -> None:
        self.cantidad_balas = cantidad
        self.lista_balas_en_cargador = self.crear_balas()
        self.lista_balas_usadas = []
        self.bandera_z = False

    def crear_balas(self):
        return[Bala(0,0,5) for i in range(self.cantidad_balas)]


    def recargar(self):
        self.lista_balas_en_cargador = self.crear_balas()

    def disparar_balas(self,enemigo):
            if self.bandera_z and self.lista_balas_en_cargador:
                bala_disparada = self.lista_balas_en_cargador.pop(0)
                bala_disparada.rect_colide.x = enemigo.rect_boca.x
                bala_disparada.rect_colide.y = enemigo.rect_boca.y
                bala_disparada.rect.x = enemigo.rect_boca.x
                bala_disparada.rect.y = enemigo.rect_boca.y
                bala_disparada.bandera_disp = True
                bala_disparada.direccion_disp = enemigo.direction
                self.bandera_z = False       
                self.lista_balas_usadas.append(bala_disparada)
                print("Disparo")
                        
    def dibujar_balas(self,screen):
        for bala in self.lista_balas_usadas:
            if bala.bandera_disp == True:
                bala.draw(screen)
                if bala.direccion_disp == DIRECTION_R:
                    bala.rect_colide.x += bala.speed
                    bala.rect.x += bala.speed
                else:
                    bala.rect_colide.x -= bala.speed
                    bala.rect.x -= bala.speed
                    

    def update(self,enemigo,screen,jugador):
        self.dibujar_balas(screen)
        self.disparar_balas(enemigo)
        self.recargar
        self.eventos(enemigo,jugador)
        return self.lista_balas_usadas

    def eventos(self,enemigo,jugador):
        if enemigo.rect_disparo_r.colliderect(jugador.rect_cuerpo):
            self.bandera_z = True
        elif enemigo.rect_disparo_l.colliderect(jugador.rect_cuerpo):
            self.bandera_z = True