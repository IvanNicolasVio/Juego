import pygame
from pygame.locals import *
from juego_widget import Widget2
from juego_constantes import *


class TextBox(Widget2):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=BLUE,color_border=L_BLUE,image_background=None,text="Button",font="Arial",font_size=14,font_color=BLACK,on_click=None,on_click_param=None,nombre=None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        self.nombre = nombre
        self.bandera_para_bloquear = False
        self.render()
        
    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(self.writing_flag):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN :
                self.writing_flag = self.slave_rect_collide.collidepoint(evento.pos)
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_RETURN:
                    self.writing_flag = False
                elif evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += evento.unicode
                    self.devolver_nombre()
        self.render()


    def devolver_nombre(self):
        self.nombre = self._text

        return self.nombre