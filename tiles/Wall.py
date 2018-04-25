import pygame
from GameObject import GameObject

class Wall(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/dc-dngn/wall/brick_dark0.png')
        super().__init__(x, y, self.image, 32)