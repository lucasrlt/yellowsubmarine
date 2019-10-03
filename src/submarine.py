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
        body = pymunk.Body(1, pymunk.moment_for_poly(10, vertices))
        body.position = pymunk.Vec2d(0, 0)
        body.friction = 1.0
        self.physicsPolygon = pymunk.Poly(body, self.polygonVertices, None, 0)
        self.physicsSpace.add(body, self.physicsPolygon)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        # print(self.polygonVertices[3])
        self.setVertices(self.polygonVertices)