from src.constants import WINDOW_SIZE
from src.window import *
from src.genetics import *
import time

if __name__ == "__main__":
    win = Window()
    start = time.time()
    play = True
    while(play):
        win.refresh()
        if(( win.terrain.nbrSubCreated == 0) or (elapsedTime(start) % (win.terrain.geneTime * (win.terrain.gene + 1)))  > win.terrain.geneTime):
            win.terrain = Terrain(newGen(win.terrain))
            win.terrain.gene += 1
        
        play = win.close()
        continue
