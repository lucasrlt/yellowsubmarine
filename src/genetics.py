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
    
    stepLifeTime = mini + (maxi - mini)*0.95
    return stepLifeTime

def stepPos(terrain):

    mini = 20000
    maxi = -20000

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        if mini < temp[0]:
            mini = temp[0]
        elif maxi > temp[0]:
            maxi = temp[0]
    
    stepPos = mini + (maxi - mini)*0.95
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


def mut(min, max):
 
    mut = random.randint(0, 100)
    rangMut = 0.20
    if mut < CHANCE_MUT:

        return random.randint(min - int(min*rangMut), max + int(max*rangMut))

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
        sonar = mut(miniSonar, maxiSonar)
        size = mut(miniSize, maxiSize)
        forceX = mut(miniForceX, maxiForceX)
        forceY = mut(miniForceY, maxiForceY)
        
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255)))
    
    return tab