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
        body.density = 3
        body.position = self.size * 2 + self.size / 2, 0
        
        self.physicsPolygon = pymunk.Poly(body, self.polygonVertices, None, 1)
        self.physicsSpace.add(body, self.physicsPolygon)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        self.setVertices(self.polygonVertices)

    def getScreenPosition(self):
        poly_center = tuple(map(sum, zip(self.position, self.sonarOffset)))
        
        return self.physicsPolygon.body.local_to_world(poly_center)