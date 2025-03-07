import pygame
from script_dialogues import *

explosion_images = []
for i in range(1, 5):
    image = pygame.image.load(f"Assets/Objects/Demage ({i}).png")
    explosion_images.append(image)
    explosion_images[i - 1].set_colorkey([0, 1, 21])

explosion_frame = 0
explosion_active = False
explosion_timer = 0

def explosion(display, rect):
    global explosion_frame, explosion_active, explosion_timer

    xPosition = rect.centerx
    yPosition = rect.centery

    if explosion_timer == 0 or explosion_timer % 10 == 0:
        explosion_frame += 0.2
        if explosion_frame >= len(explosion_images):
            explosion_active = False
            explosion_frame = 0

    if int(explosion_frame) < len(explosion_images) and (explosion_frame - int(explosion_frame) == 0):
        try:
            display.blit(explosion_images[int(explosion_frame)], (xPosition - 30, yPosition - 25))
        except:
            pass


def update_statebar(display, hit_count, screenWidth, screenHeight):

    screenW = screenWidth
    screenH = screenHeight
    
    if screenW < 1920:
        margin = 50
        bar_width = 8
        bar_height = 90
    else:
        margin = 280
        bar_width = 20
        bar_height = 250
        
    bar_x = screenW - margin - bar_width
    bar_y = screenH // 2 - bar_height // 2

    fill_height = int(bar_height * (hit_count / 3))

    pygame.draw.rect(display, (160, 23, 208), (bar_x, bar_y, bar_width, bar_height))

    pygame.draw.rect(
        display,
        (233, 227, 132),
        (bar_x, bar_y + bar_height - fill_height, bar_width, fill_height)
    )  

    return hit_count >= 3

def found_text(lan, text):
    if lan == 'es':
        return chad_texts_es[text]
    else:
        return chad_texts_en[text]

def game_over(display):

    font_path = 'Assets/Fonts/KodeMono-VariableFont_wght.ttf'
    font = pygame.font.Font(font_path, 80)
    button_font = pygame.font.Font(font_path, 50)
    blue = (10, 8, 31)
    text_color = (160, 23, 208)
    text_color_off = (50, 43, 40)

    screen_width, screen_height = display.get_size()
    game_over_text = font.render("Game Over", True, text_color)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 3))

    button_width, button_height = 360, 60
    button_x = (screen_width - button_width) // 2
    button_y = screen_height // 1.5
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    retry_text = button_font.render("Reintentar", True, (251, 206, 60))
    retry_rect = retry_text.get_rect(center=button_rect.center)

    display.blit(game_over_text, text_rect)
    pygame.draw.rect(display, text_color, button_rect, border_radius=10)
    display.blit(retry_text, retry_rect)
