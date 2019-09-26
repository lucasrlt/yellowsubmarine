import pymunk
from .constants import WINDOW_SIZE

class Submarine:
    def __init__(self, physicsSpace):
        x, y = (100, WINDOW_SIZE[1] / 2 )
        self.size = 25
        self.physicsSpace = physicsSpace

        self.setPosition((100, WINDOW_SIZE[1] / 2))

    def setVertices(self, vertices):
        self.polygonVertices = vertices
        self.physicsPolygon = pymunk.Poly(self.physicsSpace.static_body, self.polygonVertices)
        self.physicsSpace.add(self.physicsPolygon)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + 25), (x + 2 * size, y + 25), (x + 3 * size, y), (x + 2 * size, y - 25), (x + size, y - 25)]
        self.setVertices(self.polygonVertices)