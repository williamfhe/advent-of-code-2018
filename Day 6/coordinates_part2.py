from sys import maxsize
from dataclasses import dataclass
from collections import defaultdict

min_x, max_x = maxsize, -maxsize
min_y, max_y = maxsize, -maxsize

entry_points = set()

with open('input.txt') as f:
    for line in f.readlines():
        x, y = map(int, line.split(','))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

        entry_points.add((x, y))

zone_size = 0

MAX_DISTANCE = 10000

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        current_distance = 0
        for point in entry_points:
            current_distance += abs(x - point[0]) + abs(y - point[1])
            if current_distance >= MAX_DISTANCE:
                break

        else:
            # for else, nice feature python !
            zone_size += 1

print(zone_size)
