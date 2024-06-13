import pygame
from data import Data

class Menu():
	def __init__(self, screenWidth, screenHeight):
		self.init_menu = pygame.Surface((screenWidth, screenHeight))
		self.init_menu.set_alpha(5)
		self.init_menu.fill((50,50,50))
		
		
	def draw(self, display):
		display.blit(self.init_menu, (0, 0))


class Pause():
	def __init__(self, screenWidth,screenHeight):
		self.start_menu = pygame.Surface((screenWidth, screenHeight))
		self.start_menu.set_alpha(5)
		self.start_menu.fill((30,30,30))

	def draw(self, display):
		display.blit(self.start_menu, (0, 0))


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