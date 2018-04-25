import pygame
class Leaderboard(object):
    def __init__(self):
        self.path = "leaderboard.txt"
        self.scores = self.readFile(self.path).splitlines()
        self.font = pygame.font.SysFont("Times New Roman", 30)
        
    def readFile(self, path):
        with open(path, "rt") as f:
            return f.read()
            
    def writeFile(self, path, contents):
        with open(path, "wt") as f:
            f.write(contents)
        
    def addScore(self, name, t):
        allScores = ""
        lastElem = True
        print(len(self.scores))
        if len(self.scores)==0:
            self.scores.append(name+","+str(t/1000))
        else:
            for index in range(len(self.scores)):
                score = self.scores[index].split(",")[1]
                print(t, float(score))
                if t/1000 < float(score):
                    self.scores.insert(index, name+","+str(t/1000))
                    lastElem = False
                    break
            if lastElem:
                self.scores.append(name+","+str(t/1000))
        print(self.scores)
        for l in self.scores:
            elems = l.split(",")
            name, score = elems[0], str(elems[1])
            allScores += (name + "," + score + "\n")
        self.writeFile(self.path, allScores)
        
    def displayScores(self, screen, screenWidth):
        scores = self.readFile(self.path)
        lines = scores.splitlines()
        for index in range(len(lines)):
            line = lines[index]
            elems = line.split(",")
            name, score = elems[0], str(elems[1])
            textsurface=self.font.render(name+"................................."+score, False, (255, 255, 255))
            screen.blit(textsurface, (100, index * 30))
            