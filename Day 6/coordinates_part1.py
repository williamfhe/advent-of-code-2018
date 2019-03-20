from sys import maxsize
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class PointInfos:
    reach_infinity: bool = False
    nearest_to: int = 0

min_x, max_x = maxsize, -maxsize
min_y, max_y = maxsize, -maxsize

entry_points = dict()

with open('input.txt') as f:
    for line in f.readlines():
        x, y = map(int, line.split(','))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

        entry_points[(x, y)] = PointInfos(False, 1)

for y in range(min_y, max_y+1):
    is_y_infinity_limit = y in (min_y, max_y)
    for x in range(min_x, max_x+1):
        is_point_infinity_limit = is_y_infinity_limit or x in (min_x, max_x)

        current_point_infos = entry_points.get((x, y))
        if current_point_infos:
            if is_point_infinity_limit:
                current_point_infos.reach_infinity = True
            continue

        nearest_point = None
        current_min_distane = maxsize
        for point in entry_points:
            distance = abs(x - point[0]) + abs(y - point[1])
            if distance < current_min_distane:
                nearest_point = point
                current_min_distane = distance
            elif distance == current_min_distane:
                nearest_point = None


        if nearest_point is None:
            continue

        current_point_infos = entry_points[nearest_point]
        current_point_infos.nearest_to += 1
        if is_point_infinity_limit:
                current_point_infos.reach_infinity = True

print(max(point_infos.nearest_to for point_infos in entry_points.values() if not point_infos.reach_infinity))
