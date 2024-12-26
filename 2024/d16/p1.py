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
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = c

if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '.')
    scores = defaultdict(lambda: float('inf'))
    init_grid(inp)
    width = len(inp[0])
    height = len(inp)

    initial_pos = Position(find_in_grid('S'), '>')
    end = find_in_grid('E')
    queue = deque()
    start = (initial_pos, 0)
    queue.append(start)

    while queue:
        current_pos, current_score = queue.popleft()

        allowed_moves = [
            (current_pos.move(), current_score + 1),
            (current_pos.turn_left().move(), current_score + 1001),
            (current_pos.turn_right().move(), current_score + 1001),
        ]

        for next_pos, next_score in allowed_moves:
            if grid[next_pos.p] in '#': continue
            if grid[next_pos.p] in '.E' and scores[next_pos.p] > next_score:
                scores[next_pos.p] = next_score
                queue.append((next_pos, next_score))

    score = scores[end]
    print(score)


    pass
