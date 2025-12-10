from collections import defaultdict
from collections import namedtuple
import os

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

def area(p1, p2):
    return (abs(p1.x-p2.x)+1)*(abs(p1.y-p2.y)+1)
if __name__ == '__main__':

    f = open('in2.txt')
    inp = [i.split(',') for i in f.read().split('\n')]
    inp_int = [list(map(int, x)) for x in inp]
    pts = [Point(x,y) for x,y in inp_int]

    pairs = []
    for i in range(len(pts)-1):
        for j in range(i+1, len(pts)):
            pairs.append((area(pts[i], pts[j]), pts[i], pts[j]))

    pairs.sort()
    print(pairs[-1])

    pass



