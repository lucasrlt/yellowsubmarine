from .terrain import *
from .stats import Stats
from .constants import SAVE_STATS

# Classe console gérant tout l'affichage console
# Augmente la rapidité des générations et donne un aperçu global de la convergence de l'algorithme génétique


class Console:
    def __init__(self):
        self.terrain = Terrain(False)
        self.stats = Stats(False)

    def refresh(self):
        self.terrain.update(1.0 / 120.0)

    # Retourne la position maximale obtenue
    def get_max_pos(self):
        posXmax = 0
        for sub in self.terrain.tabSub:
            if sub.getScreenPosition()[0] > posXmax:
                posXmax = sub.getScreenPosition()[0]

        posXmax = (posXmax*100)/1440

        return round(posXmax, 2)

    # Affichage des informations des générations
    def print_gen_info(self):
        print("GENERATION N° ", self.terrain.gene)
        print("Nbr gagnants: ", self.terrain.nbrWinner)
        print("Distance maximale: ", self.get_max_pos(), "%")
        if SAVE_STATS:
            self.stats.writeLastGen(self.terrain)
