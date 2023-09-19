import consts
import pygame
import screen


def start_point():
    soldier = pygame.transform.scale(consts.SOLDIER, (120, 120))
    soldier_place = {"solider_x": 0, "solider_y": 0}
    screen.screen.blit(soldier_place["solider_x"], soldier_place["solider_y"])
    pygame.display.update()
    return soldier_place


# def recognize_movement(keys):
#     if keys[pygame.K_LEFT]:
#        consts.soldier_x -= 30
#        consts.position = consts.position.move((-30, 0))
#     elif keys[pygame.K_RIGHT]:
#        consts.soldier_x += 30
#        consts.position = consts.position.move((30, 0))
#     elif keys[pygame.K_UP]:
#         consts.soldier_y -= 30
#         consts.position = consts.position.move((0, -30))
#     elif keys[pygame.K_DOWN]:
#         consts.soldier_y += 30
#         consts.position = consts.position.move((0, 30))
#     start_point()

def move_left(screen, solider):
    solider["x_val"] += 1 * consts.GRID_SIZE
    screen.blit(consts.PLAYER_IMG, (solider["x_val"] * consts.GRID_SIZE, solider["y_val"] * consts.GRID_SIZE))


def move_right(screen, solider):
    solider["x_val"] -= 1 * consts.GRID_SIZE
    screen.blit(consts.PLAYER_IMG, (solider["x_val"], solider["x_val"]))


def move_up(screen, solider):
    solider["y_val"] -= 1 * consts.GRID_SIZE
    screen.blit(consts.PLAYER_IMG, (solider["x_val"], solider["x_val"]))


def move_down(screen, solider):
    solider["y_val"] += 1
    screen.blit(consts.PLAYER_IMG, (solider["x_val"], solider["x_val"]))



def drew_solider_nigth():
    soldier_nigth = pygame.transform.scale(consts.SOLDIER_NIGTH, (120, 120))
    consts.screen2.blit(soldier_nigth, (consts.soldier_x, consts.soldier_y))
    pygame.display.flip()
    consts.MINE.convert()
    return