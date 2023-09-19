import consts
import pygame
import screen


def start_point():
    # soldier = pygame.transform.scale(consts.SOLDIER, (120, 120))
#   consts.game_board.append(soldier)
    screen.screen.blit(consts.soldier, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()


def recognize_movement(keys):
    if keys[pygame.K_LEFT]:
        consts.soldier_x -= 30
    elif keys[pygame.K_RIGHT]:
        consts.soldier_x += 30
    elif keys[pygame.K_UP]:
        consts.soldier_y -= 30
    elif keys[pygame.K_DOWN]:
        consts.soldier_y += 30
    screen.screen.blit(consts.soldier, (consts.soldier_x, consts.soldier_y))
    pygame.display.update()



def drew_solider_nigth():
    soldier_nigth = pygame.transform.scale(consts.SOLDIER_NIGTH, (120, 120))
    consts.screen2.blit(soldier_nigth, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()
    consts.MINE.convert()
    return