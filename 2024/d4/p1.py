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

    left = [Point(start_point.x-i, start_point.y) for i in range(4)]
    right = [Point(start_point.x+i, start_point.y) for i in range(4)]
    up = [Point(start_point.x, start_point.y-i) for i in range(4)]
    down = [Point(start_point.x, start_point.y+i) for i in range(4)]

    up_left = [Point(start_point.x-i, start_point.y-i) for i in range(4)]
    up_right = [Point(start_point.x+i, start_point.y-i) for i in range(4)]
    down_left = [Point(start_point.x-i, start_point.y+i) for i in range(4)]
    down_right = [Point(start_point.x+i, start_point.y+i) for i in range(4)]

    directions = [left, right, up, down, up_left, up_right, down_left, down_right]

    words = []
    for direction in directions:
        word = get_word(direction)
        words.append(word)
        if word == 'XMAS':
            count += 1
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
            xmas_count += word_search(pt)


    print(xmas_count)