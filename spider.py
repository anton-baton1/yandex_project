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

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 2
        if keys[pygame.K_a]:
            self.rect.x -= 2
        if keys[pygame.K_SPACE] and pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.rect.y -= 100
        if not pygame.sprite.spritecollide(self, self.platform_group_name, False):
            self.rect.y += 5
