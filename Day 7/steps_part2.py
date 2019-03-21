from collections import defaultdict

def insert_in_order(lst: list, step: str):
    index = 0
    for i, s in enumerate(lst):
        if step > s:
            index = i + 1
            break

    lst.insert(index, step)

input_tree = defaultdict(set)
depends_on_count = defaultdict(int)

# list containing the steps that can be done next
can_be_done_list = list()

with open('input.txt') as f:
    for line in f.readlines():
        needed_step = line[5]
        todo_step = line[36]

        if needed_step not in input_tree:
            insert_in_order(can_be_done_list, needed_step)

        input_tree[needed_step].add(todo_step)

        input_tree[todo_step]
        if todo_step in can_be_done_list:
            can_be_done_list.remove(todo_step)

        depends_on_count[todo_step] += 1

done = ''

max_worker = 5

current_steps = dict()

current_time = 0
next_time = 0

while can_be_done_list or next_time:
    current_time = next_time
    next_time = 0

    # if current_time > 30:
    #     break
    done_steps = list()
    for step in current_steps:
        if current_steps[step] == current_time:
            done_steps.append(step)

    for step in done_steps:
        done += step
        del current_steps[step]
        needed_for = input_tree.pop(step)
        for todo_step in needed_for:
            depends_on_count[todo_step] -= 1
            if not depends_on_count[todo_step]:
                insert_in_order(can_be_done_list, todo_step)
    
    # current_step = can_be_done_list.pop(0)
    for _ in range(len(current_steps), max_worker):
        if not can_be_done_list:
            break
        new_step = can_be_done_list.pop(0)
        current_steps[new_step] = current_time + ord(new_step) - 4

    if current_steps:
        next_time = min(current_steps.values())

print(done, current_time)