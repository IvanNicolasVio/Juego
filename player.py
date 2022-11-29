import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigos_2 import *
from disparos_3 import *

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,vidas) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Run (32x32).png",12,1)#[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Run (32x32).png",12,1,True)#[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Idle (32x32).png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Idle (32x32).png",11,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Jump (32x32).png",1,1,False,2)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Jump (32x32).png",1,1,True,2)
        self.get_hit_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Hit (32x32).png",7,1,False)
        self.get_hit_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Pink Man\\Hit (32x32).png",7,1)
        self.die_r = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Desappearing (96x96).png",6,1,True)
        self.die_l = Auxiliar.getSurfaceFromSpriteSheet("C:\\Users\\Iván\\Desktop\\Python_UTN\\Juego\\Recursos_pixel\\Main Characters\\Desappearing (96x96).png",6,1)
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
        self.rect_cuerpo = pygame.Rect(x + 4, y + 5 , 25, 30)
        self.rect_manos = pygame.Rect(self.rect.x + self.rect.w /3 + 10, self.rect.y + 14, self.rect.w / 3,10)
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.jump_height = jump_height
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.tiempo_transcurrido = 0
        self.vidas = vidas
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.y_start_jump = 0
        self.score = 0
        self.is_jump = False
        self.vitality = True
        self.bandera_restar_vidas = False
        self.bandera_lastimarse = False


#----------------------------------------------------------------------------------------MOVIMIENTOS
    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
        

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def do_movement(self,delta_ms,lista_plataformas,lista_enemigos):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)


            if(self.is_on_platform(lista_plataformas) == False):
                 self.add_y(self.gravity)
            elif(self.is_jump): #Â SACAR
                self.jump(False)
            
            #self.choque(lista_enemigos)

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno

                           
    def add_x(self,delta_x,accion="suma"):
        if accion == "suma":
            self.rect.x += delta_x
            self.rect_ground_collition.x += delta_x
            self.rect_cuerpo.x += delta_x
            self.rect_manos.x += delta_x
        elif accion == "resta":
            self.rect.x -= delta_x
            self.rect_ground_collition.x -= delta_x
            self.rect_cuerpo.x -= delta_x
            self.rect_manos.x -= delta_x

    def add_y(self,delta_y,accion="suma"):
        if accion == "suma":
            self.rect.y += delta_y
            self.rect_ground_collition.y += delta_y
            self.rect_cuerpo.y += delta_y
            self.rect_manos.y += delta_y
        elif accion == "resta":
            self.rect.y -= delta_y
            self.rect_ground_collition.y -= delta_y
            self.rect_cuerpo.y -= delta_y
            self.rect_manos.y -= delta_y


#-----------------------------------------------------------------------------------------------------------------ANIMACION
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
        
#-------------------------------------------------------------------------------------------------------------------FUNDIR EN LA PANTALLA

    
        
    
    def draw(self,screen):
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
            pygame.draw.rect(screen,BLUE,self.rect_manos)
            #pygame.draw.rect(screen,GREEN,self.rect_cuerpo)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

#--------------------------------------------------------------------------------------------------------------------EVENTOS

    def events(self,keys):
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   
        if(keys[pygame.K_SPACE]):
            self.jump(True)

#----------------------------------------------------------------------------------------------------------------COLISIONES 

    def choque(self,lista_enemigos):
        for enemigo in lista_enemigos:
            if enemigo.vitality:
                if(self.rect.colliderect(enemigo.rect)):
                    if enemigo.bandera_de_choque:
                        self.add_x(6,"resta")
                    if enemigo.bandera_de_choque == False:
                        self.add_x(6,"suma")


    def recolectar_frutas(self,lista_frutas):
        for fruta in lista_frutas:
            if(self.rect_cuerpo.colliderect(fruta.rect_colision)) and fruta.recolectada:
                self.score += 50
                print("Aca entro")
                fruta.recolectada = False
                
                
    def lastimarse(self):
        
        if self.vidas > 1 and self.vitality and self.bandera_lastimarse:
            self.vidas -= 1
            self.bandera_restar_vidas = True
            self.bandera_lastimarse = False
            print("perdiste una vida")
        elif self.vidas == 1 and self.vitality and self.bandera_lastimarse:
            self.vidas -= 1
            self.vitality = False
            self.bandera_restar_vidas = True
            self.bandera_lastimarse = False
            print("perdiste las 3")

    def colisionar_con_enemigos(self,lista_enemigos,delta_ms):
        self.tiempo_transcurrido += delta_ms
        for enemigo in lista_enemigos:
            if(self.rect.colliderect(enemigo.rect) and self.tiempo_transcurrido >= 1800) and enemigo.vitality:  
                self.tiempo_transcurrido = 0
                self.bandera_lastimarse = True
        
    def colisionar_con_balas(self,lista_balas,delta_ms):
        self.tiempo_transcurrido += delta_ms
        for bala in lista_balas:
            if(self.rect.colliderect(bala.rect_colide) and self.tiempo_transcurrido >= 1800):  
                self.tiempo_transcurrido = 0
                self.bandera_lastimarse = True
                bala.vitality = False
        
    
    def update(self,delta_ms,lista_plataformas,lista_enemigos,lista_frutas,lista_radish,lista_balas):
        self.do_movement(delta_ms,lista_plataformas,lista_enemigos)
        self.do_animation(delta_ms)
        self.lastimarse()
        self.recolectar_frutas(lista_frutas)
        self.colisionar_con_enemigos(lista_enemigos,delta_ms)
        self.colisionar_con_enemigos(lista_radish,delta_ms)
        self.colisionar_con_balas(lista_balas,delta_ms)
                    
                    

    