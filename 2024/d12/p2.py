from collections import defaultdict
from collections import namedtuple
class Region:
    def __init__(self, initial_pt):
        self.plant_type = grid[initial_pt]
        self.pts = {initial_pt}
        self.price = 0

    def calc_price(self):
        top_pts = set()
        [top_pts.add(pt) for pt in self.pts if pt.up() not in self.pts]
        right_pts = set()
        [right_pts.add(pt) for pt in self.pts if pt.right() not in self.pts]
        left_pts = set()
        [left_pts.add(pt) for pt in self.pts if pt.left() not in self.pts]
        bottom_pts = set()
        [bottom_pts.add(pt) for pt in self.pts if pt.down() not in self.pts]

        top_edges = set()
        for start_pt in top_pts:
            next_pt = start_pt.right()
            while True:
                if next_pt in top_pts:
                    next_pt = next_pt.right()
                    continue
                else:
                    top_edges.add(next_pt)
                    break
        right_edges = set()
        for start_pt in right_pts:
            next_pt = start_pt.down()
            while True:
                if next_pt in right_pts:
                    next_pt = next_pt.down()
                    continue
                else:
                    right_edges.add(next_pt)
                    break
        bottom_edges = set()
        for start_pt in bottom_pts:
            next_pt = start_pt.right()
            while True:
                if next_pt in bottom_pts:
                    next_pt = next_pt.right()
                    continue
                else:
                    bottom_edges.add(next_pt)
                    break
        left_edges = set()
        for start_pt in left_pts:
            next_pt = start_pt.down()
            while True:
                if next_pt in left_pts:
                    next_pt = next_pt.down()
                    continue
                else:
                    left_edges.add(next_pt)
                    break

        num_sides = len(top_edges) + len(right_edges) + len(bottom_edges) + len(left_edges)
        return num_sides * len(self.pts)

    def __str__(self):
        return f'A region of {self.plant_type} with size {len(self.pts)}'




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

    def udlr(self):
        return [self.up(), self.down(), self.left(), self.right()]


def print_grid():
    f = open('out.txt', 'w')
    for y in range(height):
        ln = ''
        for x in range(width):
            ln += str(grid[Point(x,y)])
        f.write(ln+'\n')
    f.close()


def process_pt(region, start_pt):
    # get adjacent matching points
    next_pts = [x for x in start_pt.udlr() if grid[x] == region.plant_type and x in pts_to_process]
    for next_pt in next_pts:
        # remove matching pt from pts_to_process and add to current region
        pts_to_process.discard(next_pt)
        region.pts.add(next_pt)
        process_pt(region, next_pt)
    return


if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    grid = defaultdict(lambda: '.')

    width = len(inp[0])
    height = len(inp)

    regions = []
    pts_to_process = set()

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            pt = Point(x,y)
            grid[pt] = c
            pts_to_process.add(pt)

    total_price = 0

    while len(pts_to_process) != 0:
        start_pt = pts_to_process.pop()
        active_reg = Region(start_pt)
        process_pt(active_reg, start_pt)
        regions.append(active_reg)
        total_price += active_reg.calc_price()
        pass

    print(f'Total Price: {total_price}')
    pass
