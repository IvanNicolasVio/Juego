import pygame
from juego_constantes import *
from juego_auxiliar import Auxiliar

class Bala():
    '''
    clase bala: se le da una imagen, se dibuja y actualiza
    '''
    def __init__(self,x,y,speed) -> None:
        self.shoot = pygame.image.load(ROOT + "Recursos_pixel\\Enemies\\Skull\\Red Particle.png")
        self.rect = self.shoot.get_rect()
        self.rect.x = x 
        self.rect.y = y  
        self.rect_colide = pygame.Rect(x + 25 ,y + 15 ,8,8)
        self.speed = speed
        self.bandera_disp = False
        self.direccion_disp = DIRECTION_R
        self.vitality = True

    def draw(self,screen):
        '''
        dibuja el objeto bala

        screen = pantalla donde se ejecuta el juego
        '''
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect_colide)
        screen.blit(self.shoot,self.rect)
  
    def update(self,direccion):
        self.recorrido(direccion)


class lista_balas():
    '''clase lista que crea y actualiza la clase bala para poder eliminar enemigos'''
    def __init__(self,cantidad) -> None:
        self.cantidad_balas = cantidad
        self.lista_balas_en_cargador = self.crear_balas()
        self.lista_balas_usadas = []
        self.bandera_z = False
        

    def crear_balas(self):
        ''' 
        crea la cantidad de balas que se piden

        las retorna en una lista
        '''
        return[Bala(0,0,5) for i in range(self.cantidad_balas)]


    def recargar(self):
        '''
        utiliza la funcion crear para ser llamada en caso de querer recargar
        '''
        self.lista_balas_en_cargador = self.crear_balas()

    def disparar_balas(self,player,sound):
        '''
        genera la clase bala en los rectangulos del player
        se elimina la bala de la lista de balas en cargador y se agrega a la lista de balas ya disparadas
        se reproduce un sonido cuando se dispara

        player = jugador que dispara
        sound = parametro para reproducir el sonido
        '''
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
            sound.play_sound(ROOT + "Sonidos\\Piu.wav")
            
        else:
            self.bandera_z = False    
                        
    def dibujar_balas(self,screen):
        '''
        dibuja las balas y las mueve segun la direccion del jugador

        screen = pantalla donde se ejecuta el juego
        '''
        for bala in self.lista_balas_usadas:
            if bala.bandera_disp == True:
                bala.draw(screen)
                if bala.direccion_disp == DIRECTION_R:
                    bala.rect_colide.x += bala.speed
                    bala.rect.x += bala.speed
                else:
                    bala.rect_colide.x -= bala.speed
                    bala.rect.x -= bala.speed

        
    def kill(self,lista_enemigos,player,sound):
        '''
        cuando la bala disparada colisiona con el enemigo, se eliminan mutuamente
        se aumenta el score del player
        se reproduce el sonido de eliminacion de enemigo

        lista_enemigos = lista de enemigos a eliminar
        player  = jugador al cual le aumenta el score
        sound = parametro para reproducir el sonido
        '''
        for bala in self.lista_balas_usadas:
            for enemigo in lista_enemigos:
                    if bala.rect_colide.colliderect(enemigo.rect_colision) and enemigo.vitality == True :
                        enemigo.vitality = False
                        bala.bandera_disp = False
                        self.lista_balas_usadas.remove(bala)
                        player.score += 300
                        sound.play_sound(ROOT + "Sonidos\\Muerte-enemigo.wav")

                        if enemigo.poder_disparar:
                            for bala in enemigo.balas_usadas:
                                bala.vitality = False


    def eventos(self,events):
        '''
        Se realiza una accion cuando se tocan determinadas teclas (z:disparar///r:recargar)

        events : lista de eventos de pygame
        '''
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.bandera_z = True
                    
                if event.key == pygame.K_r:
                    self.recargar()

    def update(self,player,events,screen,lista_enemigos,lista_radish,sound):
        '''
        se actualiza todo el tiempo y dibuja las balas,las dispara,detecta la eliminacion de los enemigos y detectan las teclas 

        player  = jugador utilizado
        events : lista de eventos de pygame
        screen = pantalla donde se ejecuta el juego
        lista_enemigos = lista de enemigos a eliminar
        lista_radish = lista de enemigos a eliminar
        sound = parametro para reproducir el sonido

        retorna la lista de balas usadas
        '''
        self.eventos(events)
        self.dibujar_balas(screen)
        self.disparar_balas(player,sound)
        self.kill(lista_enemigos,player,sound)
        self.kill(lista_radish,player,sound)
        return self.lista_balas_usadas
        


        
