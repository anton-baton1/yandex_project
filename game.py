import json

import pygame

import constants
from camera import Camera
from constants import MAX_WEB_LENGTH, FPS, WHITE, all_sprites, clock, SIZE, VERY_DARK_GRAY, screen
from generate_level import generate_level
from lose_screen import lose_screen
from pause_screen import pause_screen
from terminate import terminate
from timer import Timer
from web import Web
from web_thread import WebThread
from win_screen import win_screen


def game(level):
    game_screen = pygame.Surface(SIZE)

    with open("settings.txt", "r") as file:
        binds = json.load(file)

    pause = pygame.Surface((40, 40), pygame.SRCALPHA)
    pause_button = pygame.draw.circle(pause, WHITE, (20, 20), 20, 2)
    pygame.draw.line(pause, WHITE, (14, 10), (14, 30), 2)
    pygame.draw.line(pause, WHITE, (24, 10), (24, 30), 2)

    web_flag = False
    timer_flag = False
    pause_flag = False

    TIMER_EVENT = pygame.USEREVENT + 1

    camera = Camera()
    timer = Timer(20)
    spider, exit = generate_level(level)

    while True:
        clock.tick(FPS)
        game_screen.fill(VERY_DARK_GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == TIMER_EVENT and not pause_flag and timer_flag:
                timer.update()

            if event.type == pygame.KEYDOWN and not timer_flag and event.key in (
                    binds["bind_move_left"], binds["bind_move_right"], binds["bind_jump"]):
                pygame.time.set_timer(TIMER_EVENT, 10)
                timer_flag = True

            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause_button.collidepoint(
                    event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pause_flag = not pause_flag
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                web = Web(event.pos, all_sprites)
                web_thread = WebThread(spider, web, all_sprites)
                game_screen.blit(web_thread.image.convert_alpha(), (0, 0))
                web_flag = True
                if web_thread.length > MAX_WEB_LENGTH or \
                        not pygame.sprite.spritecollide(web, spider.platform_group_name, False):
                    all_sprites.remove(web, web_thread)
                    web_flag = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and not pause_flag:
                all_sprites.remove(web, web_thread)
                del web, web_thread
                web_flag = False

        if spider.rect.y >= 320 and timer_flag:
            action = lose_screen()
            if action == "restart":
                return
            elif action == "home":
                game_screen.fill(VERY_DARK_GRAY)
                return "home"

        camera.update(spider)
        for sprite in all_sprites:
            camera.apply(sprite)

        if web_flag:
            spider.acceleration_y = 0
            spider.velocity_y = 0
            game_screen.blit(web_thread.image, (0, 0))

        if pygame.sprite.collide_mask(spider, exit):
            action = win_screen()
            if action == "next":
                return "next"
            elif action == "restart":
                return
            elif action == "home":
                game_screen.fill(VERY_DARK_GRAY)
                return "home"

        if not pause_flag:
            all_sprites.draw(game_screen)
            all_sprites.update()
        else:
            action = pause_screen()
            if action == "play":
                pause_flag = False
            elif action == "restart":
                return
            elif action == "home":
                game_screen.fill(VERY_DARK_GRAY)
                return "home"
        game_screen.blit(pause, (0, 0))
        game_screen.blit(timer.text, (timer.x, timer.y))
        screen.blit(game_screen, (0, 0))
        pygame.display.flip()
