import pymunk
import pymunk.pygame_util
import math
from .constants import *

LEFT_PROPULSOR_ANGLE = -math.pi / 4
BOTTOM_PROPULSOR_ANGLE = math.pi / 8

"""
A propulsor is the equivalent of an engine for the submarine. 
"""


class Propulsor:
    def __init__(self, position, force, angle=0):
        self.position = pymunk.Vec2d(position)
        self.force = pymunk.Vec2d(force)
        self.force.rotate(angle)


class Submarine:
    def __init__(self, physicsSpace, position, sonarSize, subSize, forceX, forceY, isAlive, color):
        # Initialization of instance variables
        self.size = subSize
        self.isAlive = isAlive
        self.hasWin = False
        self.physicsSpace = physicsSpace
        self.color = color
        self.lifetime = -1
        self.distance = -1

        # Forces applied to left & right propulsors
        self.forceX = forceX
        self.forceY = forceY

        # Propulsors powering the submarine
        self.leftPropulsor = Propulsor(
            (0, 0), (forceX, 0), LEFT_PROPULSOR_ANGLE)
        self.bottomPropulsor = Propulsor(
            (int(self.size + self.size / 2), -self.size), (0, forceY), BOTTOM_PROPULSOR_ANGLE)

        # The sonar detects collisions around the submarine
        self.sonarRadius = sonarSize
        self.sonarOffset = (self.size + self.size / 2, 0)

        self.initPolygon(position)
        self.initSonar()

    def initPolygon(self, position):
        self.position = position
        x, y = position
        size = self.size
        self.polygonVertices = [(x, y),  # Left
                                (x + size, y + size),  # left bot
                                (x + 2 * size, y + size),  # right bot
                                (x + 3 * size, y),  # right
                                (x + 2 * size, y - size),  # right top
                                (x + size, y - size)]  # left top

        # submarine poylgon's body
        body = pymunk.Body(10, pymunk.moment_for_poly(
            10, self.polygonVertices), body_type=pymunk.Body.DYNAMIC)
        body.density = 3
        body.position = self.size * 2 + self.size / 2, 0
        self.applyForces(body)

        # submarine polygon
        self.physicsPolygon = pymunk.Poly(body, self.polygonVertices, None, 1)
        self.physicsPolygon.color = self.color
        self.physicsPolygon.collision_type = 4
        self.physicsPolygon.filter = pymunk.ShapeFilter(
            categories=1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)

        self.physicsSpace.add(body, self.physicsPolygon)

    def initSonar(self):
        # sonar body
        sonarBody = pymunk.Body(1, pymunk.moment_for_circle(
            10, self.sonarRadius - 1, self.sonarRadius))
        sonarBody.position = self.getScreenPosition()

        # sonar polygon
        self.sonar = pymunk.Circle(
            sonarBody, self.sonarRadius, self.sonarOffset)
        self.sonar.color = (self.color[0], self.color[1], self.color[2], 1)
        # sonar collisions
        self.sonar.filter = pymunk.ShapeFilter(
            categories=1, mask=pymunk.ShapeFilter.ALL_MASKS ^ 1)
        self.sonar.collision_type = 5

        self.physicsSpace.add(sonarBody, self.sonar)

    def applyForces(self, body):
        body.apply_force_at_local_point(
            (0, 0), (body.position[0], body.position[1] - self.size))
        body.apply_force_at_local_point(
            self.leftPropulsor.force, self.leftPropulsor.position)
        body.apply_force_at_local_point(
            self.bottomPropulsor.force, self.bottomPropulsor.position)

    """ 
    Convert pymunk's body position to pygame position to get the center of gravity 
    """

    def getScreenPosition(self):
        poly_center = tuple(map(sum, zip(self.position, self.sonarOffset)))
        poly_center = (int(poly_center[0]), int(poly_center[1]))
        return self.physicsPolygon.body.local_to_world(poly_center)

    """
    Get body's center position
    """

    def getPosition(self):
        return self.physicsPolygon.body.position

    """
    Behavior to adopt in case of a detected collision by the sonar
        - collision up: go down
        - collision down: go up
    """

    def sonar_detect(self, direction):
        if direction == 'up':
            self.bottomPropulsor.force.y = -self.forceY * 3
        if direction == 'down':
            self.bottomPropulsor.force.y = self.forceY * 3
        if DEBUG:
            print("SONAR TRIGGER ", direction)

        self.physicsPolygon.body.apply_force_at_local_point(
            self.bottomPropulsor.force, self.bottomPropulsor.position)
