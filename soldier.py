import consts
import pygame
import screen


def start_point():
    soldier = pygame.transform.scale(consts.SOLDIER, (120, 120))
#   consts.game_board.append(soldier)
    screen.screen.blit(soldier, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()
    return


def recognize_movement(keys):
    move_ticker = 0
    while move_ticker == 0:
        if keys[pygame.K_LEFT]:
            consts.soldier_x -= 30
        elif keys[pygame.K_RIGHT]:
            consts.soldier_x += 30
        elif keys[pygame.K_UP]:
            consts.soldier_y -= 30
        elif keys[pygame.K_DOWN]:
            consts.soldier_y += 30
        move_ticker += 1
    start_point()

    return

def drew_solider_nigth():
    soldier_nigth = pygame.transform.scale(consts.SOLDIER_NIGTH, (120, 120))
    consts.screen2.blit(soldier_nigth, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()
    consts.MINE.convert()
    return