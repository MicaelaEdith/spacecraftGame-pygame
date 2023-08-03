import pygame
import sys
import os
from playerController import Player
from world import Starts

pygame.init()

os.environ['SDL_VIDEO_CENTERED']='1'
info=pygame.display.Info()
screenWidth, screenHeight= info.current_w, info.current_h
white=(255,255,255)
blue=(1,6,26)
clock=pygame.time.Clock()

xPosition=(screenWidth/2)-40
yPosition=(screenHeight/100*80)+40

if(screenWidth>1920 or screenHeight>1080):
    screenWidth=1920
    screenHeight=1080


display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("pygame")

player=Player(xPosition,yPosition,screenHeight, screenWidth)
starts=Starts(screenWidth, screenHeight)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    display.fill(blue)
    player.movePlayer(event)
    starts.drawStarts(display, event)
    player.drawPlayer(display)


    pygame.display.flip()
    clock.tick(60)
