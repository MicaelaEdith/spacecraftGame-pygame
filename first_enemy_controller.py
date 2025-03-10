import pygame
import random
import math

class Enemy:
    def __init__(self, display, amount):
        self.display = display
        self.screenW, self.screenH = display.get_size()
        self.hd = self.screenW > 1920
        self.amount = amount
        
        self.speed = 2
        self.rotation_speed = 0.3
        self.shoot_radius = 4
        if self.hd:
            self.shoot_radius = 7
        self.bullet_speed = 5

        self.enemy_sprite = pygame.image.load("Assets/Objects/enemy_1.png")
        self.enemy_sprite.set_colorkey([250, 105, 130])

        self.enemies = []
        self.rect_list = []
        self.angles = []
        self.distance_travelled = []
        self.bullets = []
        self.shoot_intervals = []
        
        for _ in range(self.amount):
            speed = random.randrange(1, 3)
            rotation_speed = random.uniform(-1, 1)
            shoot_radius = random.randint(4, 8) if self.hd else 4

            x = random.randint(int(self.screenW//10*2),int(self.screenW/10*8))
            y = random.randint(-700, -50)
            rect = self.enemy_sprite.get_rect(topleft=(x, y))

            scale_factor = 1.5 if self.hd else 1
            scaled_image = pygame.transform.scale(
                self.enemy_sprite, (int(self.enemy_sprite.get_width() * scale_factor), int(self.enemy_sprite.get_height() * scale_factor))
            )

            self.enemies.append(scaled_image)
            self.rect_list.append(rect)
            self.angles.append(random.uniform(0, 360))
            self.distance_travelled.append(0)
            self.shoot_intervals.append(random.randint(160, 350))
            
            self.speed = speed
            self.rotation_speed = rotation_speed
            self.shoot_radius = shoot_radius


    def draw(self):
        for i, rect in enumerate(self.rect_list):
            if not hasattr(self, 'animating_destroy') or not self.animating_destroy or self.animating_enemy_index != i:
                rect.y += self.speed
                self.angles[i] += self.rotation_speed
                rotated_image = pygame.transform.rotate(self.enemies[i], self.angles[i])
                rotated_image.set_colorkey([250, 105, 130])
                rotated_rect = rotated_image.get_rect(center=rect.center)
                self.display.blit(rotated_image, rotated_rect.topleft)

                self.distance_travelled[i] += self.speed
                if self.distance_travelled[i] >= self.shoot_intervals[i]:
                    self.shoot(rect.center, self.angles[i])
                    self.distance_travelled[i] = 0

                if rect.y > self.screenH:
                    rect.y = random.randint(-500, -50)
                    rect.x = random.randint(int(self.screenW//10*2),int(self.screenW/10*8))

        self.update_bullets()
        self.update_animation() 


    def shoot(self, position, angle):
        radians = math.radians(angle)
        direction_x = math.cos(radians)
        direction_y = math.sin(radians)

        bullet = {
            "x": position[0],
            "y": position[1],
            "dx": int(direction_x * self.bullet_speed),
            "dy": int(direction_y * self.bullet_speed)
        }
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet["x"] += bullet["dx"]
            bullet["y"] += bullet["dy"]

            if (bullet["x"] < 0 or bullet["x"] > self.screenW or 
                bullet["y"] < 0 or bullet["y"] > self.screenH):
                self.bullets.remove(bullet)
                continue

            pygame.draw.circle(self.display, (255, 255, 0), (int(bullet["x"]), int(bullet["y"])), self.shoot_radius)


    def destroy_enemy(self, enemy_rect):
        for i, rect in enumerate(self.rect_list):
            if rect == enemy_rect:
                self.animate_destroy(i)
                break
    
    def animate_destroy(self, enemy_index):
        self.animating_destroy = True
        self.animating_enemy_index = enemy_index
        self.animation_timer = 0

    def update_animation(self):
        if hasattr(self, 'animating_destroy') and self.animating_destroy:
            i = self.animating_enemy_index
            rect = self.rect_list[i]

            scale_factor = max(0.1, 1 - self.animation_timer * 0.05)
            self.angles[i] += 20

            rotated_image = pygame.transform.rotozoom(self.enemies[i], self.angles[i], scale_factor)
            rotated_image.set_colorkey([250, 105, 130])
            rotated_rect = rotated_image.get_rect(center=rect.center)

            self.display.blit(rotated_image, rotated_rect.topleft)

            self.animation_timer += 1

            if scale_factor <= 0.1:
                self.remove_enemy(i)
                self.animating_destroy = False


    def remove_enemy(self, enemy_index):
        del self.rect_list[enemy_index]
        del self.enemies[enemy_index]
        del self.angles[enemy_index]
        del self.distance_travelled[enemy_index]
        del self.shoot_intervals[enemy_index]