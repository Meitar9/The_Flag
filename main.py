import pygame
import screen

state = {"running": True}
def open_screen():
    while state["running"]:
        close()
        pygame.init()
        screen.green()


def close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False

open_screen()