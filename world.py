import pygame, random

class Starts():
    def __init__(self, screenW, screenH):
        self.screenW=screenW
        self.screenH=screenH
        self.white=(240,240,240)
        self.positionList=[]
        self.speed=1
        for i in range(50):
            self.xPosition=random.randrange((self.screenW-(screenW+10)),(screenW+10))
            self.yPosition=random.randrange(-5,self.screenH)
            self.positionList.append([self.xPosition, self.yPosition])

    def drawStarts(self, display, event):
        for i in self.positionList:
            self.xP=i[0]
            self.yP=i[1]

            pygame.draw.circle(display,self.white,(self.xP, self.yP),2)

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[1]=-5
                i[0]=self.xPosition=random.randrange((self.screenW-(self.screenW+5)),(self.screenW-5))
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.speed=3
                if event.key==pygame.K_LEFT:
                    i[0]+=2
                if event.key==pygame.K_RIGHT:
                    i[0]-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.speed=1

            



"""
        self.screenW=screenW
        self.positionList=[]

        for i in range(20):
            self.xPosition=random.randrange((self.screenW-(screenW+5)),(screenW-5))
            self.yPosition=-5
            self.positionList.append([self.xPosition,self.yPosition])
    
    def drawStart(self, event, display, color, screenH):

        for i in self.positionList:
            pygame.draw.circle(display, color, (self.xPosition, self.yPosition),1.5)


            
            if(self.yPosition<screenH+5):
                self.yPosition+=1.5
                if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                        self.xPosition+=2
                    if event.key==pygame.K_RIGHT:
                        self.xPosition-=2
            else:
                self.xPosition=random.randrange((self.screenW-(self.screenW+5)),(self.screenW-5))
                self.yPosition=-5
            pygame.draw.circle(display, color, (self.xPosition, self.yPosition),1.5)
"""
            
    
