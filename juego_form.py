import pygame
from pygame.locals import *
from juego_widget import Widget
from juego_boton import *
from juego_constantes import *
from juego_text_box import *
from juego_sqlite import *

class Form():
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox
    '''
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.nivel = nivel
        if image_background != None:
            self.image_background = pygame.image.load(image_background)
            self.image_background = pygame.transform.scale(self.image_background,(w, h)).convert_alpha()
        else:
            self.image_background = None

        self.surface = self.image_background
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        # if(self.color_background != None):
        #     self.surface.fill(self.color_background)
    
    def set_active(self,name):
        '''
        minimiza el form donde se encuentra y abre otro en su lugar

        name: nombre del form a abrir
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True
        

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,master_surface,x,y,w,h,color_background,color_border,active,image_background):
        super().__init__(master_surface,x,y,w,h,color_background,color_border,active,image_background)
        
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
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)

        self.boton1 = Button_v2(master=self,x=110,y=150,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="OPCIONES",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_opciones")
        self.boton2 = Button_v2(master=self,x=110,y=250,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="SCORE",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_score")
        self.boton3 = Button_v2(master=self,x=110,y=350,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="NIVEL 1",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton2,on_click_param="")
        self.boton4 = Button_v2(master=self,x=110,y=450,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="NIVEL 2",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton3,on_click_param="")
        self.boton5 = Button_v2(master=self,x=110,y=550,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="NIVEL 3",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton4,on_click_param="")

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]
        self.bandera_nivel = True

    def on_click_boton1(self, parametro):
        '''
        minimiza el form donde se encuentra y abre otro en su lugar

        parametro: nombre del form a abrir
        '''
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
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,sound,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)
        self.sound = sound

        self.boton1 = Button_v2(master=self,x=50,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MENU",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_principal")
        self.boton2 = Button_v3(master=self,x=50,y=150,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="SONIDO",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton2,on_click_param="")
        self.boton3 = Button_v3(master=self,x=50,y=250,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MUSICA",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton4,on_click_param="")
        self.lista_widget = [self.boton1,self.boton2,self.boton3]
        
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self,parametro):#fix
        self.sound.on_off_sound(parametro)

    def on_click_boton4(self,parametro):
        self.sound.on_off_music(parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        if self.sound.sonidos_on_off == True:
            self.boton2.on_off = True
            self.boton2._text = "SOUND ON"
        elif self.sound.sonidos_on_off == False:
            self.boton2.on_off = False
            self.boton2._text = "SOUND OFF"

        if self.sound.musica_on_off == True:
            self.boton3.on_off = True
            self.boton3._text = "MUSIC ON"
        elif self.sound.musica_on_off == False:
            self.boton3.on_off = False
            self.boton3._text = "MUSIC OFF"

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class MenuOpcionesInGame(Form):
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,sound,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)

        self.sound = sound
        self.boton1 = Button_v2(master=self,x=50,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MENU",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_principal")
        self.boton2 = Button_v3(master=self,x=50,y=250,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="SONIDO",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton2,on_click_param="")
        self.boton3 = Button_v2(master=self,x=50,y=150,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="REANUDAR",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton3,on_click_param="")
        self.boton4 = Button_v3(master=self,x=50,y=350,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MUSICA",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton4,on_click_param="")
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]
        
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self,parametro):
        self.sound.on_off_sound(parametro)

    def on_click_boton3(self, parametro):
        for aux_form in self.forms_dict.values():
            aux_form.active = False

    def on_click_boton4(self,parametro):
        self.sound.on_off_music(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        if self.sound.sonidos_on_off == True:
            self.boton2.on_off = True
            self.boton2._text = "SOUND ON"
        elif self.sound.sonidos_on_off == False:
            self.boton2.on_off = False
            self.boton2._text = "SOUND OFF"

        if self.sound.musica_on_off == True:
            self.boton4.on_off = True
            self.boton4._text = "MUSIC ON"
        elif self.sound.musica_on_off == False:
            self.boton4.on_off = False
            self.boton4._text = "MUSIC OFF"

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

class MenuPerder(Form):
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)
        self.boton1 = Button_v2(master=self,x=50,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MENU",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_principal")
        self.boton2 = Button_v2(master=self,x=50,y=250,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="INGRESAR",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton2,on_click_param="")
        self.text_box = TextBox(master=self,x=50,y=150,w=200,h=50,color_background=None,color_border=None,image_background=ROOT + "images\\images\\gui\\set_gui_01\\Comic_Border\\Buttons\\Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=BLACK,nombre=None)
        
        self.nombre = self.text_box.nombre
        self.bandera_ingresar_nombre = False
        self.lista_widget = [self.boton1,self.text_box,self.boton2]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        if not self.boton2.bandera_para_bloquear:
            self.bandera_ingresar_nombre = True
            self.boton2.bandera_para_bloquear = True
            self.boton2._text = "INGRESADO"
    
    def reiniciar_boton(self):
        self.boton2._text = "INGRESAR"
        self.boton2.bandera_para_bloquear = False
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
    

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:  
            aux_boton.draw()


class MenuScore(Form):
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)
        self.lista_score = []
        self.boton1 = Button_v2(master=self,x=50,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MENU",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_principal")
        self.lista_widget = [self.boton1]
        self.master_surface = master_surface
        self.contador = 0
        self.posicion_y = 0

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()

    def mostrar_nombre(self):
        self.lista_score = ordenar_score()
        self.contador = 1
        self.posicion_y = 150
        for i in range(7):
            fuente = pygame.font.SysFont("Arial",50)
            texto = fuente.render("{0}: {1} ".format(self.contador,self.lista_score[i][0]),True,(0,0,0))
            self.master_surface.blit(texto,(230,self.posicion_y))
            self.contador += 1
            self.posicion_y += 85 

    def mostrar_score(self):
        self.lista_score = ordenar_score()
        self.posicion_y = 150
        for i in range(7):
            fuente = pygame.font.SysFont("Arial",50)
            texto = fuente.render(" Score: {0} ".format(self.lista_score[i][1]),True,(0,0,0))
            self.master_surface.blit(texto,(600,self.posicion_y))
            self.posicion_y += 85 

    def mostrar_nivel(self):
        self.lista_score = ordenar_score()
        self.posicion_y = 150
        for i in range(7):
            fuente = pygame.font.SysFont("Arial",50)
            texto = fuente.render(" {0} ".format(self.lista_score[i][2]),True,(0,0,0))
            self.master_surface.blit(texto,(1020,self.posicion_y))
            self.posicion_y += 85 


class MenuPausa(Form):
    '''
    la clase form es utilizada para desplazarse entre unos y otros, contiene botones y textbox

    hereda la clase Form
    '''
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active,nivel,image_background)

        self.boton1 = Button_v2(master=self,x=50,y=50,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="OPCIONES",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="opciones_in_game")
        self.boton2 = Button_v2(master=self,x=50,y=150,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="MENU",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="menu_principal")
        self.boton3 = Button_v2(master=self,x=50,y=250,w=200,h=50,color_background=None,color_border=None,image_background="images\\images\\gui\\jungle\\bubble\\bgload.png",text="REGRESAR",font="Verdana",font_size=30,font_color=WHITE,on_click=self.on_click_boton2,on_click_param="")
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