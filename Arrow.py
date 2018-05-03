import pygame
from GameObject import GameObject
class Arrow(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load("images/effect/arrow4.png")
        
        super().__init__(x, y, self.image, 20)
        
    def move(self, screenwidth, screenheight):
        if self.velocity[0]>1:
            if self.velocity[1]>1:
                self.image = pygame.image.load("images/effect/arrow3.png")
            elif self.velocity[1]<-1:
                self.image = pygame.image.load("images/effect/arrow1.png")
            else:
                self.image = pygame.image.load("images/effect/arrow2.png")
        elif self.velocity[0]<-1:
            if self.velocity[1]>1:
                self.image = pygame.image.load("images/effect/arrow5.png")
            elif self.velocity[1]<-1:
                self.image = pygame.image.load("images/effect/arrow7.png")
            else:
                self.image = pygame.image.load("images/effect/arrow6.png")
        else:
            if self.velocity[1]<-1:
                self.image = pygame.image.load("images/effect/arrow0.png")
            else:
                self.image = pygame.image.load("images/effect/arrow4.png")
        super().update(screenwidth, screenheight, self.image)
        