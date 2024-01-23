import pygame

from load_image import load_image


class Star(pygame.sprite.Sprite):
    image_active = load_image("images/star_active.png")
    image_passive = load_image("images/star_passive.png")
    small_image = load_image("images/small_star.png")

    def __init__(self, x, y, active, small, *group):
        super().__init__(*group)
        self.small = small
        self.active = active
        if self.small:
            self.image = Star.small_image
        elif self.active:
            self.image = Star.image_active
        else:
            self.image = Star.image_passive
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_active(self, active):
        self.active = active
        if self.active:
            self.image = Star.image_active
        else:
            self.image = Star.image_passive
