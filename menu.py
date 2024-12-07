import pygame, time
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
    def __init__(self, screenWidth, screenHeight, game):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((50, 50, 50))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path, 50)
        self.language = ['en', 'es']
        self.lan_on = 'es'
        self.text_en = ['NEW GAME', 'LOAD', 'OPTIONS', 'EXIT']
        self.text_es = ['JUEGO NUEVO', 'CARGAR', 'OPCIONES', 'SALIR']
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []
        self.game = game
        self.full_hd = False
        self.font = pygame.font.Font(self.font_path, 50)
        self.margin = 80

        if screenWidth > 1920 or screenHeight > 1080:
            self.full_hd = True
            self.font = pygame.font.Font(self.font_path, 80)
            self.margin = 120

    def draw(self, display, lan, game):
        self.game = game
        self.lan_on = lan
        display.blit(self.init_menu, (0, 0))
        self.buttons = []
        contador = 1
        if self.lan_on == 'en':
            text_list = self.text_en
        else:
            text_list = self.text_es

        mouse_pos = pygame.mouse.get_pos()

        text_color = (160, 23, 208)
        text_color_off = (50, 43, 40)
        for i in text_list:
            if not self.game:
                text_aux = self.font.render(i, True, text_color)
                text_rect = text_aux.get_rect(topleft=(self.margin, self.height / 4 * contador))
            else:
                if i == text_list[0]:
                    if self.lan_on == 'en':
                        text_aux = self.font.render('RETURN', True, text_color)
                    else:
                        text_aux = self.font.render('VOLVER',True, text_color)
                if i == text_list[3]:
                    if self.lan_on == 'en':
                        text_aux = self.font.render('SAVE and '+i, True, text_color)
                    else:
                        text_aux = self.font.render('GUARDAR Y '+i, True, text_color)
                elif i == text_list[1] or i == text_list[2]:
                    text_aux = self.font.render(i, True, text_color_off)

                text_rect = text_aux.get_rect(topleft=(self.margin, self.height / 4 * contador))

            if text_rect.collidepoint(mouse_pos):
                text_color_hover = (251, 206, 60)
                if self.game:
                    if i == text_list[0]:
                        if self.lan_on == 'en':
                            text_aux = self.font.render('RETURN', True, text_color_hover)
                        else:
                            text_aux = self.font.render('VOLVER', True, text_color_hover)
                    if i == text_list[3]:
                        if self.lan_on == 'en':
                            text_aux = self.font.render('SAVE and '+i, True, text_color_hover)
                        else:
                            text_aux = self.font.render('GUARDAR Y '+i, True, text_color_hover)
                if not self.game:
                    text_aux = self.font.render(i, True, text_color_hover)

                        

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
            return 'new_game'
        elif text == 'LOAD' or text == 'CARGAR':
            return 'load_game'
        elif text == 'OPTIONS' or text == 'OPCIONES':
            return 'options'
        elif text == 'EXIT' or text == 'SALIR':
            time.sleep(1)
            pygame.quit()
            exit()
        return None
    
class OptionsMenu():
    def __init__(self, screenWidth, screenHeight):
        self.init_menu = pygame.Surface((screenWidth, screenHeight))
        self.init_menu.set_alpha(5)
        self.init_menu.fill((50, 50, 50))
        self.font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
        self.font = pygame.font.Font(self.font_path, 50)
        self.language = ['en', 'es']
        self.lan_on = 'es'
        self.text_en = ['LANGUAGE - EN-ES', 'FX', 'MUSIC', 'RETURN']
        self.text_es = ['IDIOMA - EN-ES', 'EFECTOS', 'MUSICA', 'VOLVER']
        self.width = screenWidth
        self.height = screenHeight
        self.buttons = []
        self.music_on = True
        self.sound_on = True
        self.margin = 80

        if screenWidth > 1920 or screenHeight > 1080:
            self.full_hd = True
            self.font = pygame.font.Font(self.font_path, 80)
            self.margin = 120

    def draw(self, display, lan, music_on, sound_on):
        self.lan_on = lan
        self.music_on = music_on
        self.sound_on = sound_on
        display.blit(self.init_menu, (0, 0))
        self.buttons = []
        self.click_on = False
        contador = 1
        if self.lan_on == 'en':
            text_list = self.text_en
        else:
            text_list = self.text_es

        mouse_pos = pygame.mouse.get_pos()

        for i in text_list:
            text_color = (160, 23, 208)
            text_color_off = (50, 43, 40)

            if (i == 'MUSIC' or i == 'MUSICA') and self.music_on == False:
                 text_aux = self.font.render(i, True, text_color_off)
            if (i == 'MUSIC' or i == 'MUSICA') and self.music_on == True:
                   text_aux = self.font.render(i, True, text_color)
            
            if (i == 'FX' or i == 'EFECTOS') and self.sound_on == False:
                 text_aux = self.font.render(i, True, text_color_off)
            if (i == 'FX' or i == 'EFECTOS') and self.sound_on == True:
                   text_aux = self.font.render(i, True, text_color)

            if i != 'FX' and i != 'EFECTOS' and i != 'MUSIC' and i != 'MUSICA':
                 text_aux = self.font.render(i, True, text_color)

            text_rect = text_aux.get_rect(topleft=(self.margin, self.height / 4 * contador))

        
            if text_rect.collidepoint(mouse_pos) and not self.click_on:
                if ((i == 'MUSIC' or i == 'MUSICA') and not self.music_on) or ((i == 'FX' or i == 'EFECTOS') and not self.sound_on):
                    text_color_current = text_color_off
                else:
                    text_color_current = (251, 206, 60)
                text_aux = self.font.render(i, True, text_color_current)

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
        if text == 'LANGUAGE - EN-ES' or text == 'IDIOMA - EN-ES':
            return 'language'
        elif text == 'FX' or text == 'EFECTOS':
            self.sound_on = not self.sound_on        
            return 'fx'
        elif text == 'MUSIC' or text == 'MUSICA':
            self.music_on = not self.music_on
            return 'music'
        elif text == 'RETURN' or text == 'VOLVER':
            return 'save'
  
        return None


class Button:
    def __init__(self, screenW, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()

        if screenW > 1920:
            scale_factor = 2
        elif screenW > 1200:
            scale_factor = 1.2
        else:
            scale_factor = 1

        original_size = self.image.get_size()
        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        self.image = pygame.transform.scale(self.image, new_size)

        self.image.set_colorkey([1, 6, 26])

        self.rect = self.image.get_rect(topleft=(x, y))

        self.clicked = False

        self.nav_bar_offset_x = 0

        if 'action' in image_path:
            self.nav_bar_offset_x = 52

    def draw(self, surface):
        if self.clicked:
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos, pressed):
        collision_rect = self.rect.copy()
        collision_rect.x += self.nav_bar_offset_x

        if collision_rect.collidepoint(pos):
            self.clicked = pressed

        return self.clicked
