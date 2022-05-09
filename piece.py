import pygame
import init
import sys

class piece(pygame.sprite.Sprite):

    # Initialization 
    def __init__(self, file, diagonal, straight, range, column, row):
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
        if diagonal == True:
            print()
        if straight == True:
            print()
        if range == True:
            print()
    def select(self):
        print()
    # Movement rules, border, collision
    #def moveDiagonal(self):
        #print()
    #def moveStraight(self):
        #print()
    def moveLeft(self):
        self.rect.x -= 88
        if self.rect.x < 8:
            self.rect.x += 88
    def moveRight(self):
        self.rect.x += 88
        if self.rect.x > 704:
            self.rect.x -= 88
    def moveUp(self):
        self.rect.y -= 88
        if self.rect.y < 8:
            self.rect.y += 88
    def moveDown(self):
        self.rect.y += 88
        if self.rect.y > 704:
            self.rect.y -= 88

    def update(self, left, right, up, down):
        if left == True:
            self.moveLeft()
        if right == True:
            self.moveRight()
        if up == True:
            self.moveUp()
        if down == True:
            self.moveDown()
        init.window.blit(self.sprite, self.rect)
        
        
