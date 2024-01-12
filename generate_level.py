from constants import platforms_group, all_sprites
from platform import Platform
from spider import Spider


def generate_level(num):
    filename = f"maps/map{num}.txt"
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    level = list(map(lambda x: x.ljust(max_width, '.'), level_map))
    px, py = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Platform((x * 40, y * 40), (40, 40), platforms_group, all_sprites)
            elif level[y][x] == '@':
                px, py = x, y
    new_player = Spider((px * 40, py * 40), platforms_group, all_sprites)
    return new_player
