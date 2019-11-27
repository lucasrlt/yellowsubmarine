import random
from .constants import WINDOW_SIZE, GEN_SIZE
from .submarine import Submarine


def createSub(space):
    tab = []
    for i in range(GEN_SIZE):
        isAlive = True
        sonar = random.randint(2, 200)
        size = random.randint(10, 20)
        forceX = random.randint(-100000, 100000)
        forceY = random.randint(-50000, 50000)
        randR = random.randint(0, 255)
        randG = random.randint(0, 255)
        randB = random.randint(0, 255)
        tab.append(Submarine(space, (150, (int(WINDOW_SIZE[1] / 2)) - 50), sonar, size, forceX, forceY, isAlive, (randR, randG, randB, 255), -1))
    return tab
