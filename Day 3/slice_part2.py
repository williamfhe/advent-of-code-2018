import re

def parse_claim(claim: str) -> (int, (int, int), (int, int)):
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
    claim_id = int(m.group(1))
    x, y = int(m.group(2)), int(m.group(3))
    w, h = int(m.group(4)), int(m.group(5))
    return claim_id, x, y, w, h

valid_claim = -1
piece = [0] * 1000 * 1000

# 0 => Empty
# 1 => Claimed
# 2 => Overlap

with open('input.txt') as f:
    claims = f.readlines()


for claim in claims:
    claim_id, x, y, w, h = parse_claim(claim)
    for i in range(x, x + w):
        for j in range(y, y + h):
            index = i + j * 1000
            if piece[index] == 0:
                piece[index] = 1
            elif piece[index] == 1:
                piece[index] = 2

for claim in claims:

    claim_id, x, y, w, h = parse_claim(claim)
    overlap = False

    for i in range(x, x + w):
        for j in range(y, y + h):
            if piece[i + j * 1000] == 2:
                overlap = True
                break

        if overlap:
            break

    if not overlap:
        valid_claim = claim_id
        break
            

print(valid_claim)

