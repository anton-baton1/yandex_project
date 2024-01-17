import pygame

from constants import RED, BLUE, BLACK, screen, SIZE, GRAY
from terminate import terminate


def settings_screen():
    fon = pygame.Surface(SIZE)
    fon.fill(GRAY)
    move_left = pygame.draw.rect(fon, RED, (350, 280, 102, 40), 3, 5)
    font = pygame.font.Font(None, 30)

    move_left_string = font.render("Влево", 1, BLACK)
    move_left_string_rect = move_left_string.get_rect()
    move_left_string_rect.x = 366
    move_left_string_rect.y = 290

    fon.blit(move_left_string, move_left_string_rect)
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and move_left.collidepoint(event.pos):
                return "start"
        pygame.display.flip()
