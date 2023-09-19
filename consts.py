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

soldier_x = 0
soldier_y = 0
soldier = pygame.transform.scale(SOLDIER, (120, 120))

solider_leg_x = soldier_x + 90
solider_leg_y = soldier_y + 120
solider_body_x = soldier_x + 90
solider_body_y = soldier_y + 90