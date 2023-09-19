import pygame, random

class Player():
    def __init__(self, xPosition, yPosition,screenHeight, screenWidth) -> None:
        self.xPosition=int(xPosition)
        self.xPositionInit=int(xPosition)
        self.yPosition=int(yPosition)
        self.yPositionInit=int(yPosition)
        self.minXPosition=int(screenWidth/4)
        self.maxXPosition=int(screenWidth/4*3)
        self.score=0
        self.health=5
        self.animation=[]
        self.animation.append(pygame.image.load("Assets/Player/spacecraft.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft1.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft2.png").convert())
        self.animation[0].set_colorkey([1,6,26])
        self.animation[1].set_colorkey([1,7,27])
        self.animation[2].set_colorkey([1,7,27])
        self.rect0=self.animation[0].get_rect()
        self.rect1=self.animation[1].get_rect()
        self.rect2=self.animation[2].get_rect()
        self.rectList=[]
        self.rectList.append(self.rect0)
        self.rectList.append(self.rect1)
        self.rectList.append(self.rect2)
        self.frame=0
        self.keyDownCount=0  # control for "self.frame", this select the img/animation in "drawPlayer()"
        self.maxYPosition=int(screenHeight-(screenHeight/1.5))  # highest coord-Y for the player in the screen
        self.minYPosition=int(screenHeight-120)
        self.slowArea=int(self.maxYPosition+(self.maxYPosition/2))
        self.up=False
        self.down=False
        self.left=False
        self.right=False
        self.leftDown=False
        self.rightDown=False
        self.aux=None
        self.collided = False
     
    def setPlayer(self, name):
        self.name=name

    def movePlayer(self, event):
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                self.up=True
            if event.key==pygame.K_LEFT:
                self.left=True
            if event.key==pygame.K_RIGHT:
                self.right=True
            if event.key==pygame.K_DOWN:
                self.down=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                self.up=False
            if event.key==pygame.K_LEFT:
                self.left=False
            if event.key==pygame.K_RIGHT:
                self.right=False
            if event.key==pygame.K_DOWN:
                self.down=False

            if event.key==pygame.K_UP and event.key==pygame.K_LEFT:
                self.up=False
                self.left=False
            if event.key==pygame.K_UP and event.key==pygame.K_RIGHT:
                self.up=False
                self.right=False

        if(self.up and self.yPosition>self.maxYPosition):
            self.keyDownCount+=1
            if(self.yPosition>=self.slowArea):
                self.yPosition-=4
            else:
                self.yPosition-=1

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False
                if event.key==pygame.K_UP:
                    self.up=False

        if(self.down):

            self.up=False
            self.keyDownCount=0
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False
            if(self.yPosition<self.yPositionInit):
                self.yPosition+=2

        if(not self.up and self.yPosition<self.yPositionInit):
            self.yPosition+=1
            self.keyDownCount=0
        

        if(self.right and self.xPosition<self.maxXPosition):
            self.left=False
            self.xPosition+=4
            if(not self.down):
                self.keyDownCount+=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.up=False

        if(self.left and self.xPosition>self.minXPosition):
            self.right=False
            self.xPosition-=4
            if(not self.down):
                self.keyDownCount+=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.up=False

        if(self.yPosition<self.maxYPosition):
            self.up=False
            self.left=False
            self.right=False

        for i in range(len(self.rectList)):
            self.rectList[i].x = self.xPosition
            self.rectList[i].y = self.yPosition

    def drawPlayer(self, display):

        if(self.keyDownCount==0):
            self.frame=0
        elif(self.keyDownCount%2==0):
            self.frame=1
        else:
            self.frame=2

        display.blit(self.animation[self.frame], [self.xPosition, self.yPosition])