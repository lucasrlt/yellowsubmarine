from .constants import WINDOW_SIZE, GEN_SIZE, NO_WINDOW
from .genetics import *
import pygame


# 1000 640

class Stats:

    def writeLastGen(self, terrain):
        self.dataFile = open("data/lastGen.txt", "w+")
        self.dataFile.write("Stats Last Gen : \n")
        self.dataFile.write("-Sonar \n-Size \n-ForceX \n-ForceY \n")
        for i in range(GEN_SIZE):
            self.dataFile.write("\n" + str(terrain.tabSub[i].sonarRadius))
            self.dataFile.write("\n" + str(terrain.tabSub[i].size))
            self.dataFile.write("\n" + str(terrain.tabSub[i].forceX))
            self.dataFile.write("\n" + str(terrain.tabSub[i].forceY))
            self.dataFile.write(
                "\n" + str(terrain.tabSub[i].sonarOffset[0]) + "\n")

        self.dataFile.close()

    def __init__(self):

        if not(NO_WINDOW):
            # Position Text Sonar
            self.posXNbrWin = 130
            self.posYNbrWin = 540
            # position nbrSub Text
            self.nbrSubX = 130
            self.nbrSubY = 520
            # Position nbr Gen text
            self.posXGenText = 130
            self.posYGenText = 500
            # Position Time
            self.posXTime = 130
            self.posYTime = 560

            self.green = (0, 255, 0)  # Couleur du texte

            self.font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self, screen, terrain):

        self.nbrSubText = self.font.render(
            "Sub_Number = " + str(terrain.nbrSubCreated), True, self.green)
        self.nbrSubTextRect = self.nbrSubText.get_rect()
        self.nbrSubTextRect.topleft = (self.nbrSubX, self.nbrSubY)
        screen.blit(self.nbrSubText, self.nbrSubTextRect)

        self.nbrGenText = self.font.render(
            "Gen Number = " + str(terrain.gene), True, self.green)
        self.nbrGenTextRect = self.nbrGenText.get_rect()
        self.nbrGenTextRect.topleft = (self.posXGenText, self.posYGenText)
        screen.blit(self.nbrGenText, self.nbrGenTextRect)

        self.nbrWinText = self.font.render(
            "Win Number = " + str(terrain.nbrWinner) + "/" + str(GEN_SIZE), True, self.green)
        self.nbrWinTextRect = self.nbrWinText.get_rect()
        self.nbrWinTextRect.topleft = (self.posXNbrWin, self.posYNbrWin)
        screen.blit(self.nbrWinText, self.nbrWinTextRect)

        self.nbrWinText = self.font.render(
            "Time = " + str(int(elapsedTime(terrain.start))), True, self.green)
        self.nbrWinTextRect = self.nbrWinText.get_rect()
        self.nbrWinTextRect.topleft = (self.posXTime, self.posYTime)
        screen.blit(self.nbrWinText, self.nbrWinTextRect)
