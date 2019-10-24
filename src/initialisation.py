import random
from .constants import WINDOW_SIZE
from .submarine import Submarine

def createSub(space):
    tab = []
    for i in range(10):
        isAlive = True
        sonar = random.randint(0,200)
        size = random.randint(10,20)
        forceX = random.randint(25000,100000)
        forceY = random.randint(-50000,0)
        tab.append(Submarine(space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive))
    return tab