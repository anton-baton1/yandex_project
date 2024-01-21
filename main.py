import pygame

from game import game
from settings_screen import settings_screen
from start_screen import start_screen

pygame.init()
pygame.display.set_caption("MY GAME")

start_screen_open = True
game_screen_open = False
settings_screen_open = False

while True:
    if start_screen_open:
        button = start_screen()
        if button == "play":
            game_screen_open = True
            start_screen_open = False
        elif button == "settings":
            settings_screen_open = True
            start_screen_open = False
    if game_screen_open:
        event = game()
        if event == "level completed":
            start_screen_open = True
            game_screen_open = False
        elif event == "home":
            start_screen_open = True
            game_screen_open = False

    if settings_screen_open:
        button = settings_screen()
        if button == "start":
            start_screen_open = True
            settings_screen_open = False
