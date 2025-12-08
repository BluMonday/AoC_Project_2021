from collections import defaultdict
from collections import namedtuple
import os
from collections import deque

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
if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '#')
    scores = defaultdict(lambda: 0)
    init_grid(inp)
    width = len(inp[0])
    height = len(inp)

    start_pt = find_all_in_grid('S')[0]
    grid[start_pt.s()] = '|'
    scores[start_pt.s()] = 1
    start = start_pt.s()
    ans = 0
    print_log(0)
    for y in range(1,height):
        # propagate into current row
        beams = find_all_in_row('|', y)
        for beam in beams:
            if grid[beam.s()] == '^':
                scores[beam.sw()] += scores[beam]
                grid[beam.sw()] = '|'
                scores[beam.se()] += scores[beam]
                grid[beam.se()] = '|'
            else:
                scores[beam.s()] += scores[beam]
                grid[beam.s()] = '|'
        print_log(y)


    # add up scores in final row
    for k, v in scores.items():
        if k.y == height - 1:
            ans += v

    print(ans)
