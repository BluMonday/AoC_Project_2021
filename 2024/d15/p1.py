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
        return f'p={self.position}'

    position = Point(0, 0)

    def move(self, cmd):
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

def init_grid(inp):
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = c

def print_grid(move):
    if move == 0:
        f = open('log.txt', 'w')
    else:
        f = open('log.txt', 'a')
    f.write(f'After {move} moves\n')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x,y)])
        f.write(ln+'\n')
    f.write('\n\n')
    f.close()


if __name__ == '__main__':

    config = 1
    f = open(f'in{config}.txt')
    inp = f.read().split('\n\n')
    grid_inp = inp[0].split('\n')
    moves_inp = inp[1]
    moves_inp = moves_inp.replace('\n', '')
    grid = defaultdict(lambda: '.')

    init_grid(grid_inp)

    width = len(grid_inp[0])
    height = len(grid_inp)


    moves = 0
    for m in moves_inp:
        print(f'After {moves} moves')
        print_grid(moves)


        moves += 1

    pass
