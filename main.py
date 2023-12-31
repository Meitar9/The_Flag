import pygame
import time
import consts
import screen
import game_field
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
            screen.draw_win_message()
            state["running"] = False
        elif game_field.touch_in_boom():
            state["state"] = consts.LOSE_STATE
            screen.draw_lose_message()
            state["running"] = False
    pygame.display.flip()


def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.KEYDOWN:
            if event.type == 768:
                game_field.build_game_board(consts.game_board)
                open_screen()
            else:
                soldier.recognize_movement(pygame.key.get_pressed())


open_screen()