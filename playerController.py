import pygame

class Player():
    def __init__(self, xPosition, yPosition, screenHeight, screenWidth) -> None:
        self.xPosition = int(xPosition)
        self.xPositionInit = int(xPosition)
        self.yPosition = int(yPosition)
        self.yPositionInit = int(yPosition)
        self.minXPosition = int(screenWidth / 6)
        self.maxXPosition = int(screenWidth / 6 * 4.5)
        self.score = 21
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
        self.minYPosition = int(screenHeight - 170)
        self.slowArea = int(self.maxYPosition + (self.maxYPosition / 2))
        self.angle = 0
        self.collided = False
        self.explosion_images = []
        self.shoot_type_a = False  # Bandera para el tipo de bala A
        self.shoot_type_b = False  # Bandera para el tipo de bala B
        self.shoots_fired = []
        self.quiet = True

        self.pick_images = [
            pygame.image.load("Assets/Objects/picker0.png").convert(),
            pygame.image.load("Assets/Objects/picker1.png").convert()
        ]
        self.pick_frame = 0  # Frame actual de la animación de recogida

        for img in self.pick_images:
            img.set_colorkey([1, 7, 27])

        self.pick_type = 0  # Tipo de imagen de recogida actual
        self.pick_delay = 100  # Delay entre recogidas
        self.last_pick_time = pygame.time.get_ticks()  # Tiempo del último recogido
        self.pick_active = False  # Bandera para indicar si se está recogiendo algo

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
        self.shoot_delay =50
        self.last_shoot_time = pygame.time.get_ticks()
        self.shoot_changed = False  # Nueva bandera para controlar el cambio de tipo de bala

    def setPlayer(self, name):
        self.name = name

    def movePlayer(self):
        return_speed = 1  # Velocidad de retorno gradual hacia la posición inicial

        # Lógica para el movimiento hacia arriba
        if self.movement['up'] and self.yPosition > self.maxYPosition:
            self.keyDownCount += 1
            self.quiet = False
            if self.yPosition >= self.slowArea-2:
                self.yPosition -= 4 * self.speed
            else:
                self.yPosition -= 1 * self.speed

        # Lógica para el movimiento hacia abajo
        if self.movement['down']:
            self.movement['up'] = False
            self.quiet = False
            self.keyDownCount = 0
            if self.yPosition < self.yPositionInit:
                self.yPosition += 2
        elif not self.movement['up'] and self.yPosition < self.yPositionInit:
            self.quiet = True

        # Lógica para el movimiento hacia la derecha
        if self.movement['right'] and self.xPosition < self.maxXPosition-2:
            self.movement['left'] = False
            self.quiet = False
            self.xPosition += 4
            if not self.movement['down']:
                self.keyDownCount += 1
        elif not self.movement['right'] and self.xPosition > self.xPositionInit:
            self.quiet = True

        # Lógica para el movimiento hacia la izquierda
        if self.movement['left'] and self.xPosition > self.minXPosition-1:
            self.quiet = False
            self.movement['right'] = False
            self.xPosition -= 4
            if not self.movement['down']:
                self.keyDownCount += 1
        elif not self.movement['left'] and self.xPosition < self.xPositionInit-1:
            self.quiet = True
        
        if self.quiet:      # Movimiento de retorno gradual hacia la posición inicial
            if self.xPosition < self.xPositionInit:
                self.xPosition += return_speed
            elif self.xPosition > self.xPositionInit:
                self.xPosition -= return_speed
            if self.yPosition < self.yPositionInit:
                self.yPosition += return_speed
            elif self.yPosition > self.yPositionInit:
                self.yPosition -= return_speed

        # Actualizar las posiciones de los rectángulos
        for i in range(len(self.rectList)):
            self.rectList[i].x = self.xPosition
            self.rectList[i].y = self.yPosition

        for i in range(len(self.rectList)):
            self.rectList[i].topleft = (self.xPosition, self.yPosition)

    def actions(self):
        if self.action['a'] and not self.shoot_type_a:  # Verificar si el tipo de bala A no ha sido disparado
            self.shoot_type_a = True  # Establecer la bandera a True para evitar múltiples disparos continuos
        if self.action['b']:
            self.shoot_changed = True  # Marcar que el tipo de disparo ha cambiado
            self.shoot_type = (self.shoot_type + 1) % len(self.shoot_images)  # Cambiar el tipo de disparo

    def resetActions(self):
        self.movement['a'] = False
        self.movement['b'] = False
        self.movement['c'] = False
            
    def updateShoots(self):
        current_time = pygame.time.get_ticks()
        if self.action['a'] and not self.shoot_type_a:
            if current_time - self.last_shoot_time > self.shoot_delay:
                shoot_rect = self.shoot_images[self.shoot_type].get_rect(midbottom=(self.xPosition + self.rect0.width // 2, self.yPosition))
                self.shoots_fired.append({'rect': shoot_rect, 'type': self.shoot_type})
                self.last_shoot_time = current_time
                self.shoot_type_a = True  # Marcar que se ha disparado
        elif not self.action['a']:
            self.shoot_type_a = False  # Restablecer para permitir disparos en futuros clicks

        for shoot in self.shoots_fired:
            shoot['rect'].y -= 11 if shoot['type'] == 0 else 14  # Velocidad de los disparos según el tipo de bala

        self.shoots_fired = [shoot for shoot in self.shoots_fired if shoot['rect'].bottom > 0]

    def updatePick(self):
        current_time = pygame.time.get_ticks()
        if self.action['d']:
            if current_time - self.last_pick_time > self.pick_delay:
                self.pick_active = True
                self.last_pick_time = current_time
        else:
            self.pick_active = False

    def drawShoots(self, display):
        for shoot in self.shoots_fired:
            display.blit(self.shoot_images[shoot['type']], shoot['rect'].topleft)

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

        if self.quiet and not self.movement['up']:
            self.frame = 0

        rotated_image = pygame.transform.rotate(self.original_images[self.frame], self.angle)
        display.blit(rotated_image, [self.xPosition, self.yPosition])
    
        # Dibujar disparos
        self.drawShoots(display)



    def drawPick(self, display):
        if self.action['d']:
            display.blit(self.pick_images[int(self.pick_frame)], [self.xPosition, self.yPosition -75])
            self.pick_frame -=.1
            self.pick_frame = (self.pick_frame + (self.pick_frame-int(self.pick_frame))) % len(self.pick_images)  # Alternar entre las dos imágenes


    def drawExplosion(self, display):        
        if self.explosion_active:
            if self.explosion_timer == 0 or self.explosion_timer % 10 == 0:
                self.explosion_frame += .2
                if self.explosion_frame >= len(self.explosion_images):
                    self.explosion_active = False
                    self.explosion_frame = 0
            if int(self.explosion_frame) < len(self.explosion_images) and (self.explosion_frame-int(self.explosion_frame)==0):
                display.blit(self.explosion_images[int(self.explosion_frame)], (self.xPosition-30, self.yPosition-25))