import pygame

from game import game
from select_level_screen import select_level_screen
from settings_screen import settings_screen
from sources import MAX_LEVEL, main_music, game_music
from start_screen import start_screen

pygame.init()
pygame.display.set_caption("SAPW")

start_screen_open = True
select_level_screen_open = False
game_screen_open = False
settings_screen_open = False

while True:
    main_music.play(-1)
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
        main_music.stop()
        game_music.stop()
        game_music.play(-1)
        event = game(level)
        if event == "next":
            level += 1
            if level > MAX_LEVEL:
                select_level_screen_open = True
                game_screen_open = False
                level -= 1
            game_music.stop()
        elif event == "home":
            start_screen_open = True
            game_screen_open = False
            game_music.stop()

    if settings_screen_open:
        button = settings_screen()
        if button == "home":
            start_screen_open = True
            settings_screen_open = False
