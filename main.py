from src.constants import WINDOW_SIZE
from src.window import *

if __name__ == "__main__":
    print(WINDOW_SIZE)
    win = Window()

    while(1):
        win.draw1()
        win.refresh()
        continue
