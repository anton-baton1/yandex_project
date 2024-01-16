import pygame

from constants import GREEN, RED, WIDTH


class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.color = GREEN

        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("{:05.2f}".format(self.seconds), True, self.color)
        self.x = WIDTH - self.text.get_width()
        self.y = 0

    def update(self):
        self.seconds -= 0.01
        if self.seconds < 0:
            self.color = RED
        self.text = self.font.render("{:05.2f}".format(self.seconds), True, self.color)
