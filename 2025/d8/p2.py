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
    # init circuits
    ckts = [set([p]) for p in pts]
    n = 0
    while n < N-1:
        # get junction pair with next shortest distance
        d,j1,j2 = distances.pop(0)
        j1_ckt = [c for c in ckts if set([j1]) <= c][0] # circuit containing j1
        j2_ckt = [c for c in ckts if set([j2]) <= c][0] # circuit containing j2
        if j1_ckt == j2_ckt:
            # a and b in same circuit already
            continue
        else:
            # merge circuits containing j1 and j2 into a single circuit
            ckts.remove(j1_ckt)
            ckts.remove(j2_ckt)
            ckts.append(j1_ckt | j2_ckt) # replace with union
            n += 1 # consume cord
            if n == 999:
                print(j1.x * j2.x)

    sizes = [len(c) for c in ckts]
    pass
