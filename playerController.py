import pygame 

class Player():
    def __init__(self, xPosition, yPosition, screenHeight, screenWidth) -> None:
        self.xPosition = int(xPosition)
        self.xPositionInit = int(xPosition)
        self.yPosition = int(yPosition)
        self.yPositionInit = int(yPosition)
        self.minXPosition = int(screenWidth / 6)
        self.maxXPosition = int(screenWidth / 6 * 4.5)
        self.score = 0
        self.speed = 1
        self.health = 5
        self.animation = []
        self.animation.append(pygame.image.load("Assets/Player/spacecraft0.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft1.png").convert())
        self.animation.append(pygame.image.load("Assets/Player/spacecraft2.png").convert())
        self.animation[0].set_colorkey([1, 6, 26])
        self.animation[1].set_colorkey([1, 7, 27])
        self.animation[2].set_colorkey([1, 7, 27])
        self.original_images = self.animation.copy()
        self.rect0 = self.animation[0].get_rect()
        self.rect1 = self.animation[1].get_rect()
        self.rect2 = self.animation[2].get_rect()
        self.rectList = []
        self.rectList.append(self.rect0)
        self.rectList.append(self.rect1)
        self.rectList.append(self.rect2)
        self.frame = 0
        self.keyDownCount = 0  # control for "self.frame", this select the img/animation in "drawPlayer()"
        self.maxYPosition = int(screenHeight - (screenHeight / 1.2))  # highest coord-Y for the player in the screen
        self.minYPosition = int(screenHeight - 120)
        self.slowArea = int(self.maxYPosition + (self.maxYPosition / 2))
        self.angle = 0
        self.collided = False
        self.movement = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

    def setPlayer(self, name):
        self.name = name

    def movePlayer(self):
        if self.movement['up'] and self.yPosition > self.maxYPosition:
            self.keyDownCount += 1
            if self.yPosition >= self.slowArea:
                self.yPosition -= 4 * self.speed
            else:
                self.yPosition -= 1 * self.speed

        if self.movement['down']:
            self.movement['up'] = False
            self.keyDownCount = 0
            if self.yPosition < self.yPositionInit:
                self.yPosition += 2

        if not self.movement['up'] and self.yPosition < self.yPositionInit:
            self.yPosition += 1
            self.keyDownCount = 0

        if self.movement['right'] and self.xPosition < self.maxXPosition:
            self.movement['left'] = False
            self.xPosition += 4
            if not self.movement['down']:
                self.keyDownCount += 1

        if self.movement['left'] and self.xPosition > self.minXPosition:
            self.movement['right'] = False
            self.xPosition -= 4
            if not self.movement['down']:
                self.keyDownCount += 1

        for i in range(len(self.rectList)):
            self.rectList[i].x = self.xPosition
            self.rectList[i].y = self.yPosition

    def drawPlayer(self, display):
        if self.keyDownCount == 0:
            self.frame = 0
        elif self.keyDownCount % 2 == 0:
            self.frame = 1
        else:
            self.frame = 2

        if self.movement['left']:
            self.angle = -4
        elif self.movement['right']:
            self.angle = 4
        else:
            self.angle = 0

        rotated_image = pygame.transform.rotate(self.original_images[self.frame], self.angle)
        display.blit(rotated_image, [self.xPosition, self.yPosition])