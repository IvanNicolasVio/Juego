import pygame
from juego_constantes import *
from pygame import mixer


class Sound():
    def __init__(self,path) -> None:
        mixer.init()
        self.sonidos_on_off = True
        self.musica_on_off = True
        self.cancion = pygame.mixer.Sound(path)
    
    def play_sound(self,path):
        sound = pygame.mixer.Sound(path)
        if self.sonidos_on_off:
            sound.set_volume(0.2)
            sound.play()

    def play_music(self,sound):
        if self.musica_on_off:
            sound.set_volume(0.1)
            sound.play()
        
        

    def stop_music(self,sound):
        sound.stop()
            
    def on_off_sound(self,parametro):
        if self.sonidos_on_off:
            self.sonidos_on_off = False
            print("ahora el sonido es falso")
        elif not self.sonidos_on_off:
            self.sonidos_on_off = True
            print("ahora el sonido es verdadero")
    
    def on_off_music(self,parametro):
        if self.musica_on_off:
            self.musica_on_off = False
            self.cancion.stop()
            print("ahora el sonido es falso")
        elif not self.musica_on_off:
            self.musica_on_off = True
            self.cancion.play()
            print("ahora el sonido es verdadero")