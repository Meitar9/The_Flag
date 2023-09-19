import pygame
game_board = []
place_of_mine = {}
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 1500
screen2 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_color = (61,145,64)
rect_color = (0,100,0)
GRASS = pygame.image.load("grass.png")
FLAG = pygame.image.load("flag.png")
EXPLOTION = pygame.image.load("explotion.png")
INJURY = pygame.image.load("injury.png")
MINE = pygame.image.load("mine.png")
SNAKE = pygame.image.load("snake.png")
SOLDIER_2 = pygame.image.load("soldier (2).png")
SOLDIER = pygame.image.load("soldier.png")
SOLDIER_NIGTH = pygame.image.load("soldier_nigth.png")
RUNNING_STATE = 1
WIN_STATE = 3
LOSE_STATE = 2
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (0, 0, 0)
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

soldier_x = 0
soldier_y = 0
soldier = pygame.transform.scale(SOLDIER, (120, 120))

