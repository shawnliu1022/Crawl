#Map.py draws the map created by MapLayout.
from MapLayout import MapLayout
import pygame
from tiles import Floor
from tiles import Wall
from tiles import Door
from tiles import OpenDoor

class Map:
    def __init__(self):
        self.startx=60   # map width
        self.starty=60   # map height
        self.mapLayout = MapLayout()
        self.mapLayout.makeMap(self.startx,self.starty,80,25,60)
        
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
                        if self.mapLayout.mapArr[y][x]==9:
                                line += "!"
                print (line)
        
                
                