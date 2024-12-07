from collections import defaultdict
from collections import namedtuple

class Point(namedtuple('Point', 'x y')):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def get_word(point_list):
    x = ''.join([grid[a] for a in point_list])
    return x


def word_search(start_point):
    count = 0

    # clockwise from top-left
    points = [Point(start_point.x-1, start_point.y-1),
              Point(start_point.x+1, start_point.y-1),
              Point(start_point.x+1, start_point.y+1),
              Point(start_point.x-1, start_point.y+1)]


    orientations = ['MSSM', 'MMSS', 'SMMS', 'SSMM']

    word = get_word(points)
    for orientation in orientations:
        if word == orientation:
            count += 1
            break
    return count


if __name__ == '__main__':
    f = open('input.txt')
    inp = f.read().split('\n')
    grid = defaultdict(str)
    xmas_count = 0

    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[Point(x,y)] = c

    for y in range(len(inp[0])):
        for x in range(len(inp)):
            pt = Point(x,y)
            if grid[pt] == 'A':
                xmas_count += word_search(pt)


    print(xmas_count)