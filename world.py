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

            pygame.draw.circle(display,self.white,(self.xP, self.yP),1)

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[1]=-5
                i[0]=random.randrange((self.screenW-(self.screenW+5)),(self.screenW-5))
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.speed=3
                if event.key==pygame.K_LEFT:
                    i[0]+=2
                if event.key==pygame.K_RIGHT:
                    i[0]-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.speed=1.5

class Meteorite():
    def __init__(self, screenW, screenH):
        self.screenW=screenW
        self.screenH=screenH
        self.speed=4
        self.chromaKey=([1,7,27])
        self.positionList=[]
        self.rectList=[]
        self.demageList=[]
        self.Img0=pygame.image.load('Assets\Objects\Demage (1).png')
        self.Img0.set_colorkey([255,255,255])
        self.Img1=pygame.image.load('Assets\Objects\Demage (2).png')
        self.Img1.set_colorkey([255,255,255])
        self.Img2=pygame.image.load('Assets\Objects\Demage (3).png')
        self.Img2.set_colorkey([255,255,255])
        self.Img3=pygame.image.load('Assets\Objects\Demage (4).png')
        self.Img3.set_colorkey([255,255,255])
        self.demageList.append(self.Img0)
        self.demageList.append(self.Img1)
        self.demageList.append(self.Img2)
        self.demageList.append(self.Img3)
        for i in range(6):
            self.xPosition=random.randrange(int((self.screenW-(self.screenW/4*3))),int((self.screenW/4*3)))
            self.yPosition=random.randrange(-750,-100)
            self.img=pygame.image.load("Assets/Objects/meteorite.png")
            self.rect=self.img.get_rect()
            self.img=pygame.transform.rotate(self.img, random.randrange(-90,90))
            self.img.set_colorkey(self.chromaKey)
            self.positionList.append([self.xPosition, self.yPosition, self.img, self.rect])
           # self.rectList.append(self.rect)


    def drawMeteorite(self, display, event, player):
        for i in self.positionList:
            self.xP=i[0]
            self.yP=i[1]

            display.blit(i[2],[self.xP, self.yP])

            if(i[1]<self.screenH+5):
                i[1]+=self.speed
            else:
                i[0]=random.randrange(int((self.screenW-(self.screenW/4*3))),int((self.screenW/4*3)))
                i[1]=random.randrange(-750,-100)
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.speed=8
                if event.key==pygame.K_LEFT:
                    i[0]+=4
                if event.key==pygame.K_RIGHT:
                    i[0]-=4
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    self.speed=4


#colliders fail/ check player get_rect() and rectList in meteorite

