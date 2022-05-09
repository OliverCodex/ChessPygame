import pygame
import sys
from piece import *

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
board_image = pygame.image.load("assets/board.png")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')

window.blit(board_image, (0, 0))
# Pieces
black_king = piece("assets/black_king.png", True, True, False, 4, 1)
black_rook = piece("assets/black_rook.png", False, True, True, 7, 1)

piece_list = pygame.sprite.Group()
piece_list.add(black_king, black_rook)


main = True
while main:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in piece_list if s.rect.collidepoint(pos)]
                if clicked_sprites:
                    window.blit(board_image, (0, 0))
                    black_rook.update(True, False, False, False)
        piece_list.update(False, False, False, False,)
        pygame.display.update()