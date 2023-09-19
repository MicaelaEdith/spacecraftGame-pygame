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
            self.xPosition=random.randrange(int(self.screenW/8),int((screenW/8*7)))
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
                i[0]=random.randrange(int(self.screenW/8),int((self.screenW/8*7)))
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.speed=3
                if event.key==pygame.K_LEFT:
                    i[0]+=2
                if event.key==pygame.K_RIGHT and i[0]>1:
                    i[0]-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.speed=1
            if i[0]<1:
                i[1]=self.screenH+4

class Meteorite():
    def __init__(self, screenW, screenH):
        self.screenW=int(screenW)
        self.screenH=int(screenH)
        self.speed=4
        self.chromaKey=([1,7,27])
        self.image=pygame.image.load("Assets/Objects/meteorite.png")
        self.image.set_colorkey(self.chromaKey)
        self.positionList=[]
        self.rectList=[]

        for i in range(10):
            self.xPosition=random.randrange(int((self.screenW-(self.screenW/4*3))),int((self.screenW/4*3)))
            self.yPosition=random.randrange(-1000,-100)
            self.meteoriteRect = self.image.get_rect()
            self.meteoriteRect.x = self.xPosition
            self.meteoriteRect.y = self.yPosition
            self.positionList.append([self.xPosition, self.yPosition])
            self.rectList.append(self.meteoriteRect)


    def draw(self, display, event):
        for i, position in enumerate(self.positionList):
            xP, yP = position
<<<<<<< HEAD
            meteorite_rect = self.rectList[i]  
=======
            meteorite_rect = self.rectList[i]
>>>>>>> 717db8891534329d2f5189b18b5d9a7d58fe163f

            if yP < self.screenH + 5:
                yP += self.speed
            else:
                yP = random.randrange(-700, -100)
                xP = random.randrange(int((self.screenW - (self.screenW / 4 * 3.5))), int((self.screenW / 4 * 3.5)))

            self.positionList[i] = [xP, yP]
<<<<<<< HEAD
            meteorite_rect.x, meteorite_rect.y = xP, yP 
=======
            meteorite_rect.x, meteorite_rect.y = xP, yP
>>>>>>> 717db8891534329d2f5189b18b5d9a7d58fe163f



        for i in self.positionList:
            display.blit(self.image, [i[0], i[1]])

        for i in self.positionList:
            self.xP=i[0]
            self.yP=i[1]

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[1]=random.randrange(-700,-100)
                i[0]=random.randrange(int((self.screenW-(self.screenW/4*3.5))),int((self.screenW/4*3.5)))
            
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

        
