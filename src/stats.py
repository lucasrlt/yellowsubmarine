from .constants import WINDOW_SIZE
import pygame


# 1000 640

class Stats:
    def __init__(self, terrain):
        self.posX = 100
        self.posY = 500
        self.green = (0,255,0) #Couleur du texte

        self.font = pygame.font.Font('freesansbold.ttf', 20)



        self.text = self.font.render('Bonjour je suis une fougère', True, self.green)

        self.textRect = self.text.get_rect()
        self.textRect.topleft = (self.posX, self.posY) #Position du texte
        
    def draw(self,screen):
        screen.blit(self.text, self.textRect)
