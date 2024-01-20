import pygame

import constants
from load_image import load_image


class Spider(pygame.sprite.Sprite):
    image = load_image("demo_spider.png", -1)

    def __init__(self, pos, platform_group_name, *group):
        super().__init__(*group)
        self.image = Spider.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.platform_group_name = platform_group_name

        self.acceleration_y = 0
        self.velocity_y = 0
        self.velocity_x = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[constants.bind_jump] and pygame.sprite.spritecollide(self, self.platform_group_name,
                                                                     False) and self.velocity_y == 0:
            self.acceleration_y = -10
        if not pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.acceleration_y = 0.5

        self.velocity_y += self.acceleration_y
        self.rect.y += self.velocity_y

        if pygame.sprite.spritecollide(self, self.platform_group_name, False):
            if self.velocity_y < 0:
                self.velocity_y = -self.velocity_y
            else:
                self.velocity_y = 0
                self.acceleration_y = 0

        coll_right = all([not ((self.rect.top - 15 <= i.rect.top <= self.rect.bottom - 15 or
                                i.rect.top <= self.rect.top <= i.rect.bottom) and
                               self.rect.right >= i.rect.left > self.rect.left) for i in self.platform_group_name])
        coll_left = all([not ((self.rect.top - 15 <= i.rect.top <= self.rect.bottom - 15 or
                               i.rect.top <= self.rect.top <= i.rect.bottom) and
                              i.rect.right >= self.rect.left > i.rect.left) for i in self.platform_group_name])

        if keys[constants.bind_move_right] and coll_right:
            self.velocity_x = 5
        if keys[constants.bind_move_left] and coll_left:
            self.velocity_x = -5
        self.rect.x += self.velocity_x
        self.velocity_x = 0
