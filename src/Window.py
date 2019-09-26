from src.constants import WINDOW_SIZE
import pygame
import random

class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))

    def refresh(self):
        pygame.display.flip()
        
    
    def draw1(self):
        d1 = random.randint(0, WINDOW_SIZE[0])
        d2 = random.randint(0, WINDOW_SIZE[1])
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        pygame.draw.rect(self.screen, (r, g, b), (d1, d2, 5, 5))