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

    def gps_coord(self):
        return 100*self.y + self.x
def try_move_boxes(start_row, mov_dir):
    # start with list of '['
    next_pts = []
    for pt in start_row:
        # adjacent to each [
        next_pts.append(mov_dir(pt))
        # adjacent to each ]
        next_pts.append(mov_dir(pt.right()))
    next_things = [grid[x] for x in next_pts]

    if all([x in '.' for x in next_things]):
        # just move
        for pt in start_row:
            grid[pt] = '.'
            grid[pt.right()] = '.'
        for pt in start_row:
            grid[mov_dir(pt)] = '['
            grid[mov_dir(pt.right())] = ']'
        return True
    elif any([x in '#' for x in next_things]):
        # can't move
        return False
    else :
        # touching only boxes and empty space
        # collect left edges of next boxes and call recursively
        next_row = [p for p, t in zip(next_pts, next_things) if t in '[']
        for p, t in zip(next_pts, next_things):
            if t in ']': next_row.append(p.left())
        next_boxes_movable = try_move_boxes(next_row, mov_dir)
        if next_boxes_movable:
            # move this thing
            for pt in start_row:
                grid[pt] = '.'
                grid[pt.right()] = '.'
            for pt in start_row:
                grid[mov_dir(pt)] = '['
                grid[mov_dir(pt.right())] = ']'
            return True
        else:
            # don't move
            return False

def try_move_h(start_pt, mov_dir):
    thing = grid[start_pt]
    next_pt = mov_dir(start_pt)
    next_thing = grid[next_pt]

    if next_thing in '.':
        # just move
        grid[start_pt] = '.'
        grid[next_pt] = thing
        return True
    elif next_thing in '#':
        # can't move
        return False
    elif next_thing in '[]':
        # check if next object can move
        next_thing_movable = try_move_h(next_pt, mov_dir)
        if next_thing_movable:
            # move this thing
            grid[start_pt] = '.'
            grid[next_pt] = thing
            return True
        else:
            # don't move
            return False

def try_move_v(start_pt, mov_dir):
    thing = grid[start_pt]
    next_pt = mov_dir(start_pt)
    next_thing = grid[next_pt]

    if next_thing in '.':
        # just move
        grid[start_pt] = '.'
        grid[next_pt] = thing
        return True
    elif next_thing in '#':
        # can't move
        return False
    elif next_thing in '[]':
        # check if next object can move
        next_row = next_pt
        if next_thing in ']':
            next_row = next_pt.left()
        next_thing_movable = try_move_boxes([next_row], mov_dir)
        if next_thing_movable:
            # move this thing
            grid[start_pt] = '.'
            grid[next_pt] = thing
            return True
        else:
            # don't move
            return False

class Gaurd:
    def __str__(self):
        return f'p={self.position}'

    position = Point(0, 0)

    def move(self, cmd):
        global height
        global width
        mov_dir = Point.right
        match cmd:
            case '<':
                mov_dir = Point.left
            case '>':
                mov_dir = Point.right
            case '^':
                mov_dir = Point.up
            case 'v':
                mov_dir = Point.down
        if mov_dir in [Point.left, Point.right]:
            if try_move_h(self.position, mov_dir):
                self.position = mov_dir(self.position)
        else:
            if try_move_v(self.position, mov_dir):
                self.position = mov_dir(self.position)
        return

def find_in_grid(value):
    for k, v in grid.items():
        if v == value:
            return k
def convert_for_p2(input):
    match input:
        case '.':
            return '..'
        case 'O':
            return '[]'
        case '@':
            return '@.'
        case '#':
            return '##'

def init_grid(inp):
    for y, line in enumerate(inp):
        p2_line = ''.join([convert_for_p2(x) for x in line])
        for x, c in enumerate(p2_line):
            pt = Point(x,y)
            grid[pt] = c

def print_grid(move, move_dir):
    if move == 0:
        f = open('log.txt', 'w')
        f.write(f'Initial State:\n')
    else:
        f = open('log.txt', 'a')
        f.write(f'{move} move {move_dir}:\n')
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
    inp = f.read().split('\n\n')
    grid_inp = inp[0].split('\n')
    moves_inp = inp[1]
    moves_inp = moves_inp.replace('\n', '')
    grid = defaultdict(lambda: '.')

    init_grid(grid_inp)
    guard = Gaurd()
    guard.position = find_in_grid('@')

    width = len(grid_inp[0])*2
    height = len(grid_inp)


    moves = 0
    print_grid(moves, '')
    for m in moves_inp:
        guard.move(m)
        moves += 1
        print_grid(moves, m)
        pass

    print(sum([p.gps_coord() for p in grid.keys() if grid[p] == 'O']))
    print(sum([p.gps_coord() for p in grid.keys() if grid[p] == '[']))
    pass
