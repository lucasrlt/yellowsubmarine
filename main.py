from src.constants import WINDOW_SIZE
from src.window import *
from src.genetics import *
import time

if __name__ == "__main__":
    win = Window()
    start = time.time()
    play = True
    while(play):
#        win.draw1()
        win.refresh()
        play = win.close()
        continue
