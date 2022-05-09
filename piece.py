import pygame
import init
import sys

class piece(pygame.sprite.Sprite):

    # Initialization 
    def __init__(self, file, column, row):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(file)
        self.rect = self.sprite.get_rect()   
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        x, y = 88 * (column - 1) + 8 + spr_w, 88 * (row - 1) + 8 + spr_h
        self.rect.x = x
        self.rect.y = y
        init.window.blit(self.sprite, self.rect)
        print(spr_w, spr_h, x, y)
    def moveLeft(self):
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        self.rect.x += -88
        if self.rect.x < 8:
            self.rect.x += 88
        column = (self.rect.x - spr_w - 8) /  88 + 1 
        row = (self.rect.y - spr_h - 8) /  88 + 1
        print(column, row)
    def moveRight(self):
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        self.rect.x += 88
        if self.rect.x > 704:
            self.rect.x -= 88
        column = (self.rect.x - spr_w - 8) /  88 + 1 
        row = (self.rect.y - spr_h - 8) /  88 + 1
        print(column, row)
    def moveUp(self):
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        self.rect.y += -88
        if self.rect.y < 8:
            self.rect.y += 88
        column = (self.rect.x - spr_w - 8) /  88 + 1 
        row = (self.rect.y - spr_h - 8) /  88 + 1
        print(column, row)
    def moveDown(self):
        spr_w = (88 - self.sprite.get_width()) / 2
        spr_h = (88 - self.sprite.get_height()) / 2
        self.rect.y += 88
        if self.rect.y > 704:
            self.rect.y -= 88
        column = (self.rect.x - spr_w - 8) /  88 + 1 
        row = (self.rect.y - spr_h - 8) /  88 +  1
        print(column, row)
    def update(self):
        init.window.blit(self.sprite, self.rect)
        
