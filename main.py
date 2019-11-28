from src.constants import WINDOW_SIZE, NO_WINDOW
from src.window import *
from src.console import *
from src.genetics import *
import time

if __name__ == "__main__":
    win = Console() if NO_WINDOW else Window()
    start = time.time()
    play = True

    if NO_WINDOW:
        print("DEBUT DE LA SIMULATION")
        print("BATCH SIZE: ", GEN_SIZE)

    while(play):
        win.refresh()

        if win.terrain.nbrSubCreated == 0 or time.time() - start >= 10:
            start = time.time()
            win.terrain.gene += 1

            if NO_WINDOW:
                win.print_gen_info()

            newTabSub = newGen(win.terrain)
            win.terrain.tabSub = newTabSub
            win.terrain.nbrWinner = 0
            win.terrain.nbrSubCreated = len(newTabSub)

        if not NO_WINDOW:
            play = win.close()
        continue
