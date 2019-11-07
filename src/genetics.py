import time
from .submarine import Submarine
from .terrain import Terrain


def elapsedTime(start):
    now = time.time()
    return now - start

def step():
    
    mini = Terrain.tabSub[0].lifetime
    maxi = Terrain.tabSub[0].lifetime

    for sub in Terrain.tabSub:
        if mini > sub.lifetime:
            mini = sub.lifetime
        elif maxi < sub.lifetime:
            maxi = sub.lifetime
    
    step = mini + (maxi - mini)*0.80
    return step
