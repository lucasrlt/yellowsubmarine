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
        
        if win.terrain.nbrSubCreated == 0:
            win.terrain.gene += 1
            newTabSub = newGen(win.terrain)
            win.terrain.tabSub = newTabSub
            win.terrain.nbrWinner = 0
            win.terrain.nbrSubCreated = len(newTabSub)

        play = win.close()
        continue
