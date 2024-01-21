import pygame
from constants import DARK_YELLOW, VERY_DARK_GRAY, LIGHT_GRAY


class Button:
    def __init__(self, x, y, w, h, text, text_size):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.text_size = text_size

        self.font = pygame.font.Font("PressStart2P-Regular.ttf", self.text_size)
        self.text_string = self.font.render(self.text, 1, DARK_YELLOW)

        self.surface = pygame.Surface((self.w, self.h))
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.x = self.x
        self.surface_rect.y = self.y
        self.surface.fill(VERY_DARK_GRAY)
        self.text_rect = self.text_string.get_rect()

        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))

    def draw(self, screen):
        self.text_string = self.font.render(self.text, 1, DARK_YELLOW)
        self.text_rect = self.text_string.get_rect()
        self.surface.fill(VERY_DARK_GRAY)
        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))
        screen.blit(self.surface, (self.x, self.y))


class Label:
    def __init__(self, x, y, w, h, text, text_size):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.text_size = text_size

        self.font = pygame.font.Font("PressStart2P-Regular.ttf", self.text_size)
        self.text_string = self.font.render(self.text, 1, LIGHT_GRAY)

        self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.x = self.x
        self.surface_rect.y = self.y
        self.text_rect = self.text_string.get_rect()

        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))

    def draw(self, screen):
        self.text_string = self.font.render(self.text, 1, LIGHT_GRAY)
        self.text_rect = self.text_string.get_rect()
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))
        screen.blit(self.surface, (self.x, self.y))


class InputBox:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.default_text = text

        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 20)
        self.text_string = self.font.render(self.text, 1, DARK_YELLOW)

        self.surface = pygame.Surface((self.w, self.h))
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.x = self.x
        self.surface_rect.y = self.y
        self.surface.fill(VERY_DARK_GRAY)
        self.text_rect = self.text_string.get_rect()

        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))

    def set_text(self, text):
        if text:
            self.text = text
        else:
            self.text = self.default_text

    def draw(self, screen):
        self.text_string = self.font.render(self.text, 1, DARK_YELLOW)
        self.text_rect = self.text_string.get_rect()
        self.surface.fill(VERY_DARK_GRAY)
        self.surface.blit(self.text_string, (self.w / 2 - self.text_rect.width / 2,
                                             self.h / 2 - self.text_rect.height / 2))
        screen.blit(self.surface, (self.x, self.y))

    def active(self):
        pass