import random
from .constants import WINDOW_SIZE, GEN_SIZE
from .submarine import Submarine
import sys

# Fonction de création des premiers sous-marins
# Se base sois sur le fichier data/lastGen.txt pour charger une génération déjà sauvegardé si un paramètre de lancement à été fournis
# ou en crée une entièrement nouvelle


def createSub(space):
    tab = []
    if len(sys.argv) != 1:
        dataFile = open("data/lastGen.txt", "r")
        for j in range(7):
            line = dataFile.readline()
            print(line)
        for i in range(GEN_SIZE):
            isAlive = True
            sonar = int(line)
            line = dataFile.readline()
            size = int(line)
            line = dataFile.readline()
            forceX = int(line)
            line = dataFile.readline()
            forceY = int(line)
            line = dataFile.readline()
            sonarOffset = int(line)
            line = dataFile.readline()
            line = dataFile.readline()
            randR = random.randint(0, 255)
            randG = random.randint(0, 255)
            randB = random.randint(0, 255)
            tab.append(Submarine(space, (150, (int(
                WINDOW_SIZE[1] / 2)) - 50), sonar, size, forceX, forceY, isAlive, (randR, randG, randB, 255), -1), sonarOffset)
            print(len(tab))

        dataFile.close()
    else:
        for i in range(GEN_SIZE):
            isAlive = True

            sonar = random.randint(2, 200)
            sonarOffset = random.randint(-20, 20)
            size = random.randint(10, 20)
            forceX = random.randint(-100000, 100000)
            forceY = random.randint(-50000, 50000)

            randR = random.randint(0, 255)
            randG = random.randint(0, 255)
            randB = random.randint(0, 255)
            tab.append(Submarine(space, (150, (int(
                WINDOW_SIZE[1] / 2)) - 50), sonar, size, forceX, forceY, isAlive, (randR, randG, randB, 255), -1, sonarOffset))

    return tab
