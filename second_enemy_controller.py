import pygame
import random

class Enemy_2:
    def __init__(self, display):
        self.display = display
        self.screenW, self.screenH = display.get_size()
        self.hd = self.screenW > 1920
        self.speed = 2
        self.rotation_speed = 0.3
        self.chroma_key = [250, 105, 130]
        self.enemy_sprite = pygame.image.load("Assets/Objects/enemy_2.png").convert_alpha()
        self.enemy_sprite.set_colorkey(self.chroma_key)

        scale_factor = 4 if self.hd else 3
        original_size = self.enemy_sprite.get_size()
        self.scaled_img = pygame.transform.scale(
            self.enemy_sprite,
            (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        )

        self.mask = pygame.mask.from_surface(self.scaled_img)

        self.x = random.randint(self.screenW // 3, self.screenW // 3 * 2)
        self.y = self.screenH
        self.angle = 0
        self.rotation_direction = random.choice([-1, 1])
        self.passes = 0
        self.center_positioned = False

    def draw(self):
        rotated_image = pygame.transform.rotate(self.scaled_img, self.angle).convert_alpha()
        rotated_image.set_colorkey(self.chroma_key)
        rect = rotated_image.get_rect(center=(self.x, self.y))

        self.display.blit(rotated_image, rect.topleft)

        self.y -= self.speed
        self.angle += self.rotation_speed * self.rotation_direction

        if self.y + rect.height < 0:
            self.passes += 1
            if self.passes < 5:
                self.y = self.screenH
                self.x = random.randint(0, self.screenW // 3)
                self.rotation_direction = random.choice([-1, 1])
                self.center_positioned = False
            else:
                self.speed = 0
                self.rotation_speed = 0

    def check_collisions(self, player):
        """
        Detecta colisiones con el jugador.
        Si el jugador colisiona con los bordes del enemigo, devuelve 'collision'.
        Si el jugador entra en el centro del enemigo, se posiciona en su centro y devuelve 'centered'.
        """
        player_mask = pygame.mask.from_surface(player.image)
        offset = (int(self.x - player.x), int(self.y - player.y))

        overlap = self.mask.overlap(player_mask, offset)

        if overlap:
            mask_pos = (overlap[0], overlap[1])
            if self.mask.get_at(mask_pos) == 1:
                if not self.center_positioned:
                    return 'collision'
            else:
                if not self.center_positioned:
                    self.center_positioned = True
                    player.x = self.x
                    player.y = self.y
                    return 'centered'

        return None
