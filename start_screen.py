import pygame

from constants import RED, BLUE, BLACK, screen, SIZE
from terminate import terminate
from widgets import Button, Label


def start_screen():
    start_window = pygame.Surface(SIZE)
    start_window.blit(pygame.image.load("data/start_window_image.png"), (-150, -50))

    sapw = Label(300, 50, 200, 50, "SAPW", 48)
    sa = Label(300, 100, 200, 12, "Spider Adventure", 12)
    pw = Label(300, 112, 200, 12, "Pixel World", 12)
    play_button = Button(300, 300, 200, 50, "Играть", 20)
    settings_button = Button(300, 375, 200, 50, "Настройки", 20)
    widgets = (sapw, sa, pw, play_button, settings_button)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and play_button.surface_rect.collidepoint(event.pos):
                return "play"
            if event.type == pygame.MOUSEBUTTONDOWN and settings_button.surface_rect.collidepoint(event.pos):
                return "settings"
        for i in widgets:
            i.draw(start_window)
        screen.blit(start_window, (0, 0))
        pygame.display.flip()
