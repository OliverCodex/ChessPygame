import pygame

window = pygame.display.set_mode((720, 720))

class piece(pygame.sprite.Sprite):

    # Initialization 
    def __init__(self, file, column, row):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(file)
        self.movex = 0
        self.movey = 0
        self.rect = self.sprite.get_rect()   
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        x, y = 88 * (column - 1) + 8 + spr_w, 88 * (row - 1) + 8 + spr_h
        self.rect.x = x
        self.rect.y = y
        window.blit(self.sprite, self.rect)
        print(spr_w, spr_h, x, y)
