from src.constants import WINDOW_SIZE
from src.window import *

if __name__ == "__main__":
    win = Window()
    
    play = True
    while(play):
#        win.draw1()
        win.refresh()
        play = win.close()
        continue
