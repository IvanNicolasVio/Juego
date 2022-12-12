import pygame
from constantes import *
from pygame import mixer


class Sound():
    def __init__(self) -> None:
        mixer.init()
        self.sonidos_on_off = True
        self.musica_on_off = True
    
    def play_sound(self,path):
        sound = pygame.mixer.Sound(path)
        if self.sonidos_on_off:
            sound.set_volume(0.2)
            sound.play()

    def play_music(self,path):
        sound = pygame.mixer.Sound(path)
        if self.musica_on_off:
            sound.set_volume(0.1)
            sound.play()
        return sound
        

    def stop_music(self,sound):
        if self.musica_on_off:
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
            print("ahora el sonido es falso")
        elif not self.musica_on_off:
            self.musica_on_off = True
            print("ahora el sonido es verdadero")