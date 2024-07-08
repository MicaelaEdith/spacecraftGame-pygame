import pygame
import os
import sys
import time 
from playerController import Player
from map import Deep, Starts, Meteorite, Status
from menu import Menu, MainMenu, Pause, Button
from cinematics import Intro

pygame.init()

# Configuración de la pantalla
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
status = Status(screenWidth, screenHeight)

clock = pygame.time.Clock()
start = True
game = False

if screenWidth > 1920 or screenHeight > 1080:
    screenWidth = 1920
    screenHeight = 1080

display = pygame.display.set_mode((screenWidth, screenHeight), pygame.SRCALPHA)
pygame.display.set_caption("Tango triste en un asteroide")

# Menú principal y pausa
menu = Menu(screenWidth, screenHeight)
main_menu = MainMenu(screenWidth,screenHeight)
start_menu = Pause(screenWidth, screenHeight)

# Cinemáticas
intro = Intro(screenWidth, screenHeight)

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
    Button(60, screenHeight // 2 + 145, "Assets/Buttons/up_arrow.png"),
    Button(60, screenHeight // 2 + 200, "Assets/Buttons/down_arrow.png"),
    Button(20, screenHeight // 2 + 170, "Assets/Buttons/left_arrow.png"),
    Button(100, screenHeight // 2 + 170, "Assets/Buttons/right_arrow.png"),
]

buttons_right = [
    Button(screenWidth - 220, screenHeight // 2 + 100, "Assets/Buttons/actionA.png"),
    Button(screenWidth - 120, screenHeight // 2 + 100, "Assets/Buttons/actionB.png"),
    Button(screenWidth - 220, screenHeight // 2 + 200, "Assets/Buttons/actionC.png"),
    Button(screenWidth - 120, screenHeight // 2 + 200, "Assets/Buttons/actionD.png"),
]

buttons_menu = [
    Button(screenWidth - 120, screenHeight // 21, "Assets/Buttons/actionA.png"),  # start
    #Button(screenWidth - 120, screenHeight // 21 + 80, "Assets/Buttons/actionA.png"),  # mute
]

# Bucle Menu
while not game:
    for event in pygame.event.get():
        result = main_menu.handle_event(event)
        if result == 'new_game':
            time.sleep(0.5)
            game = True
        elif result == 'load_game':
            pass
        elif result == 'options':
            pass

    display.fill(blue)
    main_menu.draw(display)
    starts1.drawStarts(display)
    starts2.drawStarts(display)
    starts3.drawStarts(display)
    pygame.display.flip()
    clock.tick(60)

starts1.speed = 1
starts2.speed = .5
starts3.speed = .3
# Bucle principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # Eventos de mouse para los botones de dirección (izquierda)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_left:
                button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0] if event.type == pygame.MOUSEBUTTONDOWN else False)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_left:
                button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0])


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
                        buttons_right[0].clicked=False
                        buttons_right[1].clicked=False
                        buttons_right[2].clicked=False
                        buttons_right[3].clicked=False
                        player.action['a'] = False
                        player.action['b'] = False
                        player.action['c'] = False
                        player.action['d'] = False

        # Verificar si se presiona el botón del menú
        if event.type == pygame.FINGERDOWN:
            touch_pos = (event.x * screenWidth, event.y * screenHeight)
            for button in buttons_menu:
                if button.is_clicked(touch_pos, True):
                    if button == buttons_menu[0]:
                        start = not start
                        buttons_menu[0].clicked = False

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
        player.resetActions()
        status.updateStatus( player.health ,level)
        status.draw(display, level, player.health, player.score)

        for button in buttons_left + buttons_right + buttons_menu:
            button.draw(display)
    else:
        start_menu.draw(display)
        for button in buttons_menu:
            button.draw(display)

    pygame.display.flip()
    clock.tick(60)
