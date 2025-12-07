from collections import defaultdict
from collections import namedtuple
from collections import deque


if __name__ == '__main__':

    f = open(f'in2.txt')
    inp_ranges, inp_ids = f.read().split('\n\n')
    inp_ranges = inp_ranges.split('\n')
    ranges = [[int(n) for n in x.split('-')] for x in inp_ranges]
    ids = inp_ids.split('\n')
    ids = [int(x) for x in ids]


    ans = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                ans += 1
                break



    print(ans)
