from .constants import WINDOW_SIZE
import pygame


# 1000 640

class Stats:
    def __init__(self):

        #Position Text Sonar
        self.posXSonarText = 130
        self.posYSonarText = 540
        #position nbrSub Text
        self.nbrSubX = 130
        self.nbrSubY = 520
        #Position nbr Gen text
        self.posXGenText = 130
        self.posYGenText = 500


        self.green = (0,255,0) #Couleur du texte

        self.font = pygame.font.Font('freesansbold.ttf', 20)




        
        
    def draw(self,screen, terrain):

        self.nbrSubText = self.font.render("Sub_Number = " + str(terrain.nbrSubCreated), True, self.green)
        self.nbrSubTextRect = self.nbrSubText.get_rect()
        self.nbrSubTextRect.topleft = (self.nbrSubX, self.nbrSubY)
        screen.blit(self.nbrSubText, self.nbrSubTextRect)

        self.sonarText = self.font.render("Ray_Sonar = " + str(terrain.tabSub[0].sonarRadius), True, self.green)
        self.sonarTextRect = self.sonarText.get_rect()
        self.sonarTextRect.topleft = (self.posXSonarText, self.posYSonarText)
        screen.blit(self.sonarText, self.sonarTextRect)

        self.nbrGenText = self.font.render("Gen Number = **To be edited", True, self.green)
        self.nbrGenTextRect = self.nbrGenText.get_rect()
        self.nbrGenTextRect.topleft = (self.posXGenText,self.posYGenText)
        screen.blit(self.nbrGenText,self.nbrGenTextRect)
