import pygame
from constantes import *
from pygame import mixer


class Sound():
    def __init__(self) -> None:
        mixer.init()
        self.player_auch = pygame.mixer.Sound("C:\Users\Iván\Desktop\Juego\Sonidos\AU.m4a")
        self.button_click = pygame.mixer.Sound("C:\Users\Iván\Desktop\Juego\Sonidos\Click.m4a")
        self.enemy_death = pygame.mixer.Sound("C:\Users\Iván\Desktop\Juego\Sonidos\Muerte enemigo.m4a")
        self.player_death = pygame.mixer.Sound("C:\Users\Iván\Desktop\Juego\Sonidos\NOOOO.m4a")
        self.shoot_sound = pygame.mixer.Sound("C:\Users\Iván\Desktop\Juego\Sonidos\Piu.m4a")
    
    