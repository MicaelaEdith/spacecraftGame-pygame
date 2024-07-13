import pygame

class Intro():
    def __init__(self, screenWidth, screenHeight):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((55, 55, 55))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path, 50)
        self.language = ['en', 'es']
        self.lan_on = 'en'
        self.text_en = 'CONTINUE'
        self.text_es = 'CONTINUAR'
        self.text=''
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []

    def draw(self, display, lan):
        self.lan_on = lan
        display.blit(self.init_menu, (0, 0))
        self.buttons = []  # Reinicia la lista de botones
        text_color = (160, 23, 208)
        if self.lan_on == 'en':
            self.text = self.text_en
        else:
            self.text = self.text_es

        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=(self.width // 6 * 5, self.height // 8 * 6))
        mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse

        # Verificar si el mouse está sobre el botón
        if text_rect.collidepoint(mouse_pos):
            text_color = (251, 206, 60)  # Cambia el color del texto cuando el mouse está sobre él
            text_surface = self.font.render(self.text, True, text_color)
        else:
            text_surface = self.font.render(self.text, True, text_color)
            text_color = (160, 23, 208)

        display.blit(text_surface, text_rect.topleft)
        self.buttons.append((self.text, text_rect))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for text, rect in self.buttons:
                if rect.collidepoint(mouse_pos):
                    return self.handle_click(text)
        return None

    def handle_click(self, text):
        if text == self.text_en or text == self.text_es:
            return 'continue' 
        return None
