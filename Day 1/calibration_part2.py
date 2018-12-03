
value = 0

used = set([0])

with open('input.txt') as f:
    steps = [int(i) for i in f.readlines()]


running = True

while running:
    for step in steps:
        value += step
        if value in used:
            running = False
            break
        else:
            used.add(value)

print(value)