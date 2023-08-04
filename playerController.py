import pygame

class Player():
    def __init__(self, xPosition, yPosition,screenHeight, screenWidth) -> None:
        self.xPosition=xPosition
        self.xPositionInit=xPosition
        self.yPosition=yPosition
        self.yPositionInit=yPosition
        self.minXPosition=screenWidth/4
        self.maxXPosition=screenWidth/4*3
        self.point=0
        self.health=5
        self.animation=[]
        self.animation.append(pygame.image.load("Assets/Player/spacecraft.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft1.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft2.png").convert())
        self.animation[0].set_colorkey([1,6,26])
        self.animation[1].set_colorkey([1,6,26])
        self.animation[2].set_colorkey([1,6,26])
        self.rect=self.animation[0].get_rect()
        self.rect=self.animation[1].get_rect()
        self.rect=self.animation[2].get_rect()
        self.frame=0
        self.keyDownCount=0  # control for "self.frame", this select the img/animation in "drawPlayer()"
        self.maxYPosition=screenHeight-(screenHeight/1.5)
        self.minYPosition=screenHeight-120
        self.slowArea=self.maxYPosition+(self.maxYPosition/2)
        self.up=False
        self.left=False
        self.right=False
        self.leftDown=False
        self.rightDown=False
        self.aux=None
     
    def setPlayer(self, name):
        self.name=name

    def movePlayer(self, event):

        if event.type==pygame.KEYDOWN:
            self.keyDownCount+=1.5
            if event.key==pygame.K_LEFT and self.xPosition>=self.minXPosition:
                self.left=True
            if event.key==pygame.K_RIGHT and self.xPosition<=self.maxXPosition:
                self.right=True
            if event.key==pygame.K_UP and self.yPosition>=self.maxYPosition:
                self.up=True 
            if event.key==pygame.K_DOWN and self.yPosition<=self.minYPosition:
                self.keyDownCount=0
                self.yPosition+=1.5

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                self.up=False
            if event.key==pygame.K_LEFT:
                self.left=False
            if event.key==pygame.K_RIGHT:
                self.right=False

        if(self.right and self.xPosition<self.maxXPosition and not self.up):
            self.xPosition+=3
            self.left=False
        if(self.left and self.xPosition>self.minXPosition and not self.up):
            self.xPosition-=3
            self.right=False

        if(self.up and self.yPosition>=self.maxYPosition):
            if(self.yPosition<self.slowArea):
                if(self.left and(self.xPosition>self.minXPosition)):
                    self.xPosition-=1.5
                    self.yPosition-=2
                elif(self.right and (self.xPosition<self.maxXPosition)):
                    self.xPosition+=1.5
                    self.yPosition-=2
                else:
                    self.yPosition-=2
            else:
                if(self.left and (self.xPosition>self.minXPosition)):
                    self.xPosition-=3
                    self.yPosition-=4
                elif(self.right and (self.xPosition<self.maxXPosition)):
                    self.xPosition+=3
                    self.yPosition-=4
                else:
                    self.yPosition-=4
        else:
            self.keyDownCount=0
            if(self.yPosition<self.yPositionInit):
                self.yPosition+=1
        
    def drawPlayer(self, display):
        if(self.keyDownCount==0):
            self.frame=0
        elif(self.keyDownCount%2==0):
            self.frame=1
        else:
            self.frame=2

        display.blit(self.animation[self.frame], [self.xPosition, self.yPosition])