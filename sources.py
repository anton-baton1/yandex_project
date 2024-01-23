import pygame

SIZE = WIDTH, HEIGHT = (800, 600)

FPS = 60

MAX_LEVEL = 3
MAX_WEB_LENGTH = 300

RED = pygame.Color("red")
BLACK = pygame.Color("black")
GRAY = pygame.Color("gray")
WHITE = pygame.Color("white")
GREEN = pygame.Color("green")
DARK_YELLOW = pygame.Color("#f1c232")
LIGHT_GRAY = pygame.Color("#efefef")
VERY_DARK_GRAY = pygame.Color("#1b1b1b")

screen = pygame.display.set_mode(SIZE, pygame.SRCALPHA)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
star_for_collect = pygame.sprite.Group()

pygame.mixer.init()

main_music = pygame.mixer.Sound("data/music/main.wav")
game_music = pygame.mixer.Sound("data/music/game.wav")
absolute_win_music = pygame.mixer.Sound("data/music/win.wav")
lose_music = pygame.mixer.Sound("data/music/hooooow.wav")
main_music.set_volume(0.5)
game_music.set_volume(0.5)
absolute_win_music.set_volume(0.5)
lose_music.set_volume(0.5)
