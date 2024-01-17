import pygame

from camera import Camera
from constants import WEB_LENGTH, LEVEL, FPS, WHITE, screen, all_sprites, clock, BLACK
from generate_level import generate_level
from terminate import terminate
from web import Web
from timer import Timer


def game():
    pause = pygame.Surface((40, 40))
    pause.fill(WHITE)
    pause_button = pygame.draw.circle(pause, BLACK, (20, 20), 20, 2)
    pygame.draw.line(pause, BLACK, (14, 10), (14, 30), 2)
    pygame.draw.line(pause, BLACK, (24, 10), (24, 30), 2)

    web_flag = False
    timer_flag = True

    TIMER_EVENT = pygame.USEREVENT + 1

    camera = Camera()
    timer = Timer(20)
    spider = generate_level(LEVEL)

    while True:
        clock.tick(FPS)
        screen.fill(WHITE)
        screen.blit(pause, (0, 0))
        screen.blit(timer.text, (timer.x, timer.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == TIMER_EVENT:
                timer.update()

            if event.type == pygame.KEYDOWN and timer_flag and event.key in (pygame.K_a, pygame.K_d, pygame.K_SPACE):
                pygame.time.set_timer(TIMER_EVENT, 10)
                timer_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause_button.collidepoint(event.pos):
                print("pause")
                pygame.time.delay(5000)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                web = Web(event.pos, spider, all_sprites)
                if web.length > WEB_LENGTH:
                    all_sprites.remove(web)
                else:
                    web_flag = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
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
