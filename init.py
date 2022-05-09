import pygame

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
board_image = pygame.image.load("assets/board.png")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')

#def Extra():
    #spr_w = (88 - self.sprite.get_width()) / 2
    #spr_h = (88 - self.sprite.get_height()) / 2
    #column = (self.rect.x - spr_w - 8) /  88 + 1 
    #row = (self.rect.y - spr_h - 8) /  88 + 1
    #print(column, row)
    #pieceToSelect = ['king', 'rook']
    #pieceSelected = pieceToSelect[0]
    # if event.key == pygame.K_q or event.key == ord('q'):
    #                     pieceSelected = 'rook'
    #             if event.key == pygame.K_e or event.key == ord('e'):
    #                     pieceSelected = 'king'
    # if event.type == pygame.KEYDOWN:   
    #             if event.key == pygame.K_LEFT or event.key == ord('a'):

    #             if event.key == pygame.K_RIGHT or event.key == ord('d'):
    #                 window.blit(board_image, (0, 0))
    #                 piece_list.update(False, True, False, False)
    #             if event.key == pygame.K_UP or event.key == ord('w'):
    #                 window.blit(board_image, (0, 0))
    #                 piece_list.update(False, False, True, False)
    #             if event.key == pygame.K_UP or event.key == ord('s'):
    #                 window.blit(board_image, (0, 0))
    #                 piece_list.update(False, False, False, True)
    #     piece_list.update(False, False, False, False)