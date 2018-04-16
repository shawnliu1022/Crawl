'''
Ship.py

implements the Ship class, which defines the player controllable ship
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import math
from GameObject import GameObject
import spritesheet
from spritestripanim import SpriteStripAnim

class Hero(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...
    @staticmethod
    def init():
        Hero.heroImage = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/player/base/human_m.png').convert_alpha(),
            (60, 60)), 0)
            
        
        # Sprite is 16x16 pixels at location 0,0 in the file...
        #Hero.image = ss.image_at((50, 50, 50, 50))
        # Load two images into an array, their transparent bit is (255, 255, 255)
        

    def __init__(self, x, y):
        ss = spritesheet.Spritesheet('sprites.gif')
        self.images = ss.images_at(((50, 50, 50, 50),(110, 50, 44, 50),(155, 50, 42, 50), (200, 50, 40, 50), (245, 50, 40, 50)), colorkey=(255, 255, 255))
        self.index = 0
        self.image = self.images[self.index]
        super().__init__(x, y, self.image, 15)

    def update(self, keysDown, screenWidth, screenHeight):
        vx, vy = 0, 0

        if keysDown(pygame.K_LEFT):
            vx -= 3

        if keysDown(pygame.K_RIGHT):
            vx += 3

        if keysDown(pygame.K_UP):
            vy -= 3
        
        if keysDown(pygame.K_DOWN):
            vy += 3
            self.index += 1
            if self.index == 7*len(self.images):
                self.index = 0
            
        self.image = self.images[self.index//7]
        self.velocity = vx, vy
        super(Hero, self).update(screenWidth, screenHeight, self.image)
        
