import pygame
import pymunk

class Sonar:
    def __init__(self, radius, tupleOffSet):
        self.radius = radius
        self.offSet = tupleOffSet
        