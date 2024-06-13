import pygame
from data import Data

class Menu():
	def __init__(self, screenWidth, screenHeight):
		self.init_menu = pygame.Surface((screenWidth, screenHeight))
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

