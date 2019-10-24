import pymunk
import pymunk.pygame_util
from .constants import WINDOW_SIZE

class Propulsor:
    def __init__(self, position, force, angle = 0):
        self.position = pymunk.Vec2d(position)
        self.force = pymunk.Vec2d(force)
        self.force.rotate(angle)

class Submarine:
    def __init__(self, physicsSpace, position,sonarSize,subSize,forceX,forceY, isAlive):
        x, y = position
        self.size = subSize
        self.isAlive = isAlive
        self.physicsSpace = physicsSpace

        self.leftPropulsor = Propulsor((0, 0), (forceX, 0), 0)
        self.bottomPropulsor = Propulsor((int(self.size + self.size / 2), -self.size), (0, forceY), 0)

        self.sonarRadius = sonarSize
        self.sonarOffset = (self.size + self.size / 2, 0)

        self.setPosition((x, y))
       

    def getScreenPosition(self):
        poly_center = tuple(map(sum, zip(self.position, self.sonarOffset)))
        
        return self.physicsPolygon.body.local_to_world(poly_center)
  

    def setVertices(self, vertices):
        self.polygonVertices = vertices
        body = pymunk.Body(10, pymunk.moment_for_poly(10, vertices), body_type=pymunk.Body.DYNAMIC)
        body.density = 3
        body.position = self.size * 2 + self.size / 2, 0

        body.apply_force_at_local_point((0, 0), (body.position[0], body.position[1] - self.size))

        body.apply_force_at_local_point(self.leftPropulsor.force, self.leftPropulsor.position)

        body.apply_force_at_local_point(self.bottomPropulsor.force, self.bottomPropulsor.position)

        self.physicsPolygon = pymunk.Poly(body, self.polygonVertices, None, 1)
        
        self.sonarBody = pymunk.Body(0, 0, body_type=pymunk.Body.DYNAMIC)
        self.sonarBody.position = self.getScreenPosition()
        self.sonar = pymunk.Circle(self.sonarBody, self.sonarRadius, self.sonarOffset)
        self.sonar.filter = pymunk.ShapeFilter(categories = 1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)

        self.physicsPolygon.filter = pymunk.ShapeFilter(categories=1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)
        self.physicsSpace.add(body, self.physicsPolygon, self.sonar)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        self.setVertices(self.polygonVertices)
