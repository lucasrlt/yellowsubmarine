import random
from statistics import mean
import copy
import numpy as np

FEATURE_COUNT = 8


class GeneticEvolutionTrainer():
    generation = 0
    selection_rate = 0.1
    mutation_rate = 0.01
    population_size = 100
    parents = int(population_size * selection_rate)
    population = None
    boundaries = [(1, 50), (1, 50),
                  (0, 50), (0, 50), (50, 50), (30, 30), (5, 50000), (0, 50)]

    def new_generation(self, scores=None):
        if self.population is None:
            print("GENERATION INITIALE")
            self.population = self.initial_population()
            return self.population

        print("GENERATION " + str(self.generation))

        # 1st step: parents selection
        parents = self.strongest_parents(scores)

        # 2nd step: crossover
        pairs = []
        while len(pairs) != self.population_size:
            pairs.append(self.pair(parents))

        base_offsprings = []
        for pair in pairs:
            offsprings = self.crossover(pair[0][0], pair[1][0])
            base_offsprings.append(offsprings[-1])

        # 3rd step: mutation
        new_population = self.mutation(base_offsprings)
        self.population = new_population
        self.generation += 1
        return self.population

    def pair(self, parents):
        total_parents_score = sum([x[1] for x in parents])
        pick = random.uniform(0, total_parents_score)
        return [self.roulette_selection(parents, pick), self.roulette_selection(parents, pick)]

    def roulette_selection(self, parents, pick):
        current = 0
        for parent in parents:
            current += parent[1]
            if current > pick:
                return parent

    def mutation(self, base_offsprings):
        offsprings = []
        for offspring in base_offsprings:
            offspring_mutation = copy.deepcopy(offspring)
            for i in range(0, FEATURE_COUNT):
                if np.random.choice([True, False], p=[self.mutation_rate, 1-self.mutation_rate]):
                    offspring_mutation[i] = random.randint(
                        self.boundaries[i][0], self.boundaries[i][1])
            offsprings.append(offspring_mutation)
        return offsprings

    def crossover(self, x, y):
        offspring_x = x
        offspring_y = y
        for i in range(0, FEATURE_COUNT):
            if random.choice([True, False]):
                offspring_x[i] = y[i]
                offspring_y[i] = x[i]
        return offspring_x, offspring_y

    def strongest_parents(self, scores):
        scores_for_chromosome = []
        for i in range(len(scores)):
            chromosome = self.population[i]
            scores_for_chromosome.append((chromosome, scores[i]))
        scores_for_chromosome.sort(key=lambda x: x[1])
        print("Population: " + str(mean([x[1]
                                         for x in scores_for_chromosome])))

        top_performers = scores_for_chromosome[-self.parents:]
        top_scores = [x[1] for x in top_performers]
        print("Top: " + str(self.selection_rate) + ": " + "(min: " + str(min(top_scores)
                                                                         ) + ", avg: " + str(mean(top_scores)) + ", max: " + str(max(top_scores)) + ")")

        return top_performers

    def initial_population(self):
        chromosomes = []
        for i in range(0, self.population_size):
            chromosome = []
            for j in range(0, FEATURE_COUNT):
                chromosome.append(random.randint(
                    self.boundaries[j][0], self.boundaries[j][1]))
            chromosomes.append(chromosome)
        return chromosomes
