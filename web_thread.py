import math

import pygame

from constants import SIZE, BLACK


class WebThread(pygame.sprite.Sprite):
    image = pygame.Surface(SIZE, pygame.SRCALPHA)

    def __init__(self, spider, web, *group):
        super().__init__(*group)
        self.spider = spider
        self.web = web

        self.image = WebThread.image
        self.rect = self.image.get_rect()
        self.length = math.sqrt((self.spider.rect.center[0] - self.web.rect.center[0]) ** 2 + (
                self.spider.rect.center[1] - self.web.rect.center[1]) ** 2)
        self.angle = math.sin((self.spider.rect.center[0] - self.web.rect.center[0]) / self.length)
        self.vel = 0
        self.acceleration = 0

        pygame.draw.line(self.image, BLACK, self.spider.rect.center, self.web.rect.center, 2)

    def update(self):
        if pygame.key.get_pressed()[pygame.K_q]:
            self.length -= 10
            self.angle = math.sin((self.spider.rect.center[0] - self.web.rect.center[0]) / self.length)
        if not pygame.sprite.spritecollide(self.spider, self.spider.platform_group_name, False):
            self.acceleration = -0.01 * math.sin(self.angle)
            self.vel += self.acceleration
            self.vel *= 0.995  # демпфинг
            self.angle += self.vel
            self.spider.rect.x = round(self.web.rect.x + (self.web.rect.width / 2 - self.spider.rect.width / 2) +
                                       self.length * math.sin(self.angle))
            self.spider.rect.y = round(self.web.rect.y + self.length * math.cos(self.angle))
        self.image.fill((0, 0, 0, 0))
        pygame.draw.line(self.image, BLACK, self.spider.rect.center, self.web.rect.center, 2)