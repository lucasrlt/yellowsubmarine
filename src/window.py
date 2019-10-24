from .constants import WINDOW_SIZE
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
        propulsor = self.terrain.submarine.leftPropulsor
        fLen = 20
        x = self.terrain.submarine.getScreenPosition().x - self.terrain.submarine.size - (propulsor.position[0] + math.cos(propulsor.force.angle) * fLen)
        y = self.terrain.submarine.getScreenPosition().y - self.terrain.submarine.size + (propulsor.position[1] + math.sin(propulsor.force.angle) * fLen)

        propulsor2 = self.terrain.submarine.bottomPropulsor
        x2 = self.terrain.submarine.getScreenPosition().x - self.terrain.submarine.size - (propulsor.position[0] + math.cos(propulsor2.force.angle) * fLen)
        y2 = self.terrain.submarine.getScreenPosition().y + self.terrain.submarine.size + (propulsor.position[1] + math.sin(propulsor2.force.angle) * fLen)


        self.draw_arrow(self.screen, (255, 0, 0), (x,y),  (self.terrain.submarine.getScreenPosition().x - self.terrain.submarine.size, self.terrain.submarine.getScreenPosition().y - self.terrain.submarine.size))
        self.draw_arrow(self.screen, (255, 0, 0), (x2,y2),  (self.terrain.submarine.getScreenPosition().x, self.terrain.submarine.getScreenPosition().y + self.terrain.submarine.size))


    def refresh(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.terrain.space.debug_draw(self.draw_options)
        self.terrain.update(120)
        self.stats.draw(self.screen,self.terrain)
        self.drawForces()

#    def draw1(self):
        #self.terrain.submarine.sonar.color = pygame.color.THECOLORS["pink"]
        #sonarX, sonarY = self.terrain.submarine.getScreenPosition()
        #pygame.draw.circle(self.screen, (255,0,0), (int(sonarX), int(sonarY)), self.terrain.submarine.sonarRadius, 1)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True