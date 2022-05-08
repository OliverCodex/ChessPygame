import pygame
import sys
from piece import *

# Variables
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

board_image = pygame.image.load("assets/board.png")

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')
pygame.init()

window.blit(board_image, (0, 0))

# Pieces
black_king = piece("assets/black_king.png", 2, 1)

piece_list = pygame.sprite.Group()
piece_list.add(black_king)
  
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                window.blit(board_image, (0, 0))
                black_king.rect.x += -88
                window.blit(black_king.sprite, black_king.rect)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                window.blit(board_image, (0, 0))
                black_king.rect.x += 88
                window.blit(black_king.sprite, black_king.rect)
            if event.key == pygame.K_UP or event.key == ord('w'):
                window.blit(board_image, (0, 0))
                black_king.rect.y += -88
                window.blit(black_king.sprite, black_king.rect)
            if event.key == pygame.K_UP or event.key == ord('s'):
                window.blit(board_image, (0, 0))
                black_king.rect.y += 88
                window.blit(black_king.sprite, black_king.rect)
    pygame.display.update()