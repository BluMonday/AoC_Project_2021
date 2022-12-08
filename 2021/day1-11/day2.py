if __name__ == '__main__':
    f = open('day2.txt')
    moves = f.read().split('\n')
    directions = []
    distances = []
    commands = []
    aim = 0
    h_pos = 0
    depth = 0
    for move in moves:
        command = (move.split(' '))
        command[1] = int(command[1])
        if command[0] == 'up':
            aim -= command[1]
        elif command[0] == 'down':
            aim += command[1]
        elif command[0] == 'forward':
            h_pos += command[1]
            depth += aim*command[1]

    print(h_pos * depth)
    print('hello')
