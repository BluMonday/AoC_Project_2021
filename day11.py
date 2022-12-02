from typing import Any


def take_step(matrix):
    # first step in iteration
    # add one and find triggered boxes
    matrix = add_one_all(matrix)
    delta = find_over_10(matrix)
    step_prev = delta
    while len(delta) > 0:
        for x in delta:
            nh = find_neighborhood(matrix, x)
            matrix = add_one(matrix, nh)
        # find new delta
        step = find_over_10(matrix)
        delta = list(set(step) - set(step_prev))
        step_prev = step
    flashes = len(step_prev)
    matrix = set_to_zero(matrix, step_prev)
    xs = len(matrix[0])
    ys = len([x[0] for x in matrix])
    done = xs*ys == len(step_prev)
    return matrix, flashes, done

def print_matrix(matrix):
    for x in matrix:
        print(x)

def in_range_and_coerce(input, smallest, largest):
    return max(smallest, min(input, largest))

def find_over_10(matrix):
    coords = []
    xs = len(matrix[0])
    ys = len([x[0] for x in matrix])
    for x in range(0, xs):
        for y in range(0, ys):
            coord = (x, y)
            if matrix[y][x] > 9: coords.append(coord)
    return coords

def add_one(matrix, coords):
    for x, y in coords:
        matrix[y][x] += 1
    return matrix
def set_to_zero(matrix, coords):
    for x, y in coords:
        matrix[y][x] = 0
    return matrix

def add_one_all(matrix):
    return [[x+1 for x in row] for row in matrix]


def find_neighborhood(matrix, root_coord):
    nh = list()
    xs = len(matrix[0])
    ys = len([x[0] for x in matrix])

    x1 = root_coord[0] - 1
    if x1 < 0:
        x1 = 0
    x2 = root_coord[0] + 1
    if x2 >= xs: x2 -= 1

    y1 = root_coord[1] - 1
    if y1 < 0: y1 = 0
    y2 = root_coord[1] + 1
    if y2 >= ys: y2 = ys-1

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            coord = (x, y)
            if coord != root_coord: nh.append(coord)
    return nh

if __name__ == '__main__':

    f = open('day11.txt')
    input = f.read().split('\n')

    matrix = [list(map(int, x)) for x in input]
    flashes = 0
    for x in range(0, 5000):
        matrix, f, done = take_step(matrix)
        flashes += f
        print(f'after step {x+1} and {flashes} flashes:')
        print_matrix(matrix)
        if done:
            print(f'Done after {x+1}')
            break


    print(flashes)
    print('done')