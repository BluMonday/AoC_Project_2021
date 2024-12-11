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

def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x,y)])
        f.write(ln+'\n')
    f.close()

def id_next_step(start_pt):
    start_ht = grid[start_pt]
    if start_ht < 9:
        next_ht = start_ht + 1
        summit = False
    else:
        summit = True
        next_ht = start_ht
    next_step = []
    up = start_pt.up()
    down = start_pt.down()
    left = start_pt.left()
    right = start_pt.right()
    directions = [up, down, left, right]
    next_step = [x for x in directions if grid[x] == next_ht]
    if summit:
        for pt in next_step:


    return next_step

if __name__ == '__main__':

    f = open('in1.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: -1)

    width = len(inp[0])
    height = len(inp)

    trailheads = []
    su

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = int(c)
            if c == '0':
                trailheads.append(pt)


    for t in trailheads:
        next_steps = id_next_step(t)
        while True:
            if len(next_steps) == 0 and
            for step in next_steps:


            break
        pass

    print_grid()

    pass
