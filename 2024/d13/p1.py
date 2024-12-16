from collections import defaultdict
from collections import namedtuple
import re
import numpy as np


class Coord(namedtuple('Coord', 'x y')):
    pass

def calc_cost(arr):
    return 3*arr[0] + arr[1]

class Claw_Machine:
    btn_a = Coord(0,0)
    btn_b = Coord(0,0)
    prize = Coord(0,0)
    can_win = False
    cost = 0
    solution = Coord(0,0)

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n\n')
    claw_machines = []
    re_a = re.compile(r'Button A: X\+(\d*), Y\+(\d*)')
    re_b = re.compile(r'Button B: X\+(\d*), Y\+(\d*)')
    re_p = re.compile(r'Prize: X=(\d*), Y=(\d*)')


    for claw_inp in inp:
        machine = Claw_Machine()
        ma = re.search(r'Button A: X\+(\d*), Y\+(\d*)', claw_inp)
        mb = re.search(r'Button B: X\+(\d*), Y\+(\d*)', claw_inp)
        mp = re.search(r'Prize: X=(\d*), Y=(\d*)', claw_inp)
        machine.btn_a = Coord(int(ma.group(1)),int(ma.group(2)))
        machine.btn_b = Coord(int(mb.group(1)),int(mb.group(2)))
        machine.prize = Coord(int(mp.group(1)),int(mp.group(2)))
        claw_machines.append(machine)
        pass


    for m in claw_machines:
        a = np.array([[m.btn_a.x, m.btn_b.x], [m.btn_a.y, m.btn_b.y]])
        b = np.array([m.prize.x, m.prize.y])
        if np.linalg.det(a) != 0:
            x = np.linalg.solve(a, b)
            x_int = [int(round(el, 0)) for el in x]
            if not all(np.greater_equal(x_int, [0,0])):
                pass
            if any(np.greater_equal(x_int, [100,100])):
                pass
            if np.allclose(np.dot(a, x_int), b):
                m.can_win = True
                m.cost = calc_cost(x_int)
                m.solution = Coord(x_int[0], x_int[1])
        else:
            pass
        pass

    c = [m.cost for m in claw_machines if m.can_win == True]
    print(sum(c))
    pass
