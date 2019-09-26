from src.constants import WINDOW_SIZE
from src.Window import *

if __name__ == "__main__":
    print(WINDOW_SIZE)
    win = Window()

    play = True
    while(play):
        win.draw1()
        win.refresh()
        play = win.close()
        continue