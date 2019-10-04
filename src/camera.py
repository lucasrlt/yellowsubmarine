import pygame
import pymunk
import pymunk.pygame_util
from .submarine import Submarine
from .constants import DEBUG, WINDOW_SIZE
# 1000 640

class Camera:
    def __init__(self):
        self.cameraX = (int(WINDOW_SIZE[0]) / 2) 
        self.cameraY = (int(WINDOW_SIZE[1]) / 2)
        #Position de départ

    def moveRight(self,Submarine):
        if Submarine.Position[0] > (int(WINDOW_SIZE[0] - int(WINDOW_SIZE[0]/3)):
            self.cameraX = self.cameraX + 10;