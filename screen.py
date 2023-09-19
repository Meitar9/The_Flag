import random
import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def green():
    screen.fill(consts.background_color)
    pygame.display.flip()

def drew_grass():
    grass = pygame.transform.scale(consts.GRASS, (50, 50))
    place_of_grass = {}
    for show_grass in range(20):
        x = random.randint(0, 1450)
        while x in place_of_grass.keys():
            x = random.randint(0, 1450)
        y = random.randint(0, 700)
        while y in place_of_grass.values():
            y = random.randint(0, 700)
        place_of_grass[x] = y
        screen.blit(grass, (x, y))
        pygame.display.flip()
    return

def draw_flag():
    flag = pygame.transform.scale(consts.FLAG, (120, 90))
    screen.blit(flag, (1380, 660))
    pygame.display.flip()
    return
