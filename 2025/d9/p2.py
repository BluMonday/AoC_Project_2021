import math
from collections import defaultdict
from collections import namedtuple
import os

class Point(namedtuple('Point', 'x y')):
    def __str__(self):
        return f'({self.x},{self.y})'
    def multiply(self, scalar):
        return Point(self.x*scalar, self.y*scalar)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def n(self):
        return Point(self.x, self.y-1)
    def nw(self):
        return Point(self.x-1, self.y-1)

    def ne(self):
        return Point(self.x+1, self.y-1)

    def s(self):
        return Point(self.x, self.y+1)

    def sw(self):
        return Point(self.x-1, self.y+1)

    def se(self):
        return Point(self.x+1, self.y+1)

    def w(self):
        return Point(self.x-1, self.y)

    def e(self):
        return Point(self.x+1, self.y)

    def udlr(self):
        return [self.n(), self.s(), self.e(), self.w()]
    def adj(self):
        return [self.n(), self.ne(), self.nw(), self.s(), self.se(), self.sw(), self.e(), self.w()]
def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x, y)])
        f.write(ln+'\n')
    f.close()
def print_log(i):
    if i == 0:
        try:
            os.remove('log.txt')
        except:
            pass
        f = open('log.txt', 'w')
        f.write(f'Initial State:\n')
    else:
        f = open('log.txt', 'a')
        f.write(f'Iteration {i}:\n')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x, y)])
        f.write(ln+'\n')
    f.write('\n\n')
    f.close()
def find_all_in_row(value, idx):
    return [k for k, v in grid.items() if v == value and k.y == idx]
def find_all_in_grid(value):
    return [k for k, v in grid.items() if v == value]
def init_grid(inp):
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[Point(x,y)] = c
def init_grid_from_dimensions(width, height):
    for y in range(height):
        for x in range(width):
            grid[Point(x,y)] = "."

def area(p1, p2):
    return (abs(p1.x-p2.x)+1)*(abs(p1.y-p2.y)+1)


def get_unit_vector(start_pt, end_pt):
    dir_vector = end_pt - start_pt
    if dir_vector.x != 0:
        return Point(int(math.copysign(1, dir_vector.x)), 0)
    else:
        return Point(0, int(math.copysign(1, dir_vector.y)))

def draw_line(start_pt, end_pt):
    direction = get_unit_vector(start_pt, end_pt)
    mag = int(max(map(abs,end_pt-start_pt)))+1
    if mag < 2:
        return
    draw_pt = start_pt
    for i in range(1, mag-1):
        draw_pt += direction
        grid[draw_pt] = 'X'

if __name__ == '__main__':

    f = open('in2.txt')
    inp = [i.split(',') for i in f.read().split('\n')]
    inp_int = [list(map(int, x)) for x in inp]
    pts = [Point(x,y) for x,y in inp_int]

    width = max([p.x for p in pts])+1
    height = max([p.y for p in pts])+1
    grid = defaultdict(lambda: '.')
    init_grid_from_dimensions(width, height)

    prev_pt = pts[0]
    grid[prev_pt] = '#'
    for i in range(1,len(pts)):
        # each point in input is a red tile
        grid[pts[i]] = '#'
        draw_line(prev_pt, pts[i])
        prev_pt = pts[i]
    draw_line(prev_pt,pts[0])

    print_grid()

    pairs = []
    for i in range(len(pts)-1):
        for j in range(i+1, len(pts)):
            pairs.append((area(pts[i], pts[j]), pts[i], pts[j]))

    pairs.sort()
    print(pairs[-1])

    pass



