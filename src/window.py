from .constants import WINDOW_SIZE
import pygame
import pymunk
import pymunk.pygame_util
import random
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

    def refresh(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        self.terrain.space.debug_draw(self.draw_options)
        self.terrain.update(120)
        self.stats.draw(self.screen,self.terrain)

    def draw1(self):
        self.terrain.submarine.sonar.color = pygame.color.THECOLORS["pink"]
        #sonarX, sonarY = self.terrain.submarine.getScreenPosition()
        #pygame.draw.circle(self.screen, (255,0,0), (int(sonarX), int(sonarY)), self.terrain.submarine.sonarRadius, 1)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True