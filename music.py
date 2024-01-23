import pygame


class MainMusic(pygame.mixer.Sound):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_playing = True