from Monster import Monster
import pygame

class Demon(Monster):
    def __init__(self, x, y):
        self.image = pygame.image.load("images/dc-mon/demons/fiend.png")
        super(Demon, self).__init__(x, y, self.image)
        
    def fire(self):
        pass