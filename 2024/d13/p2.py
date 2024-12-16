from collections import defaultdict
from collections import namedtuple
import re
import numpy as np


class Coord(namedtuple('Coord', 'x y')):
    pass

def calc_cost(arr):
    return 3*arr[0] + arr[1]

class Claw_Machine:
    def __str__(self):
        if self.can_win:
            return f'Solution at X={self.btn_a}, Y={self.btn_b}'
        else: return f'No Solution'
    btn_a = Coord(0,0)
    btn_b = Coord(0,0)
    prize = Coord(0,0)
    can_win = False
    cost = 0
    solution = Coord(0,0)

    def try_solve(self):
        a = self.btn_a.x
        b = self.btn_b.x
        c = self.prize.x
        d = self.btn_a.y
        e = self.btn_b.y
        f = self.prize.y
        num_a = int(round((e*c - b*f)/(e*a - b*d), 0))
        num_b = int(round((c - a*num_a)/b, 0))
        positive_sol = num_a >= 0 and num_b >= 0
        int_sol = a*num_a + b*num_b == c and d*num_a + e*num_b == f
        if positive_sol and int_sol:
            self.solution = Coord(num_a, num_b)
            self.can_win = True
            self.cost = calc_cost(self.solution)
        else:
            self.can_win = False

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
        machine.prize = Coord(int(mp.group(1))+10000000000000, int(mp.group(2))+10000000000000)
        claw_machines.append(machine)
        pass
    claw_machines2 = claw_machines.copy()

    for m in claw_machines:
        a = np.array([[m.btn_a.x, m.btn_b.x], [m.btn_a.y, m.btn_b.y]])
        b = np.array([m.prize.x, m.prize.y])
        if np.linalg.det(a) != 0:
            x = np.linalg.solve(a, b)
            x_int = [int(round(el, 0)) for el in x]
            if np.allclose(np.dot(a, x_int), b) and not all(np.greater_equal(x_int, [0, 0])):
                m.can_win = True
                m.cost = calc_cost(x_int)
                m.solution = Coord(x_int[0], x_int[1])
        else:
            pass
        pass

    c = [m.cost for m in claw_machines if m.can_win == True]
    print(f'numpy answer: {sum(c)}')


    [m.try_solve() for m in claw_machines2]
    c = [m.cost for m in claw_machines2 if m.can_win == True]
    print(f'math answer: {sum(c)}')

    delta = [(m1, m2) for m1, m2 in zip(claw_machines, claw_machines2) if m1.can_win != m2.can_win]
    pass
