import pygame
from script_dialogues import *

class Intro():
    def __init__(self, screenWidth, screenHeight):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((55, 55, 55))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        font_size = int(screenHeight * 0.03)
        self.font = pygame.font.Font(self.font_path, font_size)
        self.language = ['en', 'es']
        self.lan_on = 'en'
        self.text_en = 'CONTINUE'
        self.text_es = 'CONTINUAR'
        self.text = ''
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []
        self.count = 0
        self.animation = []
        self.animation.append(pygame.image.load("Assets/imgs/cinematica1-1.png").convert())
        self.animation.append(pygame.image.load("Assets/imgs/cinematica1-2.png").convert())
        self.animation.append(pygame.image.load("Assets/imgs/cinematica1-3.png").convert())
        self.animation[0].set_colorkey([0, 114, 178])
        self.animation[1].set_colorkey([0, 114, 178])
        self.animation[2].set_colorkey([0, 114, 178])
        self.full_hd = False
        self.screenWidth = screenWidth
        self.screenHeight = screenWidth

        if screenWidth >= 1920:
            self.full_hd = True

    def draw(self, display, lan, count):
        self.count = count
        self.lan_on = lan
        display.blit(self.init_menu, (0, 0))
        self.buttons = []
        text_color = (160, 23, 208)
        dialog_color = (160, 23, 208)
        dialog = ''

        if self.lan_on == 'en':
            self.text = self.text_en
            aux_dialog = intro_script_en
        else:
            self.text = self.text_es
            aux_dialog = intro_script_es

        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=(self.width // 7 * 6, self.height // 8 * 6.8))

        mouse_pos = pygame.mouse.get_pos()

        if text_rect.collidepoint(mouse_pos):
            text_color = (251, 206, 60)
            text_surface = self.font.render(self.text, True, text_color)
        else:
            text_color = (160, 23, 208)
            text_surface = self.font.render(self.text, True, text_color)
        
        dialog = aux_dialog[self.count]
        
        self.draw_centered_image(display, self.animation[self.count])

        lines = self.wrap_text(dialog, self.font, self.width // 1.7)


        image_height = self.height // 3
        y_offset = image_height +  image_height + 8
        for line in lines:
            dialog_surface = self.font.render(line, True, dialog_color)
            dialog_rect = dialog_surface.get_rect(center=(self.width // 2, y_offset))
            display.blit(dialog_surface, dialog_rect)
            y_offset += dialog_surface.get_height() + 5

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

    def draw_centered_image(self, display, image):
        display_width, display_height = display.get_size()
        
        image_original_width, image_original_height = image.get_size()

        new_width = display_width // 2.5
        new_height = int(image_original_height * (new_width / image_original_width))
        
        scaled_image = pygame.transform.scale(image, (new_width, new_height))
        
        x_centered = ((display_width - new_width) // 2) + 29
        y_centered = (display_height - new_height) // 3
        
        display.blit(scaled_image, (x_centered, y_centered))

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        if current_line:
            lines.append(current_line)

        return lines


class LevelUp:
    def __init__(self, screenH, screenW):
        self.current_level = None
        original_image = pygame.image.load("Assets/imgs/cinematica2-LevelUp.png").convert_alpha()
        new_width = int(screenW * 0.8)
        aspect_ratio = original_image.get_height() / original_image.get_width()
        new_height = int(new_width * aspect_ratio)
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        
        self.x = (screenW - new_width) // 2
        self.y = screenH + 300
        self.speed = -20

    def level_up_animation(self, display):
        self.y += self.speed
        display.blit(self.image, (int(self.x), int(self.y)))

        if self.y + self.image.get_height() < 0:
            return True
        return False






    