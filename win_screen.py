import pygame

from constants import screen
from terminate import terminate
from widgets import Button, Label
from star import Star


def win_screen(status1, status2, status3):
    win_window = pygame.Surface((400, 300))

    win = Label(0, 0, 400, 50, "Победа", 32)
    next_button = Button(175, 220, 50, 50, "▶▶", 12)
    restart_button = Button(320, 220, 50, 50, "r", 20)
    home_button = Button(30, 220, 50, 50, "h", 20)
    widgets = (win, next_button, restart_button, home_button)

    stars = pygame.sprite.Group()
    star1 = Star(115, 120, status1, False, stars)
    star2 = Star(175, 120, status2, False, stars)
    star3 = Star(235, 120, status3, False, stars)

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
        stars.draw(win_window)
        stars.update()
        screen.blit(win_window, (200, 150))
        pygame.display.flip()
