from collections import defaultdict
from collections import namedtuple

class Point(namedtuple('Point', 'x y')):
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
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


x_count = 0
x_limit = 130*4
in_loop = False
def mark_x(point):
    global x_count
    global x_limit
    global in_loop
    if grid[point] != 'x':
        x_count = 0
        grid[point] = 'x'
    else:
        x_count += 1
    if x_count > x_limit:
        in_loop = True
    return
def reset_grid():
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[Point(x,y)] = c
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
        # to end of grid
        for i in range(start_point.y):
            current_pt = current_pt.up()
            current_val = grid[current_pt]
            # hit obstacle
            if current_val == '#':
                grid[current_pt.down()] = '>'
                return False
            # no obstacle
            else:
                mark_x(current_pt)
    if start_dir == 'v':
        for i in range(height-start_point.y):
            current_pt = current_pt.down()
            if grid[current_pt] == '#':
                grid[current_pt.up()] = '<'
                return False
            else:
                mark_x(current_pt)
    if start_dir == '<':
        for i in range(start_point.x):
            current_pt = current_pt.left()
            if grid[current_pt] == '#':
                grid[current_pt.right()] = '^'
                return False
            else:
                mark_x(current_pt)
    if start_dir == '>':
        for i in range(width-start_point.x):
            current_pt = current_pt.right()
            if grid[current_pt] == '#':
                grid[current_pt.left()] = 'v'
                return False
            else:
                mark_x(current_pt)
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



    count = 0
    x_count = 0
    guard_present = True
    for y in range(len(inp[0])):
        for x in range(len(inp)):
            k = Point(x, y)
            v = grid[k]
            if v == '.':
                # try obstacle at this point
                grid[k] = '#'
                print(f'Try obstacle at {str(k)}')
                #print_grid()
                point, val = find_gaurd()
                while val != '!' and guard_present:
                    guard_present = not move_gaurd(point, val)
                    point, val = find_gaurd()
                    #print(point)
                    if in_loop:
                        in_loop = False
                        count += 1
                        print_grid()
                        x_count = 0
                        break
                reset_grid()
                guard_present = True

    print(count)
