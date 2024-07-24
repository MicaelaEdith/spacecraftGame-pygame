import pygame
import os
import sys
import time 
from playerController import Player
from map import Deep, Starts, Meteorite, Status
from menu import Menu, MainMenu, OptionsMenu, Button
from cinematics import Intro
from audioController import MainMusic

pygame.init()

# Configuración de la pantalla
icon = pygame.image.load("Assets/Player/spacecraft0.png")
icon.set_colorkey([1, 6, 26])
pygame.display.set_icon(icon)
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
white = (255, 255, 255)
blue = (1, 6, 26)
blue_light = (4, 19, 40)
alpha = 5
level = 0
up_level = 0
menus=1
language = 'en'
music_on = True
sound_on = True
status = Status(screenWidth, screenHeight,language)

clock = pygame.time.Clock()
start = True
game = False

if screenWidth > 1920 or screenHeight > 1080:
    screenWidth = 1920
    screenHeight = 1080

display = pygame.display.set_mode((screenWidth, screenHeight), pygame.SRCALPHA)
pygame.display.set_caption("Tango triste en un asteroide")

# Menú principal, opciones y pausa
menu = Menu(screenWidth, screenHeight)
main_menu = MainMenu(screenWidth,screenHeight, game)
option_menu = OptionsMenu(screenWidth, screenHeight)
options_open = False
pygame.mixer.music.load('Assets/Audio/main.mp3')

# Cinemáticas
intro = Intro(screenWidth, screenHeight)
intro_flag = False

# Inicialización del jugador y el fondo de estrellas
xPosition = int((screenWidth / 2) - 40)
yPosition = int(screenHeight / 100 * 80 + 40)
player = Player(xPosition, yPosition, screenHeight, screenWidth)
starts1 = Starts(screenWidth, screenHeight)
starts1.speed = .4
starts2 = Starts(screenWidth, screenHeight)
starts2.speed = .2
starts2.white = (125, 120, 168)
starts2.quiet = True
starts3 = Starts(screenWidth, screenHeight)
starts3.speed = .1
starts3.white = (105, 80, 80)
starts3.quiet = True

# Elementos de interacción
meteorite = Meteorite(screenWidth, screenHeight)

