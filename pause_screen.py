import pygame

from constants import screen
from terminate import terminate
from widgets import Button, Label


def pause_screen():
    pause_window = pygame.Surface((300, 200))

    pause = Label(0, 0, 300, 50, "Пауза", 32)
    play_button = Button(125, 120, 50, 50, "▶", 20)
    restart_button = Button(220, 120, 50, 50, "r", 20)
    home_button = Button(30, 120, 50, 50, "h", 20)
    widgets = (pause, play_button, restart_button, home_button)

    while True:
        pause_window.fill(pygame.Color("#595959"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "play"
                if restart_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "restart"
                if home_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "home"
        for i in widgets:
            i.draw(pause_window)
        screen.blit(pause_window, (250, 200))
        pygame.display.flip()
