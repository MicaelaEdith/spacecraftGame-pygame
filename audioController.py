import pygame

class MainMusic():
    def __init__(self, on):
        pygame.mixer.music.load('Assets/Audio/main.mp3')
        self.on = on

    def play(self):
        pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.pause()
