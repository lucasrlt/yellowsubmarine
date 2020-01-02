from src.constants import WINDOW_SIZE, NO_WINDOW, GEN_TIME, SAVE_STATS, GEN_NUM
from src.window import *
from src.console import *
from src.genetics import *
import time
import sys
from src.geneticEvolutionTrainer import GeneticEvolutionTrainer

if __name__ == "__main__":
    win = Console() if NO_WINDOW else Window()
    start = time.time()
    play = True
    trainer = GeneticEvolutionTrainer()
    if len(sys.argv) != 1:
        filePath = sys.argv[1]
        print("IMPORTATION DU FICHIER : ", str(filePath))

    if NO_WINDOW:
        print("DEBUT DE LA SIMULATION")
        print("BATCH SIZE: ", GEN_SIZE)

    while(play):
        win.refresh()

        if time.time() - start >= (GEN_TIME if NO_WINDOW else GEN_TIME * 4):
            print("----Gen Time Out----")
            for sub in win.terrain.tabSub:
                if sub.isAlive:
                    sub.isAlive = False
                    win.terrain.space.remove(
                        sub.physicsPolygon, sub.sonar, sub.sonar.body, sub.physicsPolygon.body)
                    win.terrain.nbrSubCreated -= 1
                if sub.distance == -1:
                    sub.distance = sub.getScreenPosition()[0]

        if win.terrain.nbrSubCreated == 0:
            start = time.time()
            win.terrain.gene += 1
            if SAVE_STATS:
                win.stats.writeLastGen(win.terrain)

            if NO_WINDOW:
                win.print_gen_info()

            newTabSub = []
            scores = []
            for sub in win.terrain.tabSub:
                scores.append(sub.distance / 1475.0)

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

        if not NO_WINDOW:
            play = win.close()
        continue
