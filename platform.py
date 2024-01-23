import pygame


class Platform(pygame.sprite.Sprite):
    image = pygame.image.load("data/images/grass.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Platform.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
