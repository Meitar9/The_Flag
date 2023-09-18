import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def green():
    screen.fill(consts.background_color)
    pygame.display.flip()