import re

def parse_claim(claim: str) -> (int, (int, int), (int, int)):
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
    claim_id = int(m.group(1))
    x, y = int(m.group(2)), int(m.group(3))
    w, h = int(m.group(4)), int(m.group(5))
    return claim_id, x, y, w, h

piece = [0] * 1000 * 1000

# 0 => Empty
# 1 => Claimed
# 2 => Overlap

with open('input.txt') as f:
    for line in f.readlines():
        _, x, y, w, h = parse_claim(line)
        for i in range(x, x + w):
            for j in range(y, y + h):
                index = i + j * 1000
                if piece[index] == 0:
                    piece[index] = 1
                elif piece[index] == 1:
                    piece[index] = 2

print(piece.count(2))

