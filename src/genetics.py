import time
import random
from .submarine import Submarine
from .terrain import Terrain
from .constants import WINDOW_SIZE, GEN_SIZE, CHANCE_MUT


def elapsedTime(start):
    now = time.time()
    return now - start

def stepLifeTime(terrain):
    
    mini = terrain.tabSub[0].lifetime
    maxi = terrain.tabSub[0].lifetime

    for sub in terrain.tabSub:
        if mini > sub.lifetime:
            mini = sub.lifetime
        elif maxi < sub.lifetime:
            maxi = sub.lifetime
    
    stepLifeTime = mini + (maxi - mini)*0.80
    return stepLifeTime

def stepPos(terrain):

    mini = terrain.tabSub[0].getScreenPosition()
    maxi = terrain.tabSub[0].getScreenPosition()

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        if mini[0] > temp[0]:
            mini[0] = temp[0]
        elif maxi[0] < temp[0]:
            maxi[0] = temp[0]
    
    stepPos = mini[0] + (maxi[0] - mini[0])*0.85
    return stepPos

def getMinMax(attr, terrain, step):
    mini = 1000
    maxi = 0

    for sub in terrain.tabSub:
        subPos = sub.getScreenPosition()
        if subPos.x >= step:
            if getattr(sub, attr) < mini:
                mini = getattr(sub, attr)
            if getattr(sub, attr) > maxi:
                maxi = getattr(sub, attr)

    return mini, maxi


def mut(mutMin, mutMax, min, max):
 
    mut = random.randint(0, 100)
    if mut % CHANCE_MUT:

        return random.randint(mutMin, mutMax)

    else:

        return random.randint(min, max)

def newGen(terrain):
    step = stepPos(terrain)
    miniSonar, maxiSonar = getMinMax("sonarRadius", terrain, step)
    miniSize, maxiSize = getMinMax("size", terrain, step)
    miniForceX, maxiForceX = getMinMax("forceX", terrain, step)
    miniForceY, maxiForceY = getMinMax("forceY", terrain, step)
    isAlive = True
    tab  = []
    

    for i in range(GEN_SIZE):
        sonar = mut(2, 250, miniSonar, maxiSonar)
        size = mut(5, 30, miniSize, maxiSize)
        forceX = mut(-100000, 100000, miniForceX, maxiForceX)
        forceY = mut(-50000, 50000, miniForceY, maxiForceY)
        
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255)))
    
    return tab