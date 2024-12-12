import pygame, random
    
class Deep:
    def __init__(self, width, height, speed, line_length, line_spacing, color):
        self.width = width
        self.height = height
        self.color = color + (128,)
        self.speed = speed
        self.line_length = line_length
        self.line_spacing = line_spacing
        self.lines = []
        self.generate_lines()

    def generate_lines(self):
        self.lines.clear()
        x = 0
        y = 0
        while y < self.height:
            self.lines.append((x, y, self.line_length))
            y += self.line_spacing
            x -= 3

    def move_lines(self):
        for i in range(len(self.lines)):
            line = list(self.lines[i])
            line[0] += self.speed
            if line[0] > self.width:
                line[0] -= self.width + self.line_length - random.randrange(-500, 500)
            self.lines[i] = tuple(line)

    def drawDeep(self, display):
        for line in self.lines:
            pygame.draw.line(display, self.color, (line[0], line[1]), (line[0] + line[2], line[1]), 3)

        self.move_lines()

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
        self.off = False
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.speed = 5
        self.chromaKey = [250, 105, 130]
        self.image = pygame.image.load("Assets/Objects/meteorite_.png")
        self.image.set_colorkey(self.chromaKey)
        self.positionList = []
        self.rectList = []
        self.hit_count = [0] * 4
        self.explosion_images = []
        self.scaled_images = []
        self.metorites_count = 0
        self.fade_out = False
        self.fade_count = 0

        for i in range(10):
            self.xPosition = random.randrange(2, int(self.screenW - 95))
            self.yPosition = random.randrange(-1000, -100)
            self.meteoriteRect = self.image.get_rect(topleft=(self.xPosition, self.yPosition))
            self.positionList.append([self.xPosition, self.yPosition])
            self.rectList.append(self.meteoriteRect)

            scale_factor = random.uniform(1.5, 2)
            new_size = (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor))
            scaled_image = pygame.transform.scale(self.image, new_size)

            scaled_image.set_colorkey(self.chromaKey)
            self.scaled_images.append(scaled_image)

        for i in range(1, 5):
            image = pygame.image.load(f"Assets/Objects/Demage ({i}).png")
            self.explosion_images.append(image)
            self.explosion_images[i - 1].set_colorkey([0, 1, 21])

        self.explosion_frame = 0
        self.explosion_active = [False] * 4
        self.explosion_timer = [0] * 4

    def draw(self, display):
        for i, position in enumerate(self.positionList):
            xP, yP = position
            meteorite_rect = self.rectList[i]

            if yP < self.screenH + 5 and not self.fade_out:
                yP += self.speed
            elif not self.off:
                self.metorites_count += 1
                yP = random.randrange(-700, -100)
                xP = random.randrange(2, int(self.screenW - 95))

            self.positionList[i] = [xP, yP]
            meteorite_rect.topleft = (xP, yP)

            if self.fade_out:
                self.scaled_images[i].set_alpha(255 - self.fade_count)
                self.fade_count += 0.8

        for i, rect in enumerate(self.rectList):
            if self.positionList[i][1] < self.screenH + 5:
                display.blit(self.scaled_images[i], rect.topleft)

        for i, active in enumerate(self.explosion_active):
            if active:
                self.draw_explosion(display, i)


    def check_collisions(self, player):
        if self.off:
            return

        for i, rect in enumerate(self.rectList):
            for shoot in player.shoots:
                if rect.colliderect(shoot):
                    player.shoots.remove(shoot)
                    self.hit_count[i] += 1
                    if self.hit_count[i] >= 2:
                        self.explosion_active[i] = True
                        self.explosion_timer[i] = 0
                        self.hit_count[i] = 0
                        self.reset_meteorite(i)

    def draw_explosion(self, display, index):
        if self.explosion_active[index]:
            timer = self.explosion_timer[index]
            if timer == 0 or timer % 10 == 0:
                self.explosion_frame += 0.2
                if self.explosion_frame >= len(self.explosion_images):
                    self.explosion_active[index] = False
                    self.explosion_frame = 0
            if int(self.explosion_frame) < len(self.explosion_images) and (self.explosion_frame - int(self.explosion_frame) == 0):
                display.blit(self.explosion_images[int(self.explosion_frame)], (self.positionList[index][0] - 30, self.positionList[index][1] - 25))
            self.explosion_timer[index] += 1

    def reset_meteorite(self, index):
        if not self.off:
            self.positionList[index] = [random.randrange(2, int(self.screenW - 95)), random.randrange(-700, -100)]
            self.rectList[index].topleft = self.positionList[index]


class Status():
    def __init__(self, screenW, screenH, lan):
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.helth_position = 40
        self.level_position = self.screenW - 300
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path,25)
        self.text_en = ['Points','Health', 'Level']
        self.text_es = ['Puntos','Salud', 'Nivel']
        self.color = (160, 23, 208)
        self.lan_on = lan
        self.health = 0
        self.level = 0
        self.full_hd = False
        self.animation = []
        self.animation.append(pygame.image.load("Assets/Buttons/Chad0.png"))
        self.animation.append(pygame.image.load("Assets/Buttons/Chad1.png"))
        self.animation.append(pygame.image.load("Assets/Buttons/Chad2.png"))
        self.animation[0].set_colorkey([71, 60, 120])
        self.animation[1].set_colorkey([71, 60, 120])
        self.animation[2].set_colorkey([71, 60, 120])

        if screenW > 1920 or screenH > 1080:
            self.full_hd = True
            self.level_position = self.screenW - 480
            self.font = pygame.font.Font(self.font_path, 40)
        

    def updateStatus(self,health, level):
        self.health = health
        self.level = level 

    def draw(self, display, level, health, points, lan):
        self.lan_on = lan

        if self.lan_on == 'en':
            text_list = self.text_en
        else:
            text_list = self.text_es
        
        text_aux0 = self.font.render(" "+text_list[0] + " - " + str(points)+" ",True,self.color,(0,0,0))
        text_aux1 = self.font.render(" "+text_list[1] + " - " + str(health)+" ",True,self.color,(0,0,0))
        text_aux2 = self.font.render(" "+text_list[2] + " - " + str(level)+" ",True,self.color,(0,0,0))
        if not self.full_hd:
            display.blit(text_aux0,(self.helth_position,25))
            display.blit(text_aux1,(self.helth_position,50))
            display.blit(text_aux2,(self.level_position,25))
            aux_h = 20+ (text_aux1.get_height() + text_aux0.get_height())
            display.blit(pygame.transform.scale(self.animation[0], (80,85)), (self.screenW // 24 , aux_h))
        else:
            display.blit(text_aux0,(self.helth_position,33))
            display.blit(text_aux1,(self.helth_position,85))
            display.blit(text_aux2,(self.level_position,33))

"""
class PlatformSpeed():
    def __init__(self):
        self.xPosition = 500
        self.yPosition = 500
        self.image1 = pygame.image.load("Assets/Objects/platform1.png")
        self.image2 = pygame.image.load("Assets/Objects/platform2.png")
        self.chromaKey = [1, 7, 27]
"""