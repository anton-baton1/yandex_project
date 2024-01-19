import pygame


class Web(pygame.sprite.Sprite):
    image = pygame.image.load("data/web.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Web.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
