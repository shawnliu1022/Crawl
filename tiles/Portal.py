import pygame
from GameObject import GameObject

class Portal(GameObject):
    def __init__(self, x, y):
        image = pygame.image.load('images/dc-dngn/gateways/dngn_portal.png')
        super().__init__(x, y, image, 20)