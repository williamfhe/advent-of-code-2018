
value = 0

with open('input.txt') as f:
    for line in f.readlines():
        value += int(line)

print(value)