import pygame

from constants import screen, SIZE
from terminate import terminate
from widgets import Button, Label


def win_screen(star1, star2, star3):
    win_window = pygame.Surface((400, 300))

    win = Label(0, 0, 400, 50, "Победа", 32)
    next_button = Button(175, 220, 50, 50, "▶▶", 12)
    restart_button = Button(320, 220, 50, 50, "↻", 20)
    home_button = Button(30, 220, 50, 50, "⌂", 20)
    widgets = (win, next_button, restart_button, home_button)

    while True:
        win_window.fill(pygame.Color("#595959"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if next_button.surface_rect.collidepoint(x - 200, y - 150):
                    return "next"
                if restart_button.surface_rect.collidepoint(x - 200, y - 150):
                    return "restart"
                if home_button.surface_rect.collidepoint(x - 200, y - 150):
                    return "home"
        for i in widgets:
            i.draw(win_window)
        screen.blit(win_window, (200, 150))
        pygame.display.flip()
