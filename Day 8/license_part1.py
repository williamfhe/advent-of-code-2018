
def parse_node(get_number):
    child_count = next(get_number)
    metadata_count = next(get_number)

    metadata_sum = sum(parse_node(get_number) for _ in range(child_count))
    metadata_sum += sum(next(get_number) for _ in range(metadata_count))

    return metadata_sum

with open('input.txt') as f:
    line = f.readline()
    print(parse_node((int(number) for number in line.split())))
