import random

import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def green():
    screen.fill(consts.background_color)
    pygame.display.flip()

def drew_grass():
    pygame.transform.scale(consts.GRASS, (1, 1))
#    consts.GRASS.get_size(50, 50)
    for show_grass in range(20):
        x = random.randint(0, 750)
        y = random.randint(0, 1500)

        screen.blit(consts.GRASS, (x, y))
        pygame.display.flip()
    return
