import pygame
from data import Data
class Menu():
	def __init__(self, screenWidth, screenHeight):
		self.init_menu = pygame.Surface((screenWidth, screenHeight))
		self.init_menu.set_alpha(5)
		self.init_menu.fill((50,50,50))
		self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
		self.font = pygame.font.Font(self.font_path,35)
		self.text = self.font.render("Tango triste en un asteroide",0,(200,50,150))
		self.width = screenWidth
		self.height = screenHeight
		
	def draw(self, display):
		display.blit(self.init_menu, (0, 0))
		display.blit(self.text,(80,self.height / 6 *4))

class MainMenu():
    def __init__(self, screenWidth, screenHeight):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((50, 50, 50))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path, 50)
        self.language = ['en', 'es']
        self.lan_on = 'en'
        self.text_en = ['NEW GAME', 'LOAD', 'OPTIONS', 'EXIT']
        self.text_es = ['JUEGO NUEVO', 'CARGAR', 'OPCIONES', 'SALIR']
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []

    def draw(self, display):
        display.blit(self.init_menu, (0, 0))
        self.buttons = []  # Reinicia la lista de botones
        contador = 1
        if self.lan_on == 'en':
            text_list = self.text_en
        else:
            text_list = self.text_es

        mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse

        for i in text_list:
            text_color = (160, 23, 208)
            text_aux = self.font.render(i, True, text_color)
            text_rect = text_aux.get_rect(topleft=(80, self.height / 4 * contador))

            # Verificar si el mouse está sobre el botón
            if text_rect.collidepoint(mouse_pos):
                text_color = (251, 206, 60)  # Cambia el color del texto cuando el mouse está sobre él
                text_aux = self.font.render(i, True, text_color)

            display.blit(text_aux, text_rect.topleft)
            self.buttons.append((i, text_rect))
            contador += .7

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for text, rect in self.buttons:
                if rect.collidepoint(mouse_pos):
                    return self.handle_click(text)
        return None

    def handle_click(self, text):
        if text == 'NEW GAME' or text == 'JUEGO NUEVO':
            print("Start a new game")
            return 'new_game'
        elif text == 'LOAD' or text == 'CARGAR':
            print("Load game")
            return 'load_game'
        elif text == 'OPTIONS' or text == 'OPCIONES':
            print("Options menu")
            return 'options'
        elif text == 'EXIT' or text == 'SALIR':
            print("Exit game")
            pygame.quit()
            exit()
        return None

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

