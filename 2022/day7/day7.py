import re


if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read()
    prompt = puzzle_input.split('\n')

    dir = dict()
    current_dir = tuple('/')
    dir[current_dir] = 0
    for line in prompt:
        if line[0] == '$':
            cmd = line[2:4]
            if cmd == 'cd':
                cd_cmd = line[5::]
                if cd_cmd == '/':
                    current_dir = tuple('/')
                elif cd_cmd == '..':
                    current_dir = current_dir[:-1:]
                else:
                    current_dir = current_dir + tuple([cd_cmd])
                    if current_dir not in dir:
                        dir[current_dir] = 0
            elif cmd == 'ls':
                continue
        elif line[0:3] == 'dir':
            continue
        else:
            m = re.match(r'\d+', line)
            value = int(m.group())
            for i in range(len(current_dir)):
                key = current_dir[:i+1]
                dir[key] = dir[key] + value
        continue

    print(sum([v for (k, v) in dir.items() if v <= 100000]))

    total_size = 70000000
    needed_size = 30000000
    total_used = dir[tuple('/')]
    unused = total_size - total_used

    to_delete = needed_size - (total_size - total_used)
    dir2 = [(k, v) for (k, v) in dir.items() if v >= to_delete]
    sorter = lambda x: x[1]
    dir2.sort(key= sorter)
    print(dir2[0][1])
    print('done')