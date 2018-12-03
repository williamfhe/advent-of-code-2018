from collections import defaultdict

two_count, three_count = 0, 0

with open('input.txt') as f:
    for word in f.readlines():

        letter_count = defaultdict(int)
        for letter in word:
            letter_count[letter] += 1

        two_added, three_added = False, False
        for count in letter_count.values():
            if count == 2 and not two_added:
                two_count += 1
                two_added = True

            if count == 3 and not three_added:
                three_count += 1
                three_added = True

            if two_added and three_added:
                break

print(two_count * three_count)