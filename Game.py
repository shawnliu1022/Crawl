'''
Game.py

Actually implements the game
Code taken from Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import math
from Map import Map
from Hero import Hero
from pygamegame import PygameGame
import random

from Camera import *
from Leaderboard import *
from Textbox import *
from Monster import Monster
from Demon import Demon
from Fireball import Fireball

from tiles import Floor
from tiles import Wall
from tiles import Door
from tiles import OpenDoor
from tiles import Stairs


class Game(PygameGame):
    def init(self):
        pygame.font.init()
        self.bgColor = (0, 0, 0)
        self.map = Map()
        self.mapArray = self.map.mapLayout.mapArr
        self.camera = Camera(complex_camera, len(self.mapArray[0])*32, len(self.mapArray)*32)
        self.leaderboard = Leaderboard()
        self.textbox = Textbox(self.width/2 - 150, self.height/2+100, 300, 50)
        
        self.floorTiles = pygame.sprite.Group()
        self.wallTiles = pygame.sprite.Group()
        self.doorTiles = pygame.sprite.Group()
        self.openDoorTiles = pygame.sprite.Group()
        self.stairs = pygame.sprite.GroupSingle()
        for row in range(len(self.mapArray)):
            for col in range(len(self.mapArray[row])):
                if self.mapArray[row][col] == 0:
                    tile = Floor.Floor(col*32, row*32)
                    self.floorTiles.add(tile)
                elif self.mapArray[row][col] == 2:
                    tile = Wall.Wall(col*32, row*32)
                    self.wallTiles.add(tile)
                elif self.mapArray[row][col]==3:
                    tile = Door.Door(col*32, row*32)
                    self.doorTiles.add(tile)
                elif self.mapArray[row][col]==4:
                    tile = OpenDoor.OpenDoor(col*32, row*32)
                    self.openDoorTiles.add(tile)
                elif self.mapArray[row][col]==9:
                    tile = Stairs.Stairs(col*32, row*32)
                    self.stairs.add(tile)
                else:
                    continue
                    
        self.hero = Hero(random.randint(0, self.width), random.randint(0, self.height))
        self.heroGroup = pygame.sprite.GroupSingle(self.hero)
        while (not (pygame.sprite.groupcollide(self.heroGroup, self.floorTiles, False, False, pygame.sprite.collide_rect))  
         or pygame.sprite.groupcollide(self.heroGroup, self.wallTiles, False, False, pygame.sprite.collide_rect)):
            self.hero = Hero(random.randint(0, self.width), random.randint(0, self.height))
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            
        self.monsterGroup = pygame.sprite.Group()
        self.monsterGroup.add(Demon(random.randint(self.hero.x-50,self.hero.x+50),
            random.randint(self.hero.y-50,self.hero.y+50)))
        self.fireballGroup = pygame.sprite.Group()
        self.timePassed = 0
        
        #Game states
        self.gameOver = False
        self.win = False
        self.high_scores = False
        self.done = False
    def keyPressed(self, code, mod):
        if code == pygame.K_SPACE:
            self.hero.index = 0
            self.hero.isAttacking = True

    def timerFired(self, dt):
        if self.gameOver or self.win:
            return
        self.timePassed += 1
        if self.hero.isAttacking:
            self.hero.attack(self.isKeyPressed, self.width, self.height)
        else:
            self.heroGroup.update(self.isKeyPressed, self.width, self.height)
        if pygame.sprite.groupcollide(self.heroGroup, self.wallTiles, False, False, pygame.sprite.collide_rect):
            self.hero.move(-self.hero.velocity[0], -self.hero.velocity[1], self.width, self.height)
            
        if pygame.sprite.groupcollide(self.heroGroup, self.stairs, False, False, pygame.sprite.collide_rect):
            self.win = True
            self.totalTime = pygame.time.get_ticks()/1000
            
        #move monsters
        for monster in self.monsterGroup:
            monster.moveTowardsPlayer(self.hero, self.width, self.height)
                
        if self.timePassed % 60 == 0:
            for monster in self.monsterGroup:
                #create fireball
                fireball = Fireball(monster.x, monster.y)
                dx, dy = self.hero.x - monster.x, self.hero.y - monster.y
                dist = math.hypot(dx, dy)
                if dist == 0: break
                dx, dy = dx / dist, dy / dist
                fireball.velocity = dx * 3, dy * 3
                self.fireballGroup.add(fireball)
                
        for fireball in self.fireballGroup:
            fireball.move(self.width, self.height)
            #for wall in self.wallTiles:
                #if pygame.sprite.collide_circle(fireball, wall):
                    #self.fireballGroup.remove(fireball)
            if pygame.sprite.collide_circle(fireball, self.hero):
                self.hero.health -= 10
                self.fireballGroup.remove(fireball)
                if self.hero.health == 0:
                    self.gameOver = True
                    self.totalTime = pygame.time.get_ticks()/1000
        
            
####################################################
#Drawing functions
####################################################
    def displayHealthBar(self, screen):
        emptyBar = pygame.transform.scale(pygame.image.load("images/player/EmptyBar.png"), (200, 20))
        healthBar = pygame.transform.scale(pygame.image.load("images/player/RedBar.png"), (200, 20))
        crop_rect=(0, 0, self.hero.health*2, 20)
        croppedHealth = healthBar.subsurface(crop_rect)
        screen.blit(emptyBar, (20, 20, 200, 200))
        screen.blit(croppedHealth, (20, 20, 200, 200))
        
    def displayTimer(self, screen):
        if self.gameOver or self.win:
            timePassed = self.totalTime
        else:
            timePassed = pygame.time.get_ticks()/1000
        font = pygame.font.SysFont('Times New Roman', 25)
        textsurface = font.render(str(timePassed), False, (255, 255, 255))
        screen.blit(textsurface, (self.width - 100, 25))

    def redrawAll(self, screen):
        if self.done:
            self.leaderboard.displayScores(screen, self.width)
            return
        if self.high_scores == True:
            self.leaderboard.addScore(self.textbox.text, self.timePassed)
            self.leaderboard.displayScores(screen, self.width)
            self.done = True
            return
        self.camera.update(self.hero)
        #self.tiles.draw(screen)
        for e in self.floorTiles:
            screen.blit(e.image, self.camera.apply(e))
        for e in self.wallTiles:
            screen.blit(e.image, self.camera.apply(e))
        for e in self.doorTiles:
            screen.blit(e.image, self.camera.apply(e))
        for e in self.openDoorTiles:
            screen.blit(e.image, self.camera.apply(e))
        for e in self.stairs:
            screen.blit(e.image, self.camera.apply(e))
        for hero in self.heroGroup:
            screen.blit(hero.image, self.camera.apply(hero))
        for monster in self.monsterGroup:
            screen.blit(monster.image, self.camera.apply(monster))
        for fireball in self.fireballGroup:
            screen.blit(fireball.image, self.camera.apply(fireball))
        self.displayHealthBar(screen)
        self.displayTimer(screen)
        if self.gameOver:
            font = pygame.font.SysFont('Comic Sans MS', 65)
            textsurface = font.render('Congratulations! You Died!', False, (255, 48, 48))
            screen.blit(textsurface, (0, self.height/2-30))
        elif self.win:
            font = pygame.font.SysFont('Comic Sans MS', 65)
            textsurface = font.render('Congratulations! You Win!', False, (255, 215, 0))
            screen.blit(textsurface, (0, self.height/2-200))
            font2 = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface2 = font2.render('Input your name here:', False, (255, 210, 0))
            screen.blit(textsurface2, (self.width/2 - 150, self.height/2))
            if self.textbox.updateText() == True:
                self.high_scores = True
            self.textbox.displayText(screen)
        #self.heroGroup.draw(screen)

Game(800, 500).run()
