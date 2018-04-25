import pygame
from GameObject import GameObject
class Fireball(GameObject):
    def __init__(self, x, y):
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), (5, 5)), -45)
        super().__init__(x, y, self.image, 20)
        
    def move(self, screenwidth, screenheight):
        if self.velocity[0] > 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), 135)
        elif self.velocity[0] < 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), -45)
        elif self.velocity[1] > 0:
            self.image = pygame.transform.rotate(pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), 45)
        else:
            self.image = pygame.transform.rotate(pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), -135)
        super().update(screenwidth, screenheight, self.image)
        