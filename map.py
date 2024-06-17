import pygame, random

class Deep():
	def __init__(self,  screenW, screenH):
		self.blue=(1, 4, 19)
		self.deep = pygame.Surface((screenW, screenH))
		self.deep.set_alpha(random.randrange(1,20))
		
	def drawDeep(self, display):
		while True:
			self.deep.set_alpha(random.randrange(1,20))
		display.blit(self.deep, (0,0))
		
		
		


class Starts():
    def __init__(self, screenW, screenH):
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.white = (241, 240, 245)
        self.positionList = []
        self.speed = 1
        self.quiet = False
        for i in range(50):
            self.xPosition = random.randrange((self.screenW - (screenW + 10)), (screenW + 10))
            self.xPosition = random.randrange(1, int(screenW - 1))
            self.yPosition = random.randrange(-5, self.screenH)
            self.positionList.append([self.xPosition, self.yPosition])

    def drawStarts(self, display):
        for i in self.positionList:
            self.xP = i[0]
            self.yP = i[1]

            pygame.draw.circle(display, self.white, (int(self.xP), int(self.yP)), 1)
            if not self.quiet: 
                if(i[1] < self.screenH + 5):
                    i[1] += self.speed
                else:
                    i[1] = -5
                    i[0] = random.randrange(1, int(self.screenW - 1))
            else:
                if(i[1] < self.screenH + 2.5):
                    i[1] += self.speed
                else:
                    i[1] = -2.5
                    i[0] = random.randrange(1, int(self.screenW - 1))

class Meteorite():
    def __init__(self, screenW, screenH):
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.speed = 2
        self.chromaKey = [1, 7, 27]
        self.image = pygame.image.load("Assets/Objects/meteorite.png")
        self.image.set_colorkey(self.chromaKey)
        self.positionList = []
        self.rectList = []

        for i in range(4):
            self.xPosition = random.randrange(2, int(self.screenW - 95))
            self.yPosition = random.randrange(-1000, -100)
            self.meteoriteRect = self.image.get_rect(topleft=(self.xPosition, self.yPosition))
            self.positionList.append([self.xPosition, self.yPosition])
            self.rectList.append(self.meteoriteRect)

    def draw(self, display):
        for i, position in enumerate(self.positionList):
            xP, yP = position
            meteorite_rect = self.rectList[i]

            if yP < self.screenH + 5:
                yP += self.speed
            else:
                yP = random.randrange(-700, -100)
                xP = random.randrange(2, int(self.screenW - 95))

            self.positionList[i] = [xP, yP]
            meteorite_rect.topleft = (xP, yP)

        for rect in self.rectList:
            display.blit(self.image, rect.topleft)


"""
class PlatformSpeed():
    def __init__(self):
        self.xPosition = 500
        self.yPosition = 500
        self.image1 = pygame.image.load("Assets/Objects/platform1.png")
        self.image2 = pygame.image.load("Assets/Objects/platform2.png")
        self.chromaKey = [1, 7, 27]
"""