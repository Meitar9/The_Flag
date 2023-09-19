import random
import consts
import pygame
import soldier

import screen


def build_game_board(game_board):
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append(draw_rect(row, col))
        game_board.append(row_list)
    game_board.append(drew_mine())
    game_board.append(soldier.drew_solider_nigth())
    while True:
        pygame.init()

def draw_rect(row, col):
    pygame.draw.rect(surface=consts.screen2, color=consts.rect_color, rect=((place_rect(row, col)), (30, 30)), width=1)
    pygame.display.flip()
    return

def place_rect(row, col):
    rect_y = 30 * row
    rect_x = 30 * col
    return rect_x, rect_y

def drew_mine():
    mine = pygame.transform.scale(consts.MINE, (90, 30))
    place_of_mine = {}
    for show_grass in range(20):
        x = random.randrange(90, 1410, 30)
        while x in place_of_mine.keys():
            x = random.randrange(90, 1410, 30)
        y = random.randrange(30, 720, 30)
        while y in place_of_mine.values():
            y = random.randrange(30, 720, 30)
        while x <= 60 and y <= 120 or x >= 1380 and y >= 630:
            x = random.randrange(90, 1410, 30)
            y = random.randrange(30, 720, 30)
        place_of_mine[x] = y
        consts.screen2.blit(mine, (x, y))
    pygame.display.flip()
    consts.MINE.convert()
    return

build_game_board(consts.game_board)
drew_mine()