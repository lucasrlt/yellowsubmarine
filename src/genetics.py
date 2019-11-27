import time
import random
import bisect
from .submarine import Submarine
from .terrain import Terrain
from .constants import WINDOW_SIZE, GEN_SIZE, CHANCE_MUT, EXP


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
    rangMut = 0.15
    if mut < CHANCE_MUT:

        return random.randint(min - int(min*rangMut), max + int(max*rangMut))

    else:

        return random.randint(min, max)

def sortTab(tabSub):
    for i in range(1, GEN_SIZE):
        temp = tabSub[i]
        j = i
        while j > 0 and temp.distance < tabSub[j-1].distance:
            tabSub[j]=tabSub[j-1]
            j-=1
        tabSub[j]=temp
    return tabSub

def newGen(terrain):

    tempTab = terrain.tabSub
    tempTab = sortTab(tempTab)
    distrib = [x.distance for x in tempTab]
    dMin = distrib[0]
    dMax = distrib[-1]
    distrib = [pow((x-dMin)/(dMin - dMax), EXP) for x in distrib]
    
    for i in range(1, GEN_SIZE-1):
        distrib[i] = distrib[i] + distrib[i-1]


    isAlive = True
    distance = -1
    tab  = []
#    j = GEN_SIZE-1

    for j in range(int(GEN_SIZE/2)):
        val0 = random.uniform(0, distrib[-1])
        i0 = bisect.bisect_right(distrib, val0) - 1
        val1 = random.uniform(0, distrib[-1])
        i1 = bisect.bisect_right(distrib, val1) - 1
        
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)        
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),tempTab[i0].sonarRadius,tempTab[i1].size,tempTab[i0].forceX,tempTab[i1].forceY,isAlive,(randR,randG,randB,255), distance))
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),tempTab[i1].sonarRadius,tempTab[i0].size,tempTab[i1].forceX,tempTab[i0].forceY,isAlive,(randR,randG,randB,255), distance))


    step = stepPos(terrain)
    miniSonar, maxiSonar = getMinMax("sonarRadius", terrain, step)
    miniSize, maxiSize = getMinMax("size", terrain, step)
    miniForceX, maxiForceX = getMinMax("forceX", terrain, step)
    miniForceY, maxiForceY = getMinMax("forceY", terrain, step)

    for i in range(int(GEN_SIZE/2)):
        sonar = mut(miniSonar, maxiSonar)
        size = mut(miniSize, maxiSize)
        forceX = mut(miniForceX, maxiForceX)
        forceY = mut(miniForceY, maxiForceY)
        
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255), distance))
    
    return tab