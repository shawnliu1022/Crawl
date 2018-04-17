'''
Game.py

Actually implements the game
Code taken from Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
from Map import Map
from Hero import Hero
from pygamegame import PygameGame
import random


class Game(PygameGame):
    def init(self):
        self.bgColor = (0, 0, 0)
        self.map = Map()
        self.map.drawMap(800, 500)
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
