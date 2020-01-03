import pygame
import pymunk


## Classe sonar générant le sonar du sous marin
## Param : Radius : Int
##         tupleOffSet : Tuple d'int
class Sonar:
    def __init__(self, radius, tupleOffSet):
        self.radius = radius
        self.offSet = tupleOffSet
        