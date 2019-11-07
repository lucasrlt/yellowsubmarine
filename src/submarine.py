import pymunk
import pymunk.pygame_util
import math
from .constants import *

class Propulsor:
    def __init__(self, position, force, angle = 0):
        self.position = pymunk.Vec2d(position)
        self.force = pymunk.Vec2d(force)
        self.force.rotate(angle)

class Submarine:
    def __init__(self, physicsSpace, position,sonarSize,subSize,forceX,forceY, isAlive, color):
        x, y = position
        self.size = subSize
        self.isAlive = isAlive
        self.physicsSpace = physicsSpace
        self.color = color
        self.lifetime = -1
        self.distance = -1


        self.forceX = forceX
        self.forceY = forceY

        self.leftPropulsor = Propulsor((0, 0), (forceX, 0), -math.pi / 4)
        self.bottomPropulsor = Propulsor((int(self.size + self.size / 2), -self.size), (0, forceY), math.pi / 8)

        self.sonarRadius = sonarSize
        self.sonarOffset = (self.size + self.size / 2, 0)

        self.setPosition((x, y))
       

    def getScreenPosition(self):
        poly_center = tuple(map(sum, zip(self.position, self.sonarOffset)))
        poly_center = (int(poly_center[0]), int(poly_center[1]))
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
        self.physicsPolygon.color = self.color
        
        sonarBody = pymunk.Body(1, pymunk.moment_for_circle(10, self.sonarRadius - 1, self.sonarRadius))
        sonarBody.position = self.getScreenPosition()
        self.sonar = pymunk.Circle(sonarBody, self.sonarRadius, self.sonarOffset)

        self.sonar.filter = pymunk.ShapeFilter(categories = 1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)
        self.sonar.collision_type = 5

        self.sonar.color = (self.color[0], self.color[1], self.color[2], 1)
        self.physicsPolygon.collision_type = 4

        self.physicsPolygon.filter = pymunk.ShapeFilter(categories=1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)
        # self.physicsSpace.add(body, self.sonar, self.physicsPolygon)
        self.physicsSpace.add(body, self.physicsPolygon);
        self.physicsSpace.add(sonarBody, self.sonar);
        # self.physicsSpace.add(self.sonarBody, self.sonar)
        # self.physicsSpace.add(c)

    def setPosition(self, position):
        self.position = position
        x, y = position 
        size = self.size
        self.polygonVertices = [(x, y), (x + size, y + size), (x + 2 * size, y + size), (x + 3 * size, y), (x + 2 * size, y - size), (x + size, y - size)]
        self.setVertices(self.polygonVertices)

    def sonar_detect(self, direction):
        if direction == 'up':
            self.bottomPropulsor.force.y =  -self.physicsPolygon.body.velocity_at_local_point(self.bottomPropulsor.position).y
        if direction == 'down':
            self.bottomPropulsor.force.y = self.forceY * 4
        if DEBUG:
            print("SONAR TRIGGER ", direction)
        self.physicsPolygon.body.apply_force_at_local_point(self.bottomPropulsor.force, self.bottomPropulsor.position)
        