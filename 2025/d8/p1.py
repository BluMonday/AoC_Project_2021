from collections import defaultdict
from collections import namedtuple
import os

class Point(namedtuple('Point', 'x y z')):
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    def __str__(self):
        return f'({self.x},{self.y}{self.z})'
    def multiply(self, scalar):
        return Point(self.x*scalar, self.y*scalar, self.z*scalar)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return self+other.multiply(-1)
    def distance(self, other):
        return sum([x ** 2 for x in self - other])**(1 / 2)

if __name__ == '__main__':
    config = 2
    if config == 1: N = 10
    else: N = 1000
    f = open(f'in{config}.txt')
    inp = [x.split(',') for x in f.read().split('\n')]
    inp_int = [list(map(int, x)) for x in inp]
    pts = [Point(x,y,z) for x,y,z in inp_int]

    distances = []
    for i in range(len(pts)-1):
        for j in range(i+1, len(pts)):
            distances.append((pts[i].distance(pts[j]), pts[i], pts[j]))

    distances.sort()
    n = 0
    ckts = []
    while n < N:
        # get next shortest distance
        print(n)
        if n == 173:
            pass
        d,a,b = distances.pop(0)
        a_int = [c for c in ckts if a in c]
        b_int = [c for c in ckts if b in c]
        if len(a_int) == 0 and len(b_int) == 0:
            # new circuit of ab
            ckts.append([a,b])
            # note a connection made
            n += 1
        elif len(a_int) == 1 and len(b_int) == 0:
            # remove circuit and add b to it
            c = ckts.pop(ckts.index(a_int[0]))
            c.append(b)
            ckts.append(c)
            n += 1
        elif len(a_int) == 0 and len(b_int) == 1:
            # remove circuit and add a to it
            c = ckts.pop(ckts.index(b_int[0]))
            c.append(a)
            ckts.append(c)
            n += 1
        elif a_int == b_int:
            continue
        elif set(a_int[0]) == set(b_int[0]):
            # a and b in same circuit already
            continue
        else:
            # a and b in different circuits, join them
            ac = ckts.pop(ckts.index(a_int[0]))
            bc = ckts.pop(ckts.index(b_int[0]))
            ac.append(bc)
            ckts.append(ac)
            n +=1



    sizes = [len(c) for c in ckts]
    sizes.sort(reverse=True)
    score = sizes[0]*sizes[1]*sizes[2]


    print(score)
    pass
