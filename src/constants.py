## Fichier de constantes, modifie toutes les variables dans l'algorithme
DEBUG = False
WINDOW_SIZE = (1500, 640)
NO_WINDOW = False
CHANCE_MUT = 5
GEN_SIZE = 14
EXP = 5
PROPORTION = 0.75
GEN_TIME = 5
COEFF = 5
NB_CHILD = (GEN_SIZE*PROPORTION)/COEFF if ((GEN_SIZE*PROPORTION) /
                                           COEFF) % 2 == 0 else int((GEN_SIZE*PROPORTION)/COEFF) + 1
SAVE_STATS = False
GEN_NUM = 1000
FEATURE_COUNT = 5
