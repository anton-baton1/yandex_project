import pygame

from constants import screen, SIZE
from terminate import terminate
from widgets import Button, Label


def lose_screen():
    win_window = pygame.Surface((300, 200))

    lose = Label(0, 0, 300, 50, "Поражение", 32)
    restart_button = Button(200, 120, 50, 50, "r", 20)
    home_button = Button(50, 120, 50, 50, "h", 20)
    widgets = (lose, restart_button, home_button)

    while True:
        win_window.fill(pygame.Color("#595959"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "restart"
                if home_button.surface_rect.collidepoint(x - 250, y - 200):
                    return "home"
        for i in widgets:
            i.draw(win_window)
        screen.blit(win_window, (250, 200))
        pygame.display.flip()
