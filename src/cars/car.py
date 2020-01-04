import pymunk


class Car:
    def get_position(self):
        return self.chassi_b.position

    def remove(self, space):
        space.remove(self.wheel1_s, self.wheel1_b)
        space.remove(self.wheel2_s, self.wheel2_b)
        space.remove(self.chassi_s, self.chassi_b)
        space.remove(self.motor1, self.motor2)
        for joint in self.joints:
            space.remove(joint)

    def __init__(self, space, wheel1_radius, wheel2_radius, wheel1_offset, wheel2_offset, chassi_width, chassi_height, chassi_mass, speed, count):
        pos = pymunk.Vec2d(100, 555)

        shapeFilter = pymunk.ShapeFilter.ALL_MASKS ^ 1

        wheel_color = 52, 219, 119
        mass = 100
        radius = wheel1_radius
        moment = pymunk.moment_for_circle(mass, 20, radius)
        wheel1_b = pymunk.Body(mass, moment)
        wheel1_s = pymunk.Circle(wheel1_b, radius)
        wheel1_s.friction = 1.5
        wheel1_s.color = wheel_color
        self.wheel1_b, self.wheel1_s = wheel1_b, wheel1_s
        wheel1_s.filter = pymunk.ShapeFilter(
            categories=1, mask=shapeFilter)
        space.add(wheel1_b, wheel1_s)

        mass = 100
        radius = wheel2_radius
        moment = pymunk.moment_for_circle(mass, 20, radius)
        wheel2_b = pymunk.Body(mass, moment)
        wheel2_s = pymunk.Circle(wheel2_b, radius)
        wheel2_s.friction = 1.5
        wheel2_s.color = wheel_color
        wheel2_s.filter = pymunk.ShapeFilter(
            categories=1, mask=shapeFilter)
        self.wheel2_b, self.wheel2_s = wheel2_b, wheel2_s
        space.add(wheel2_b, wheel2_s)

        mass = chassi_mass
        size = (chassi_width, chassi_height)
        moment = pymunk.moment_for_box(mass, size)
        chassi_b = pymunk.Body(mass, moment)
        chassi_s = pymunk.Poly.create_box(chassi_b, size)
        chassi_s.filter = pymunk.ShapeFilter(
            categories=1, mask=shapeFilter)
        self.chassi_b, self.chassi_s = chassi_b, chassi_s
        space.add(chassi_b, chassi_s)

        wheel1_b.position = pos - (wheel1_offset, 0)
        wheel2_b.position = pos + (wheel2_offset, 0)
        chassi_b.position = pos + (0, -25)

        self.joints = [pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), (-25, -15)),
                       pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), (-25, 15)),
                       pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), (25, -15)),
                       pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), (25, 15))]

        for joint in self.joints:
            space.add(joint)

        speed = speed
        self.motor1 = pymunk.SimpleMotor(wheel1_b, chassi_b, speed)
        self.motor1.max_force = speed * 1000000
        self.motor2 = pymunk.SimpleMotor(wheel2_b, chassi_b, speed)
        self.motor2.max_force = speed * 1000000

        space.add(
            self.motor1,
            self.motor2
        )
