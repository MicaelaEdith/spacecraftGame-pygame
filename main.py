import pygame
import os, sys
from playerController import Player
from map import Deep, Starts, Meteorite
from menu import Menu, Pause, Button

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
start_menu = Pause(screenWidth, screenHeight)

# Inicialización del jugador y el fondo de estrellas
xPosition = int((screenWidth / 2) - 40)
yPosition = int(screenHeight / 100 * 80 + 40)
player = Player(xPosition, yPosition, screenHeight, screenWidth)
starts1 = Starts(screenWidth, screenHeight)
starts2 = Starts(screenWidth, screenHeight)
starts2.speed = .5
starts2.white = (125, 120, 168)
starts2.quiet = True
starts3 = Starts(screenWidth, screenHeight)
starts3.speed = .2
starts3.white = (105, 80, 80)
starts3.quiet = True

# Elementos de interacción
meteorite = Meteorite(screenWidth, screenHeight)

# Crear botones
buttons_left = [
    Button(80, screenHeight // 2 + 90, "Assets/Buttons/up_arrow.png"),
    Button(80, screenHeight // 2 + 150, "Assets/Buttons/down_arrow.png"),
    Button(40, screenHeight // 2 + 120, "Assets/Buttons/left_arrow.png"),
    Button(120, screenHeight // 2 + 120, "Assets/Buttons/right_arrow.png"),
]

buttons_right = [
    Button(screenWidth - 200, screenHeight // 2 + 100, "Assets/Buttons/actionA.png"),
    Button(screenWidth - 100, screenHeight // 2 + 100, "Assets/Buttons/actionB.png"),
    Button(screenWidth - 200, screenHeight // 2 + 200, "Assets/Buttons/actionC.png"),
    Button(screenWidth - 100, screenHeight // 2 + 200, "Assets/Buttons/actionD.png"),
]

buttons_menu = [
    Button(screenWidth - 100, screenHeight // 21, "Assets/Buttons/actionA.png"),  # start
    Button(screenWidth - 100, screenHeight // 21 + 80, "Assets/Buttons/actionA.png"),  # mute
]

# Variables para acciones
a, b, c, d = False, False, False, False

# Bucle Menu
while not game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_menu:
                button.is_clicked(mouse_pos)
            if buttons_menu[0].clicked:
                game = True
    menu.draw(display)
    for button in buttons_menu:
        button.draw(display)
    pygame.display.flip()
    clock.tick(60)

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

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_left + buttons_right:
                button.is_clicked(mouse_pos)

            # Actualizar el movimiento del jugador basado en los botones presionados
            player.movement['up'] = buttons_left[0].clicked
            player.movement['down'] = buttons_left[1].clicked
            player.movement['left'] = buttons_left[2].clicked
            player.movement['right'] = buttons_left[3].clicked

            # Actualizar las acciones basadas en los botones de acción
            player.action['a'] = buttons_right[0].clicked
            player.action['b'] = buttons_right[1].clicked
            player.action['c'] = buttons_right[2].clicked
            player.action['d'] = buttons_right[3].clicked

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons_menu:
                button.is_clicked(mouse_pos)
            if buttons_menu[0].clicked:
                start = not start

    if level == 0:
        player.movePlayer()
        meteorite.draw(display)
        meteorite.check_collisions(player)
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

        player.drawPlayer(display)
        player.drawExplosion(display)

        for button in buttons_left + buttons_right + buttons_menu:
            button.draw(display)
    else:
        start_menu.draw(display)
        for button in buttons_menu:
            button.draw(display)

    pygame.display.flip()
    clock.tick(60)
