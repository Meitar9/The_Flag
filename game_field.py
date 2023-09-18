import random
import consts
import pygame
import screen


def build_game_board(game_board):
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append(draw_rect(row, col))
        game_board.append(row_list)

    while True:
        pygame.init()

def draw_rect(row, col):
    pygame.draw.rect(surface=screen.screen, color=consts.rect_color, rect=((place_rect(row, col)), (30, 30)), width=1)
    pygame.display.flip()

def place_rect(row, col):
    rect_y = 30 * row
    rect_x = 30 * col
    return rect_x, rect_y

def drew_mine():
    mine = pygame.transform.scale(consts.MINE, (90, 30))
    place_of_mine = {}
    for show_grass in range(20):
        x = random.randint(120, 1430)
        while x in place_of_mine.keys():
            x = random.randint(120, 1430)
        y = random.randint(0, 600)
        while y in place_of_mine.values():
            y = random.randint(0, 600)
        place_of_mine[x] = y
        consts.game_board.blit(mine, (x, y))
#        consts.game_board[x][y].append(mine)
#        pygame.draw.(surface=screen.screen, rect = mine, (30, 30)), width = 1)
        pygame.display.flip()
    return

build_game_board(consts.game_board)
drew_mine()