import time
import random
import bisect
from .submarine import Submarine
from .terrain import Terrain
from .constants import WINDOW_SIZE, GEN_SIZE, CHANCE_MUT, EXP, PROPORTION, NB_CHILD


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

"""
Returns sorted tabSub acording to sub's position.
"""
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
    distrib = [x.distance for x in tempTab] # fitness
  
    dMin = distrib[0]
    dMax = distrib[-1]

    print("Meilleur sous marin: [" + str(tempTab[-1].sonarRadius) + ", " + str(tempTab[-1].size) + ", " + str(tempTab[-1].forceX) + ", " + str(tempTab[-1].forceY) + "]")

    # Normalisation des données, les plus forts ont plus de chance d'être choisi si EXP augmente. 
    distrib = [pow((x-dMin)/(dMax - dMin), EXP) for x in distrib]
    
    # Effectif cumulé croissant, on cumule les % de chance d'être choisi pour chaque élément
    # %x = SUM(%y <= x)
    for i in range(1, GEN_SIZE):
        distrib[i] = distrib[i] + distrib[i-1]

    # print(distrib)
    isAlive = True
    distance = -1
    tab  = []
#    j = GEN_SIZE-1

    
        
    # Offspring
    while len(tab) < (int(GEN_SIZE * PROPORTION)): # 90% de la pop update par croisement
        val0 = random.uniform(0, distrib[-1])
        i0 = bisect.bisect_right(distrib, val0)
        val1 = random.uniform(0, distrib[-1])
        i1 = bisect.bisect_right(distrib, val1)
        for e in range(NB_CHILD):

            randR = random.randint(0,255)
            randG = random.randint(0,255)
            randB = random.randint(0,255)        
            
            sonar = tempTab[i0].sonarRadius if random.randint(0,1) else tempTab[i1].sonarRadius
            size = tempTab[i0].size if random.randint(0,1) else tempTab[i1].size
            forceX = tempTab[i0].forceX if random.randint(0,1) else tempTab[i1].forceX
            forceY = tempTab[i0].forceY if random.randint(0,1) else tempTab[i1].forceY

            tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255), distance))

    # Mutation
    while len(tab) < GEN_SIZE:
        sonar = mut(2, 200)
        size = mut(10, 20)
        forceX = mut(-100000, 100000)
        forceY = mut(-50000, 50000)
        
        randR = random.randint(0,255)
        randG = random.randint(0,255)
        randB = random.randint(0,255)
        tab.append(Submarine(terrain.space, (150, (int(WINDOW_SIZE[1] / 2))- 50),sonar,size,forceX,forceY,isAlive,(randR,randG,randB,255), distance))
    
    return tab