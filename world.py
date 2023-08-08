import pygame, random

class Starts():
    def __init__(self, screenW, screenH):
        self.screenW=int(screenW)
        self.screenH=int(screenH)
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

            pygame.draw.circle(display,self.white,(int(self.xP), int(self.yP)),1)

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[1]=-5
                i[0]=random.randrange(int((self.screenW-(self.screenW+5))),int((self.screenW-5)))
            
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

class Meteorite():
    def __init__(self, screenW, screenH):
        self.screenW=int(screenW)
        self.screenH=int(screenH)
        self.speed=4
        self.chromaKey=([1,7,27])
        self.image=pygame.image.load("Assets/Objects/meteorite.png")
        self.image.set_colorkey(self.chromaKey)
        self.rect=self.image.get_rect()
        self.positionList=[]
        self.rectList=[]

        for i in range(8):
            self.xPosition=random.randrange(int((self.screenW-(self.screenW/4*3))),int((self.screenW/4*3)))
            self.yPosition=random.randrange(-1000,-100)
            #self.image=pygame.transform.rotate(self.image, random.randrange(-90,90))
            #self.image.set_colorkey(self.chromaKey)
            self.positionList.append([self.xPosition, self.yPosition])
            self.rectList.append(self.rect)

    def draw(self, display, event):
        for i in self.positionList:
            display.blit(self.image, [i[0], i[1]])

        for i in self.positionList:
            self.xP=i[0]
            self.yP=i[1]

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[1]=random.randrange(-700,-100)
                i[0]=random.randrange(int((self.screenW-(self.screenW/4*3))),int((self.screenW/4*3)))
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.speed=4
                if event.key==pygame.K_LEFT:
                    i[0]+=2
                if event.key==pygame.K_RIGHT:
                    i[0]-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.speed=2
    