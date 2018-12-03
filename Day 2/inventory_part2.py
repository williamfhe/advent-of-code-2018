from collections import defaultdict

with open('input.txt') as f:
    words = [word.strip() for word in f.readlines()]


end = len(words)
word_len = len(words[0])
same_letter_string = ''

for i in range(end):
    if i == end:
        break

    for j in range(i+1, end):
        current_string = ''
        for l in range(word_len):
            if words[i][l] == words[j][l]:
                current_string += words[i][l]

        if len(current_string) > len(same_letter_string):
            same_letter_string = current_string
    


print(same_letter_string)