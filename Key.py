import pygame
from GameObject import GameObject

class Key(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/key.png')
        super().__init__(x, y, self.image, 32)