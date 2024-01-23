import json

import pygame

from constants import screen, SIZE
from terminate import terminate
from widgets import Button, Label, InputBox


def settings_screen():
    settings_window = pygame.Surface(SIZE)
    settings_window.blit(pygame.image.load("data/images/blured_jungle.png"), (-150, -50))

    with open("settings.txt", "r") as file:
        binds = json.load(file)

    back_button = Button(20, 550, 100, 30, "Назад", 15)
    move_left = InputBox(550, 100, 220, 50, pygame.key.name(binds["bind_move_left"]).upper())
    move_right = InputBox(550, 200, 220, 50, pygame.key.name(binds["bind_move_right"]).upper())
    jump = InputBox(550, 300, 220, 50, pygame.key.name(binds["bind_jump"]).upper())
    pause = InputBox(550, 400, 220, 50, pygame.key.name(binds["bind_pause"]).upper())
    move_left_lbl = Label(50, 100, 290, 50, "Движение влево", 20)
    move_right_lbl = Label(50, 200, 310, 50, "Движение вправо", 20)
    jump_lbl = Label(50, 300, 130, 50, "Прыжок", 20)
    pause_lbl = Label(50, 400, 115, 50, "Пауза", 20)
    widgets = (back_button, move_left, move_right, jump, pause, move_left_lbl, move_right_lbl, jump_lbl, pause_lbl)

    text_input_pause = False
    text_input_jump = False
    text_input_move_right = False
    text_input_move_left = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.surface_rect.collidepoint(event.pos):
                    return "home"
                text_input_move_left = False
                text_input_move_right = False
                text_input_jump = False
                text_input_pause = False
                if move_left.surface_rect.collidepoint(event.pos):
                    text_input_move_left = True
                elif move_right.surface_rect.collidepoint(event.pos):
                    text_input_move_right = True
                elif jump.surface_rect.collidepoint(event.pos):
                    text_input_jump = True
                elif pause.surface_rect.collidepoint(event.pos):
                    text_input_pause = True

            if event.type == pygame.KEYDOWN:
                new_binds = binds
                key = event.key
                if key not in binds.values():
                    if text_input_move_left:
                        move_left.set_text(pygame.key.name(event.key).upper())
                        new_binds["bind_move_left"] = pygame.key.key_code(move_left.text)
                    elif text_input_move_right:
                        move_right.set_text(pygame.key.name(event.key).upper())
                        new_binds["bind_move_right"] = pygame.key.key_code(move_right.text)
                    elif text_input_jump:
                        jump.set_text(pygame.key.name(event.key).upper())
                        new_binds["bind_jump"] = pygame.key.key_code(jump.text)
                    elif text_input_pause:
                        pause.set_text(pygame.key.name(event.key).upper())
                        new_binds["bind_pause"] = pygame.key.key_code(pause.text)

                with open("settings.txt", "w") as file:
                    json.dump(new_binds, file)

        for i in widgets:
            i.draw(settings_window)
        screen.blit(settings_window, (0, 0))
        pygame.display.flip()
