from .constants import WINDOW_SIZE
import pygame
import pymunk
import pymunk.pygame_util
import random
from .terrain import Terrain

class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.terrain = Terrain()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        pymunk.pygame_util.positive_y_is_up = False

    def refresh(self):
        pygame.display.flip()
        self.terrain.space.debug_draw(self.draw_options)
        self.terrain.update(120)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True