import pygame
import screen

state = {"running" : True}
def open_screen():
    while state["running"]:
        pygame.init()

