from collections import defaultdict
from collections import namedtuple
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
class Position:
    def __init__(self, p, dir):
        self.p = p
        self.dir = dir
    def move(self):
        match self.dir:
            case '<': return Position(self.p.left(), self.dir)
            case '>': return Position(self.p.right(), self.dir)
            case '^': return Position(self.p.up(), self.dir)
            case 'v': return Position(self.p.down(), self.dir)
    def turn_left(self):
        match self.dir:
            case '<': return Position(self.p, 'v')
            case '>': return Position(self.p, '^')
            case '^': return Position(self.p, '<')
            case 'v': return Position(self.p, '>')
    def turn_right(self):
        match self.dir:
            case '<': return Position(self.p, '^')
            case '>': return Position(self.p, 'v')
            case '^': return Position(self.p, '>')
            case 'v': return Position(self.p, '<')
def find_in_grid(value):
    for k, v in grid.items():
        if v == value:
            return k
def init_grid(inp):
    for y in range(height):
        for x in range(width):
            pt = Point(x,y)
            grid[pt] = '.'
def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x, y)])
        f.write(ln+'\n')
    f.close()
if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    falling_bytes = [(int(c.split(',')[0]), int(c.split(',')[1])) for c in inp]
    grid = defaultdict(lambda: '#')
    if config == 1:
        width = 6+1
        height = 6+1
        corrupt_bytes = 12
    else:
        width = 70+1
        height = 70+1
        corrupt_bytes = 1024

    while True:
        scores = defaultdict(lambda: float('inf'))
        corrupted_pts = set()
        corrupted_time = defaultdict(lambda: float('inf'))

        corrupt_bytes += 1
        for i in range(corrupt_bytes):
            x, y = falling_bytes[i]
            pt = Point(x, y)
            if pt == Point(70,70):
                pass
            corrupted_pts.add(pt)
            corrupted_time[pt] = i+1

        init_grid(inp)

        start_pt = Point(0,0)
        end_pt = Point(width-1, height-1)
        queue = deque()
        start = (start_pt, 0)
        queue.append(start)
        visited = set()
        visited.add(start)

        while queue:
            current_pt, current_step = queue.popleft()

            next_pts = current_pt.udlr()
            next_step = current_step + 1

            for next_pt in next_pts:
                if grid[next_pt] in '#': continue
                if next_pt in corrupted_pts: continue
                if grid[next_pt] in '.' and next_pt not in visited:
                    visited.add(next_pt)
                    queue.append((next_pt, next_step))
                    scores[next_pt] = next_step


        score = scores[end_pt]
        if score == float('inf'): break

    print(falling_bytes[corrupt_bytes-1])
    print_grid()

    pass
