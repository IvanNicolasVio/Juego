import pygame
from constantes import *
from auxiliar import Auxiliar
from disparos import Bala
import random



class Dust():
    def __init__(self,x,y,speed_walk,tope_izq,tope_derecho,gravity):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Radish\\Run (30x38).png",12,1,True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Radish\\Run (30x38).png",12,1)
        self.frame = 0
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.gravity = gravity
        #self.rect = pygame.Rect(100,30,40,40)# x , y , ancho , alto
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_colision = pygame.Rect(x,y + 9,30,30)
        self.speed_walk =  speed_walk
        self.bandera_inico_mov = True
        self.bandera_de_choque = True
        self.vitality = True
        self.tope_izq = tope_izq
        self.tope_derecho = tope_derecho

#-------------------------------------------------------------------------------------------------------------------MOVIMIENTOS

    def movimiento(self,lista_plataformas): #Lo mueve de lado a lado
        if self.bandera_inico_mov:
            self.rect.x += self.speed_walk
            self.rect_colision.x += self.speed_walk
            self.bandera_inico_mov = False
        else:
            if self.rect.x > self.tope_derecho - 30:
                self.bandera_de_choque = True
            if self.rect.x < self.tope_izq:
                self.bandera_de_choque = False
        
        if self.bandera_de_choque:
            self.animation = self.walk_l
            self.rect.x -= self.speed_walk
            self.rect_colision.x -= self.speed_walk
        if not self.bandera_de_choque:
            self.animation = self.walk_r
            self.rect.x += self.speed_walk
            self.rect_colision.x += self.speed_walk

        if(self.is_on_platform(lista_plataformas) == False):
            self.add_y(self.gravity)

    def add_y(self,delta_y,accion="suma"):
        if accion == "suma":
            self.rect.y += delta_y
            self.rect_colision.y += delta_y
            self.rect_cuerpo.y += delta_y
            self.rect_manos.y += delta_y
        elif accion == "resta":
            self.rect.y -= delta_y
            self.rect_colision.y -= delta_y  

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect_colision.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_colision(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno

#----------------------------------------------------------------------------------------------------------------ANIMACION

    def do_animation(self): #Hace la animacion
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

#-----------------------------------------------------------------------------------------------------------------FUNDIR EN LA PANTALLA

    def draw(self,screen):
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,RED,self.rect_colision)
            #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
  
    def update(self,lista_plataformas,screen):
        if self.vitality:
            self.draw(screen)
            self.movimiento(lista_plataformas)
            self.do_animation()

#-----------------------------------------------------------------------------------------------------------------------------------Colision

    def morir(self,lista_de_balas,screen):
        for bala in lista_de_balas:
            if self.rect_colision.colliderect(bala.rect_colide):
                self.vitality = False
                return False
        if self.vitality == True:
            self.draw(screen)
            return True

        





class TrunkPatrulla():
    def __init__(self,x,y,speed_walk,tope_izq,tope_derecho,gravity):
        self.idle_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Idle (64x32).png",18,1)
        self.idle_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Idle (64x32).png",18,1,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Run (64x32).png",14,1,True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Run (64x32).png",14,1)
        self.atk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Attack (64x32).png",11,1,True)
        self.atk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Enemies\\Trunk\\Attack (64x32).png",11,1)
        self.frame = 0
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.gravity = gravity
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_colision = pygame.Rect(x + 13,y + 3,30,30)# x , y , ancho , alto
        self.rect_disparo_r = pygame.Rect(x - 150,y + 3,200,30)
        self.rect_disparo_l = pygame.Rect(x + 20,y + 3,200,30)
        self.rect_boca = pygame.Rect(x + 20,y + 15,25,5)
        self.speed_walk =  speed_walk
        self.bandera_mov = False
        self.bandera_de_choque = True
        self.vitality = True
        self.bandera_inicio_mov = True
        self.direction = DIRECTION_R
        self.tope_izq = tope_izq
        self.tope_derecho = tope_derecho
        self.tiempo_acumulado = 0
        self.numero_aleatorio = 0
        
