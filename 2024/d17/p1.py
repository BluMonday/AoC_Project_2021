from collections import defaultdict
from collections import namedtuple
import re
import numpy as np


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
    global rB
    if rA != 0:
        ip = operand - 2
    return ip

def bxc():
    global rB
    rB = rB ^ rC

def out(operand):
    return f'{operand % 8}'

def bdv(operand):
    global rB
    rB = rB // 2 ** operand

def cdv(operand):
    global rC
    rC = rC // 2 ** operand


if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n\n')
    r_inp = inp[0]
    prog_inp = inp[1]

    rA = int(r_inp.split('\n')[0].split(':')[1])
    rB = int(r_inp.split('\n')[1].split(':')[1])
    rC = int(r_inp.split('\n')[2].split(':')[1])

    prog = [int(x) for x in prog_inp.split(':')[1].split(',')]
    #prog = zip(prog_inp[0::2], prog_inp[1::2])

    output = ''
    i = 0
    while i < len(prog):
        opcode = prog[i]
        operand = prog[i+1]
        # process combo and literal operand
        combo_op = 0
        if operand in [0,1,2,3]:
            combo_op = operand
        elif operand == 4:
            combo_op = rA
        elif operand == 5:
            combo_op = rB
        elif operand == 6:
            combo_op = rC

        # match opcode to operation
        match opcode:
            case 0:
                adv(combo_op)
            case 1:
                bxl(operand)
            case 2:
                bst(combo_op)
            case 3:
                i = jnz(operand, i)
            case 4:
                bxc()
            case 5:
                output = output + out(combo_op) + ','
            case 6:
                bdv(combo_op)
            case 7:
                cdv(combo_op)
        i += 2

    print(output[:-1])

    pass
