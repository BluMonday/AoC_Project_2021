from collections import defaultdict
from collections import namedtuple

class Num:
    def __init__(self, i):
        self.i = i
    def __add__(self, other):
        return Num(self.i + other.i)
    def __sub__(self, other):
        return Num(self.i * other.i)

def put_at_idx(base, idx, char):
    return base[:idx]+char+base[idx+1:]

def my_eval(x):
    s = ''
    in_num = False
    for c in x:
        if c in '0123456789' and in_num is False:
            s += 'Num('
            in_num = True
        if in_num is True and c not in '0123456789':
            s += ')'
            in_num = False
        s += c
    if in_num:
        s += ')'
    return eval(s).i

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')

    sum = 0
    for line in inp:
        ans, expr = line.split(':')
        ans = int(ans)
        expr = expr.strip()
        spaces = [i for i, x in enumerate(expr) if x == ' ']
        for x in range(2**len(spaces)):
            bin_str = ('{0:0' + str(len(spaces)) + 'b}').format(x)
            for i in range(len(bin_str)):
                if bin_str[i] == '0':
                    expr = put_at_idx(expr, spaces[i], '+')
                else:
                    # subtract is multiply
                    expr = put_at_idx(expr, spaces[i], '-')
            result = my_eval(expr)
            if result == ans:
                #expr = expr.replace('-', '+')
                sum += ans
                break
    print(sum)

