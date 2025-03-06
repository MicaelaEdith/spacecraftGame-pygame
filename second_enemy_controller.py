import pygame
import random

class Enemy_2:
    def __init__(self, display, position):
        self.display = display
        self.screenW, self.screenH = display.get_size()
        self.hd = self.screenW > 1920
        self.speed = 2
        self.rotation_speed = 0.3
        self.position = position

        self.enemy_sprite = pygame.image.load("Assets/Objects/enemy_2.png").convert_alpha()

        scale_factor = 3 if self.hd else 2
        original_size = self.enemy_sprite.get_size()
        self.scaled_img = pygame.transform.scale(
            self.enemy_sprite,
            (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        ).convert_alpha()

        self.mask = pygame.mask.from_surface(self.scaled_img)

        #self.x = random.randint(self.screenW // 3, self.screenW // 3 * 2)
        self.x= (self.screenW // 3) * self.position
        self.y = random.randint(int(self.screenH * 1.1), int(self.screenH * 1.6))
        #self.y = self.screenH * 2
        self.angle = 0
        self.rotation_direction = random.choice([-1, 1])
        self.passes = 0
        self.center_positioned = False

        self.opacity = 255
        self.opacity_direction = -15

    def draw(self):
        rotated_image = pygame.transform.rotate(self.scaled_img, self.angle).convert_alpha()
        rotated_image.fill((255, 255, 255, self.opacity), special_flags=pygame.BLEND_RGBA_MULT)
        
        rect = rotated_image.get_rect(center=(self.x, self.y))
        self.display.blit(rotated_image, rect.topleft)

        self.y -= self.speed
        self.angle += self.rotation_speed * self.rotation_direction

        if self.y + rect.height < 0:
            self.passes += 1
            if self.passes < 5:
                self.y = self.screenH + rect.height
                self.x = random.randint(self.screenW // 3, self.screenW // 3 * 2)
                self.rotation_direction = random.choice([-1, 1])
                self.center_positioned = False
            else:
                self.speed = 0
                self.rotation_speed = 0


    def update_opacity(self):
        self.opacity += self.opacity_direction
        if self.opacity <= 100 or self.opacity >= 255:
            self.opacity_direction *= -1


    def check_collisions(self, player):
        player_mask = pygame.mask.from_surface(player.image)
        offset = (int(self.x - player.xPosition), int(self.y - player.yPosition))

        overlap = self.mask.overlap(player_mask, offset)

        if overlap:
            enemy_rect = self.scaled_img.get_rect(center=(self.x, self.y))
            third_width = enemy_rect.width // 3
            third_height = enemy_rect.height // 3

            central_rect = pygame.Rect(
                self.x - third_width // 2, 
                self.y - third_height // 2, 
                third_width, 
                third_height
            )


            if central_rect.collidepoint(player.xPosition, player.yPosition):
                self.center_positioned = True
                player.x = self.x
                player.y = self.y
                return False


            self.update_opacity()
            return True

        return False


