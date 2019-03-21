
def parse_node(get_number):
    child_count = next(get_number)
    metadata_count = next(get_number)

    if child_count == 0:
        return sum(next(get_number) for _ in range(metadata_count))
        
    child_values = [parse_node(get_number) for _ in range(child_count)]
    child_sum = 0

    for _ in range(metadata_count):
        metadata = next(get_number)
        if metadata and metadata - 1 < len(child_values):
            child_sum += child_values[metadata - 1] 

    return child_sum

with open('input.txt') as f:
    line = f.readline()
    print(parse_node((int(number) for number in line.split())))
