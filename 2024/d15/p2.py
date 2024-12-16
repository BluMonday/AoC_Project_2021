from collections import defaultdict
from collections import namedtuple
import re

class Point(namedtuple('Point', 'x y')):
    def __str__(self):
        return f'({self.x},{self.y})'
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

    def udlr(self):
        return [self.up(), self.down(), self.left(), self.right()]

class Gaurd:
    def __str__(self):
        return f'p={self.position} v={self.vel}'

    position = Point(0, 0)
    vel = Point(0, 0)

    def move(self):
        global height
        global width
        next_pos = self.position + self.vel
        if next_pos.x >= width:
            next_pos -= Point(width, 0)
        elif next_pos.x < 0:
            next_pos += Point(width, 0)
        if next_pos.y >= height:
            next_pos -= Point(0, height)
        elif next_pos.y < 0:
            next_pos += Point(0, height)
        self.position = next_pos
        return next_pos

def init_grid():
    for y in range(height):
        for x in range(width):
            pt = Point(x,y)
            grid[pt] = '.'
def print_grid(seconds):
    f = open('out1.txt', 'a')
    f.write(f'After {seconds} seconds\n')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x,y)])
        f.write(ln+'\n')
    f.write('\n\n')
    f.close()


if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '.')

    if config == 1:
        width = 11
        height = 7
    else:
        width = 101
        height = 103

    gaurds = []
    for line in inp:
        g = Gaurd()
        mp = re.search(r'p=(-?\d*),(-?\d*)', line)
        mv = re.search(r'v=(-?\d*),(-?\d*)', line)
        g.position = Point(int(mp.group(1)), int(mp.group(2)))
        g.vel = Point(int(mv.group(1)), int(mv.group(2)))
        gaurds.append(g)

    seconds = 0
    while seconds != 8169:
        init_grid()
        print(f'After {seconds} seconds')
        for g in gaurds:
            grid[g.position] = 'X'
        [g.move() for g in gaurds]
        if (seconds-88) % 101 == 0 or (seconds-31) % 103 == 0:
            print_grid(seconds)
        if seconds % 10000 == 0:
            break
        seconds += 1
    # answer 8168
    half_width = width//2
    half_height = height//2

    nw = sum([grid[Point(x, y)] for x in range(half_width) for y in range(half_height)])
    ne = sum([grid[Point(x, y)] for x in range(half_width+1, width) for y in range(half_height)])
    sw = sum([grid[Point(x, y)] for x in range(half_width) for y in range(half_height+1, height)])
    se = sum([grid[Point(x, y)] for x in range(half_width+1, width) for y in range(half_height+1, height)])


    print(f'Safety Factor: {nw*ne*sw*se}')
    pass
