import re
from dataclasses import dataclass
from typing import List
from sys import maxsize

@dataclass
class Star:
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0

    def move(self, i):
        self.x += i * self.vx
        self.y += i * self.vy


def draw_message(sec: int, stars: List[Star], width: int, height: int, min_x: int, min_y: int):
    print(f'Found possible message at {sec}')
    content = [[' ' for x in range(width)] for y in range(height)]
    for star in stars:
        content[star.y - min_y][star.x - min_x] = '#'

    for row in content:
        print(''.join(row))


stars = list()

with open('input.txt') as f:
    for line in f.readlines():
        m = re.match(r'position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>', line)
        x, y, vx, vy = map(int, m.groups())
        stars.append(Star(x, y, vx, vy))


N = 20000
CHAR_HEIGHT = 10
CHAR_WIDTH = 6
SPACING = 2

for sec in range(1, N + 1):
    min_x, min_y  = maxsize, maxsize
    max_x, max_y  = -maxsize, -maxsize
    for star in stars:
        star.move(1)
        min_x = min(min_x, star.x)
        max_x = max(max_x, star.x)
        min_y = min(min_y, star.y)
        max_y = max(max_y, star.y)

    width = abs(min_x - max_x) + 1
    height = abs(min_y - max_y) + 1

    if height == CHAR_HEIGHT and  width < 150 and (width + SPACING) % (CHAR_WIDTH + SPACING) == 0:
        draw_message(sec, stars, width, height, min_x, min_y)