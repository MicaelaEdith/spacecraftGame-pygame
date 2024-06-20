import pygame
#from data import Data
class Menu():
	def __init__(self, screenWidth, screenHeight):
		self.init_menu = pygame.Surface((screenWidth, screenHeight))
		self.init_menu.set_alpha(5)
		self.init_menu.fill((50,50,50))
		self.font = pygame.font.Font(None,50)
		self.text = self.font.render("Tango triste en un asteroide",0,(200,50,150))
		self.width = screenWidth
		self.height = screenHeight
		
	def draw(self, display):
		display.blit(self.init_menu, (0, 0))
		display.blit(self.text,(60,self.height / 6 *4))


class Pause():
	def __init__(self, screenWidth,screenHeight):
		self.start_menu = pygame.Surface((screenWidth, screenHeight))
		self.start_menu.set_alpha(5)
		self.start_menu.fill((30,30,30))

	def draw(self, display):
		display.blit(self.start_menu, (0, 0))

class Button:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos, pressed):
        if self.rect.collidepoint(pos):
            self.clicked = pressed
        return self.clicked

