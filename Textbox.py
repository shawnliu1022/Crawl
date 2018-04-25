import pygame
from GameObject import GameObject
class Textbox(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.boxSurface = pygame.Surface((width, height))
        self.text = ""
        
    def addText(self, ch):
        self.text += chr
        
    def displayText(self, screen):
        screen.blit(self.boxSurface, (self.x, self.y))
        font = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = font.render(self.text, False, (255, 210, 0))
        screen.blit(textsurface, (self.x+10, self.y+10))
        
    def updateText(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode