import sys

import pygame

from platform import Platform
from spider import Spider
from web import Web

pygame.init()

SIZE = WIDTH, HEIGHT = (800, 600)
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLUE = pygame.Color("blue")
BLACK = pygame.Color("#000000")
WHITE = pygame.Color(255, 255, 255)
FPS = 30


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.Surface((WIDTH, HEIGHT))
    fon.fill(BLUE)
    play_button = pygame.draw.rect(fon, RED, (350, 280, 102, 40), 3, 5)
    settings_button = pygame.draw.rect(fon, RED, (350, 340, 102, 40), 3, 5)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)

    play_string = font.render("Играть", 1, pygame.Color('black'))
    play_string_rect = play_string.get_rect()
    play_string_rect.x = 366
    play_string_rect.y = 290

    settings_string = font.render("Настройки", 1, pygame.Color('black'))
    settings_string_rect = settings_string.get_rect()
    settings_string_rect.x = 366
    settings_string_rect.y = 350

    screen.blit(settings_string, settings_string_rect)
    screen.blit(play_string, play_string_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos):
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("MY GAME")

all_sprites = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()

spider = Spider(platforms_group, all_sprites)
spider.rect.x = WIDTH / 2
spider.rect.y = HEIGHT / 2

ground = Platform((0, HEIGHT - 20), (WIDTH, 20), platforms_group, all_sprites)

running = True
spider_flag = True
web_flag = False

start_screen()

while running:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and spider_flag:
            web = Web(event.pos, spider, all_sprites)
            web_flag = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and spider_flag:
            web.length = 0
            web.angle = 0
            web.vel = 0
            web.acceleration = 0
            all_sprites.remove(web)
            web_flag = False
    if web_flag:
        pygame.draw.line(screen, WHITE, (web.rect.x + web.rect.width / 2, web.rect.y + web.rect.height / 2),
                         (spider.rect.x + spider.rect.width / 2, spider.rect.y + spider.rect.height / 2), 2)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
sys.exit(pygame.quit())
