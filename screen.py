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
        while x < 60 and y < 120 or x > 1380 and y > 660:
            x = random.randint(0, 1450)
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

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    pygame.time.delay(3000)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.time.delay(3000)

def draw_message(message, font, color, location):
    font = pygame.font.SysFont(consts.LOSE_FONT_SIZE)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_massage_on_start():

    pygame.time.delay(3000)