# Crear botones
buttons_left = [
    Button(60, screenHeight // 3 * 2.15 , "Assets/Buttons/up_arrow.png"),
    Button(60, screenHeight // 3 * 2.15 + 55, "Assets/Buttons/down_arrow.png"),
    Button(20, screenHeight // 3 * 2.15 + 25, "Assets/Buttons/left_arrow.png"),
    Button(100, screenHeight // 3 * 2.15 + 25, "Assets/Buttons/right_arrow.png"),
]

buttons_right = [
    Button(screenWidth - 245, screenHeight // 3 * 2 + 10, "Assets/Buttons/actionA.png"),
    Button(screenWidth - 165, screenHeight // 3 * 2 + 10, "Assets/Buttons/actionB.png"),
    Button(screenWidth - 245, screenHeight // 3 * 2 + 95, "Assets/Buttons/actionC.png"),
    Button(screenWidth - 165, screenHeight // 3 * 2 + 95, "Assets/Buttons/actionD.png"),
]

buttons_menu = [
    Button(screenWidth - 120, screenHeight // 21, "Assets/Buttons/pause.png"),  # start
    Button(screenWidth - 120, screenHeight // 21 + 30, "Assets/Buttons/exit.png"),  # salir
]

music_on = option_menu.music_on
# Bucle Menu
while not game and not intro_flag:
    for event in pygame.event.get():
        if not options_open:
            result = main_menu.handle_event(event)
            if result == 'new_game':
                time.sleep(.8)
                intro_flag = True
                options_open = False
            elif result == 'load_game':
                pass
            elif result == 'options':
                    options_open= True
        
        if options_open:
            result_option = option_menu.handle_event(event)
                
            if result_option == 'language':
                if language == 'en':
                    language = 'es'
                else:
                    language = 'en'
            elif result_option == 'fx':
                sound_on = option_menu.sound_on
            elif result_option == 'music':
                music_on = option_menu.music_on
            elif result_option == 'save':
                options_open = False

            #if event.type == pygame.MOUSEBUTTONUP and result_option != None:
             #   option_menu.click_on = True


    display.fill(blue)
    starts1.drawStarts(display)
    starts2.drawStarts(display)
    starts3.drawStarts(display)
    if options_open:
        option_menu.draw(display,language,music_on,sound_on)
    else:
        main_menu.draw(display, language, game)

    pygame.display.flip()
    clock.tick(60)

count_intro = 0
while intro_flag:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    
    display.fill(blue)
    starts2.drawStarts(display)
    intro.draw(display, language, count_intro)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        result = intro.handle_event(event)
        if result == 'continue':
            count_intro+=1
            intro.count = count_intro

        if count_intro >= 3:
            time.sleep(.8)
            intro_flag = False
            game = True
    
    pygame.display.flip()
    clock.tick(60)
                
          
starts1.speed = 1
starts2.speed = .5
starts3.speed = .3
# Bucle principal

pygame.mixer.music.play(-1)
time.sleep(.9)
while game:
    for event in pygame.event.get():

        # Eventos de mouse para los botones de dirección (izquierda)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_left:
                button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0] if event.type == pygame.MOUSEBUTTONDOWN else False)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_left:
                button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0])
                #button.clicked = False
        if event.type == pygame.MOUSEBUTTONUP:
            for button in buttons_left:
                button.clicked = False
            player.movement['left'] = False
            player.movement['right'] = False
            player.movement['up'] = False
            player.movement['down'] = False


        # Eventos de toque para los botones de acción (derecha)
        if event.type == pygame.FINGERDOWN or event.type == pygame.FINGERUP:
            touch_pos = (event.x * screenWidth, event.y * screenHeight)
            for button in buttons_right:
                if button.is_clicked(touch_pos, True):
                    # Actualizar el estado de las acciones al presionar
                    if event.type == pygame.FINGERDOWN:
                        if button == buttons_right[0]:
                            player.action['a'] = True
                        elif button == buttons_right[1]:
                            player.action['b'] = True
                        elif button == buttons_right[2]:
                            player.action['c'] = True
                        elif button ==  buttons_right[3]:
                            player.action['d'] = True

                    # Actualizar el estado de las acciones al soltar
                    elif event.type == pygame.FINGERUP:
                        player.action['a'] = False                        
                        player.action['b'] = False
                        player.action['c'] = False
                        player.action['d'] = False
                        button.clicked = False

        # Verificar si se presiona el botón del menú
        if start:
            if event.type == pygame.FINGERDOWN:
                touch_pos = (event.x * screenWidth, event.y * screenHeight)
                if buttons_menu[0].is_clicked(touch_pos, True): 
                    start = not start
                    options_open = True
                if buttons_menu[1].is_clicked(touch_pos, True): 
                    start = not start
                    options_open = False

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if buttons_menu[0].is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
                    options_open = True
                    start = not start
                if buttons_menu[1].is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
                    options_open = False
                    start = not start
        if not start:
            if not options_open:
                result = main_menu.handle_event(event)
                if result == 'new_game':
                    buttons_menu[1].clicked = False
                    start = True
                    if music_on:
                        pygame.mixer.music.set_volume(1)
                elif result == 'exit':
                    options_open = False

        
            if options_open:
                result_option = option_menu.handle_event(event)
                if result_option == 'language':
                    if language == 'en':
                        language = 'es'
                    else:
                        language = 'en'
                elif result_option == 'fx':
                    sound_on = option_menu.sound_on
                elif result_option == 'music':
                    if music_on:
                        pygame.mixer.music.stop()
                    if not music_on:
                        pygame.mixer.music.play(-1)
                    music_on = option_menu.music_on
                elif result_option == 'save':
                    options_open = False
                    start = True
                    buttons_menu[0].clicked = False

                    if music_on:
                        pygame.mixer.music.set_volume(1)


    # Actualizar el movimiento del jugador basado en los botones presionados
    player.movement['up'] = buttons_left[0].clicked
    player.movement['down'] = buttons_left[1].clicked
    player.movement['left'] = buttons_left[2].clicked
    player.movement['right'] = buttons_left[3].clicked

    if level == 0:
        collision_detected = False
        for player_rect in player.rectList:
            for meteorite_rect in meteorite.rectList:
                if player_rect.colliderect(meteorite_rect):
                    collision_detected = True
                    player.explosion_active = True
                    player.explosion_timer = 0
                    break

        if collision_detected:
            up_level += 1

    if level == 1:
        player.movePlayer()

    if start:
        player.movePlayer()
        player.updateShoots()  # Actualiza los disparos del jugador
        player.actions()
        display.fill(blue)
        starts1.drawStarts(display)
        starts2.drawStarts(display)
        starts3.drawStarts(display)
        if level == 0:
            meteorite.draw(display)

        meteorite.draw(display)
        meteorite.check_collisions(player)
        player.drawPlayer(display)
        player.updatePick()
        player.drawPick(display)
        player.drawExplosion(display)
        status.updateStatus( player.health ,level)
        status.draw(display, level, player.health, player.score,language)
        player.resetActions()

        for button in buttons_left + buttons_right + buttons_menu:
            button.draw(display)        
    
    else:
        if music_on:
            pygame.mixer.music.set_volume(.25)
        display.fill(blue)
        starts2.drawStarts(display)
        starts3.drawStarts(display)
        if not options_open:
            main_menu.draw(display, language, game)
        else:
            option_menu.draw(display, language, music_on, sound_on)

    #for button in buttons_right:
        #button.clicked = False


    pygame.display.flip()
    clock.tick(60)
