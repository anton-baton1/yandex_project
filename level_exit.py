import pygame


class LevelExit(pygame.sprite.Sprite):
    sheet = pygame.image.load("data/images/black_hole.png")

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.columns = 8
        self.rows = 4
        self.frames = []
        self.cut_sheet(LevelExit.sheet, self.columns, self.rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() / columns, sheet.get_height() / rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
