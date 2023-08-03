import pygame, random

class Starts():
    def __init__(self, screenW):
        self.screenW=screenW
        self.xPosition=random.randrange((self.screenW-(screenW+5)),(screenW-5))
        self.yPosition=-5
    
    def drawStart(self, display, color, screenH):
        if(self.yPosition<screenH+5):
            self.yPosition+=1.5
        else:
            self.xPosition=random.randrange((self.screenW-(self.screenW+5)),(self.screenW-5))
            self.yPosition=screenH


        pygame.draw.circle(display, color, (self.xPosition, self.yPosition),2)
        
