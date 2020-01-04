from .window import Window
import sys

if __name__ == "__main__":
    win = Window()

    play = True
    while(play):
        win.update()

        play = win.close()
