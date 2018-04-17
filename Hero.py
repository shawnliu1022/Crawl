'''
Hero.py

'''
import pygame
import math
from GameObject import GameObject
import spritesheet
from spritestripanim import SpriteStripAnim

class Hero(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...
    def __init__(self, x, y):
        ss = spritesheet.Spritesheet('sprites/sprites.gif')
        self.downImages = ss.images_at(((50, 50, 42, 50),(110, 50, 44, 50),(155, 50, 42, 50), (200, 50, 40, 50), (245, 50, 40, 50)), colorkey=(255, 255, 255))
        self.upImages = ss.images_at(((50, 130, 42, 50),(110, 130, 44, 50),(154, 130, 42, 50), (200, 130, 40, 50), (245, 130, 40, 50)), colorkey=(255, 255, 255))
        self.rightImages = ss.images_at(((50, 210, 42, 50),(108, 210, 42, 50),(152, 210, 42, 50), (198, 210, 40, 50), (245, 210, 40, 50)), colorkey=(255, 255, 255))
        images = ss.images_at(((50, 210, 42, 50),(108, 210, 42, 50),(152, 210, 42, 50), (198, 210, 40, 50), (245, 210, 40, 50)), colorkey=(255, 255, 255))
        self.leftImages = []
        for image in images:
            self.leftImages.append(pygame.transform.flip(image, True, False))
        self.index = 0
        self.image = self.downImages[self.index]
        super().__init__(x, y, self.image, 15)

    def update(self, keysDown, screenWidth, screenHeight):
        vx, vy = 0, 0

        if keysDown(pygame.K_LEFT):
            vx -= 3
            self.index += 1
            if self.index == 6*len(self.leftImages):
                self.index = 0
            self.image = self.leftImages[self.index//6]

        if keysDown(pygame.K_RIGHT):
            vx += 3
            self.index += 1
            if self.index == 6*len(self.rightImages):
                self.index = 0
            self.image = self.rightImages[self.index//6]

        if keysDown(pygame.K_UP):
            vy -= 3
            self.index += 1
            if self.index == 6*len(self.upImages):
                self.index = 0
            self.image = self.upImages[self.index//6]
        
        if keysDown(pygame.K_DOWN):
            vy += 3
            self.index += 1
            if self.index == 6*len(self.downImages):
                self.index = 0
            self.image = self.downImages[self.index//6]

        self.velocity = vx, vy
        super(Hero, self).update(screenWidth, screenHeight, self.image)
        
