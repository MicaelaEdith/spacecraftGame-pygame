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
        self.keyDownCount = 0
        self.maxYPosition = int(screenHeight - (screenHeight / 1.2))
        self.minYPosition = int(screenHeight - 120)
        self.slowArea = int(self.maxYPosition + (self.maxYPosition / 2))
        self.angle = 0
        self.collided = False
        self.explosion_images = []

        for i in range(1, 5):
            image = pygame.image.load(f"Assets/Objects/Demage ({i}).png")
            self.explosion_images.append(image)
            self.explosion_images[i-1].set_colorkey([0,1,21])
                          
        self.explosion_frame = 0
        self.explosion_active = False
        self.explosion_timer = 0

        self.movement = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }
        self.action = {
        	'a': False,
        	'b': False,
        	'c': False,
        	'd': False
        }

        # Disparo
        self.shoot_images = [
            pygame.image.load("Assets/Objects/shoot0.png").convert(),
            pygame.image.load("Assets/Objects/shoot1.png").convert(),
            pygame.image.load("Assets/Objects/shoot2.png").convert()
        ]
        for img in self.shoot_images:
            img.set_colorkey([0, 1, 20])
        
        self.shoots = []
        self.shoot_type = 0
        self.shoot_delay = 500
        self.last_shoot_time = pygame.time.get_ticks()

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

        for i in range(len(self.rectList)):
            self.rectList[i].topleft = (self.xPosition, self.yPosition)

    def actions(self):
        if self.action['a']:
            self.action['b'] = False
            self.speed =12
        if self.action['b']:
            self.action['a'] = False
            self.speed = 1	

    def updateShoots(self):
        current_time = pygame.time.get_ticks()
        if self.action['a'] and current_time - self.last_shoot_time > self.shoot_delay:
            shoot_rect = self.shoot_images[self.shoot_type].get_rect(midbottom=(self.xPosition + self.rect0.width // 2, self.yPosition))
            self.shoots.append(shoot_rect)
            self.last_shoot_time = current_time

        for shoot in self.shoots:
            shoot.y -= 5  # Velocidad de los disparos

        self.shoots = [shoot for shoot in self.shoots if shoot.bottom > 0]

        if self.action['b']:
            self.shoot_type = (self.shoot_type + 1) % len(self.shoot_images)
            self.action['b'] = False

    def drawShoots(self, display):
        for shoot in self.shoots:
            display.blit(self.shoot_images[self.shoot_type], shoot.topleft)

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
        
        # Dibujar disparos
        self.drawShoots(display)

    def drawExplosion(self, display):        
        if self.explosion_active:
            if self.explosion_timer == 0 or self.explosion_timer % 10 == 0:
                self.explosion_frame += .2
                if self.explosion_frame >= len(self.explosion_images):
                    self.explosion_active = False
                    self.explosion_frame = 0
            if int(self.explosion_frame) < len(self.explosion_images) and (self.explosion_frame-int(self.explosion_frame)==0):
                display.blit(self.explosion_images[int(self.explosion_frame)], (self.xPosition-30, self.yPosition-25))
            self.explosion_timer += 1
