'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
from Hero import Hero
from pygamegame import PygameGame
import random


class Game(PygameGame):
    def init(self):
        self.bgColor = (0, 0, 0)
        Hero.init()
        hero = Hero(self.width / 2, self.height / 2)
        self.heroGroup = pygame.sprite.GroupSingle(hero)

    def keyPressed(self, code, mod):
        pass

    def timerFired(self, dt):
        self.heroGroup.update(self.isKeyPressed, self.width, self.height)

        hero = self.heroGroup.sprite

    def redrawAll(self, screen):
        self.heroGroup.draw(screen)

Game(800, 500).run()
