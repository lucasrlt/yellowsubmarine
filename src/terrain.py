import pygame
import pymunk
import pymunk.pygame_util
import time
from .initialisation import *
from .submarine import Submarine
from .constants import DEBUG, WINDOW_SIZE
# 1000 640

class Terrain:
    def hit_wall(space, arbiter, a, data):
        submarine_pos = arbiter.shapes[0].body.position
        sub = data["terrain"].find_real_submarine(submarine_pos)   
        sub.isAlive = False 

        data["terrain"].space.remove(sub.physicsPolygon, sub.sonar, sub.sonar.body, sub.physicsPolygon.body)
        data["terrain"].nbrSubCreated -= 1
        return True

    def find_submarine(self, sonar_pos): 
        for sub in self.tabSub:
            if sub.sonar.body.position == sonar_pos:
                return sub
    
    def find_real_submarine(self, pos): 
        for sub in self.tabSub:
            if sub.physicsPolygon.body.position == pos:
                return sub

    def trigger_sonar(space, arbiter, n, data):
        sonar_pos = arbiter.shapes[0].body.position
        obj_pos = arbiter.contact_point_set.points[0].point_a
        
        sub = data["terrain"].find_submarine(sonar_pos)
        if sonar_pos.y > obj_pos.y:
            sub.sonar_detect('up')
        elif sonar_pos.y < obj_pos.y:
            sub.sonar_detect('down')

        return True



    def __init__(self):
        self.space = pymunk.Space()
        self.start = time.time
        self.gene = 0
        self.geneTime = 30
        
        h = self.space.add_collision_handler(4, 6)
        h.data["terrain"] = self
        h.begin = self.hit_wall

        w = self.space.add_collision_handler(5, 6)
        w.data["terrain"] = self
        w.begin = self.trigger_sonar


        self.space.gravity = 0, 10
        pymunk.pygame_util.positive_y_is_up = False

        self.clock = pygame.time.Clock()    
        
        # Tableaux de points pour les lignes / cubes sur le terrain
        self.verticesBottomList = [(0,600),(100,550),(110,540),(150,400),
        (200,460),(225,480),(250,430),(400,620),(500,550),(550,485),
        (550,500),(600,500),(800,450),(875,600),(950,350),(1000,500),(1150,450),(1200,375),(1300,550),(1350,600),(1400,530),(1450,500),(1550,400),
        (1600,375),(1700,375),(1750,350),(1800,400),(1850,500),(1900,550),(2000,550)]
        #30
        self.verticesTopList = [(0,100),(150,150),(200,125),(225,75),(275,50),(350,100),
        (450,150),(550,175),(650,200),(750,200),(850,150),(900,100),(950,175),(1000,175),
        (1100,200),(1200,130),(1300,130),(1350,120),(1500,200),(1600,250),(1650,200),(1700,100),(1750,125),(1800,200),
        (1850,200),(1900,50),(1950,100),(2000,150)]
        #28
        
        self.verticesBoxList = [(300,200),(400,325),(600,250),(800,375)]
        self.nbrSubCreated = 0

        if DEBUG:
            print('Bottom vertices list lenght : ' + str(len(self.verticesBottomList)))
            print('Top vertices list lenght : ' + str(len(self.verticesTopList)))
            print('#### Entering Bottom Lines Loop ####')

        for i in range(len(self.verticesBottomList)-1):
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.bottomLine = pymunk.Segment(self.space.static_body, self.verticesBottomList[i], self.verticesBottomList[i+1], 4)
            self.bottomLine.collision_type = 6

            self.space.add(self.bottomLine)

        if DEBUG:
            print('## Bottom Lines : DONE ##')
            print('#### Entering Top Lines Loop ####')
        for i in range(len(self.verticesTopList)-1):
            self.topLine = pymunk.Segment(self.space.static_body, self.verticesTopList[i], self.verticesTopList[i+1], 4)
            self.topLine.collision_type = 6

            self.space.add(self.topLine)

        if DEBUG: 
            print('## Top Lines : DONE ##')
            print('### Entering Block Creation Loop ####')

        for i in range(len(self.verticesBoxList)):
            self.boxBody = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.boxBody.position = self.verticesBoxList[i]
            self.box = pymunk.Poly.create_box(self.boxBody,(20,20))
            self.box.collision_type = 6
            self.space.add(self.box)
        if DEBUG:
            print('## Box : DONE ##')


        # Affichage d'une grille en DEBUG pour une lecture plus facile des coordonnées (1 ligne tout les 100 pixels)
        if DEBUG:
            for i in range(20):
                self.grid = pymunk.Segment(self.space.static_body, (i*100 ,0), (i*100, 640), 2)
                self.grid.filter = pymunk.ShapeFilter(categories = 1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)

                self.space.add(self.grid)
            for i in range(10):
                self.grid2 = pymunk.Segment(self.space.static_body, (0,i*100), (2000,i*100),2)
                self.grid2.filter = pymunk.ShapeFilter(categories = 1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)
                self.space.add(self.grid2)

        #self.submarine = Submarine(self.space, (150, (int(WINDOW_SIZE[1] / 2))- 50))
        self.tabSub = createSub(self.space)
        
        self.nbrSubCreated = len(self.tabSub)
        #self.secondSub = Submarine(self.space, (150, int(WINDOW_SIZE[1] / 2)))
    
    # Mise à jour de l'image
    def update(self, fps):
        self.space.step(1.0/fps)
        self.clock.tick(fps)

        if self.nbrSubCreated < 0:
            self.nbrSubCreated = 0
        
        for sub in self.tabSub:
            sub.sonar.body.position = sub.getScreenPosition()
        # print(self.submarine.physicsPolygon.body.force)
