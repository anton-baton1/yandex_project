import pygame

WIDTH = 800
HEIGHT = 600
SIZE = WIDTH, HEIGHT

FPS = 60

LEVEL = 1
WEB_LENGTH = 300

RED = pygame.Color("red")
BLUE = pygame.Color("blue")
BLACK = pygame.Color("black")
GRAY = pygame.Color("gray")
WHITE = pygame.Color("white")

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
