import pygame
import pymunk
import pymunk.pygame_util
from constants import DEBUG
# 1000 640

class Terrain:
    def __init__(self):
        self.space = pymunk.Space()
        pymunk.pygame_util.positive_y_is_up = False

        self.clock = pygame.time.Clock()
        
        self.verticesBottomList = [(0,600),(100,550),(110,540),(150,400),(200,460),(225,480),(250,430),(400,640),(500,550),(550,485),(550,500),(600,500),(800,450),(875,600),(950,300),(1000,450)]
        self.verticesTopList = [(0,200),(150,250),(200,225),(225,175),(275,150),(350,200),(450,250),(550,275),(650,300),(750,300),(850,250),(900,200),(950,275),(1000,325)]
        if DEBUG:
            print('Bottom vertices list lenght : ' + str(len(self.verticesBottomList)))
            print('Top vertices list lenght : ' + str(len(self.verticesTopList)))
            print('#### Entering Bottom Lines Loop ####')
        for i in range(len(self.verticesBottomList)-1):
            self.bottomLine = pymunk.Segment(self.space.static_body, self.verticesBottomList[i], self.verticesBottomList[i+1], 4)
            self.space.add(self.bottomLine)
            if DEBUG:
                print('first vertices : ' + str(self.verticesBottomList[i]) + ' second vertices : ' + str(self.verticesBottomList[i+1]))

        if DEBUG:
            print('#### Entering Top Lines Loop ####')
        for i in range(len(self.verticesTopList)-1):
            self.topLine = pymunk.Segment(self.space.static_body, self.verticesTopList[i], self.verticesTopList[i+1], 4)
            self.space.add(self.topLine)
            if DEBUG:
                print('first vertices : ' + str(self.verticesTopList[i]) + ' second vertices : ' + str(self.verticesTopList[i+1]))
    
    def update(self, fps):
        self.space.step(1.0/fps)
        self.clock.tick(fps)


        


Terrain()
