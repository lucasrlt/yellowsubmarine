import time
from .submarine import Submarine
from .terrain import Terrain


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


def newGen(terrain):
    if elapsedTime(terrain) > (terrain.geneTime * (terrain.gene +1)):
        step = stepPos(terrain)
        minMaxSonar = sonarMinMax(terrain, step)
        minMaxSize = sizeMinMax(terrain, step)
        minMaxForceX = forceXMinMax(terrain, step)
        minMaxForceY = forceYMinMax(terrain, step)



      
    