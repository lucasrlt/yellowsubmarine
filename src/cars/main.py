import pygame
import pymunk
import pymunk.pygame_util
import time
from ..genetic.geneticEvolutionTrainer import GeneticEvolutionTrainer
import sys

gen_size = 20
time_gen = 30


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


class Terrain:
    space = None
    cars = []

    def __init__(self):
        self.show_trained = '--trained' in sys.argv

        self.space = pymunk.Space()
        self.space.gravity = 0, 1500

        self.initPhysX()
        self.trainer = GeneticEvolutionTrainer([(15, 40), (15, 40),
                  (0, 60), (0, 60), (80, 120), (30, 30), (5, 50000), (2, 20)])
        
        if self.show_trained:
            self.trained_model()
        else:
            self.chromosomes_to_car(self.trainer.new_generation())
        self.start = time.time()

    def initPhysX(self):
        segments = [(1, 590), (420, 590), (440, 620), (460, 590), (520, 590),
                    (540, 620), (560, 590), (600, 590), (610, 580), (630, 570), (650, 560), (660, 575), (680, 590), (690, 560), (690, 550),
                    (750,550),(850,565),(900,530),(910,530),(920,530),(930,520),(950,500),(960,490),(970,480),(975,480),
                    (980,470),(990,480),(1000,500),(1100,550),(1200,550),(1230,580),(1260,570),(1300,565),(1320,550),(1340,600),
                    (1350,580),(1370,530),(1370,540),(1400,550),(1450,600),(1490,590),(1500,590),(1600,500),(1600,600),(1650,550),(1650,530),(1700,530),
                    (1750,500),(1760,530),(1770,500),(1780,530),(1790,500),(1800,550),(1810,560),(1820,565),(1830,560),(1840,555),(1850,550),(2200,350),
                    (2200,400),(2300,400),(2300,390),(2500,390)]
        
        for i in range(len(segments) - 1):
            seg = pymunk.Segment(self.space.static_body,
                                 segments[i], segments[i + 1], 2)
            seg.friction = 1.0

            self.space.add(seg)

    def clear_cars(self):
        for car in self.cars:
            car.remove(self.space)
        self.cars = []

    def get_scores(self):
        scores = []
        for car in self.cars:
            scores.append(car.get_position().x)
        return scores

    def chromosomes_to_car(self, chromosomes):
        for i in range(len(chromosomes)):
            chromosome = chromosomes[i]
            self.cars.append(Car(self.space, chromosome[0], chromosome[1], chromosome[2],
                                 chromosome[3], chromosome[4], chromosome[5], chromosome[6], chromosome[7], i + 1))

    def trained_model(self): 
        self.cars.append(Car(self.space, 28, 24, 56, 63, 134, 22, 98, 11, 1))

    def update(self):
        self.space.step(1.0 / 120.0)

        if not self.show_trained and time.time() - self.start >= time_gen:
            chromosomes = self.trainer.new_generation(self.get_scores())
            self.clear_cars()
            self.chromosomes_to_car(chromosomes)
            self.start = time.time()


class Window:
    def __init__(self):
        pygame.init()
        self.camera = pygame.Vector2((0, 0))
        self.screen = pygame.display.set_mode((800, 640))
        self.pymunk_layer = pygame.Surface((3000, 640))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.pymunk_layer)
        pymunk.pygame_util.positive_y_is_up = False
        self.terrain = Terrain()
        self.clock = pygame.time.Clock()

    def update(self):
        max_car_pos = 0
        for car in self.terrain.cars:
            if car.get_position().x > max_car_pos:
                max_car_pos = car.get_position().x
        
        pressed = pygame.key.get_pressed()
        camera_move = pygame.Vector2()
        if pressed[pygame.K_UP]:
            camera_move += (0, 1)
        if pressed[pygame.K_LEFT]:
            camera_move += (1, 0)
        if pressed[pygame.K_DOWN]:
            camera_move += (0, -1)
        if pressed[pygame.K_RIGHT]:
            camera_move += (-1, 0)
        if camera_move.length() > 0:
            camera_move.normalize_ip()
        # self.camera += (camera_move*5)
        self.camera = pygame.Vector2((-max_car_pos + 200, 0))
        self.terrain.update()
        self.terrain.space.debug_draw(self.draw_options)
        self.screen.blit(self.pymunk_layer, self.camera)
        pygame.display.flip()
        self.pymunk_layer.fill((0, 0, 0))
        self.screen.fill((0, 0, 0))
        self.clock.tick(60)

    def close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True


if __name__ == "__main__":
    win = Window()

    play = True
    while(play):
        win.update()

        play = win.close()
