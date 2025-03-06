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
