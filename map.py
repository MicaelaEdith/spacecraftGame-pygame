import pygame, random

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
        else:
            self.clicked = False

class Starts():
    def __init__(self, screenW, screenH):
        self.screenW=int(screenW)
        self.screenH=int(screenH)
        self.white=(240,240,240)
        self.positionList=[]
        self.speed=1
        self.quiet=False
        for i in range(50):
            self.xPosition=random.randrange((self.screenW-(screenW+10)),(screenW+10))
            self.xPosition=random.randrange(int(self.screenW/8),int((screenW/8*7)))
            self.yPosition=random.randrange(-5,self.screenH)
            self.positionList.append([self.xPosition, self.yPosition])

    def drawStarts(self, display):
        for i in self.positionList:
            self.xP=i[0]
            self.yP=i[1]

            pygame.draw.circle(display,self.white,(int(self.xP), int(self.yP)),1)
            if not self.quiet: 
                if(i[1]<self.screenH+5):
                    i[1]+=self.speed
                else:
                    i[1]=-5
                    i[0]=random.randrange(int(self.screenW/8),int((self.screenW/8*7)))
            else:
                if(i[1]<self.screenH+2.5):
                    i[1]+=self.speed
                else:
                    i[1]=-2.5
                    i[0]=random.randrange(int(self.screenW/8),int((self.screenW/8*7)))


"""
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
            meteorite_rect = self.rectList[i]  

            if yP < self.screenH + 5:
                yP += self.speed
            else:
                yP = random.randrange(-700, -100)
                xP = random.randrange(int((self.screenW - (self.screenW / 4 * 3.5))), int((self.screenW / 4 * 3.5)))

            self.positionList[i] = [xP, yP]
            meteorite_rect.x, meteorite_rect.y = xP, yP 



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

class PlatformSpeed():
    def __init__(self):
        self.xPosition=500
        self.yPosition=500
        self.image1=pygame.image.load("Assets/Objects/platform1.png")
        self.image2=pygame.image.load("Assets/Objects/platform2.png")
        self.chromaKey=([1,7,27])
        self.image1.set_colorkey(self.chromaKey)
        self.image2.set_colorkey(self.chromaKey)
        self.image=self.image1
        self.rect=self.image.get_rect()
        self.turboSpeed=False
        self.count=0

    def draw(self, display):
        if (self.count%2==0):
            self.image=self.image2
            self.count+=.5
        else:
            self.image=self.image1
            self.count+=.5

        display.blit(self.image,[self.xPosition,self.yPosition])
        
"""