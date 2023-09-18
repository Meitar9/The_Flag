import consts
import pygame
import screen


def start_point():
    soldier = pygame.transform.scale(consts.SOLDIER, (50, 50))
#   consts.game_board.append(soldier)
    screen.screen.blit(soldier, (0, 0))
    pygame.display.flip()
    return
