from collections import defaultdict
from collections import namedtuple

class Num:
    def __init__(self, i):
        self.i = i
    def __add__(self, other):
        return Num(self.i + other.i)
    def __sub__(self, other):
        return Num(self.i * other.i)
    def __mul__(self, other):
        return str(self.i)+str()

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
    bitness = 3
    for i in range(3**bitness):
        print(f'i = {i}: {(i//3**3)%3}-{(i//3**2)%3}-{(i//3**1)%3}-{i%3}')
        op = ''.join([f'{(i//3**j)%3}' for j in range(bitness-1, -1, -1)])

        print(op)


    f = open('in2.txt')
    inp = f.read().split('\n')

    sum = 0
    num_good = 0
    for line in inp:
        ans, expr = line.split(':')
        ans = int(ans)
        expr = expr.strip()
        nums = [int(x) for x in expr.split(' ')]
        bits = len(nums)-1
        for x in range(3**bits):
            op_str = ''.join([f'{(x//3**j)%3}' for j in range(bits-1, -1, -1)])
            acc = nums[0]
            for i in range(len(op_str)):
                match op_str[i]:
                    case '0':
                        acc += nums[i+1]
                    case '1':
                        acc *= nums[i+1]
                    case '2':
                        acc = int(str(acc)+str(nums[i+1]))
            if acc == ans:
                #expr = expr.replace('-', '+')
                sum += acc
                num_good += 1
                break
    print(sum)
    print(num_good)

