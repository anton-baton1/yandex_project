import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, size, *group):
        super().__init__(*group)
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color("grey"))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
