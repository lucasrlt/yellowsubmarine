import pymunk
from .constants import WINDOW_SIZE

class Submarine:
    def __init__(self, physicsSpace):
        x, y = (10, int(WINDOW_SIZE[1] / 2) )
        self.size = 15
        self.physicsSpace = physicsSpace

        self.setPosition((x, y))

        self.sonar = 250

    def setVertices(self, vertices):
        self.polygonVertices = vertices
        self.physicsPolygon = pymunk.Poly(self.physicsSpace.static_body, self.polygonVertices)
        self.physicsSpace.add(self.physicsPolygon)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        self.setVertices(self.polygonVertices)