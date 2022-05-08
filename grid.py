import pygame

window = pygame.display.set_mode((720, 720))

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
tiles = []

def grid():
    coords = []
    for i in range(0, 8):
        name = letters[0] + numbers[0 + i]
        placement = 8, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[1] + numbers[0 + i]
        placement = 96, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[2] + numbers[0 + i]
        placement = 184, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[3] + numbers[0 + i]
        placement = 272, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[4] + numbers[0 + i]
        placement = 360, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[5] + numbers[0 + i]
        placement = 448, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[6] + numbers[0 + i]
        placement = 536, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    for i in range(0, 8):
        name = letters[7] + numbers[0 + i]
        placement = 624, 8 + 88 * i
        coords.append(placement)
        tiles.append(name)
        name = pygame.Rect((88, 88), (placement))
    print(tiles, coords, len(coords + tiles))
