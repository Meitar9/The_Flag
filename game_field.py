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


build_game_board(consts.game_board)
