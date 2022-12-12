from juego_widget import Widget
import pygame
from juego_constantes import *

class Button(Widget):
    '''
    Clase usada como boton donde se le puede poner texto y color
    '''
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.render()
        
    def render(self):
        '''
        dibuja el boton, le pone texto,color, y un collide

        no tiene parametros ni return
        '''
        image_text = self.font_sys.render(self._text,True,self.font_color,self.color_background)
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
        self.slave_surface.fill(self.color_background)
        self.slave_surface.blit(image_text,(5,5))

        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        '''
        ejecuta los collide con la posicion/click del mouse

        lista_eventos : eventos que suceden en pygame 
        '''
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)



        self.render()


class ButtonScreen(Widget):
    '''
    Clase usada como boton donde se le puede poner texto y color, para ser usada in game
    '''
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.render()
        
    def render(self):
        '''
        dibuja el boton, le pone texto,color, y un collide

        no tiene parametros ni return
        '''
        image_text = self.font_sys.render(self._text,True,self.font_color,self.color_background)
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_surface.blit(image_text,(5,5))

        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        '''
        ejecuta los collide con la posicion/click del mouse

        lista_eventos : eventos que suceden en pygame 
        '''
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.slave_rect_collide.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.render()

    def draw(self,screen):
        '''
        dibuja el boton en la pantalla de juego

        screen = pantalla donde se ejecuta el juego
        '''
        screen.blit(self.slave_surface,self.slave_rect)
        
