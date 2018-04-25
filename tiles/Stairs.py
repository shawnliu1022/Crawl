import pygame
from GameObject import GameObject

class Stairs(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/dc-dngn/gateways/stone_stairs_up.png')
        super().__init__(x, y, self.image, 32)