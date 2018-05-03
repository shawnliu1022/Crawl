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
        #add images
        self.downImages = ss.images_at(((328, 50, 30, 50),(386, 50, 30, 50),(430, 50, 30, 50), (478, 50, 30, 50), (523, 50, 30, 50)), colorkey=(255, 255, 255))
        self.upImages = ss.images_at(((328, 130, 30, 50),(386, 130, 30, 50),(430, 130, 30, 50), (478, 130, 30, 50), (523, 130, 30, 50)), colorkey=(255, 255, 255))
        self.rightImages = ss.images_at(((328, 210, 30, 48),(386, 210, 30, 48),(430, 210, 30, 48), (478, 210, 27, 48), (523, 210, 27, 48)), colorkey=(255, 255, 255))
        
        self.leftImages = []
        #scale images down
        for index in range(len(self.downImages)):
            temp = pygame.transform.scale(self.downImages[index], (15, 25))
            self.downImages[index] = temp
        for index in range(len(self.upImages)):
            temp = pygame.transform.scale(self.upImages[index], (15, 25))
            self.upImages[index] = temp
        for index in range(len(self.rightImages)):
            temp = pygame.transform.scale(self.rightImages[index], (15, 25))
            self.rightImages[index] = temp
        #add left images
        for image in self.rightImages:
            self.leftImages.append(pygame.transform.flip(image, True, False))
            
        ssA = spritesheet.Spritesheet('sprites/sprite_attack.gif')
        self.downAttackImages = ssA.images_at(((338, 42, 55, 65),(390, 42, 55, 65),(445, 42, 55, 65), (504, 42, 55, 65), (555, 42, 55, 65)), colorkey=(255, 255, 255))
        self.upAttackImages = ssA.images_at(((346, 120, 50, 65),(398, 120, 50, 65),(450, 120, 50, 65), (500, 120, 50, 65), (555, 120, 50, 65)), colorkey=(255, 255, 255))
        self.rightAttackImages = ssA.images_at(((331, 210, 65, 65),(387, 210, 65, 65),(445, 210, 65, 65), (508, 210, 65, 65), (515, 210, 65, 65)), colorkey=(255, 255, 255))
        
        self.leftAttackImages = []
        #scale images down
        for index in range(len(self.downAttackImages)):
            temp = pygame.transform.scale(self.downAttackImages[index], (20, 30))
            self.downAttackImages[index] = temp
        for index in range(len(self.upAttackImages)):
            temp = pygame.transform.scale(self.upAttackImages[index], (20, 30))
            self.upAttackImages[index] = temp
        for index in range(len(self.rightAttackImages)):
            temp = pygame.transform.scale(self.rightAttackImages[index], (20, 30))
            self.rightAttackImages[index] = temp
        #add left images
        for image in self.rightAttackImages:
            self.leftAttackImages.append(pygame.transform.flip(image, True, False))
            
        self.index = 0
        self.image = self.downImages[self.index]
        self.isAttacking = False
        self.health = 100
        self.keys = 0
        self.arrows = 0
        super().__init__(x, y, self.image, 10)
        
    def attack(self, keysDown, screenWidth, screenHeight):
        vx, vy = 0, 0

        if keysDown(pygame.K_LEFT):
            vx -= 2
            self.index += 1
            if self.index == 3*len(self.leftAttackImages):
                self.isAttacking = False
                self.index = 0
            self.image = self.leftAttackImages[self.index//3]

        if keysDown(pygame.K_RIGHT):
            vx += 2
            self.index += 1
            if self.index == 3*len(self.rightAttackImages):
                self.isAttacking = False
                self.index = 0
            self.image = self.rightAttackImages[self.index//3]

        if keysDown(pygame.K_UP):
            vy -= 2
            self.index += 1
            if self.index == 3*len(self.upAttackImages):
                self.isAttacking = False
                self.index = 0
            self.image = self.upAttackImages[self.index//3]
        
        if keysDown(pygame.K_DOWN):
            vy += 2
            self.index += 1
            if self.index == 3*len(self.downAttackImages):
                self.isAttacking = False
                self.index = 0
            self.image = self.downAttackImages[self.index//3]

        self.velocity = vx, vy
        super(Hero, self).update(screenWidth, screenHeight, self.image)
        
    def move(self, vx, vy, screenWidth, screenHeight):
        self.velocity = vx, vy
        super(Hero, self).update(screenWidth, screenHeight, self.image)

    def update(self, keysDown, screenWidth, screenHeight):
        vx, vy = 0, 0

        if keysDown(pygame.K_LEFT):
            vx -= 2
            self.index += 1
            if self.index == 6*len(self.leftImages):
                self.index = 0
            self.image = self.leftImages[self.index//6]

        if keysDown(pygame.K_RIGHT):
            vx += 2
            self.index += 1
            if self.index == 6*len(self.rightImages):
                self.index = 0
            self.image = self.rightImages[self.index//6]

        if keysDown(pygame.K_UP):
            vy -= 2
            self.index += 1
            if self.index == 6*len(self.upImages):
                self.index = 0
            self.image = self.upImages[self.index//6]
        
        if keysDown(pygame.K_DOWN):
            vy += 2
            self.index += 1
            if self.index == 6*len(self.downImages):
                self.index = 0
            self.image = self.downImages[self.index//6]

        self.velocity = vx, vy
        super(Hero, self).update(screenWidth, screenHeight, self.image)
        
