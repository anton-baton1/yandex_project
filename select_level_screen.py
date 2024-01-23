import pygame

import constants
from terminate import terminate
from widgets import Button, Label, InputBox
from generate_level import generate_level


def select_level_screen():
    select_level_window = pygame.Surface(constants.SIZE)
    select_level_window.blit(pygame.image.load("data/blured_jungle.png"), (-150, -50))

    level_1 = Button(10, 275, 50, 50, "1", 24)
    level_2 = Button(110, 275, 50, 50, "2", 24)
    level_3 = Button(210, 275, 50, 50, "3", 24)
    back_button = Button(20, 550, 100, 30, "Назад", 15)

    widgets = (level_1, level_2, level_3, back_button)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in widgets:
                    if i is back_button and i.surface_rect.collidepoint(event.pos):
                        return "home"
                    elif i.surface_rect.collidepoint(event.pos):
                        return int(i.text)
        for i in widgets:
            i.draw(select_level_window)
        constants.screen.blit(select_level_window, (0, 0))
        pygame.display.flip()
