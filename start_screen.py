import pygame

from constants import RED, BLUE, BLACK, screen, SIZE


def start_screen():
    fon = pygame.Surface(SIZE)
    fon.fill(BLUE)
    play_button = pygame.draw.rect(fon, RED, (350, 280, 102, 40), 3, 5)
    settings_button = pygame.draw.rect(fon, RED, (350, 340, 102, 40), 3, 5)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)

    play_string = font.render("Играть", 1, BLACK)
    play_string_rect = play_string.get_rect()
    play_string_rect.x = 366
    play_string_rect.y = 290

    settings_string = font.render("Настройки", 1, BLACK)
    settings_string_rect = settings_string.get_rect()
    settings_string_rect.x = 366
    settings_string_rect.y = 350

    screen.blit(settings_string, settings_string_rect)
    screen.blit(play_string, play_string_rect)

    while True:
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos):
                return  # начинаем игру
        pygame.display.flip()
