import pygame
import pymunk
import pymunk.pygame_util
from .submarine import Submarine
from .constants import DEBUG, WINDOW_SIZE
# 1000 640

class Terrain:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, 100
        pymunk.pygame_util.positive_y_is_up = False

        self.clock = pygame.time.Clock()    
        
        # Tableaux de points pour les lignes / cubes sur le terrain
        self.verticesBottomList = [(0,600),(100,550),(110,540),(150,400),(200,460),(225,480),(250,430),(400,620),(500,550),(550,485),(550,500),(600,500),(800,450),(875,600),(950,350),(1000,500)]
        self.verticesTopList = [(0,100),(150,150),(200,125),(225,75),(275,50),(350,100),(450,150),(550,175),(650,200),(750,200),(850,150),(900,100),(950,175),(1000,175)]
        self.verticesBoxList = [(300,200),(400,325),(600,250),(800,375)]

        if DEBUG:
            print('Bottom vertices list lenght : ' + str(len(self.verticesBottomList)))
            print('Top vertices list lenght : ' + str(len(self.verticesTopList)))
            print('#### Entering Bottom Lines Loop ####')

        for i in range(len(self.verticesBottomList)-1):
            self.bottomLine = pymunk.Segment(self.space.static_body, self.verticesBottomList[i], self.verticesBottomList[i+1], 4)
            self.space.add(self.bottomLine)

        if DEBUG:
            print('## Bottom Lines : DONE ##')
            print('#### Entering Top Lines Loop ####')
        for i in range(len(self.verticesTopList)-1):
            self.topLine = pymunk.Segment(self.space.static_body, self.verticesTopList[i], self.verticesTopList[i+1], 4)
            self.space.add(self.topLine)

        if DEBUG: 
            print('## Top Lines : DONE ##')
            print('### Entering Block Creation Loop ####')

        for i in range(len(self.verticesBoxList)):
            self.boxBody = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.boxBody.position = self.verticesBoxList[i]
            self.box = pymunk.Poly.create_box(self.boxBody,(20,20))
            self.space.add(self.box)
        if DEBUG:
            print('## Box : DONE ##')


        # Affichage d'une grille en DEBUG pour une lecture plus facile des coordonnées (1 ligne tout les 100 pixels)
        if DEBUG:
            for i in range(10):
                self.grid = pymunk.Segment(self.space.static_body, (i*100 ,0), (i*100, 640), 2)
                self.space.add(self.grid)
            for i in range(10):
                self.grid2 = pymunk.Segment(self.space.static_body, (0,i*100), (1000,i*100),2)
                self.space.add(self.grid2)

        self.submarine = Submarine(self.space)
    
    # Mise à jour de l'image
    def update(self, fps):
        self.space.step(1.0/fps)
        self.clock.tick(fps)
<<<<<<< HEAD
    


        
=======
       # print(self.submarine.physicsPolygon.body.position)
>>>>>>> 1f120c55ea5119a8e2729868faeb63f0e0e507ca
