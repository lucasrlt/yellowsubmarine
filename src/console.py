from .terrain import *


class Console:
    def __init__(self):
        self.terrain = Terrain()

    def refresh(self):
        self.terrain.update(0.01)

    def get_max_pos(self):
        posXmax = 0
        for sub in self.terrain.tabSub:
            if sub.getScreenPosition()[0] > posXmax:
                posXmax = sub.getScreenPosition()[0]

        return posXmax

    def print_gen_info(self):
        print("GENERATION N° ", self.terrain.gene)
        print("Nbr gagnants: ", self.terrain.nbrWinner)
        print("Distance maximale: ", self.get_max_pos())
