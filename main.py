import pygame
import os, sys
from playerController import Player
from map import Starts, Button

pygame.init()

# Configuración de la pantalla
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
white = (255, 255, 255)
blue = (1, 6, 26)
clock = pygame.time.Clock()

if screenWidth > 1920 or screenHeight > 1080:
    screenWidth = 1920
    screenHeight = 1080

display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tango triste para un asteroide")

# Inicialización del jugador y el fondo de estrellas
xPosition = int((screenWidth / 2) - 40)
yPosition = int(screenHeight / 100 * 80 + 40)
player = Player(xPosition, yPosition, screenHeight, screenWidth)
starts1 = Starts(screenWidth, screenHeight)
starts2 = Starts(screenWidth, screenHeight)
starts2.speed = 1
starts2.quiet = True

# Crear botones
buttons_left = [
    Button(50, screenHeight // 2 + 100,"Assets/Buttons/up_arrow.png"),
    Button(50, screenHeight // 2 + 200, "Assets/Buttons/down_arrow.png"),
    Button(0, screenHeight // 2 + 150, "Assets/Buttons/left_arrow.png"),
    Button(100, screenHeight // 2 + 150, "Assets/Buttons/right_arrow.png"),
]

buttons_right = [
    Button(screenWidth - 200, screenHeight // 2 + 100, "Assets/Buttons/actionA.png"),
    Button(screenWidth - 100, screenHeight // 2 + 100, "Assets/Buttons/actionB.png"),
    Button(screenWidth - 200, screenHeight // 2 + 200, "Assets/Buttons/actionC.png"),
    Button(screenWidth - 100, screenHeight // 2 + 200, "Assets/Buttons/actionD.png"),
]

# Variables para acciones
a, b, c, d = False, False, False, False

# Bucle principal
while True:
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
            a = buttons_right[0].clicked
            b = buttons_right[1].clicked
            c = buttons_right[2].clicked
            d = buttons_right[3].clicked

    player.movePlayer()
    display.fill(blue)
    starts1.drawStarts(display)
    starts2.drawStarts(display)
    player.drawPlayer(display)
    
    # Dibujar botones
    for button in buttons_left + buttons_right:
        button.draw(display)
         
    pygame.display.flip()
    clock.tick(60)
