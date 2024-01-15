import pygame

from camera import Camera
from constants import WEB_LENGTH, LEVEL, FPS, WHITE, screen, all_sprites
from generate_level import generate_level
from start_screen import start_screen
from terminate import terminate
from web import Web

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("MY GAME")

spider_flag = True
web_flag = False

start_screen()

camera = Camera()
spider = generate_level(LEVEL)

while True:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and spider_flag:
            web = Web(event.pos, spider, all_sprites)
            if web.length > WEB_LENGTH:
                all_sprites.remove(web)
            else:
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
        spider.velocity_y = 0

    camera.update(spider)
    for sprite in all_sprites:
        camera.apply(sprite)

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
