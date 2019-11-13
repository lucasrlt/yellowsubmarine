import time
import random
from .submarine import Submarine
from .terrain import Terrain
from .constants import WINDOW_SIZE


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
    
    stepPos = mini[0] + (maxi[0] - mini[0])*0.50
    return stepPos

def sonarMinMax(terrain, step):
    mini = 500
    maxi = 0

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        
        if temp[0] >= step:
            print(sub.sonarRadius)
            if sub.sonarRadius < mini:
                mini = sub.sonarRadius
            if sub.sonarRadius > maxi:
                maxi = sub.sonarRadius

    return mini, maxi
    
def sizeMinMax(terrain, step):
    mini = 500
    maxi = 0

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        if temp[0] >= step:
            if sub.size < mini:
                mini = sub.size
            if sub.size > maxi:
                maxi = sub.size
    
    return mini, maxi

def forceXMinMax(terrain, step):
    mini = 500
    maxi = 0

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        if temp[0] >= step:
            if sub.forceX < mini:
                mini = sub.forceX
            if sub.forceX > maxi:
                maxi = sub.forceX
    
    return mini, maxi

def forceYMinMax(terrain, step):
    mini = 500
    maxi = 0

    for sub in terrain.tabSub:
        temp = sub.getScreenPosition()
        if temp[0] >= step:
            if sub.forceY < mini:
                mini = sub.forceY
            if sub.forceY > maxi:
                maxi = sub.forceY
    
    return mini, maxi

def newGen(terrain):

    step = stepPos(terrain)
    miniSonar, maxiSonar = sonarMinMax(terrain, step)
    miniSize, maxiSize = sizeMinMax(terrain, step)
    miniForceX, maxiForceX = forceXMinMax(terrain, step)
    miniForceY, maxiForceY = forceYMinMax(terrain, step)
    isAlive = True
    tab  = []
    print(miniSonar, maxiSonar)
    
    for i in range(10):
        sonar = random.randint(miniSonar, maxiSonar)
        size = random.randint(miniSize, maxiSize)
        forceX = random.randint(miniForceX, maxiForceX)
        forceY = random.randint(miniForceY, maxiForceY)
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255)))
    
    return tab


      
    