

with open('input.txt') as f:
    entry = f.readline()

parsed = False

alphabet = dict([(c, c.upper()) for c in 'abcdefghijklmnopqrstuvwxyz'] + [(c.upper(), c) for c in 'abcdefghijklmnopqrstuvwxyz'])

while not parsed:
    parsed = True
    new_entry = ''
    last_char = ''
    for current_char in entry:
        if not last_char:
            last_char = current_char
            continue
        
        if current_char == alphabet[last_char]:
            last_char = ''
            parsed = False
        else:
            new_entry += last_char
            last_char  = current_char

    new_entry += last_char
    entry = new_entry

print(len(entry))