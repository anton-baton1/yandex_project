import pygame

from camera import Camera
from constants import WEB_LENGTH, LEVEL, FPS, WHITE, screen, all_sprites, clock, BLACK
from generate_level import generate_level
from terminate import terminate
from timer import Timer
from web import Web
from web_thread import WebThread


def game():
    pause = pygame.Surface((40, 40), pygame.SRCALPHA)
    # pause.fill(WHITE)
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
                web = Web(event.pos, all_sprites)
                web_thread = WebThread(spider, web, all_sprites)
                print(web_thread.rect)
                screen.blit(web_thread.image.convert_alpha(), (0, 0))
                web_flag = True
                if web_thread.length > WEB_LENGTH or not pygame.sprite.spritecollide(web, spider.platform_group_name, False):
                    all_sprites.remove(web, web_thread)
                    web_flag = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                all_sprites.remove(web, web_thread)
                del web, web_thread
                web_flag = False

        if web_flag:
            spider.acceleration_y = 0
            spider.velocity_y = 0

        camera.update(spider)
        for sprite in all_sprites:
            camera.apply(sprite)

        all_sprites.draw(screen)
        all_sprites.update()
        screen.blit(pause, (0, 0))
        screen.blit(timer.text, (timer.x, timer.y))
        if web_flag:
            screen.blit(web_thread.image, (0, 0))
        pygame.display.flip()
