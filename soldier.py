import consts
import pygame
import screen
import os


def start_point():
    # soldier = pygame.transform.scale(consts.SOLDIER, (120, 120))
#   consts.game_board.append(soldier)
    screen.screen.blit(consts.soldier, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()


def recognize_movement(keys):
    if keys[pygame.K_LEFT] and check_lines():
        consts.soldier_x -= 30
    elif keys[pygame.K_RIGHT] and check_lines():
        consts.soldier_x += 30
    elif keys[pygame.K_UP] and check_lines():
        consts.soldier_y -= 30
    elif keys[pygame.K_DOWN] and check_lines():
        consts.soldier_y += 30
    screen.screen.blit(consts.soldier, (consts.soldier_x, consts.soldier_y))
    pygame.display.update()



def drew_solider_nigth():
    soldier_nigth = pygame.transform.scale(consts.SOLDIER_NIGTH, (120, 120))
    consts.screen2.blit(soldier_nigth, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()
    consts.MINE.convert()
    return

solider_leg_x = consts.soldier_x + 90
solider_leg_y = consts.soldier_y + 120
solider_body_x = consts.soldier_x + 90
solider_body_y = consts.soldier_y + 90

def check_lines(): #בודק האם אפשר להתקדם
    if consts.soldier_x <= 1450 or consts.soldier_y <= 600 or consts.soldier_x >= 30 or consts.soldier_y >= 30:
        return True
    return False
