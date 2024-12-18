import pygame, random    

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


class Garbage():
    def __init__(self, screenW, screenH, amount):
        self.off = False
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.amount = amount
        self.speed = 3
        self.chromaKey = [250, 105, 130]
        self.image = pygame.image.load("Assets/Objects/spacial_garbage.png")
        self.image.set_colorkey(self.chromaKey)
        self.positionList = []
        self.rectList = []
        self.hit_count = 0
        self.garbage_count = 0
        self.fade_out = False
        self.fade_count = 0
        self.active_states = []
        

        for i in range(amount):
            self.xPosition = random.randrange(2, int(self.screenW - 95))
            self.yPosition = random.randrange(-500, -100)

            x_mov = random.randrange(-1, 2)
            self.garbageRect = self.image.get_rect(topleft=(self.xPosition, self.yPosition))
            self.positionList.append([self.xPosition, self.yPosition, x_mov])
            self.rectList.append(self.garbageRect)
            self.active_states.append(True)

        if screenW > 1920:
            scale_factor = 2.2
        else:
            scale_factor = 1.5

        new_size = (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor))
        self.scaled_image = pygame.transform.scale(self.image, new_size)
        self.scaled_image.set_colorkey(self.chromaKey)

    def draw(self, display):
        for i, position in enumerate(self.positionList):
            xP, yP, x_mov = position
            garbage_rect = self.rectList[i]

            if self.active_states[i]:
                if yP < self.screenH + 5:
                    yP += self.speed
                    xP += x_mov
                else:
                    xP = random.randrange(100, int(self.screenW - 250))
                    yP = random.randrange(-500, -100)
                    x_mov = random.randrange(-1, 2)

            self.positionList[i] = [xP, yP, x_mov]
            garbage_rect.topleft = (xP, yP)

        for i, rect in enumerate(self.rectList):
            if self.active_states[i]:
                display.blit(self.scaled_image, rect.topleft)


    def check_collisions(self, player):
        playerHeight = player.animation[0].get_height()
        player_rect = player.img_picker.get_rect(topleft=(player.xPosition, player.yPosition - (playerHeight * 0.8)))

        for i, r in enumerate(self.rectList):
            if self.active_states[i] and r.colliderect(player_rect) and player.action['d']:
                self.hit_count += 1
                self.active_states[i] = False
            elif self.active_states[i] and r.colliderect(player_rect):
                player.xPosition += random.randrange(-4,4)

    def reset_garbage(self, index):
        
        if not self.off:
            self.positionList[index] = [random.randrange(2, int(self.screenW - 95)), random.randrange(-600, -100)]
            self.rectList[index].topleft = self.positionList[index]
            self.active_states[index] = True

    def reset_all_garbage(self):
        for i in range(len(self.positionList)):
            self.reset_garbage(i)


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
        text_aux1 = self.font.render(" "+text_list[1] + " - " + str(health + 1)+" ",True,self.color,(0,0,0))
        text_aux2 = self.font.render(" "+text_list[2] + " - " + str(level)+" ",True,self.color,(0,0,0))
        if not self.full_hd:
            display.blit(text_aux0,(self.helth_position,25))
            display.blit(text_aux1,(self.helth_position,50))
            display.blit(text_aux2,(self.level_position,25))
        else:
            display.blit(text_aux0,(self.helth_position,33))
            display.blit(text_aux1,(self.helth_position,85))
            display.blit(text_aux2,(self.level_position,33))


class Chad():
    def __init__(self, screenW, screenH, lan):
        self.screenW = int(screenW)
        self.screenH = int(screenH)
        self.text = ''
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path,25)
        self.color = (160, 23, 208)
        self.lan_on = lan
        self.full_hd = False
        self.animation = []
        self.chroma = [250, 105, 130]
        self.animation.append(pygame.image.load("Assets/Objects/Chad0.png").convert())
        self.animation.append(pygame.image.load("Assets/Objects/Chad1.png").convert())
        self.animation.append(pygame.image.load("Assets/Objects/Chad2.png").convert())
        self.animation[0].set_colorkey(self.chroma)
        self.animation[1].set_colorkey(self.chroma)
        self.animation[2].set_colorkey(self.chroma)
        self.text_timer = 0
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 200 

        if screenW > 1920 or screenH > 1080:
            self.full_hd = True
            self.level_position = self.screenW - 480
            self.font = pygame.font.Font(self.font_path, 40)
        

    def draw(self, display, text):
        current_time = pygame.time.get_ticks()

        if current_time > self.animation_timer:
            self.animation_index = (self.animation_index + 1) % len(self.animation)
            self.animation_timer = current_time + self.animation_speed

        current_animation = pygame.transform.scale(
            self.animation[self.animation_index],
            (80, 85) if not self.full_hd else (90, 95)
        )

        if text != self.text:
            self.text = text
            self.text_timer = current_time + 5000

        if text != '' and current_time < self.text_timer:
            max_width = self.screenW * 0.5

            words = text.split(' ')
            lines = []
            current_line = ''

            for word in words:
                test_line = current_line + ' ' + word if current_line else word
                test_text = self.font.render(test_line, True, (255, 255, 255))
                if test_text.get_width() <= max_width:
                    current_line = test_line
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)

            rect_width = self.screenW
            rect_height = self.screenH * 0.17
            rect_surface = pygame.Surface((rect_width, rect_height))
            rect_surface.set_alpha(100)
            rect_surface.fill((0, 0, 0))
            display.blit(rect_surface, (0, 0))

            y_offset = rect_height // 2 - len(lines) * self.font.get_height() // 2 + 20
            for line in lines:
                text_aux0 = self.font.render(line, True, (255, 255, 255))
                text_rect = text_aux0.get_rect(center=(self.screenW // 2, y_offset))
                display.blit(text_aux0, text_rect)
                y_offset += self.font.get_height() 

            display.blit(current_animation, (self.screenW // 24, self.screenH // 8))

        if text == '' or current_time > self.text_timer:
            if not self.full_hd:
                display.blit(pygame.transform.scale(self.animation[2], (80, 85)), (self.screenW // 24, self.screenH // 8))
            else:
                display.blit(pygame.transform.scale(self.animation[2], (90, 95)), (self.screenW // 24, self.screenH // 8))



"""
class PlatformSpeed():
    def __init__(self):
        self.xPosition = 500
        self.yPosition = 500
        self.image1 = pygame.image.load("Assets/Objects/platform1.png")
        self.image2 = pygame.image.load("Assets/Objects/platform2.png")
        self.chromaKey = [1, 7, 27]
"""