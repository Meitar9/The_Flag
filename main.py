import pygame
import screen
import soldier

state = {"running": True}
def open_screen():
    pygame.init()
    screen.green()
    screen.drew_grass()
    soldier.start_point()
    screen.draw_flag()
    while state["running"]:
        close()
        if pygame.key.get_focused():
            soldier.recognize_movement(pygame.key.get_pressed())



def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False

open_screen()