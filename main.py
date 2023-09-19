import pygame, random
import sys
import os
from playerController import Player
from world import Starts, Meteorite

pygame.init()

os.environ['SDL_VIDEO_CENTERED']='1'
info=pygame.display.Info()
screenWidth, screenHeight= info.current_w,info.current_h
screenWidth+=1
screenHeight+=1
white=(255,255,255)
blue=(1,6,26)
clock=pygame.time.Clock()
level=1

xPosition=int((screenWidth/2)-40)
yPosition=int((screenHeight/100*80)+40)

if(screenWidth>1920 or screenHeight>1080):
    screenWidth=1920
    screenHeight=1080


display = pygame.display.set_mode((int(screenWidth),int(screenHeight)))
pygame.display.set_caption("pygame")

player=Player(xPosition,yPosition,screenHeight, screenWidth)
starts=Starts(screenWidth, screenHeight)
meteorite=Meteorite(screenWidth,screenHeight)
level1=True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    player.movePlayer(event)


    ############## Level : 1
    for player_rect in player.rectList:
            for meteorite_rect in meteorite.rectList:
                if player_rect.colliderect(meteorite_rect):         ### check lists and colliders
                    if not player.collided:
                        print("check")
                        player.collided = True
                else:
                    player.collided = False


    display.fill(blue)
    starts.drawStarts(display, event)
    meteorite.draw(display, event)     
    player.drawPlayer(display)

    pygame.display.flip()
    clock.tick(30)



