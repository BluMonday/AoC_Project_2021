import re, copy


def process_input(input):
    towers, moves = input.split('\n\n')
    tower_rows = towers.split('\n')
    tower_rows = tower_rows[-2::-1]

    stacks = list()
    for row in tower_rows:
        values = [row[i] for i in range(1, len(row), 4)]
        stacks.append(values)

    s2 = list()
    for x in zip(*stacks):
        s2.append(list(x))
    stacks1 = [x for x in list(zip(*stacks))]

    stacks2 = list()
    for stack in stacks1:
        values = [x for x in stack if x != ' ']
        stacks2.append(values)

    return stacks2, moves.split('\n')

def apply_move(stacks, qty, src, dest):
    from_stack = stacks[src-1]
    to_stack = stacks[dest-1]
    for i in range(qty):
        to_stack.append(from_stack.pop())
    stacks[src-1] = from_stack
    stacks[dest-1] = to_stack

    return stacks

def apply_move2(stacks, qty, src, dest):
    from_stack = stacks[src-1]
    to_stack = stacks[dest-1]
    to_stack = to_stack + from_stack[-qty::1]
    from_stack = from_stack[:-qty]
    stacks[src-1] = from_stack
    stacks[dest-1] = to_stack

    return stacks



if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read()
    stacks1, moves = process_input(puzzle_input)
    stacks2 = copy.deepcopy(stacks1)
    for move in moves:
        qty, src, dest = [int(x) for x in re.findall(r'\d+', move)]
        stacks1 = apply_move(stacks1, qty, src, dest)
        stacks2 = apply_move2(stacks2, qty, src, dest)

    message1 = [stack[-1] for stack in stacks1]
    message1 = ''.join(message1)
    message2 = [stack[-1] for stack in stacks2]
    message2 = ''.join(message2)

    print(message1)
    print(message2)
    print('done')
