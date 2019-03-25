from collections import defaultdict
from sys import maxsize

SERIAL_NUMBER = 2187

WIDTH = 300
HEIGHT = 300


square_powers = defaultdict(int)

for x in range(1, WIDTH + 1):
    rack_id = x + 10
    for y in range(1, HEIGHT + 1):
        power_level = rack_id * y
        power_level += SERIAL_NUMBER
        power_level *= rack_id
        power_level = (power_level % 1000) // 100
        power_level -= 5

        square_powers[x, y] = power_level


def generate_power(start_x: int, start_y: int, zone_size: int):
    for x in range(start_x, start_x + zone_size):
        for y in range(start_y, start_y + zone_size):
            yield square_powers[x, y]


largest_zone = None
largest_zone_power = -maxsize

for zone_size in range(1, 300):
    print(f'current={zone_size} - max_power={largest_zone_power} : {largest_zone}')
    for x in range(1, WIDTH - zone_size):
        for y in range(1, HEIGHT - zone_size):
            max_zone_power = sum(generate_power(x, y, zone_size))   
            if max_zone_power > largest_zone_power:
                largest_zone = (x, y, zone_size)
                largest_zone_power = max_zone_power


x, y, size = largest_zone
print(f'{x},{y},{size}')