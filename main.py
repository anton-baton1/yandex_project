import pygame

from game import game
from settings_screen import settings_screen
from start_screen import start_screen
from select_level_screen import select_level_screen
from constants import MAX_LEVEL

pygame.init()
pygame.display.set_caption("MY GAME")

start_screen_open = True
select_level_screen_open = False
game_screen_open = False
settings_screen_open = False

while True:
    if start_screen_open:
        button = start_screen()
        if button == "play":
            select_level_screen_open = True
            start_screen_open = False
        elif button == "settings":
            settings_screen_open = True
            start_screen_open = False
    if select_level_screen_open:
        level = select_level_screen()
        if level == "home":
            start_screen_open = True
            select_level_screen_open = False
        else:
            game_screen_open = True
            select_level_screen_open = False
    if game_screen_open:
        event = game(level)
        if event == "next":
            level += 1
            if level > MAX_LEVEL:
                select_level_screen_open = True
                game_screen_open = False
                level -= 1
        elif event == "home":
            start_screen_open = True
            game_screen_open = False

    if settings_screen_open:
        button = settings_screen()
        if button == "home":
            start_screen_open = True
            settings_screen_open = False
