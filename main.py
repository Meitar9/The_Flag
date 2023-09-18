import pygame
import screen

state = {"running": True}
def open_screen():
    pygame.init()
    screen.green()
    screen.drew_grass()
    while state["running"]:
        close()


def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False

open_screen()