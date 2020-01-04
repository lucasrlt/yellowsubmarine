import random
from statistics import mean
import copy
import numpy as np

# Algorithme génétique adatpé à différents types de problèmes.
# Cet algorithme est utilisé à la fois pour l'entrainement des voitures et des sous-marins.
# Les différents paramètres à faire varier sont:
# selection_rate => le nombre des meilleurs parents que l'on sélectionne
# mutation_rate => chance pour un spécimen de muter
# parents => nombre de parents
# boundaries => les limites que l'on impose à la génération aléatoire pour chaque chromosome


class GeneticEvolutionTrainer():
    generation = 0
    selection_rate = 0.1
    mutation_rate = 0.01
    population_size = 100
    parents = int(population_size * selection_rate)
    population = None
    boundaries = None
    feature_count = 0

    def __init__(self, boundaries, population_size=100, selection_rate=0.1, mutation_rate=0.01):
        self.boundaries = boundaries
        self.population_size = population_size
        self.selection_rate = selection_rate
        self.mutation_rate = mutation_rate
        self.feature_count = len(boundaries)

    def new_generation(self, scores=None):
        if self.population is None:
            print("GENERATION INITIALE")
            self.population = self.initial_population()
            return self.population

        print("GENERATION N°" + str(self.generation))

        # Sélection des parents
        parents = self.select_parents(scores)

        # Reproduction entre les parents
        pairs = []
        while len(pairs) != self.population_size:
            pairs.append(self.pair(parents))

        base_offsprings = []
        for pair in pairs:
            offsprings = self.breeding(pair[0][0], pair[1][0])
            base_offsprings.append(offsprings[-1])

        # Mutation de la population
        new_population = self.mutation(base_offsprings)
        self.population = new_population
        self.generation += 1

        print("Taille: " + str(len(self.population)))
        return self.population

    # Crée des paires de parents pour les faire se reproduire enemble
    def pair(self, parents):
        total_parents_score = sum([x[1] for x in parents])
        treshold = random.uniform(0, total_parents_score)
        return [self.roulette_selection(parents, treshold), self.roulette_selection(parents, treshold)]

    # Sélection des paires de parents à reproduire.
    # Ce type de sélection ne paire que les spécimens de niveau similaire entre eux.
    def roulette_selection(self, parents, treshold):
        curr_score = 0
        for parent in parents:
            curr_score += parent[1]
            if curr_score > treshold:
                return parent

    # Il est important de faire muter une partie de notre population pour préserver la diversité.
    # Un gène mutant sera re-généré aléatoirement.
    def mutation(self, children):
        new_children = []
        for child in children:
            child_mutation = copy.deepcopy(child)
            for i in range(0, self.feature_count):
                if np.random.choice([True, False], p=[self.mutation_rate, 1-self.mutation_rate]):
                    child_mutation[i] = random.randint(
                        self.boundaries[i][0], self.boundaries[i][1])
            new_children.append(child_mutation)
        return new_children

    # Reproduction entre deux spéciments. L'enfant prendra aléatoirement les gènes des deux parents.
    def breeding(self, x, y):
        child_x = x
        child_y = y

        for i in range(0, self.feature_count):
            if random.choice([True, False]):
                child_x[i] = y[i]
                child_y[i] = x[i]

        return child_x, child_y

    # Sélection des parents qui se reproduiront pour créer la prochaine population.
    # Les parents seront les 10% des meilleurs spécimens.
    def select_parents(self, scores):
        # On crée des pairs [chromosome, score pour chromosome]
        pairs_score_chromosome = []
        for i in range(len(scores)):
            chromosome = self.population[i]
            pairs_score_chromosome.append((chromosome, scores[i]))

        # On trie les chromosomes par score pour la sélection
        pairs_score_chromosome.sort(key=lambda x: x[1])
        print("Moyenne ssur la population: " + str(mean([x[1]
                                                         for x in pairs_score_chromosome])))

        best_specimens = pairs_score_chromosome[-self.parents:]
        best_scores = [x[1] for x in best_specimens]
        print("Max: " + str(max(best_scores)) + ")")

        return best_specimens

    # Génère la population initiale, les chromosomes sont générés aléatoirement en fonction des limites données.
    def initial_population(self):
        chromosomes = []
        for i in range(0, self.population_size):
            chromosome = []
            for j in range(0, self.feature_count):
                chromosome.append(random.randint(
                    self.boundaries[j][0], self.boundaries[j][1]))
            chromosomes.append(chromosome)
        return chromosomes
