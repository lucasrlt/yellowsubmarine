import time
from .submarine import Submarine
from .terrain import Terrain


def elapsedTime(start):
    now = time.time()
    return now - start

def stepLifeTime():    
    mini = Terrain.tabSub[0].lifetime
    maxi = Terrain.tabSub[0].lifetime

    for sub in Terrain.tabSub:
        if mini > sub.lifetime:
            mini = sub.lifetime
        elif maxi < sub.lifetime:
            maxi = sub.lifetime
    
    stepLifeTime = mini + (maxi - mini)*0.80
    return stepLifeTime

def stepPos():

    mini = Terrain.tabSub[0].getPosition()
    maxi = Terrain.tabSub[0].getPosition()

    for sub in Terrain.tabSub:
        if mini > sub.getPosition():
            mini = sub.getPosition()
        elif maxi < sub.getPosition():
            maxi = sub.getPosition()
    
    stepPos = mini + (maxi - mini)*0.80
    return stepPos

def newGen():
    
    return True