#------------------------------------------------------------------------------------------------------------------MOVIMIENTO

    def movimiento_aleatorio(self,delta_ms,lista_plataformas,jugador): # se mueve aleatoriamente
        if self.bandera_inicio_mov:
            self.add_x(self.speed_walk)
            self.animation = self.walk_r
            self.bandera_inicio_mov = False
        else:
            if self.rect_disparo_r.colliderect(jugador.rect_cuerpo):
                self.animation = self.idle_l
                self.add_x(0)
            elif self.rect_disparo_l.colliderect(jugador.rect_cuerpo):
                self.animation = self.idle_r
                self.add_x(0)
            else:
                if self.bandera_mov and self.rect_colision.x < self.tope_derecho - 3:
                    self.animation = self.walk_r
                    self.add_x(self.speed_walk)
                    self.direction = DIRECTION_R
                elif not self.bandera_mov and self.rect_colision.x > self.tope_izq +3:
                    self.animation = self.walk_l
                    self.add_x(self.speed_walk,"resta")
                    self.direction = DIRECTION_L
                self.tiempo_acumulado += delta_ms
                if self.tiempo_acumulado > 1200:
                    self.numero_aleatorio = random.randint(1,6)
                    self.tiempo_acumulado = 0
                    if self.numero_aleatorio == 1 or self.numero_aleatorio == 2 or self.numero_aleatorio == 3:
                        self.bandera_mov = True # <-
                    elif self.numero_aleatorio == 4 or self.numero_aleatorio == 5 or self.numero_aleatorio == 6:
                        self.bandera_mov = False # ->

        if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)

    def add_x(self,delta_x,accion="suma"):
        if accion == "suma":
            self.rect.x += delta_x
            self.rect_colision.x += delta_x  
            self.rect_disparo_r.x += delta_x 
            self.rect_disparo_l.x += delta_x
            self.rect_boca.x += delta_x
        elif accion == "resta":
            self.rect.x -= delta_x
            self.rect_colision.x -= delta_x
            self.rect_disparo_r.x -= delta_x
            self.rect_disparo_l.x -= delta_x
            self.rect_boca.x -= delta_x

    def add_y(self,delta_y,accion="suma"):
        if accion == "suma":
            self.rect.y += delta_y
            self.rect_colision.y += delta_y
            self.rect_disparo_r.y += delta_y
            self.rect_disparo_l.y += delta_y
            self.rect_boca.y += delta_y
        elif accion == "resta":
            self.rect.y -= delta_y
            self.rect_colision.y -= delta_y  
            self.rect_disparo_r.y -= delta_y 
            self.rect_disparo_l.y -= delta_y
            self.rect_boca.y -= delta_y

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect_colision.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_colision.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
            
    def disparar():
        pass

#-----------------------------------------------------------------------------------------------------------------------------ANIMACION

    def do_animation(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

#----------------------------------------------------------------------------------------------------------------------------- FUNDIR EN PANTALLA

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_colision)
            pygame.draw.rect(screen,GREEN,self.rect_disparo_l)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
  
    def update(self,delta_ms,lista_plataformas,screen,jugador):
        if self.vitality:
            self.draw(screen)
            self.movimiento_aleatorio(delta_ms,lista_plataformas,jugador)
            self.do_animation()


#------------------------------------------------------------------------------------------------------------------------------ Colicion

    def morir(self,lista_de_balas,screen):
        for bala in lista_de_balas:
            if self.rect_colision.colliderect(bala.rect_colide):
                self.vitality = False

        if self.vitality == True:
            self.draw(screen)

        

















































class RobotPerseguidor():
    def __init__(self,x,y,speed_walk,tope_izq,tope_derecho,p_scale):
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\images\\images\\caracters\\players\\robot\\Run ({0}).png",8,flip=False,scale=p_scale,repeat_frame=2)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\images\\images\\caracters\\players\\robot\\Run ({0}).png",8,flip=True,scale=p_scale,repeat_frame=2)
        self.atk_r = Auxiliar.getSurfaceFromSeparateFiles("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\images\\images\\caracters\\players\\robot\\Shoot ({0}).png",4,flip=False,scale=p_scale,repeat_frame=2)
        self.atk_l = Auxiliar.getSurfaceFromSeparateFiles("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\images\\images\\caracters\\players\\robot\\Shoot ({0}).png",4,flip=True,scale=p_scale,repeat_frame=2)
        self.frame = 0
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_walk =  speed_walk
        self.bandera_mov = True
        self.bandera_de_choque = True
        self.tope_izq = tope_izq
        self.tope_derecho = tope_derecho
        self.tiempo_acumulado = 0
        

    def persecucion(self,delta_ms):
        self.tiempo_acumulado += delta_ms
        if self.tiempo_acumulado >= 3000:
            numero = random.randint(1,2)
            print("5 segs")
            self.tiempo_acumulado = 0
            if numero == 1:
                self.bandera_mov = True
                if self.rect.x > self.tope_derecho:
                    self.bandera_mov = False
                    print("choco")
            elif numero == 2:
                self.bandera_mov = False
                if self.rect.x < self.tope_derecho:
                    self.bandera_mov = True
                    print("choco")
            
        if self.bandera_mov:
            self.rect.x += self.speed_walk
            self.animation = self.walk_r
        elif not self.bandera_mov:
            self.rect.x -= self.speed_walk
            self.animation = self.walk_l
            
    def disparar():
        pass


    def do_animation(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
  
    def update(self,delta_ms):
        self.do_animation()

