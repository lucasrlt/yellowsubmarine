from .constants import WINDOW_SIZE, GEN_SIZE, NO_WINDOW
import pygame


# Classe de statistiques
# Gère l'affichage des stats à l'écran + Sauvegarde dernière génération
class Stats:

    # Enregistre les valeurs de la dernière génération dans data/lastGen.txt
    def writeLastGen(self, terrain):
        self.dataFile = open("data/lastGen.txt", "w+")
        self.dataFile.write("Stats Last Gen : \n")
        self.dataFile.write("-Sonar \n-Size \n-ForceX \n-ForceY \n")
        for i in range(len(terrain.tabSub)):
            self.dataFile.write("\n" + str(terrain.tabSub[i].sonarRadius))
            self.dataFile.write("\n" + str(terrain.tabSub[i].size))
            self.dataFile.write("\n" + str(terrain.tabSub[i].forceX))
            self.dataFile.write("\n" + str(terrain.tabSub[i].forceY))
            self.dataFile.write(
                "\n" + str(terrain.tabSub[i].sonarOffset[0]) + "\n")

        self.dataFile.close()

    def __init__(self, with_window=True):

        # Initialisation des positions des textes + Couleurs
        if with_window:
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

            self.green = (0, 255, 0)

            self.font = pygame.font.Font('freesansbold.ttf', 20)

    # Affichage à l'écran des textes de statistiques
    def draw(self, screen, terrain, elapsedTime):

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
            "Time = " + str(int(elapsedTime)), True, self.green)
        self.nbrWinTextRect = self.nbrWinText.get_rect()
        self.nbrWinTextRect.topleft = (self.posXTime, self.posYTime)
        screen.blit(self.nbrWinText, self.nbrWinTextRect)
