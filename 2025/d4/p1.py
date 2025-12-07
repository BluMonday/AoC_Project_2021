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

def find_in_grid(value):
    for k, v in grid.items():
        if v == value:
            return k

def find_all_in_grid(value):
    all_k = []
    for k, v in grid.items():
        if v == value:
            all_k.append(k)
    return all_k
def init_grid(inp):
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = c

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '.')
    init_grid(inp)
    width = len(inp[0])
    height = len(inp)

    rolls = find_all_in_grid('@')
    ans = 0

    for r in rolls:
        x = 0
        num_adjacent = sum([grid[p]=='@' for p in r.adj()])
        if num_adjacent < 4:
            ans += 1
        pass

    print(ans)
