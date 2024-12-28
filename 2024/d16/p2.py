from collections import defaultdict
from collections import namedtuple
from collections import deque

class Coord(namedtuple('Coord', 'x y')):
    def __str__(self):
        return f'({self.x},{self.y})'
    def multiply(self, scalar):
        return Coord(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def up(self):
        return Coord(self.x, self.y - 1)

    def down(self):
        return Coord(self.x, self.y + 1)

    def left(self):
        return Coord(self.x - 1, self.y)

    def right(self):
        return Coord(self.x + 1, self.y)

    def udlr(self):
        return [self.up(), self.down(), self.left(), self.right()]
class Reindeer:
    def __init__(self, coord, dir, path, score):
        self.coord = coord
        self.dir = dir
        self.path = path # a list of coords
        self.score = score
    def move(self):
        next_rd = Reindeer(self.coord, self.dir, self.path.copy(), self.score+1)
        match self.dir:
            case '<':
                next_rd.coord =  self.coord.left()
            case '>':
                next_rd.coord = self.coord.right()
            case '^':
                next_rd.coord = self.coord.up()
            case 'v':
                next_rd.coord = self.coord.down()
        next_rd.path.append(next_rd.coord)
        return next_rd
    def turn_left(self):
        match self.dir:
            case '<': return Reindeer(self.coord, 'v', self.path, self.score + 1000)
            case '>': return Reindeer(self.coord, '^', self.path, self.score + 1000)
            case '^': return Reindeer(self.coord, '<', self.path, self.score + 1000)
            case 'v': return Reindeer(self.coord, '>', self.path, self.score + 1000)
    def turn_right(self):
        match self.dir:
            case '<': return Reindeer(self.coord, '^', self.path, self.score + 1000)
            case '>': return Reindeer(self.coord, 'v', self.path, self.score + 1000)
            case '^': return Reindeer(self.coord, '>', self.path, self.score + 1000)
            case 'v': return Reindeer(self.coord, '<', self.path, self.score + 1000)
def find_in_grid(value):
    for k, v in grid.items():
        if v == value:
            return k
def init_grid(inp):
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Coord(x, y)
            grid[pt] = c
def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Coord(x, y)])
        f.write(ln+'\n')
    f.close()
def print_log(i):
    if i == 0:
        f = open('log.txt', 'w')
        f.write(f'Initial State:\n')
    else:
        f = open('log.txt', 'a')
        f.write(f'Iteration {i}:\n')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Coord(x, y)])
        f.write(ln+'\n')
    f.write('\n\n')
    f.close()
if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '.')
    scores = defaultdict(lambda: float('inf'))
    width = len(inp[0])
    height = len(inp)
    init_grid(inp)
    print_log(0)

    start_coord = find_in_grid('S')
    end_coord = find_in_grid('E')
    initial_rd = Reindeer(start_coord, '>', [start_coord], 0)


    # BFS to score paths through maze
    queue = deque()
    queue.append(initial_rd)
    finishing_rd = []
    while queue:
        current_rd = queue.popleft()

        allowed_moves = [
            current_rd.move(),
            current_rd.turn_left().move(),
            current_rd.turn_right().move(),
        ]

        for next_rd in allowed_moves:
            if grid[next_rd.coord] in '#': continue
            if grid[next_rd.coord] in '.E':
                if next_rd.score < scores[next_rd.coord] + 2000:
                    queue.append(next_rd)
                    if next_rd.score < scores[next_rd.coord]:
                        scores[next_rd.coord] = next_rd.score
                if grid[next_rd.coord] in 'E':
                    finishing_rd.append(next_rd)

    best_score = scores[end_coord]


    seats = set()
    for rd in finishing_rd:
        if rd.score == best_score:
            seats |= set(rd.path)

    for seat in seats:
        grid[seat] = 'O'
    print_grid()
    print(f'best score: {best_score}')
    print(f'seats: {len(seats)}')


    pass