class lista_balas_enemigas():
    '''clase lista que crea y actualiza la clase bala para poder eliminar al jugador'''
    def __init__(self,cantidad) -> None:
        self.cantidad_balas = cantidad
        #self.lista_balas_en_cargador = self.crear_balas(lista_de_enemigos)
        self.lista_balas_usadas = []
        self.bandera_z = False
        self.tiempo_acumulado = 0

    def crear_balas(self,enemigo):
        ''' 
        crea la cantidad de balas que se piden

        enemigo: enemigo al cual  se le quiere agregar la bala
        '''
        if enemigo.cargador == []:
            enemigo.cargador.append(Bala(0,0,5))
            
    def dibujar_balas(self,screen,enemigo):
        '''
        dibuja las balas y las mueve segun la direccion del jugador

        screen = pantalla donde se ejecuta el juego
        enemigo: enemigo que dispara la bala
        '''
        for bala in enemigo.balas_usadas:
            if bala.vitality:
                if bala.bandera_disp == True:
                    bala.draw(screen)
                    if bala.direccion_disp == DIRECTION_L:
                        bala.rect_colide.x += bala.speed
                        bala.rect.x += bala.speed
                    else:
                        bala.rect_colide.x -= bala.speed
                        bala.rect.x -= bala.speed
                    

    def update(self,enemigo,screen,jugador,lista_de_enemigos,delta_ms,sound):
        '''
        se actualiza todo el tiempo y dibuja las balas,las dispara segun el tiempo estipulado

        enemigo  = enemigo utilizado
        screen = pantalla donde se ejecuta el juego
        player  = jugador a disparar
        lista_enemigos = lista de enemigos utilizado
        delta_ms = tiempo para medir el tiempo estipulado
        sound = parametro para reproducir el sonido

        retorna la lista de balas usadas
        '''
        self.tiempo_acumulado += delta_ms 
        if self.tiempo_acumulado > 1800:
            self.tiempo_acumulado = 0
            self.crear_balas(enemigo)
        self.disparar_balas(enemigo,sound)
        self.dibujar_balas(screen,enemigo)
        self.eventos(lista_de_enemigos,jugador,delta_ms)

        return self.lista_balas_usadas

#-----------------------------------------------------------------------------------------------------------------------DISPAROS ENEMIGOS
   
    def disparar_balas(self,enemigo,sound):    
        '''
        genera la clase bala en los rectangulos del enemigo
        se elimina la bala de la lista de balas en cargador y se agrega a la lista de balas ya disparadas
        se reproduce un sonido cuando se dispara

        enemigo = enemigo que dispara
        sound = parametro para reproducir el sonido
        '''
        if enemigo.bandera_para_disparar and enemigo.cargador and enemigo.poder_disparar:
            bala_disparada = enemigo.cargador.pop(0)
            bala_disparada.rect_colide.x = enemigo.rect_boca.x
            bala_disparada.rect_colide.y = enemigo.rect_boca.y
            bala_disparada.rect.x = enemigo.rect_boca.x
            bala_disparada.rect.y = enemigo.rect_boca.y
            bala_disparada.bandera_disp = True
            bala_disparada.direccion_disp = enemigo.direction
            enemigo.balas_usadas.append(bala_disparada)
            self.lista_balas_usadas.append(bala_disparada)
            sound.play_sound(ROOT + "Sonidos\\Piu.wav")
            
            #print("Disparo")
        else:
            enemigo.bandera_para_disparar = False       


    def eventos(self,lista_de_enemigos,jugador,delta_ms):
        '''
        detecta las colisiones para el movimiento automatico del enemigo

        lista_enemigos = lista de enemigos utilizado
        player  = jugador con el que colisionas los rectangulos
        '''
        for enemigo in lista_de_enemigos:
            if enemigo.poder_disparar:
                if enemigo.rect_disparo_r.colliderect(jugador.rect_cuerpo) or enemigo.rect_disparo_l.colliderect(jugador.rect_cuerpo):
                    enemigo.bandera_para_disparar = True
                    enemigo.bandera_quedarse_quieto = True
                    

    def kill(self,jugador,delta_ms):
        '''
        cuando la bala disparada colisiona con el jugador, se elimina la bala y le resta una vida al jugador
       
        jugador  = jugador al cual se le resta una vida
        delta_ms = tiempo para medir el tiempo estipulado
        '''
        for bala in self.lista_balas_usadas:
            if bala.rect_colide.colliderect(jugador.rect_cuerpo):
                self.tiempo_acumulado += delta_ms # arrelgar esto
                if self.tiempo_acumulado > 1800:
                    self.tiempo_acumulado = 0
                    self.lista_balas_usadas.remove(bala)
                    jugador.vidas -= 1
            else:
                self.lista_balas_usadas.remove(bala)