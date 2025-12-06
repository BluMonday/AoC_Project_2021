from z3 import *


def adv(operand):
    global rA
    rA = rA // 2**operand

def bxl(operand):
    global rB
    rB = rB ^ operand

def bst(operand):
    global rB
    rB = operand % 8

def jnz(operand, ip):
    global rA
    if rA != 0:
        ip = operand - 2
    return ip

def bxc():
    global rB
    rB = rB ^ rC

def out(operand):
    return f'{operand % 8}'

def bdv(operand):
    global rA
    global rB
    rB = rA // (2 ** operand)

def cdv(operand):
    global rA
    global rC
    rC = rA // (2 ** operand)


if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n\n')
    r_inp = inp[0]
    prog_inp = inp[1]

    rA = int(r_inp.split('\n')[0].split(':')[1])
    rB = int(r_inp.split('\n')[1].split(':')[1])
    rC = int(r_inp.split('\n')[2].split(':')[1])

    prog = [int(x) for x in prog_inp.split(':')[1].split(',')]

    s = Optimize()
    A = BitVec('A', 64)
    s.minimize(A)
    for v in prog:
        B = (A & 7) ^ 5
        C = A >> B
        B = B ^ 6
        A = A >> 3
        s.add(v == (B ^ C) & 7)
    print(s)
    print(s.check())
    print(s.model())


    pass
