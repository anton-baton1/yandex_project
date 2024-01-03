import pygame


class Spider(pygame.sprite.Sprite):
    image = pygame.image.load("data/spider_image.png")

    def __init__(self, pos, platform_group_name, *group):
        super().__init__(*group)
        self.image = Spider.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.platform_group_name = platform_group_name
        self.acc_y = 0.5
        self.vel_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_SPACE] and pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.acc_y = -10
        # if not pygame.sprite.spritecollide(self, self.platform_group_name, False) and self.vel_y == 0:
        #     self.acc_y = -10

        #     self.rect.y += 5
        if not pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.acc_y = 0.5
        self.vel_y += self.acc_y
        self.rect.y += self.vel_y
        if pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.vel_y = 0
            self.acc_y = 0
