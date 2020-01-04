import pymunk
import time
from ..genetic.geneticEvolutionTrainer import GeneticEvolutionTrainer
from .car import Car
from .constants import TIME_GEN, GEN_SIZE
import sys

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

        if not self.show_trained and time.time() - self.start >= TIME_GEN:
            chromosomes = self.trainer.new_generation(self.get_scores())
            self.clear_cars()
            self.chromosomes_to_car(chromosomes)
            self.start = time.time()
