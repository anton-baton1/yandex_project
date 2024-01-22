import pygame

from constants import screen,SIZE
from terminate import terminate
from widgets import Button, Label, InputBox
import json


def settings_screen():
    settings_window = pygame.Surface(SIZE)
    settings_window.blit(pygame.image.load("data/blured_jungle.png"), (-150, -50))

    with open("settings.txt", "r") as file:
        binds = json.load(file)

    back_button = Button(20, 550, 100, 30, "Назад", 15)
    move_left = InputBox(550, 100, 220, 50, pygame.key.name(binds["bind_move_left"]).upper())
    move_right = InputBox(550, 200, 220, 50, pygame.key.name(binds["bind_move_right"]).upper())
    jump = InputBox(550, 300, 220, 50, pygame.key.name(binds["bind_jump"]).upper())
    move_left_lbl = Label(50, 100, 290, 50, "Движение влево", 20)
    move_right_lbl = Label(50, 200, 310, 50, "Движение вправо", 20)
    jump_lbl = Label(50, 300, 130, 50, "Прыжок", 20)
    widgets = (back_button, move_left, move_right, jump, move_left_lbl, move_right_lbl, jump_lbl)

    text_input_move_left = False
    text_input_move_right = False
    text_input_jump = False

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
                if move_left.surface_rect.collidepoint(event.pos):
                    text_input_move_left = True
                if move_right.surface_rect.collidepoint(event.pos):
                    text_input_move_right = True
                if jump.surface_rect.collidepoint(event.pos):
                    text_input_jump = True
            if event.type == pygame.KEYDOWN:
                new_binds = binds
                if text_input_move_left:
                    move_left.set_text(pygame.key.name(event.key).upper())
                    new_binds["bind_move_left"] = event.key
                elif text_input_move_right:
                    move_right.set_text(pygame.key.name(event.key).upper())
                    new_binds["bind_move_right"] = event.key
                elif text_input_jump:
                    jump.set_text(pygame.key.name(event.key).upper())
                    new_binds["bind_jump"] = event.key

                with open("settings.txt", "w") as file:
                    json.dump(new_binds, file)

        for i in widgets:
            i.draw(settings_window)
        screen.blit(settings_window, (0, 0))
        pygame.display.flip()
