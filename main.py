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

        if time.time() - start >= 10:
            for sub in win.terrain.tabSub:
                if sub.isAlive:
                    sub.isAlive = False
                    win.terrain.space.remove(
                        sub.physicsPolygon, sub.sonar, sub.sonar.body, sub.physicsPolygon.body)
                    win.terrain.nbrSubCreated -= 1
                if sub.distance == -1:
                    sub.distance = sub.getScreenPosition()[0]

        if win.terrain.nbrSubCreated == 0:

            start = time.time()
            win.terrain.gene += 1
            win.stats.writeLastGen(win.terrain)

            if NO_WINDOW:
                win.print_gen_info()

            newTabSub = newGen(win.terrain)
            win.terrain.tabSub = newTabSub
            win.terrain.nbrWinner = 0
            win.terrain.nbrSubCreated = len(newTabSub)

        if not NO_WINDOW:
            play = win.close()
        continue
