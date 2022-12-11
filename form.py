import pygame
from pygame.locals import *
from widget import Widget
from boton import Button
from constantes import *
from text_box import *
from banner import Banner


class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.nivel = nivel

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        if(self.color_background != None):
            self.surface.fill(self.color_background)
    
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True
        print((self.forms_dict[name].active))

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    def __init__(self,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=100,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        print("CLICK",parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()



class MenuPrincipal(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel)

        self.boton1 = Button(master=self,x=50,y=50,w=200,h=50,color_background=VIOLET,color_border=L_VIOLET,on_click=self.on_click_boton1,on_click_param="menu_opciones",text="OPCIONES",font="Verdana",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=50,y=150,w=200,h=50,color_background=VIOLET,color_border=L_VIOLET,on_click=self.on_click_boton1,on_click_param="menu_score",text="SCORE",font="Verdana",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=50,y=250,w=200,h=50,color_background=VIOLET,color_border=L_VIOLET,on_click=self.on_click_boton2,on_click_param="form_menu_B",text="NIVEL 1",font="Verdana",font_size=30,font_color=WHITE)
        self.boton4 = Button(master=self,x=50,y=350,w=200,h=50,color_background=VIOLET,color_border=L_VIOLET,on_click=self.on_click_boton3,on_click_param="form_menu_B",text="NIVEL 2",font="Verdana",font_size=30,font_color=WHITE)
        self.boton5 = Button(master=self,x=50,y=450,w=200,h=50,color_background=VIOLET,color_border=L_VIOLET,on_click=self.on_click_boton4,on_click_param="form_menu_B",text="NIVEL 3",font="Verdana",font_size=30,font_color=WHITE)

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]
        self.bandera_nivel = True
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        

    def on_click_boton2(self, parametro):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.nivel = "nivel_1"
        print(self.nivel)
    
    def on_click_boton3(self, parametro):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.nivel = "nivel_2"
        print(self.nivel)

    def on_click_boton4(self, parametro):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.nivel = "nivel_3"
        print(self.nivel)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()


class MenuOpciones(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel)

        self.boton1 = Button(master=self,x=50,y=50,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu_principal",text="MENU PRINCIPAL",font="Verdana",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=50,y=150,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton2,on_click_param="menu_principal",text="SOUND",font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton1,self.boton2]
        
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):#fix
        if sonido:
            sonido = False
            print("ahora el sonido es falso")
        else:
            sonido = True
            print("ahora el sonido es verdadero")
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class MenuPerder(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel)
        self.boton1 = Button(master=self,x=50,y=350,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu_principal",text="MENU PRINCIPAL",font="Verdana",font_size=30,font_color=WHITE)
        self.text_box = TextBox(master=self,x=50,y=250,w=200,h=50,color_background=None,color_border=None,image_background="C:\\Users\\Iván\\Desktop\\Juego\\images\\images\\gui\\set_gui_01\\Comic_Border\\Buttons\\Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=BLACK)
        self.lista_widget = [self.boton1,self.text_box]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

    def mostrar_score(self):
        fuente = pygame.font.SysFont("Arial",100)
        texto = fuente.render("Score: {0}".format(self.player.score),True,(0,0,0))
        self.blit(texto,(50,330))

class MenuScore(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel)

        self.boton1 = Button(master=self,x=51,y=50,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu_principal",text="MENU PRINCIPAL",font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton1]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class MenuPausa(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel)

        self.boton1 = Button(master=self,x=50,y=50,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu_opciones",text="OPCIONES",font="Verdana",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=50,y=150,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="menu_principal",text="MENU PRINCIPAL",font="Verdana",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=50,y=250,w=200,h=50,color_background=BLUE,color_border=(255,0,255),on_click=self.on_click_boton2,on_click_param="menu_principal",text="REGRESAR",font="Verdana",font_size=30,font_color=WHITE)
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        print(parametro)

    def on_click_boton2(self, parametro):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()