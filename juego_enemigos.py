import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar
from juego_disparos import *
import random



class Radish():
    '''
    clase Radish: enemigo que se mueve de izquierda a derecha,con gravedad
    '''
    def __init__(self,x,y,speed_walk,tope_izq,tope_derecho,gravity):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Radish\\Run (30x38).png",12,1,True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Radish\\Run (30x38).png",12,1)
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
        self.poder_disparar = False
#-------------------------------------------------------------------------------------------------------------------MOVIMIENTOS

    def movimiento(self,lista_plataformas): #Lo mueve de lado a lado
        '''
        movimiento automatico de radish de izquierda a derecha rebotando entre los parametros seteados en el creador

        lista_plataformas : plataformas donde se puede mantener en pie el radish
        '''
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
        '''
        mueve el personaje en el eje y

        delta_y: valor para mover el personaje
        accion= "suma" si se quiere mover para abajo "resta" si se quiere mover para arriba
        '''
        if accion == "suma":
            self.rect.y += delta_y
            self.rect_colision.y += delta_y
        elif accion == "resta":
            self.rect.y -= delta_y
            self.rect_colision.y -= delta_y  

    def is_on_platform(self,lista_plataformas):
        '''
        detecta si no esta en la plataforma para poder activar/desactivar la gravedad

        lista_plataformas = plataformas donde coliciona el enemigo
        retorna: true si esta colicionando / False si no esta colicionando
        '''
        retorno = False
        if(self.rect_colision.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_colision.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno

#----------------------------------------------------------------------------------------------------------------ANIMACION

    def do_animation(self): #Hace la animacion
        '''
        anima el objeto dibujado utiliza las funciones de la carpeta auxiliar
        '''
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

#-----------------------------------------------------------------------------------------------------------------FUNDIR EN LA PANTALLA

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
  
    def update(self,delta_ms,lista_plataformas,screen,player):
        '''
        llama a la funcion para dibujar , a la funcion para animar y a la funcion para mover automaticamente

        lista_plataformas = plataformas donde coliciona el enemigo
        screen = pantalla donde se ejecuta el juego
        '''
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
    '''
    clase Trunk: enemigo que se mueve de izquierda a derecha aleatoriamente,con gravedad y puede disparar
    '''
    def __init__(self,x,y,speed_walk,tope_izq,tope_derecho,gravity):
        self.idle_l = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Idle (64x32).png",18,1)
        self.idle_r = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Idle (64x32).png",18,1,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Run (64x32).png",14,1,True)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Run (64x32).png",14,1)
        self.atk_r = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Attack (64x32).png",11,1,True)
        self.atk_l = Auxiliar.getSurfaceFromSpriteSheet(ROOT + "Recursos_pixel\\Enemies\\Trunk\\Attack (64x32).png",11,1)
        self.frame = 0
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.gravity = gravity
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_colision = pygame.Rect(x + 13,y + 3,30,30)# x , y , ancho , alto
        self.rect_disparo_l = pygame.Rect(x - 150,y + 3,200,30)
        self.rect_disparo_r = pygame.Rect(x + 20,y + 3,200,30)
        self.rect_boca = pygame.Rect(x + 20,y + 15,25,5)
        self.speed_walk =  speed_walk
        self.bandera_mov = False
        self.bandera_de_choque = True
        self.vitality = True
        self.poder_disparar = True
        self.bandera_quedarse_quieto = False
        self.bandera_inicio_mov = True
        self.bandera_para_disparar = False
        self.direction = DIRECTION_R
        self.tope_izq = tope_izq
        self.tope_derecho = tope_derecho
        self.tiempo_acumulado = 0
        self.numero_aleatorio = 0
        self.cargador = []
        self.balas_usadas = []
        
#------------------------------------------------------------------------------------------------------------------MOVIMIENTO

    def movimiento_aleatorio(self,delta_ms,lista_plataformas,jugador): # se mueve aleatoriamente
        '''
        movimiento automatico de trunk de izquierda a derecha aleatoriamente rebotando entre los parametros seteados en el creador

        lista_plataformas : plataformas donde se puede mantener en pie el radish
        jugador : jugador al que se quiere disparar
        delta_ms = tiempo para medir el tiempo estipulado
        '''

        if self.bandera_inicio_mov:
            self.add_x(self.speed_walk)
            self.animation = self.walk_r
            self.bandera_inicio_mov = False
        else:
            if not self.bandera_quedarse_quieto: #Bandera para poder disparar, cambia en disparos
                if self.bandera_mov:
                    self.animation = self.walk_r
                    self.add_x(self.speed_walk)
                    self.direction = DIRECTION_L  
                elif not self.bandera_mov:
                    self.animation = self.walk_l
                    self.add_x(self.speed_walk,"resta")
                    self.direction = DIRECTION_R
                self.tiempo_acumulado += delta_ms
                if self.tiempo_acumulado > 1200:
                    self.bandera_mov = random.choice((True,False))
                    self.tiempo_acumulado = 0
                if self.rect_colision.x + 15  >= self.tope_derecho:
                    self.bandera_mov = False #Con esto mueve a la izquierda
                elif self.rect_colision.x - 15 <= self.tope_izq:
                    self.bandera_mov = True # Con esto mueve a la derecha
            else:   #Enfocar al jugador para poder dispararle
                if self.rect_disparo_l.colliderect(jugador.rect_cuerpo):
                    self.animation = self.idle_l   
                    self.direction = DIRECTION_R
                    self.add_x(0)
                elif self.rect_disparo_r.colliderect(jugador.rect_cuerpo):
                    self.animation = self.idle_r 
                    self.direction = DIRECTION_L   
                    self.add_x(0)
                else:
                    self.bandera_quedarse_quieto = False
                
                    
                

        if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)

    def add_x(self,delta_x,accion="suma"):
        '''
        mueve el personaje en el eje x

        delta_x: valor para mover el personaje
        accion= "suma" si se quiere mover para la derecha "resta" si se quiere mover para la izquierda
        '''
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
        '''
        mueve el personaje en el eje y

        delta_y: valor para mover el personaje
        accion= "suma" si se quiere mover para abajo "resta" si se quiere mover para arriba
        '''
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
        '''
        detecta si no esta en la plataforma para poder activar/desactivar la gravedad

        lista_plataformas = plataformas donde coliciona el enemigo
        retorna: true si esta colicionando / False si no esta colicionando
        '''
        retorno = False
        if(self.rect_colision.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_colision.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
            
#-----------------------------------------------------------------------------------------------------------------------------ANIMACION

    def do_animation(self):
        '''
        anima el objeto dibujado utiliza las funciones de la carpeta auxiliar
        '''
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

#----------------------------------------------------------------------------------------------------------------------------- FUNDIR EN PANTALLA

    def draw(self,screen):
        '''
        dibuja el objeto en la pantalla de juego

        screen = pantalla donde se ejecuta el juego
        '''
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_colision)
            #pygame.draw.rect(screen,GREEN,self.rect_disparo_l)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
  
    def update(self,delta_ms,lista_plataformas,screen,jugador):
        '''
        llama a la funcion para dibujar , a la funcion para animar y a la funcion para mover automaticamente

        delta_ms = tiempo para medir el tiempo estipulado
        lista_plataformas = plataformas donde coliciona el enemigo
        screen = pantalla donde se ejecuta el juego
        jugador: al que se dispara
        '''
        #if self.vitality:
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


            



    








