import random
from .constants import WINDOW_SIZE
from .submarine import Submarine


def createSub(space):
    tab = []
    for i in range(20):
        isAlive = True
        sonar = random.randint(0, 200)
        size = random.randint(10, 20)
        forceX = random.randint(25000, 100000)
        forceY = random.randint(-50000, 0)
        randR = random.randint(0, 255)
        randG = random.randint(0, 255)
        randB = random.randint(0, 255)
        tab.append(Submarine(space, (150, (int(
            WINDOW_SIZE[1] / 2)) - 50), sonar, size, forceX, forceY, isAlive, (randR, randG, randB, 255)))
    return tab
