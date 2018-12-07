
with open('input.txt') as f:
    entry = f.readline()


alphabet = dict([(c, c.upper()) for c in 'abcdefghijklmnopqrstuvwxyz'] + [(c.upper(), c) for c in 'abcdefghijklmnopqrstuvwxyz'])

def polymerize(test_entry: str, unit: str) -> int:
    units = (unit, unit.upper())
    test_entry = ''.join([c for c in test_entry if c not in units])
    
    parsed = False
    while not parsed:
        parsed = True
        new_entry = ''
        last_char = ''
        for current_char in test_entry:
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
        test_entry = new_entry

    return len(test_entry)


min_size = len(entry)
for unit in 'abcdefghijklmnopqrstuvwxyz':
    min_size = min(min_size, polymerize(entry, unit))

print(min_size)