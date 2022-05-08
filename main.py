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
black_king = piece("assets/black_king.png", 4, 1)
black_rook = piece("assets/black_rook.png", 1, 1)

piece_list = pygame.sprite.Group()
piece_list.add(black_king, black_rook)
pieceToSelect = ['king', 'rook']
pieceSelected = pieceToSelect[0]

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == ord('q'):
                        pieceSelected = 'rook'
                if event.key == pygame.K_e or event.key == ord('e'):
                        pieceSelected = 'king'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    init.window.blit(init.board_image, (0, 0))
                    if pieceSelected == 'king':
                        black_king.moveLeft()
                        if black_king.rect == black_rook.rect:
                            black_king.rect.x += 88
                    else:
                        black_rook.moveLeft()
                        if black_king.rect == black_rook.rect:
                            black_king.rect.x += 88
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    init.window.blit(init.board_image, (0, 0))
                    if pieceSelected == 'king':
                        black_king.moveRight()
                    else:
                        black_rook.moveRight()
                if event.key == pygame.K_UP or event.key == ord('w'):
                    init.window.blit(init.board_image, (0, 0))
                    if pieceSelected == 'king':
                        black_king.moveUp()
                    else:
                        black_rook.moveUp()
                if event.key == pygame.K_UP or event.key == ord('s'):
                    init.window.blit(init.board_image, (0, 0))
                    if pieceSelected == 'king':
                        black_king.moveDown()
                    else:
                       black_rook.moveDown()
        piece_list.update()
        pygame.display.update()