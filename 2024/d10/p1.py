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


def climb_to_top(t, start_pt):
    start_ht = grid[start_pt]
    global score
    if start_ht == 9 and start_pt not in trailhead_summits[t]:
        score += 1
        trailhead_summits[t].append(start_pt)
        return
    elif start_ht < 9:
        up = start_pt.up()
        down = start_pt.down()
        left = start_pt.left()
        right = start_pt.right()
        directions = [up, down, left, right]
        next_steps = [x for x in directions if grid[x] == start_ht + 1]
        for step in next_steps:
            climb_to_top(t, step)
    return


if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: -1)

    width = len(inp[0])
    height = len(inp)

    trailheads = []
    trailhead_summits = defaultdict(list)
    score = 0

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = int(c)
            if c == '0':
                trailheads.append(pt)

    for t in trailheads:
        score_prev = score
        climb_to_top(t, t)
        this_trail_score = score - score_prev
        print(f'Trailhead: {t} Score: {this_trail_score}')
        pass
    print(f'Total map score: {score}')
    print_grid()

    pass
