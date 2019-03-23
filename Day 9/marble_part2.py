from collections import defaultdict, deque

player_count = 424
last_marble = 71482 * 100

player_scores = defaultdict(int)

circle = deque([0])

current_player = 0

for marble in range(1, last_marble + 1):
    current_player = (current_player + 1) % player_count
    if marble % 23 == 0:
        circle.rotate(7)
        player_scores[current_player] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)

print(max(player_scores.values()) if player_scores else 0)