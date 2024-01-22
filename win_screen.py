import pygame

from constants import screen, SIZE
from terminate import terminate
from widgets import Button, Label


def win_screen():
    win_window = pygame.Surface((300, 200))

    pause = Label(0, 0, 300, 50, "Победа", 32)
    next_button = Button(125, 120, 50, 50, "▶▶", 12)
    restart_button = Button(220, 120, 50, 50, "↻", 20)
    home_button = Button(30, 120, 50, 50, "⌂", 20)
    widgets = (pause, next_button, restart_button, home_button)

    while True:
        win_window.fill(pygame.Color("#595959"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if next_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "next"
                if restart_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "restart"
                if home_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "home"
        for i in widgets:
            i.draw(win_window)
        screen.blit(win_window, (250, 200))
        pygame.display.flip()
