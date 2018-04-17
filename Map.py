#Map.py draws the map created by MapLayout.
from MapLayout import MapLayout
import pygame
from tiles import Floor
from tiles import Wall
from tiles import Door
from tiles import Portal

class Map:
    def __init__(self):
        self.startx=60   # map width
        self.starty=60   # map height
        self.mapLayout = MapLayout()
        self.mapLayout.makeMap(self.startx,self.starty,80,50,60)
        for y in range(self.starty):
                line = ""
                for x in range(self.startx):
                        if self.mapLayout.mapArr[y][x]==0:
                                line += "."
                        if self.mapLayout.mapArr[y][x]==1:
                                line += " "
                        if self.mapLayout.mapArr[y][x]==2:
                                line += "#"
                        if (self.mapLayout.mapArr[y][x]==3 or self.mapLayout.mapArr[y][x]==4 
                           or self.mapLayout.mapArr[y][x]==5):
                                line += "="
                print (line)
        
    def drawMap(self, screenWidth, screenHeight):
        for row in range(self.starty):
            for col in range(self.startx):
                if self.mapLayout.mapArr[row][col] == 1:
                    tile = Floor.Floor(col*32, row*32)
                elif self.mapLayout.mapArr[row][col] == 3:
                    tile = Wall.Wall(col*32, row*32)
                elif self.mapLayout.mapArr[row][col]==4:
                    tile = Door.Door(col*32, row*32)
                elif self.mapLayout.mapArr[row][col]==5:
                    tile = Portal.Portal(col*32, row*32)
                else:
                    continue
                tile.update(screenWidth, screenHeight, tile.image)
        
                
                