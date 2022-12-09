from widget import Widget
import pygame

class Button(Widget):
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color):
        super().__init__(master,x,y,w,h,color_background,color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text
        self.font_sys = pygame.font.SysFont(font,font_size)
        self.font_color = font_color
        self.render()