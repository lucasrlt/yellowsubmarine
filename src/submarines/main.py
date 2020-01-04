from .constants import WINDOW_SIZE, GEN_TIME, SAVE_STATS, GEN_NUM
from .window import *
from .console import *
from ..genetic.geneticEvolutionTrainer import GeneticEvolutionTrainer
import time
import sys

gen_boundaries = [(2, 200), (10, 20),
                  (-100000, 100000), (-50000, 50000), (-20, 20)]

if __name__ == "__main__":
    with_window = len(sys.argv) <= 1 or (
        len(sys.argv) > 1 and not sys.argv[1] == '--console')
    show_trained = '--trained' in sys.argv
    load = '--load_file' in sys.argv

    win = Window(show_trained) if with_window else Console()
    start = time.time()
    play = True
    trainer = GeneticEvolutionTrainer(gen_boundaries)

    if load:
        filePath = sys.argv[1]
        print("IMPORTATION DU FICHIER : ", str(filePath))

    print("DEBUT DE LA SIMULATION")

    while(play):
        win.refresh()

        if not show_trained:
            # Chaque génération a une durée limitée. Si la fin de la génération est atteinte, on en crée une nouvelle.
            if time.time() - start >= (GEN_TIME if not with_window else GEN_TIME * 4):
                print("----Gen Time Out----")
                for sub in win.terrain.tabSub:
                    if sub.isAlive:
                        sub.isAlive = False
                        win.terrain.space.remove(
                            sub.physicsPolygon, sub.sonar, sub.sonar.body, sub.physicsPolygon.body)
                        win.terrain.nbrSubCreated -= 1
                    if sub.distance == -1:
                        sub.distance = sub.getScreenPosition()[0]

            # Tous les sous-marins se sont échoués, on passe à la génération suivante.
            if win.terrain.nbrSubCreated == 0:
                start = time.time()
                win.terrain.gene += 1
                if SAVE_STATS:
                    win.stats.writeLastGen(win.terrain)

                if NO_WINDOW:
                    win.print_gen_info()

                # Création du tableau de scores par sous marin
                newTabSub = []
                scores = []
                for sub in win.terrain.tabSub:
                    scores.append(sub.distance / 1475.0)

                # Création des sous marins créés à partir des chromosomes généras par l'algo génétique.
                newChromosomes = trainer.new_generation(scores)
                for chromosome in newChromosomes:
                    randR = random.randint(0, 255)
                    randG = random.randint(0, 255)
                    randB = random.randint(0, 255)
                    newTabSub.append(Submarine(win.terrain.space, (150, (int(
                        WINDOW_SIZE[1] / 2)) - 50), chromosome[0], chromosome[1], chromosome[2], chromosome[3], True, (randR, randG, randB, 255), -1, chromosome[4]))

                win.terrain.tabSub = newTabSub
                win.terrain.nbrWinner = 0
                win.terrain.nbrSubCreated = len(newTabSub)

        if with_window:
            play = win.close()
        continue
