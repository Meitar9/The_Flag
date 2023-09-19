import pygame
import time
import consts
import game_field
import screen
import soldier

state = {"running": True, "state": consts.RUNNING_STATE}
def open_screen():
    pygame.init()
    screen.green()
    screen.drew_grass()
    soldier.start_point()
    screen.draw_flag()
    while state["running"]:
        event()
        if game_field.touch_in_flag():
            state["state"] = consts.WIN_STATE
        elif game_field.touch_in_boom():
            state["state"] = consts.LOSE_STATE


def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.KEYDOWN:
            # if event.type == pygame.K_SPACE:
                # if event.type == pygame.K_SPACE:
                #     space()
                # else:
                    soldier.recognize_movement(pygame.key.get_pressed())

# def space():
#     game_field.build_game_board(consts.game_board)
#     time.sleep(1)
#     return



open_screen()