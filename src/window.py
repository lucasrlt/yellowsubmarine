from .constants import *
import pygame
import pymunk
import pymunk.pygame_util
import random
import math
from .terrain import Terrain
from .stats import Stats


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.terrain = Terrain()
        self.stats = Stats()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        pymunk.pygame_util.positive_y_is_up = False


    def draw_arrow(self, screen, colour, start, end):
        pygame.draw.line(screen,colour,start,end,4)
        rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
        pygame.draw.polygon(screen, (255, 0, 0), ((end[0]+10*math.sin(math.radians(rotation)), end[1]+10*math.cos(math.radians(rotation))), (end[0]+10*math.sin(math.radians(rotation-120)), end[1]+10*math.cos(math.radians(rotation-120))), (end[0]+10*math.sin(math.radians(rotation+120)), end[1]+10*math.cos(math.radians(rotation+120)))))

    def drawForces(self):
        for sub in self.terrain.tabSub:
            propulsor = sub.leftPropulsor
            fLen = 20
            x = sub.getScreenPosition().x - sub.size - (propulsor.position[0] + math.cos(propulsor.force.angle) * fLen)
            y = sub.getScreenPosition().y - sub.size + (propulsor.position[1] + math.sin(propulsor.force.angle) * fLen)

            propulsor2 = sub.bottomPropulsor
            x2 = sub.getScreenPosition().x - sub.size - (propulsor.position[0] + math.cos(propulsor2.force.angle) * fLen)
            y2 = sub.getScreenPosition().y + sub.size + (propulsor.position[1] + math.sin(propulsor2.force.angle) * fLen)


            self.draw_arrow(self.screen, (255, 0, 0), (x,y),  (sub.getScreenPosition().x - sub.size, sub.getScreenPosition().y - sub.size))
            self.draw_arrow(self.screen, (255, 0, 0), (x2,y2),  (sub.getScreenPosition().x, sub.getScreenPosition().y + sub.size))

    def drawLinesBoxes(self):
        for i in range(len(self.terrain.verticesBottomList)-1):
            pygame.draw.line(self.screen,(255,0,0),self.terrain.verticesBottomList[i],self.terrain.verticesBottomList[i+1], 8)
        for i in range(len(self.terrain.verticesTopList)-1):
            pygame.draw.line(self.screen,(255,0,0),self.terrain.verticesTopList[i], self.terrain.verticesTopList[i+1], 8)
        pygame.draw.line(self.screen,(255,0,0),(15,0),(15,640),8)

        for i in range(len(self.terrain.verticesBoxList)):
            pygame.draw.rect(self.screen,(255,0,0),(self.terrain.verticesBoxList[i][0]-10,self.terrain.verticesBoxList[i][1]-10,20,20), 0)

    def drawSubmarines(self):
        verts = []
        for sub in self.terrain.tabSub:
            for v in sub.physicsPolygon.get_vertices():
                x = v.rotated(sub.physicsPolygon.body.angle)[0] + sub.physicsPolygon.body.position[0]
                y = v.rotated(sub.physicsPolygon.body.angle)[1] + sub.physicsPolygon.body.position[1]
                verts.append((x,y))
            if sub.isAlive:
                pygame.draw.polygon(self.screen,sub.color,verts,0)
                pygame.draw.circle(self.screen, sub.color, (int(sub.physicsPolygon.body.position.x + sub.sonarOffset[0]), int(sub.physicsPolygon.body.position.y + sub.sonarOffset[1])),sub.sonarRadius, 1)
            verts = []
    
    
    def refresh(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.terrain.update(120)
        if DEBUG:
            self.terrain.space.debug_draw(self.draw_options)
        else:
            self.drawLinesBoxes()
            self.drawSubmarines()

        self.stats.draw(self.screen,self.terrain)

        #self.drawForces()

#    def draw1(self):
        #self.terrain.submarine.sonar.color = pygame.color.THECOLORS["pink"]
        #sonarX, sonarY = self.terrain.submarine.getScreenPosition()
        #pygame.draw.circle(self.screen, (255,0,0), (int(sonarX), int(sonarY)), self.terrain.submarine.sonarRadius, 1)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True