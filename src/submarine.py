import pymunk
from .constants import WINDOW_SIZE

class Submarine:
    def __init__(self, physicsSpace):
        x, y = (200, int(WINDOW_SIZE[1] / 2))
        self.size = 15
        self.physicsSpace = physicsSpace

        self.setPosition((x, y))

        self.sonarRadius = 50
        self.sonarOffset = (self.size + self.size / 2, 0)

    def setVertices(self, vertices):
        self.polygonVertices = vertices
        body = pymunk.Body(10, pymunk.moment_for_poly(10, vertices), body_type=pymunk.Body.DYNAMIC)
        
        
        self.physicsPolygon = pymunk.Poly(body, self.polygonVertices, None, 1)
        self.physicsSpace.add(body, self.physicsPolygon)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        self.setVertices(self.polygonVertices)

    def getScreenPosition(self):
        return self.position + self.physicsPolygon.body.position + self.sonarOffset