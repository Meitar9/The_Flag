import random
import consts
import pygame

import screen
import soldier


def build_game_board(game_board):#בניית המטריצה
    for row in range(25):
        row_list = []
        for col in range(50):
            row_list.append(draw_rect(row, col))
        game_board.append(row_list)
    game_board.append(drew_mine())
    game_board.append(soldier.drew_solider_nigth())
    return pygame.display.flip()

def draw_rect(row, col):#ציור הקוביות
    pygame.draw.rect(surface=consts.screen2, color=consts.rect_color, rect=((place_rect(row, col)), (30, 30)), width=1)
    # pygame.display.flip()
    return

def place_rect(row, col):#מיקום הקוביות
    rect_y = 30 * row
    rect_x = 30 * col
    return rect_x, rect_y

def drew_mine():#מצייר וממקם פצצות
    mine = pygame.transform.scale(consts.MINE, (90, 30))
    for show_grass in range(20):
        x = random.randrange(90, 1410, 30)
        while x in consts.place_of_mine.keys():
            x = random.randrange(90, 1410, 30)
        y = random.randrange(30, 720, 30)
        while y in consts.place_of_mine.values():
            y = random.randrange(30, 720, 30)
        while x < 60 and y < 120 or x > 1380 and y > 660:
            x = random.randrange(90, 1410, 30)
            y = random.randrange(30, 720, 30)
        consts.place_of_mine[x] = y
        consts.screen2.blit(mine, (x, y))
    pygame.display.flip()
    consts.MINE.convert()
    return

def touch_in_flag():#בודק האם נוגע בדגל
    if soldier.solider_body_x > 1380 and soldier.solider_body_y > 660:
        return True
    return False

def touch_in_boom():#בודק האם נוגע בפצצה
    for x in consts.place_of_mine.keys():
        boom_start_place_x = x
        boom_start_place_y = consts.place_of_mine[x]
        boom_end_place_x = x + 90
        boom_end_place_y = consts.place_of_mine[x] + 30
        if soldier.solider_leg_x > boom_start_place_x and soldier.solider_leg_x < boom_end_place_x and soldier.solider_leg_y > boom_start_place_y and soldier.solider_leg_y < boom_end_place_y:
            return True
        else:
            return False

def draw_game_board(game_board):
    screen.screen.fill(consts.BLACK)
    rect = pygame.Rect(game_board)
    pygame.draw.rect(screen.screen, consts.BLACK, rect)
    pygame.display.flip()
    pygame.time.wait(1000)

build_game_board(consts.game_board)