import pygame

class Intro():
    def __init__(self, width, height):
        self.intro = pygame.Surface((width, height))
        self.color = (55, 55, 55)
        self.intro.fill(self.color)
        self.width = width
        self.height = height
        
    def draw(self, display):
        display.blit(self.intro, (0, 0))

    