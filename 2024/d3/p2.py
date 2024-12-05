import re

if __name__ == '__main__':
    f = open('input.txt')
    input = f.read()

    dont = re.search(r"don't\(\)", input)
    while dont is not None:
        do = re.search(r"do\(\)", input)
        while do is not None and do.end() < dont.start():
            input = input[:do.start()] + input[do.end():] # remove redundant do()
            do = re.search(r"do\(\)", input)
            dont = re.search(r"don't\(\)", input)
        if do is not None:
            input = input[:dont.start()] + input[do.end():] # remove dont() to do() span
            dont = re.search(r"don't\(\)", input)
        else:
            input = input[:dont.start()]
            break

    commands = re.findall(r"mul\(\d*,\d*\)", input)
    sum = 0
    for cmd in commands:
        numbers = [int(x) for x in cmd[4:-1].split(',')]
        sum += numbers[0] * numbers[1]
    print(sum)