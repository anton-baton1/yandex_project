import pygame

from sources import WIDTH, DARK_YELLOW


class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.color = DARK_YELLOW

        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 32)
        self.text = self.font.render("{:05.2f}".format(self.seconds), True, self.color)
        self.x = WIDTH - self.text.get_width()
        self.y = 0

    def update(self):
        self.seconds -= 0.01
        self.text = self.font.render("{:05.2f}".format(self.seconds), True, self.color)
        self.x = WIDTH - self.text.get_width()
