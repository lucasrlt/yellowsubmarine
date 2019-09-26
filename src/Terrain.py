import pygame
import pymunk
import pymunk.pygame_util

# 1000 640

class Terrain:
    def __init__(self):
        self.space = pymunk.Space()
        pymunk.pygame_util.positive_y_is_up = False
        
        self.verticesList = [(0,600),(100,550),(110,540),(150,400),(200,460),(225,480),(250,430),(400,640),(500,550),(550,485),(550,500),(600,500),(800,450),(875,600),(950,300),(1000,450)]

    # 16 points
        for i in range(len(self.verticesList)-1):
            self.line = pymunk.Segment(self.space.static_body, self.verticesList[i], self.verticesList[i+1], 4)
            self.space.add(self.line)
            print(i)


Terrain()
