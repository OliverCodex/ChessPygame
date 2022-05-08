import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
board_image = pygame.image.load("assets/board.png")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')