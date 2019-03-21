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

while can_be_done_list:
    current_step = can_be_done_list.pop(0)
    needed_for = input_tree.pop(current_step)
    for todo_step in needed_for:
        depends_on_count[todo_step] -= 1
        if not depends_on_count[todo_step]:
            insert_in_order(can_be_done_list, todo_step)

    done += current_step

print(done)