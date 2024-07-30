import pygame
from script_dialogues import *

class Intro():
    def __init__(self, screenWidth, screenHeight):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((55, 55, 55))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        font_size = int(screenHeight * 0.05)
        self.font = pygame.font.Font(self.font_path, font_size)
        self.language = ['en', 'es']
        self.lan_on = 'en'
        self.text_en = 'CONTINUE'
        self.text_es = 'CONTINUAR'
        self.text=''
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []
        self.count = 0
        self.animation = []
        self.animation.append(pygame.image.load("Assets/Buttons/1980/Chad0.png").convert())
        self.animation.append(pygame.image.load("Assets/Buttons/1980/Chad1.png").convert())
        self.animation.append(pygame.image.load("Assets/Buttons/1980/Chad2.png").convert())
        self.animation[0].set_colorkey([255, 224, 9])
        self.animation[1].set_colorkey([255, 224, 9])
        self.animation[2].set_colorkey([255, 224, 9])


    def draw(self, display, lan, count):
        self.count = count
        self.lan_on = lan
        display.blit(self.init_menu, (0, 0))
        self.buttons = []  # Reinicia la lista de botones
        text_color = (160, 23, 208)
        text_color_dialog = (160, 23, 208)
        dialog = ''

        if self.lan_on == 'en':
            self.text = self.text_en
        else:
            self.text = self.text_es

        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=(self.width // 7 * 6, self.height // 8 * 6.8))
        mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse

        # Verificar si el mouse está sobre el botón
        if text_rect.collidepoint(mouse_pos):
            text_color = (251, 206, 60)  # Cambia el color del texto cuando el mouse está sobre él
            text_surface = self.font.render(self.text, True, text_color)
        else:
            text_surface = self.font.render(self.text, True, text_color)
            text_color = (160, 23, 208)

        if lan == 'en':
            aux_dialog = intro_script_en
        else:
            aux_dialog = intro_script_es
        
        if self.count == 0:
            dialog = aux_dialog[0]
            dialog_surface = self.font.render(dialog, True, text_color_dialog)
            pos_dialog=(self.width // 7 * 1, self.height // 8 * 1.5)
        elif self.count == 1:
            dialog = aux_dialog[1]
            dialog_surface = self.font.render(dialog, True, text_color_dialog)
            pos_dialog=(self.width // 7 * .5, self.height // 8 * 2.5)
        elif self.count == 2:
            dialog = aux_dialog[2]
            dialog_surface = self.font.render(dialog, True, text_color_dialog)
            pos_dialog=(self.width // 7 * 1.2, self.height // 8 * 3.5)
        
        display.blit(self.animation[self.count], self.width // 7 * 1, self.height // 8 * 1)
        display.blit(dialog_surface, pos_dialog)
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
