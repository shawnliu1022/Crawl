import pygame
from GameObject import GameObject

class OpenDoor(GameObject):
    def __init__(self, x, y):
        image = pygame.image.load('images/dc-dngn/dngn_open_door.png')
        super().__init__(x, y, image, 32)