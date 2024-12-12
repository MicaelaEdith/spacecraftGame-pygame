import pygame
import random
import os
import sys
import time 
from playerController import Player
from map import Deep, Starts, Meteorite, Status
from menu import Menu, MainMenu, OptionsMenu, Button
from cinematics import Intro, LevelUp

pygame.init()

icon = pygame.image.load("Assets/Player/0.png")
icon.set_colorkey([1, 6, 26])
pygame.display.set_icon(icon)
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
white = (255, 255, 255)
blue = (10, 8, 31)
blue_light = (4, 19, 40)
alpha = 5
level = 0
up_level = 0
menus=1
language = 'es'
music_on = False
sound_on = True
status = Status(screenWidth, screenHeight,language)
full_hd = False
img_button = 'Assets/Buttons/'
transition = False


clock = pygame.time.Clock()
start = True
game = False

if screenWidth > 1920 or screenHeight > 1080:
    full_hd = True
    scale_factor = 2
else:
    scale_factor = 1.3


display = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN | pygame.SRCALPHA)
pygame.display.set_caption("Tango triste en un asteroide")

menu = Menu(screenWidth, screenHeight)
main_menu = MainMenu(screenWidth,screenHeight, game)
option_menu = OptionsMenu(screenWidth, screenHeight)
options_open = False
pygame.mixer.music.load('Assets/Audio/intro.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)


intro = Intro(screenWidth, screenHeight)
intro_flag = False
level_up = LevelUp (screenHeight, screenWidth)


xPosition = int((screenWidth / 2) - 60)
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

meteorite = Meteorite(screenWidth, screenHeight)


if not full_hd:
    buttons_left = [
        Button(screenWidth, 75, screenHeight // 3 * 2.15 - 52, img_button + "up_arrow.png"),
        Button(screenWidth, 75, screenHeight // 3 * 2.15 + 52, img_button + "down_arrow.png"),
        Button(screenWidth, 20, screenHeight // 3 * 2.15, img_button + "left_arrow.png"),
        Button(screenWidth, 130, screenHeight // 3 * 2.15, img_button + "right_arrow.png"),
    ]

    buttons_right = [
        Button(screenWidth, (screenWidth - 255), screenHeight // 3 * 2, img_button + "action_A.png"),
        Button(screenWidth, (screenWidth - 160), screenHeight // 3 * 2, img_button + "action_B.png"),
        Button(screenWidth, (screenWidth - 255), screenHeight // 3 * 2 + 85, img_button + "action_C.png"),
        Button(screenWidth, (screenWidth - 160), screenHeight // 3 * 2 + 85, img_button + "action_D.png"),
    ]

    buttons_menu = [
        Button(screenWidth, screenWidth - 120, screenHeight // 20, img_button + "pause.png"),
        Button(screenWidth, screenWidth - 120, screenHeight // 20 + 30, img_button + "exit.png"),
    ]
else:
    buttons_left = [
        Button(screenWidth, 160, screenHeight // 3 * 2.25 - 90 , img_button + "up_arrow.png"),
        Button(screenWidth, 160, screenHeight // 3 * 2.25 + 90, img_button + "down_arrow.png"),
        Button(screenWidth, 66, screenHeight // 3 * 2.25, img_button + "left_arrow.png"),
        Button(screenWidth, 250, screenHeight // 3 * 2.25, img_button + "right_arrow.png"),
    ]

    buttons_right = [
        Button(screenWidth, screenWidth - 550, screenHeight // 3 * 2, img_button + "action_A.png"),
        Button(screenWidth, screenWidth - 370, screenHeight // 3 * 2, img_button + "action_B.png"),
        Button(screenWidth, screenWidth - 550, screenHeight // 3 * 2 + 160, img_button + "action_C.png"),
        Button(screenWidth, screenWidth - 370, screenHeight // 3 * 2 + 160, img_button + "action_D.png"),
    ]

    buttons_menu = [
        Button(screenWidth, screenWidth - 380, screenHeight // 11.5, img_button + "pause.png"),  # start
        Button(screenWidth, screenWidth - 380, screenHeight // 11.5 + 70, img_button + "exit.png"),  # salir
    ]

music_on = option_menu.music_on
count_music = 0


################################################################################# Bucle Menu
while not game and not intro_flag:
    if count_music<1 and music_on:
        count_music+= 0.001
        pygame.mixer.music.set_volume(count_music)
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
                if music_on:
                    pygame.mixer.music.stop()
                    music_on = False
                elif not music_on:
                    pygame.mixer.music.play(-1)
                    music_on = True
                music_on = option_menu.music_on
            elif result_option == 'save':
                options_open = False


    display.fill(blue)
    starts1.drawStarts(display)
    starts2.drawStarts(display)
    starts3.drawStarts(display)
    if options_open:
        option_menu.draw(display,language,music_on,sound_on)
    else:
        main_menu.draw(display, language, game)

    pygame.display.flip()
    clock.tick(30)

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
            if count_music<0 and music_on:
                count_music-= 0.01
                pygame.mixer.music.set_volume(count_music)
            time.sleep(.5)
            intro_flag = False
            game = True
    
    
    pygame.display.flip()
    clock.tick(30)
                
          
starts1.speed = 1
starts2.speed = .5
starts3.speed = .3

#################################################################################### Bucle principal
pygame.mixer.music.load('Assets/Audio/main.mp3')
if music_on:
    pygame.mixer.music.play(-1)
else:
    pygame.mixer.music.stop()
time.sleep(.9)
while game:
    if count_music<1 and music_on:
        count_music+= 0.001
        pygame.mixer.music.set_volume(count_music)

    for event in pygame.event.get():
        if not transition:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons_left:
                    button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0] if event.type == pygame.MOUSEBUTTONDOWN else False)
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons_left:
                    button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0])
            if event.type == pygame.MOUSEBUTTONUP:
                for button in buttons_left:
                    button.clicked = False
                player.movement['left'] = False
                player.movement['right'] = False
                player.movement['up'] = False
                player.movement['down'] = False


            if event.type == pygame.FINGERDOWN or event.type == pygame.FINGERUP:
                if full_hd:
                    touch_pos = (event.x * screenWidth - 110, event.y * screenHeight)
                else:
                    touch_pos = (event.x * screenWidth, event.y * screenHeight)
                for button in buttons_right:
                    if button.is_clicked(touch_pos, True):
                        if event.type == pygame.FINGERDOWN:
                            if button == buttons_right[0]:
                                player.action['a'] = True
                            elif button == buttons_right[1]:
                                player.action['b'] = True
                            elif button == buttons_right[2]:
                                player.action['c'] = True
                            elif button ==  buttons_right[3]:
                                player.action['d'] = True

                        elif event.type == pygame.FINGERUP:
                            player.action['a'] = False                        
                            player.action['b'] = False
                            player.action['c'] = False
                            player.action['d'] = False
                            button.clicked = False

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
                            music_on = False
                        elif not music_on:
                            pygame.mixer.music.play(-1)
                            music_on = True
                        music_on = option_menu.music_on
                    elif result_option == 'save':
                        options_open = False
                        start = True
                        buttons_menu[0].clicked = False

                        if music_on:
                            pygame.mixer.music.set_volume(1)


    player.movement['up'] = buttons_left[0].clicked
    player.movement['down'] = buttons_left[1].clicked
    player.movement['left'] = buttons_left[2].clicked
    player.movement['right'] = buttons_left[3].clicked


######################################################################## LEVEL 0 ###############################################
    if level == 0:
        collision_detected = False
        for player_rect in player.rectList:
            for meteorite_rect in meteorite.rectList:
                if player_rect.colliderect(meteorite_rect):
                    collision_detected = True
                    player.explosion_active = True
                    player.explosion_timer = 0
                    player.xPosition += random.randrange(-4,4)
                    break

        if collision_detected:
            up_level += 1

        if meteorite.metorites_count > 1 :
            start = False
            transition = True
            player.transition = True
            meteorite.fade_out = True

    if level == 1:
        #player.movePlayer()
        pass


############################################################################# update
    if start:
        player.movePlayer()
        player.updateShoots()
        player.actions()
        display.fill(blue)
        starts1.drawStarts(display)
        starts2.drawStarts(display)
        starts3.drawStarts(display)

        if level == 0:
            meteorite.draw(display)
            meteorite.check_collisions(player)

        if level == 1:
            pass

        if level == 2:
            pass

        if level == 3:
            pass

        if level == 4:
            pass

        if level == 5:
            pass

        player.updatePick()
        player.drawPick(display)
        player.drawPlayer(display)
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

        if not transition:
            if not options_open:
                main_menu.draw(display, language, game)
            else:
                option_menu.draw(display, language, music_on, sound_on)

        if transition:
            player.drawPlayer(display)
            if level == 0:
                meteorite.off = True
                meteorite.draw(display)
            start = level_up.level_up_animation(display)
            transition = not start
            if not transition:
                level += 1
                player.transition = False

            status.draw(display, level, player.health, player.score,language)

            for button in buttons_left + buttons_right + buttons_menu:
                button.draw(display)   


    pygame.display.flip()
    clock.tick(30)
    