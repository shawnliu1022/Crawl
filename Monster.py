'''
Monster.py
'''
import pygame
import math
from GameObject import GameObject


class Monster(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...

    def __init__(self, x, y, image):
        super(Monster, self).__init__(x, y, image, 20)
        
    def moveTowardsPlayer(self, hero, screenWidth, screenHeight):
        vx, vy = 0, 0
        if self.x-hero.x > 50:
            vx -= 1.5
        elif self.x-hero.x < -50:
            vx += 1.5
        if self.y-hero.y > 50:
            vy -= 1.5
        elif self.y-hero.y < -50:
            vy += 1.5
        self.velocity = vx, vy
        super(Monster, self).update(screenWidth, screenHeight, self.image)
        
    def move(self, vx, vy, screenWidth, screenHeight):
        self.velocity = vx, vy
        super(Monster, self).update(screenWidth, screenHeight, self.image)

    def update(self, dt, keysDown, screenWidth, screenHeight):
        vx, vy = 0, 0

        if keysDown(pygame.K_LEFT):
            vx -= 2

        if keysDown(pygame.K_RIGHT):
            vx += 2

        if keysDown(pygame.K_UP):
            vy -= 2
        
        if keysDown(pygame.K_DOWN):
            vy += 2

        self.velocity = vx, vy
        super(Monster, self).update(screenWidth, screenHeight, self.image)
