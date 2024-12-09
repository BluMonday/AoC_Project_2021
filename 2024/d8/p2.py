from collections import defaultdict
from collections import namedtuple

class Point(namedtuple('Point', 'x y')):
    def multiply(self, scalar):
        return Point(self.x*scalar, self.y*scalar)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def up(self):
        return Point(self.x, self.y-1)
    def down(self):
        return Point(self.x, self.y+1)
    def left(self):
        return Point(self.x-1, self.y)
    def right(self):
        return Point(self.x+1, self.y)

def get_nodes(pt1, pt2):
    a = pt1.multiply(2)-pt2
    b = pt2.multiply(2)-pt1
    return a,b

def process_ant(ant_list, node_list):
    pt1 = ant_list[0]
    ant_list = ant_list[1:]
    for x in ant_list:
        a, b = get_nodes(pt1, x)
        node_list.append(a)
        node_list.append(b)
    if len(ant_list) == 1:
        return node_list
    else:
        process_ant(ant_list, node_list)

def count_grid():
    count = 0
    for y in range(height):
        for x in range(width):
            if grid[Point(x,y)] == '#':
                count += 1
    return count

def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += grid[Point(x,y)]
        f.write(ln+'\n')
    f.close()

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(str)
    antennas = defaultdict(list)

    width = len(inp[0])
    height = len(inp)

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = c
            if c != '.':
                current_val = antennas[c]
                new_val = current_val.append(pt)

    for k, v in antennas.items():
        node_list = []
        process_ant(v, node_list)
        for p in node_list:
            grid[p] = '#'

    print_grid()
    print(count_grid())
    pass
