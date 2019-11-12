import time
import random
from .submarine import Submarine
from .terrain import Terrain
from .constants import WINDOW_SIZE


def elapsedTime(terrain):
    now = time.time()
    return now - terrain.start

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

    mini = terrain.tabSub[0].getPosition()
    maxi = terrain.tabSub[0].getPosition()

    for sub in terrain.tabSub:
        if mini > sub.getPosition():
            mini = sub.getPosition()
        elif maxi < sub.getPosition():
            maxi = sub.getPosition()
    
    stepPos = mini + (maxi - mini)*0.80
    return stepPos

def sonarMinMax(terrain, step):
    minMax(500, 0)

    for sub in terrain.tabSub:
        if sub.getPosition() >= step:
            if sub.sonarRadius < minMax[1]:
                minMax[1] = sub.sonarRadius
            elif sub.sonarRadius > minMax[2]:
                minMax[2] = sub.sonarRadius

    return minMax
    
def sizeMinMax(terrain, step):
    minMax(500, 0)

    for sub in terrain.tabSub:
        if sub.getPosition() >= step:
            if sub.size < minMax[1]:
                minMax[1] = sub.size
            elif sub.size > minMax[2]:
                minMax[2] = sub.size
    
    return minMax

def forceXMinMax(terrain, step):
    minMax(500, 0)

    for sub in terrain.tabSub:
        if sub.getPosition() >= step:
            if sub.forceX < minMax[1]:
                minMax[1] = sub.forceX
            elif sub.forceX > minMax[2]:
                minMax[2] = sub.forceX
    
    return minMax

def forceYMinMax(terrain, step):
    minMax(500, 0)

    for sub in terrain.tabSub:
        if sub.getPosition() >= step:
            if sub.forceY < minMax[1]:
                minMax[1] = sub.forceY
            elif sub.forceY > minMax[2]:
                minMax[2] = sub.forceY
    
    return minMax

def endGene(terrain):
    deadSub = 0
    for sub in terrain.tabSub:
        if sub.isAlive == False:
            deadSub += 1
        else:
            return 0
    
    if((deadSub == 10) or (elapsedTime(terrain) % (terrain.geneTime * (terrain.gene + 1)))  > terrain.geneTime):
        return 1 



def newGen(space, terrain):

    step = stepPos(terrain)
    minMaxSonar = sonarMinMax(terrain, step)
    minMaxSize = sizeMinMax(terrain, step)
    minMaxForceX = forceXMinMax(terrain, step)
    minMaxForceY = forceYMinMax(terrain, step)
    isAlive = True
    tab  = []
    
    for i in range(10):
        sonar = random.randint(minMaxSonar[0], minMaxSonar[1])
        size = random.randint(minMaxSize[0], minMaxSize[1])
        forceX = random.randint(minMaxForceX[0], minMaxForceX[1])
        forceY = random.randint(minMaxForceY[0], minMaxForceY[1])
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255)))
    
    return tab


      
    