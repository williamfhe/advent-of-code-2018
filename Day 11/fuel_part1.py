from collections import defaultdict
from sys import maxsize

SERIAL_NUMBER = 2187

WIDTH = 300
HEIGHT = 300


square_powers = defaultdict(int)
better_index = (-1, -1)
max_power = -maxsize

for x in range(1, WIDTH + 1):
    rack_id = x + 10
    for y in range(1, HEIGHT + 1):
        power_level = rack_id * y
        power_level += SERIAL_NUMBER
        power_level *= rack_id
        power_level = (power_level % 1000) // 100
        power_level -= 5

        for i in range(-2, 1):
            xx = x + i

            if not 1 <= xx <= WIDTH - 3:
                continue

            for j in range(-2, 1):
                yy = y + j

                if not 1 <= yy <= HEIGHT - 3:
                    continue

                square_powers[xx, yy] += power_level
                if square_powers[xx, yy] > square_powers[better_index]:
                    better_index = xx, yy
                    max_power = square_powers[xx, yy]

print(f'{better_index[0]},{better_index[1]}')
