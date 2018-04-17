import pygame
from GameObject import GameObject

class Door(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/dc-dngn/dngn_closed_door.png')
        super().__init__(x, y, self.image, 20)