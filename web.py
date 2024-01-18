import math

import pygame


class Web(pygame.sprite.Sprite):
    image = pygame.image.load("data/web.png")

    def __init__(self, pos, spider, *group):
        super().__init__(*group)
        self.spider = spider
        self.image = Web.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.length = math.sqrt((self.spider.rect.center[0] - self.rect.center[0]) ** 2 + (
                    self.spider.rect.center[1] - self.rect.center[1]) ** 2)
        self.angle = math.sin((self.spider.rect.center[0] - self.rect.center[0]) / self.length)
        self.vel = 0
        self.acceleration = 0

    def update(self):
        if pygame.key.get_pressed()[pygame.K_q]:
            self.length -= 10
            self.angle = math.sin((self.spider.rect.center[0] - self.rect.center[0]) / self.length)
        if not pygame.sprite.spritecollide(self.spider, self.spider.platform_group_name, False):
            self.acceleration = -0.01 * math.sin(self.angle)
            self.vel += self.acceleration
            self.vel *= 0.995  # демпфинг
            self.angle += self.vel

        self.spider.rect.x = round(self.rect.x + (self.rect.width / 2 - self.spider.rect.width / 2) +
                                   self.length * math.sin(self.angle))
        self.spider.rect.y = round(self.rect.y + self.length * math.cos(self.angle))
