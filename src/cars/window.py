import pygame
import pymunk
import pymunk.pygame_util
from .terrain import Terrain


class Window:
    def __init__(self):
        pygame.init()
        self.camera = pygame.Vector2((0, 0))
        self.screen = pygame.display.set_mode((800, 640))
        self.pymunk_layer = pygame.Surface((3000, 640))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.pymunk_layer)
        pymunk.pygame_util.positive_y_is_up = False
        self.terrain = Terrain()
        self.clock = pygame.time.Clock()

    def update(self):
        max_car_pos = 0
        for car in self.terrain.cars:
            if car.get_position().x > max_car_pos:
                max_car_pos = car.get_position().x

        self.camera = pygame.Vector2((-max_car_pos + 200, 0))
        self.terrain.update()
        self.terrain.space.debug_draw(self.draw_options)
        self.screen.blit(self.pymunk_layer, self.camera)
        pygame.display.flip()
        self.pymunk_layer.fill((0, 0, 0))
        self.screen.fill((0, 0, 0))
        self.clock.tick(60)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
