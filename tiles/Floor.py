import pygame
from GameObject import GameObject

class Floor(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/dc-dngn/floor/cobble_blood1.png')
        super().__init__(x, y, self.image, 20)