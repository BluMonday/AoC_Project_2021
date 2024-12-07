from collections import defaultdict
from collections import namedtuple

class Point(namedtuple('Point', 'x y')):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def up(self):
        return Point(self.x, self.y-1)
    def down(self):
        return Point(self.x, self.y+1)
    def left(self):
        return Point(self.x-1, self.y)
    def right(self):
        return Point(self.x+1, self.y)

def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += grid[Point(x,y)]
        f.write(ln+'\n')
    f.close()
def find_gaurd():
    for k, v in grid.items():
        if v == '^' or v == 'v' or v == '<' or v == '>':
            return k, v
    return Point(-1,-1), '!'
def move_gaurd(start_point, start_dir):
    grid[start_point] = 'x'
    current_pt = start_point
    if start_dir == '^':
        for i in range(start_point.y):
            current_pt = current_pt.up()
            current_val = grid[current_pt]
            if current_val == '#':
                grid[current_pt.down()] = '>'
                return False
            else:
                grid[current_pt] = 'x'
    if start_dir == 'v':
        for i in range(height-start_point.y):
            current_pt = current_pt.down()
            if grid[current_pt] == '#':
                grid[current_pt.up()] = '<'
                return False
            else:
                grid[current_pt] = 'x'
    if start_dir == '<':
        for i in range(start_point.x):
            current_pt = current_pt.left()
            if grid[current_pt] == '#':
                grid[current_pt.right()] = '^'
                return False
            else:
                grid[current_pt] = 'x'
    if start_dir == '>':
        for i in range(width-start_point.x):
            current_pt = current_pt.right()
            if grid[current_pt] == '#':
                grid[current_pt.left()] = 'v'
                return False
            else:
                grid[current_pt] = 'x'
    grid[current_pt] = '.'
    return True

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(str)

    width = len(inp[0])
    height = len(inp)

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[Point(x,y)] = c

    point, val = find_gaurd()
    while val != '!':
        move_gaurd(point, val)
        point, val = find_gaurd()
    print_grid()

    total = 1
    for v in grid.values():
        if v == 'x':
            total += 1
    print(total)
