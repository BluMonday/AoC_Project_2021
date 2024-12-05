import re

if __name__ == '__main__':
    f = open('input.txt')
    input = f.read()
    commands = re.findall(r"mul\(\d*,\d*\)", input)
    sum = 0
    for cmd in commands:
        numbers = [int(x) for x in cmd[4:-1].split(',')]
        sum += numbers[0] * numbers[1]
    print(sum)